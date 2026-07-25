#!/usr/bin/env python3
"""Validate the minimum, traceable EngineeringOS discovery contract."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ISSUE_URL = "https://github.com/JuanCarlosBP/portfolio/issues/1"

COMMON_MARKERS = (
    "**Proyecto:** EngineeringOS",
    "**Fase:** Discovery inicial",
    "**Día de trabajo:** W01D01",
    f"**Issue relacionada:** [#1]({ISSUE_URL})",
    "**Estado:** Validado en W01D01",
)

DOCUMENT_RULES = {
    "problem-statement.md": (
        "# Planteamiento del problema",
        "## Problema principal",
        "## Consecuencias",
        "## Hipótesis inicial",
        "## Pregunta de discovery",
    ),
    "users-and-needs.md": (
        "# Usuarios y necesidades",
        "## Usuario principal",
        "## Usuarios secundarios",
        "## Prioridad inicial",
        "## Límites",
    ),
    "current-process.md": (
        "# Proceso actual",
        "## Proceso actual de referencia",
        "## Carencias detectadas",
        "## Puntos de fricción prioritarios",
        "## Estado deseado inicial",
    ),
    "success-metrics.md": (
        "# Métricas de éxito",
        "## Métricas principales",
        "## Línea base inicial",
        "## Método de recogida",
        "## Limitaciones",
    ),
}


@dataclass(frozen=True)
class Check:
    """One deterministic discovery validation result."""

    document: str
    requirement: str
    passed: bool


def validate_discovery(discovery_dir: Path) -> list[Check]:
    """Return all 40 checks for the four discovery documents."""
    checks: list[Check] = []

    for filename, specific_markers in DOCUMENT_RULES.items():
        path = discovery_dir / filename
        if not path.is_file():
            markers = (*COMMON_MARKERS, *specific_markers)
            checks.extend(
                Check(filename, f"contains {marker}", False) for marker in markers
            )
            continue

        content = path.read_text(encoding="utf-8")
        for marker in (*COMMON_MARKERS, *specific_markers):
            checks.append(Check(filename, f"contains {marker}", marker in content))

    return checks


def failures(checks: Iterable[Check]) -> list[Check]:
    """Return failed checks without mutating the validation result."""
    return [check for check in checks if not check.passed]


def render_summary(checks: list[Check]) -> str:
    """Render a stable, human-readable quality-gate summary."""
    failed = failures(checks)
    passed_count = len(checks) - len(failed)
    lines = [
        "EngineeringOS discovery quality gate",
        f"Checks: {passed_count}/{len(checks)} passed",
    ]

    if failed:
        lines.append("Result: FAIL")
        lines.append("Failures:")
        lines.extend(
            f"- {check.document}: {check.requirement}" for check in failed
        )
    else:
        lines.append("Result: PASS")

    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line interface."""
    default_root = Path(__file__).resolve().parents[1] / "docs" / "discovery"
    parser = argparse.ArgumentParser(
        description="Validate the W01D01 EngineeringOS discovery contract."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=default_root,
        help="Directory containing the four discovery Markdown files.",
    )
    return parser


def main() -> int:
    """Run the quality gate and expose success through the process exit code."""
    args = build_parser().parse_args()
    checks = validate_discovery(args.root)
    print(render_summary(checks))
    return 1 if failures(checks) else 0


if __name__ == "__main__":
    raise SystemExit(main())
