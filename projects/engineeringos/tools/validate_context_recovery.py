#!/usr/bin/env python3
"""Validate the EngineeringOS context-recovery contract."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


AM_SHA = "8b2e968f8aa1fd3f37da5d7cb43de622c5ab42c3"
PM_MESSAGE = "test(w0014pm): discovery engineeringos"
EXERCISE_SHA = (
    "07c3e38e1ed7d812409c4920d5814e80"
    "f8383ccfb1291b7981f725f52cc3bea7"
)


@dataclass(frozen=True)
class Check:
    """One deterministic validation result."""

    name: str
    passed: bool


def read_text(path: Path) -> str:
    """Read UTF-8 text or return an empty string."""

    if not path.is_file():
        return ""

    return path.read_text(encoding="utf-8")


def evidence_answer_rows_are_complete(content: str) -> bool:
    """Require the five recovery-answer rows."""

    required = (
        "| Objetivo |",
        "| Estado |",
        "| Decisión vigente |",
        "| Bloqueos |",
        "| Siguiente acción |",
    )

    return all(marker in content for marker in required)


def validate(repository_root: Path) -> list[Check]:
    """Return the 36 context-recovery checks."""

    project = (
        repository_root
        / "projects"
        / "engineeringos"
    )

    evidence_path = (
        project
        / "docs"
        / "evidence"
        / "w01d04-context-recovery.md"
    )

    state_path = (
        project
        / "docs"
        / "state"
        / "current-state.md"
    )

    backlog_path = (
        project
        / "docs"
        / "planning"
        / "backlog.md"
    )

    dod_path = (
        project
        / "docs"
        / "standards"
        / "definition-of-done.md"
    )

    root_readme_path = repository_root / "README.md"
    project_readme_path = project / "README.md"

    workflow_path = (
        repository_root
        / ".github"
        / "workflows"
        / "engineeringos-discovery.yml"
    )

    evidence = read_text(evidence_path)
    state = read_text(state_path)
    backlog = read_text(backlog_path)
    dod = read_text(dod_path)
    root_readme = read_text(root_readme_path)
    project_readme = read_text(project_readme_path)
    workflow = read_text(workflow_path)

    checks = [
        Check("W01D04 evidence exists", evidence_path.is_file()),
        Check("canonical state exists", state_path.is_file()),
        Check("backlog exists", backlog_path.is_file()),
        Check("root README exists", root_readme_path.is_file()),
        Check("project README exists", project_readme_path.is_file()),
        Check("workflow exists", workflow_path.is_file()),
        Check(
            "Definition of Done contains canonical-state rule",
            (
                dod_path.is_file()
                and "ubicación canónica con objetivo, estado, decisiones"
                in dod
            ),
        ),
        Check(
            "evidence contains W01D04 title",
            "# Evidencia de incremento · W01D04" in evidence,
        ),
        Check(
            "evidence contains project, day and date",
            all(
                marker in evidence
                for marker in (
                    "| Proyecto | EngineeringOS |",
                    "| Día de trabajo | W01D04 |",
                    "| Fecha de ejecución | 2026-08-03 |",
                )
            ),
        ),
        Check(
            "evidence identifies issue 14",
            (
                "https://github.com/JuanCarlosBP/"
                "portfolio/issues/14"
            )
            in evidence,
        ),
        Check(
            "evidence identifies working branch",
            (
                "| Rama | "
                "`docs/p01-w01d04-context-recovery` |"
            )
            in evidence,
        ),
        Check(
            "evidence identifies AM commit",
            AM_SHA in evidence,
        ),
        Check(
            "evidence identifies PM message",
            PM_MESSAGE in evidence,
        ),
        Check(
            "evidence remains En validación",
            "| Estado | En validación |" in evidence,
        ),
        Check(
            "evidence contains recovery section",
            "## Ejercicio de recuperación" in evidence,
        ),
        Check(
            "source is only the local repository",
            "| Fuente utilizada | Solo repositorio local |"
            in evidence,
        ),
        Check(
            "network was not used",
            "| Red utilizada | No |" in evidence,
        ),
        Check(
            "external-source count is zero",
            "| Fuentes externas | 0 |" in evidence,
        ),
        Check(
            "mode is autonomous during measurement",
            "| Modo | Autónomo durante la medición |"
            in evidence,
        ),
        Check(
            "guidance was absent during measurement",
            "| Ayuda durante la medición | No |"
            in evidence,
        ),
        Check(
            "focus recovered is EOS-005",
            "| Foco recuperado | EOS-005 |" in evidence,
        ),
        Check(
            "five fields were required",
            "| Campos requeridos | 5 |" in evidence,
        ),
        Check(
            "five fields were recovered",
            "| Campos recuperados | 5 |" in evidence,
        ),
        Check(
            "elapsed time is 83 seconds",
            "| Tiempo utilizado (segundos) | 83 |"
            in evidence,
        ),
        Check(
            "contradiction count is zero",
            "| Contradicciones | 0 |" in evidence,
        ),
        Check(
            "exercise record SHA is preserved",
            EXERCISE_SHA in evidence,
        ),
        Check(
            "all five answer rows exist",
            evidence_answer_rows_are_complete(evidence),
        ),
        Check(
            "evidence contains no unresolved placeholders",
            not bool(
                re.search(
                    r"\{\{[A-Z0-9_]+\}\}",
                    evidence,
                )
            ),
        ),
        Check(
            "state points to EOS-006",
            (
                "| Foco actual | "
                "`EOS-006 · Política de decisiones técnicas` |"
            )
            in state,
        ),
        Check(
            "EOS-006 is pending",
            "| Estado del foco actual | `Pendiente` |"
            in state,
        ),
        Check(
            "EOS-005 is the last completed item",
            (
                "| Último elemento completado | "
                "`EOS-005 · Recuperación de contexto` |"
            )
            in state,
        ),
        Check(
            "backlog summary marks EOS-005 terminated",
            (
                "| 5 | `EOS-005` | `P1` | "
                "Recuperación de contexto | Terminado | EOS-001 |"
            )
            in backlog,
        ),
        Check(
            "backlog detail marks EOS-005 terminated",
            bool(
                re.search(
                    r"(?ms)^## EOS-005 · Recuperación de contexto\n"
                    r".*?\*\*Estado:\*\* Terminado"
                    r".*?(?=^## EOS-006 ·)",
                    backlog,
                )
            ),
        ),
        Check(
            "root README reflects W01D04 and EOS-006",
            (
                "W01D04 · recuperación de contexto"
                in root_readme
                and "El siguiente paso priorizado "
                "de EngineeringOS es **EOS-006**"
                in root_readme
            ),
        ),
        Check(
            "project README reflects measured context gate",
            (
                "W01D04 · Recuperación de contexto"
                in project_readme
                and "36/36 comprobaciones"
                in project_readme
                and "83 segundos"
                in project_readme
            ),
        ),
        Check(
            "workflow executes context-recovery validator",
            (
                "Validate context recovery contract"
                in workflow
                and (
                    "python projects/engineeringos/tools/"
                    "validate_context_recovery.py"
                )
                in workflow
            ),
        ),
    ]

    if len(checks) != 36:
        raise RuntimeError(
            f"Internal contract error: {len(checks)} checks"
        )

    return checks


def main() -> int:
    """Run the validator and return a process exit code."""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
    )

    args = parser.parse_args()

    checks = validate(args.root.resolve())
    passed = sum(check.passed for check in checks)

    for check in checks:
        status = "PASS" if check.passed else "FAIL"
        print(f"[{status}] {check.name}")

    print(f"Checks: {passed}/{len(checks)} passed")

    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
