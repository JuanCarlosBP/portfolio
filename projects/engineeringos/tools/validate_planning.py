#!/usr/bin/env python3
"""Validate the EngineeringOS planning and Definition of Done contract."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ISSUE_URL = "https://github.com/JuanCarlosBP/portfolio/issues/8"
BRANCH = "docs/p01-w01d02-backlog-dod"

BACKLOG_MARKERS = (
    "# Backlog priorizado de EngineeringOS",
    "**Proyecto:** EngineeringOS",
    "**Día de trabajo:** W01D02",
    f"**Issue relacionada:** [#8]({ISSUE_URL})",
    f"**Rama:** `{BRANCH}`",
    "**Estado:** Validado en W01D02",
    "## Política de prioridad",
    "## Flujo de estados",
    "## Límite de trabajo en curso",
    "WIP = 1 elemento en estado En curso",
    "## Criterios para pasar a Preparado",
    "## Control de cambios de alcance",
    "## Regla de cierre",
)

DOD_MARKERS = (
    "# Definition of Done de EngineeringOS",
    "**Proyecto:** EngineeringOS",
    "**Día de trabajo:** W01D02",
    f"**Issue relacionada:** [#8]({ISSUE_URL})",
    f"**Rama:** `{BRANCH}`",
    "**Estado:** Validada en W01D02",
    "## Regla general",
    "## Estados permitidos",
    "## Núcleo obligatorio literal de la ruta",
    "## Checklist reutilizable",
    "## Evidencias aceptables",
    "## Uso de No aplica",
    "## Regla sobre CI",
    "W01D02 debe terminar con CI aplicable y verde.",
    "## Regla sobre atomicidad",
    "## Regla sobre documentación coherente",
    "## Responsabilidad humana",
    "## Condición de cierre",
)

EXPECTED_IDS = tuple(
    f"EOS-{number:03d}"
    for number in range(1, 11)
)

ALLOWED_PRIORITIES = {
    "P0",
    "P1",
    "P2",
    "P3",
}

ALLOWED_STATES = {
    "Pendiente",
    "Preparado",
    "En curso",
    "En validación",
    "Terminado",
    "Bloqueado",
    "Aparcada",
}

ACTIVE_STATES = {
    "En curso",
    "En validación",
}

EXPECTED_CORE_ITEMS = (
    "Issue enlazada.",
    "Rama correcta.",
    "Cambio atómico.",
    "Validación ejecutada.",
    "CI verde.",
    "Documentación coherente.",
)

SUMMARY_ROW_PATTERN = re.compile(
    r"^\|\s*\d+\s*"
    r"\|\s*`(?P<id>EOS-\d{3})`\s*"
    r"\|\s*`(?P<priority>[^`]+)`\s*"
    r"\|\s*(?P<title>[^|]+?)\s*"
    r"\|\s*(?P<state>[^|]+?)\s*"
    r"\|\s*(?P<dependencies>[^|]+?)\s*\|$",
    flags=re.MULTILINE,
)


@dataclass(frozen=True)
class Check:
    """One deterministic planning validation result."""

    document: str
    requirement: str
    passed: bool


@dataclass(frozen=True)
class BacklogRow:
    """One parsed row from the prioritized backlog summary."""

    item_id: str
    priority: str
    title: str
    state: str
    dependencies: str


def read_text(path: Path) -> str:
    """Read UTF-8 text or return an empty string for an absent file."""

    if not path.is_file():
        return ""

    return path.read_text(encoding="utf-8")


def parse_backlog_rows(content: str) -> list[BacklogRow]:
    """Parse the ten operational rows from the backlog summary."""

    rows: list[BacklogRow] = []

    for match in SUMMARY_ROW_PATTERN.finditer(content):
        rows.append(
            BacklogRow(
                item_id=match.group("id").strip(),
                priority=match.group("priority").strip(),
                title=match.group("title").strip(),
                state=match.group("state").strip(),
                dependencies=match.group("dependencies").strip(),
            )
        )

    return rows


def parse_core_items(content: str) -> tuple[str, ...]:
    """Return the exact six mandatory Definition of Done items."""

    section = re.search(
        r"## Núcleo obligatorio literal de la ruta\n"
        r"(?P<body>.*?)(?=\n## )",
        content,
        flags=re.DOTALL,
    )

    if section is None:
        return ()

    return tuple(
        re.findall(
            r"^- \[ \] (.+)$",
            section.group("body"),
            flags=re.MULTILINE,
        )
    )


def validate_planning(project_root: Path) -> list[Check]:
    """Return all 39 deterministic planning-contract checks."""

    backlog_path = project_root / "docs" / "planning" / "backlog.md"
    dod_path = (
        project_root
        / "docs"
        / "standards"
        / "definition-of-done.md"
    )

    backlog = read_text(backlog_path)
    dod = read_text(dod_path)

    checks: list[Check] = [
        Check(
            "backlog.md",
            "file exists",
            backlog_path.is_file(),
        )
    ]

    checks.extend(
        Check(
            "backlog.md",
            f"contains {marker}",
            marker in backlog,
        )
        for marker in BACKLOG_MARKERS
    )

    checks.append(
        Check(
            "definition-of-done.md",
            "file exists",
            dod_path.is_file(),
        )
    )

    checks.extend(
        Check(
            "definition-of-done.md",
            f"contains {marker}",
            marker in dod,
        )
        for marker in DOD_MARKERS
    )

    heading_ids = tuple(
        re.findall(
            r"^## (EOS-\d{3}) ·",
            backlog,
            flags=re.MULTILINE,
        )
    )

    rows = parse_backlog_rows(backlog)
    row_ids = tuple(row.item_id for row in rows)

    checks.append(
        Check(
            "backlog.md",
            "contains EOS-001 through EOS-010 headings in order",
            heading_ids == EXPECTED_IDS,
        )
    )

    checks.append(
        Check(
            "backlog.md",
            "contains exactly ten summary rows in order",
            len(rows) == 10 and row_ids == EXPECTED_IDS,
        )
    )

    checks.append(
        Check(
            "backlog.md",
            "uses only allowed priorities",
            bool(rows)
            and all(
                row.priority in ALLOWED_PRIORITIES
                for row in rows
            ),
        )
    )

    checks.append(
        Check(
            "backlog.md",
            "uses only allowed states",
            bool(rows)
            and all(
                row.state in ALLOWED_STATES
                for row in rows
            ),
        )
    )

    active_items = [
        row.item_id
        for row in rows
        if row.state in ACTIVE_STATES
    ]

    checks.append(
        Check(
            "backlog.md",
            "respects WIP by having at most one active item",
            len(active_items) <= 1,
        )
    )

    checks.append(
        Check(
            "definition-of-done.md",
            "contains the exact six mandatory route criteria",
            parse_core_items(dod) == EXPECTED_CORE_ITEMS,
        )
    )

    return checks


def failures(checks: Iterable[Check]) -> list[Check]:
    """Return failed checks without mutating the validation result."""

    return [
        check
        for check in checks
        if not check.passed
    ]


def render_summary(checks: list[Check]) -> str:
    """Render a stable, human-readable quality-gate summary."""

    failed = failures(checks)
    passed_count = len(checks) - len(failed)

    lines = [
        "EngineeringOS planning quality gate",
        f"Checks: {passed_count}/{len(checks)} passed",
    ]

    if failed:
        lines.append("Result: FAIL")
        lines.append("Failures:")
        lines.extend(
            f"- {check.document}: {check.requirement}"
            for check in failed
        )
    else:
        lines.append("Result: PASS")

    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line interface."""

    default_root = Path(__file__).resolve().parents[1]

    parser = argparse.ArgumentParser(
        description=(
            "Validate the W01D02 EngineeringOS planning contract."
        )
    )

    parser.add_argument(
        "--root",
        type=Path,
        default=default_root,
        help=(
            "EngineeringOS project root containing docs/planning "
            "and docs/standards."
        ),
    )

    return parser


def main() -> int:
    """Run the quality gate and expose success through the exit code."""

    args = build_parser().parse_args()
    checks = validate_planning(args.root)

    print(render_summary(checks))

    return 1 if failures(checks) else 0


if __name__ == "__main__":
    raise SystemExit(main())
