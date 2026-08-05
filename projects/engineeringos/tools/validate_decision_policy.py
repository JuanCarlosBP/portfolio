#!/usr/bin/env python3
"""Validate the EngineeringOS technical-decision policy contract."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ISSUE_URL = "https://github.com/JuanCarlosBP/portfolio/issues/16"
BRANCH = "docs/p01-w01d05-technical-decision-policy"

POLICY_HEADINGS = (
    "# Política de decisiones técnicas de EngineeringOS",
    "## Propósito",
    "## Problema que resuelve",
    "## Alcance",
    "## Fuera de alcance",
    "## Principio general",
    "## Niveles de clasificación",
    "## Regla de precedencia",
    "## Algoritmo de clasificación",
    "## Desencadenantes de ADR",
    "## Regla de nota local",
    "## Cambios sin registro específico",
    "## Contenido obligatorio de un ADR",
    "## Ciclo de vida de una decisión",
    "## Ejemplos de clasificación",
    "## Escenarios fronterizos",
    "## Revisión humana",
    "## Control de burocracia",
    "## Criterio de revisión de esta política",
    "## Trazabilidad",
    "## Regla de cierre de EOS-006",
)

ADR_TEMPLATE_HEADINGS = (
    "# ADR-{{ADR_NUMBER}} · {{TITLE}}",
    "## Contexto",
    "## Desencadenantes aplicables",
    "## Decisión",
    "## Alternativas consideradas",
    "## Consecuencias",
    "## Trade-off aceptado",
    "## Plan de reversión",
    "## Criterio de revisión",
    "## Trazabilidad",
    "## Lista de comprobación",
)

LOCAL_TEMPLATE_HEADINGS = (
    "# Nota local · {{TITLE}}",
    "## Contexto local",
    "## Decisión",
    "## Motivo de clasificación",
    "## Alcance y límites",
    "## Consecuencias",
    "## Reversión",
    "## Criterio de escalado",
    "## Trazabilidad",
    "## Lista de comprobación",
)

ADR_REQUIRED_HEADINGS = (
    "## Contexto",
    "## Desencadenantes aplicables",
    "## Decisión",
    "## Alternativas consideradas",
    "## Consecuencias",
    "## Trade-off aceptado",
    "## Plan de reversión",
    "## Criterio de revisión",
    "## Compatibilidad con decisiones anteriores",
    "## Trazabilidad",
)

LOCAL_REQUIRED_HEADINGS = (
    "## Contexto local",
    "## Decisión",
    "## Motivo de clasificación",
    "## Alcance y límites",
    "## Consecuencias",
    "## Reversión",
    "## Criterio de escalado",
    "## Trazabilidad",
    "## Lista de comprobación",
)

ADR_TRIGGER_IDS = tuple(
    f"ADR-{number:02d}"
    for number in range(1, 11)
)

LOCAL_RULE_IDS = tuple(
    f"LOCAL-{number:02d}"
    for number in range(1, 7)
)

TRIVIAL_IDS = tuple(
    f"TRIV-{number:02d}"
    for number in range(1, 8)
)

ADR_CONTENT_IDS = tuple(
    f"ADR-CONTENT-{number:02d}"
    for number in range(1, 9)
)

LIFECYCLE_STATES = (
    "Propuesta",
    "Aceptada",
    "Rechazada",
    "Sustituida",
    "Obsoleta",
)

ACTIVE_STATES = {
    "En curso",
    "En validación",
}


@dataclass(frozen=True)
class Check:
    """One deterministic decision-policy validation result."""

    document: str
    requirement: str
    passed: bool


def read_text(path: Path) -> str:
    """Read UTF-8 text or return an empty string."""

    if not path.is_file():
        return ""

    return path.read_text(encoding="utf-8")


def contains_all(
    content: str,
    markers: Iterable[str],
) -> bool:
    """Return whether every marker occurs."""

    return all(
        marker in content
        for marker in markers
    )


def exact_ids(
    content: str,
    pattern: str,
    expected: tuple[str, ...],
) -> bool:
    """Require every expected identifier once and in order."""

    found = re.findall(
        pattern,
        content,
    )

    return (
        tuple(found) == expected
        and len(set(found)) == len(expected)
    )


def has_no_trailing_whitespace(content: str) -> bool:
    """Reject spaces or tabs at line endings."""

    return all(
        not line.endswith((" ", "\t"))
        for line in content.splitlines()
    )


def count_checkboxes(
    content: str,
    checked: bool,
) -> int:
    """Count checked or unchecked Markdown checkboxes."""

    marker = "x" if checked else " "

    return len(
        re.findall(
            rf"(?mi)^- \[{marker}\] ",
            content,
        )
    )


def active_backlog_items(content: str) -> list[str]:
    """Return backlog identifiers in active states."""

    rows = re.findall(
        r"(?m)^\|\s*\d+\s*"
        r"\|\s*`(?P<id>EOS-\d{3})`\s*"
        r"\|\s*`P[0-3]`\s*"
        r"\|[^|]+\|"
        r"\s*(?P<state>[^|]+?)\s*"
        r"\|[^|]+\|$",
        content,
    )

    return [
        item_id
        for item_id, state in rows
        if state.strip() in ACTIVE_STATES
    ]


def current_state_is_active(content: str) -> bool:
    """Accept the active W01D05 states."""

    match = re.search(
        r"(?m)^\| Estado del foco actual "
        r"\| `(?P<state>[^`]+)` \|$",
        content,
    )

    return (
        match is not None
        and match.group("state") in ACTIVE_STATES
    )


def validate(repository_root: Path) -> list[Check]:
    """Return all 44 deterministic checks."""

    project = (
        repository_root
        / "projects"
        / "engineeringos"
    )

    policy_path = (
        project
        / "docs"
        / "standards"
        / "technical-decision-policy.md"
    )

    adr_template_path = (
        project
        / "docs"
        / "templates"
        / "adr-template.md"
    )

    local_template_path = (
        project
        / "docs"
        / "templates"
        / "local-decision-note-template.md"
    )

    adr_path = (
        project
        / "docs"
        / "adr"
        / "ADR-0003-technical-decision-policy.md"
    )

    local_path = (
        project
        / "docs"
        / "decisions"
        / "local"
        / "w01d05-reuse-existing-workflow.md"
    )

    backlog_path = (
        project
        / "docs"
        / "planning"
        / "backlog.md"
    )

    state_path = (
        project
        / "docs"
        / "state"
        / "current-state.md"
    )

    policy = read_text(policy_path)
    adr_template = read_text(adr_template_path)
    local_template = read_text(local_template_path)
    adr = read_text(adr_path)
    local = read_text(local_path)
    backlog = read_text(backlog_path)
    state = read_text(state_path)

    checks = [
        Check(
            "policy",
            "file exists",
            policy_path.is_file(),
        ),
        Check(
            "policy",
            "contains 21 canonical headings",
            contains_all(
                policy,
                POLICY_HEADINGS,
            ),
        ),
        Check(
            "policy",
            "contains W01D05 metadata",
            contains_all(
                policy,
                (
                    "**Proyecto:** EngineeringOS",
                    "**Elemento de backlog:** `EOS-006`",
                    "**Día de trabajo:** `W01D05`",
                    "**Fecha de ejecución:** `2026-08-05`",
                    f"**Issue:** [#16]({ISSUE_URL})",
                    "**Versión de la política:** `1.0.0`",
                ),
            ),
        ),
        Check(
            "policy",
            "defines three levels",
            contains_all(
                policy,
                (
                    "| `ADR` |",
                    "| `LOCAL_NOTE` |",
                    "| `NO_EXTRA_RECORD` |",
                ),
            ),
        ),
        Check(
            "policy",
            "defines precedence",
            (
                "ADR > LOCAL_NOTE > NO_EXTRA_RECORD"
                in policy
            ),
        ),
        Check(
            "policy",
            "contains six algorithm steps",
            len(
                re.findall(
                    r"(?m)^### Paso [1-6] · ",
                    policy,
                )
            )
            == 6,
        ),
        Check(
            "policy",
            "contains ADR identifiers exactly once",
            exact_ids(
                policy,
                r"`(ADR-(?:0[1-9]|10))`",
                ADR_TRIGGER_IDS,
            ),
        ),
        Check(
            "policy",
            "contains local identifiers exactly once",
            exact_ids(
                policy,
                r"`(LOCAL-0[1-6])`",
                LOCAL_RULE_IDS,
            ),
        ),
        Check(
            "policy",
            "contains trivial identifiers exactly once",
            exact_ids(
                policy,
                r"`(TRIV-0[1-7])`",
                TRIVIAL_IDS,
            ),
        ),
        Check(
            "policy",
            "contains ADR content identifiers exactly once",
            exact_ids(
                policy,
                r"`(ADR-CONTENT-0[1-8])`",
                ADR_CONTENT_IDS,
            ),
        ),
        Check(
            "policy",
            "defines five lifecycle states",
            all(
                f"`{state_name}`" in policy
                for state_name in LIFECYCLE_STATES
            ),
        ),
        Check(
            "policy",
            "contains anti-bureaucracy control",
            "## Control de burocracia" in policy,
        ),
        Check(
            "policy",
            "contains review criterion",
            (
                "## Criterio de revisión de esta política"
                in policy
            ),
        ),
        Check(
            "policy",
            "contains no unresolved placeholders",
            (
                "{{" not in policy
                and "}}" not in policy
            ),
        ),
        Check(
            "policy",
            "contains no trailing whitespace",
            has_no_trailing_whitespace(policy),
        ),
        Check(
            "ADR template",
            "file exists",
            adr_template_path.is_file(),
        ),
        Check(
            "ADR template",
            "contains canonical headings",
            contains_all(
                adr_template,
                ADR_TEMPLATE_HEADINGS,
            ),
        ),
        Check(
            "ADR template",
            "contains status and date placeholders",
            contains_all(
                adr_template,
                (
                    "**Estado:** {{STATUS}}",
                    "**Fecha:** {{DATE}}",
                ),
            ),
        ),
        Check(
            "ADR template",
            "contains ten unchecked items",
            (
                count_checkboxes(
                    adr_template,
                    checked=False,
                )
                == 10
                and count_checkboxes(
                    adr_template,
                    checked=True,
                )
                == 0
            ),
        ),
        Check(
            "ADR template",
            "contains instructions",
            "TEMPLATE_INSTRUCTION" in adr_template,
        ),
        Check(
            "ADR template",
            "contains no trailing whitespace",
            has_no_trailing_whitespace(adr_template),
        ),
        Check(
            "local template",
            "file exists",
            local_template_path.is_file(),
        ),
        Check(
            "local template",
            "contains canonical headings",
            contains_all(
                local_template,
                LOCAL_TEMPLATE_HEADINGS,
            ),
        ),
        Check(
            "local template",
            "declares LOCAL_NOTE",
            (
                "**Nivel elegido:** `LOCAL_NOTE`"
                in local_template
            ),
        ),
        Check(
            "local template",
            "contains ten unchecked items",
            (
                count_checkboxes(
                    local_template,
                    checked=False,
                )
                == 10
                and count_checkboxes(
                    local_template,
                    checked=True,
                )
                == 0
            ),
        ),
        Check(
            "local template",
            "contains instructions",
            "TEMPLATE_INSTRUCTION" in local_template,
        ),
        Check(
            "local template",
            "contains no trailing whitespace",
            has_no_trailing_whitespace(local_template),
        ),
        Check(
            "ADR-0003",
            "file exists",
            adr_path.is_file(),
        ),
        Check(
            "ADR-0003",
            "uses an allowed state",
            bool(
                re.search(
                    r"(?m)^\*\*Estado:\*\* "
                    r"(?:Propuesta|Aceptada)$",
                    adr,
                )
            ),
        ),
        Check(
            "ADR-0003",
            "identifies W01D05, EOS-006 and issue 16",
            contains_all(
                adr,
                (
                    (
                        "**Decisión relacionada:** "
                        "W01D05 · EOS-006"
                    ),
                    f"**Issue:** [#16]({ISSUE_URL})",
                ),
            ),
        ),
        Check(
            "ADR-0003",
            "contains required sections",
            contains_all(
                adr,
                ADR_REQUIRED_HEADINGS,
            ),
        ),
        Check(
            "ADR-0003",
            "uses expected triggers",
            set(
                re.findall(
                    r"`(ADR-(?:0[1-9]|10))`",
                    adr,
                )
            )
            == {
                "ADR-01",
                "ADR-02",
                "ADR-08",
                "ADR-10",
            },
        ),
        Check(
            "ADR-0003",
            "contains four alternatives",
            len(
                re.findall(
                    r"(?m)^### Alternativa [A-D] · ",
                    adr,
                )
            )
            == 4,
        ),
        Check(
            "ADR-0003",
            "contains no template residue",
            (
                "{{" not in adr
                and "}}" not in adr
                and "TEMPLATE_INSTRUCTION" not in adr
            ),
        ),
        Check(
            "ADR-0003",
            "preserves previous ADR compatibility",
            (
                "ADR-0001 y ADR-0002 "
                "conservan su validez histórica."
                in adr
            ),
        ),
        Check(
            "local note",
            "file exists",
            local_path.is_file(),
        ),
        Check(
            "local note",
            "declares LOCAL_NOTE",
            (
                "**Nivel elegido:** `LOCAL_NOTE`"
                in local
            ),
        ),
        Check(
            "local note",
            "uses LOCAL-01 through LOCAL-06",
            set(
                re.findall(
                    r"`(LOCAL-0[1-6])`",
                    local,
                )
            )
            == set(LOCAL_RULE_IDS),
        ),
        Check(
            "local note",
            "contains ten checked items",
            (
                count_checkboxes(
                    local,
                    checked=True,
                )
                == 10
                and count_checkboxes(
                    local,
                    checked=False,
                )
                == 0
            ),
        ),
        Check(
            "local note",
            "contains sections without residue",
            (
                contains_all(
                    local,
                    LOCAL_REQUIRED_HEADINGS,
                )
                and "{{" not in local
                and "}}" not in local
                and "TEMPLATE_INSTRUCTION" not in local
            ),
        ),
        Check(
            "backlog",
            "has exactly EOS-006 active",
            active_backlog_items(backlog) == ["EOS-006"],
        ),
        Check(
            "current state",
            "identifies active W01D05",
            (
                contains_all(
                    state,
                    (
                        "| Día lógico | `W01D05` |",
                        (
                            "| Foco actual | `EOS-006 · "
                            "Política de decisiones técnicas` |"
                        ),
                        (
                            "| Issue activa | "
                            f"[#16]({ISSUE_URL}) |"
                        ),
                        (
                            "| Rama activa | "
                            f"`{BRANCH}` |"
                        ),
                    ),
                )
                and current_state_is_active(state)
                and "Crear el commit PM de W01D04"
                not in state
            ),
        ),
        Check(
            "cross-document",
            "preserves canonical paths",
            all(
                marker in policy + adr + local
                for marker in (
                    "technical-decision-policy.md",
                    "adr-template.md",
                    "local-decision-note-template.md",
                )
            ),
        ),
        Check(
            "cross-document",
            "preserves issue traceability",
            all(
                "#16" in content
                for content in (
                    policy,
                    adr,
                    local,
                    state,
                )
            ),
        ),
    ]

    if len(checks) != 44:
        raise RuntimeError(
            f"Internal contract error: "
            f"{len(checks)} checks"
        )

    return checks


def render_summary(checks: list[Check]) -> str:
    """Render the stable gate result."""

    failed = [
        check
        for check in checks
        if not check.passed
    ]

    passed = len(checks) - len(failed)

    lines = [
        "EngineeringOS decision-policy quality gate",
        f"Checks: {passed}/{len(checks)} passed",
        (
            "Result: PASS"
            if not failed
            else "Result: FAIL"
        ),
    ]

    if failed:
        lines.append("Failures:")

        lines.extend(
            (
                f"- {check.document}: "
                f"{check.requirement}"
            )
            for check in failed
        )

    return "\n".join(lines)


def main() -> int:
    """Run the decision-policy quality gate."""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
    )

    args = parser.parse_args()
    checks = validate(args.root.resolve())

    print(render_summary(checks))

    return (
        0
        if all(check.passed for check in checks)
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
