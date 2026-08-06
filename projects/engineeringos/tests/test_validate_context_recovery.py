"""Tests for the EngineeringOS context-recovery validator."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


VALIDATOR = (
    Path(__file__).resolve().parents[1]
    / "tools"
    / "validate_context_recovery.py"
)


class ContextRecoveryValidatorTests(unittest.TestCase):
    """Exercise the valid contract and relevant failures."""

    def setUp(self) -> None:
        self.temp_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_directory.cleanup)

        self.root = Path(self.temp_directory.name)
        self._write_valid_fixture()

    def write(self, relative: str, content: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            content,
            encoding="utf-8",
            newline="\n",
        )

    def read(self, relative: str) -> str:
        return (
            self.root
            / relative
        ).read_text(encoding="utf-8")

    def replace(
        self,
        relative: str,
        old: str,
        new: str,
    ) -> None:
        content = self.read(relative)

        self.assertIn(old, content)

        self.write(
            relative,
            content.replace(old, new, 1),
        )

    def run_gate(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                "-B",
                str(VALIDATOR),
                "--root",
                str(self.root),
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    def _write_valid_fixture(self) -> None:
        self.write(
            "projects/engineeringos/docs/evidence/"
            "w01d04-context-recovery.md",
            """# Evidencia de incremento · W01D04

| Proyecto | EngineeringOS |
| Día de trabajo | W01D04 |
| Fecha de ejecución | 2026-08-03 |
| Issue | https://github.com/JuanCarlosBP/portfolio/issues/14 |
| Rama | `docs/p01-w01d04-context-recovery` |
| Commit AM | `8b2e968f8aa1fd3f37da5d7cb43de622c5ab42c3` |
| Commit PM | `test(w0014pm): discovery engineeringos` |
| Estado | En validación |

## Ejercicio de recuperación

| Señal | Valor |
|---|---|
| Fuente utilizada | Solo repositorio local |
| Red utilizada | No |
| Fuentes externas | 0 |
| Modo | Autónomo durante la medición |
| Ayuda durante la medición | No |
| Foco recuperado | EOS-005 |
| Campos requeridos | 5 |
| Campos recuperados | 5 |
| Tiempo utilizado (segundos) | 83 |
| Contradicciones | 0 |

07c3e38e1ed7d812409c4920d5814e80f8383ccfb1291b7981f725f52cc3bea7

## Respuestas recuperadas

| Campo | Respuesta |
|---|---|
| Objetivo | válido |
| Estado | válido |
| Decisión vigente | válida |
| Bloqueos | válidos |
| Siguiente acción | válida |
""",
        )

        self.write(
            "projects/engineeringos/docs/state/current-state.md",
            """# Estado actual

| Foco actual | `EOS-007 · Medición de carga administrativa` |
| Estado del foco actual | `Pendiente` |
| Último elemento completado | `EOS-006 · Política de decisiones técnicas` |
""",
        )

        self.write(
            "projects/engineeringos/docs/planning/backlog.md",
            """| 6 | `EOS-006` | `P1` | Política de decisiones técnicas | Terminado | EOS-001 |

## EOS-006 · Política de decisiones técnicas

**Estado:** Terminado

## EOS-007 · Medición de carga administrativa
""",
        )

        self.write(
            "projects/engineeringos/docs/standards/"
            "definition-of-done.md",
            (
                "Existe una ubicación canónica con objetivo, "
                "estado, decisiones, bloqueos y siguiente acción.\n"
            ),
        )

        self.write(
            "README.md",
            (
                "W01D05 · política de decisiones técnicas\n"
                "El siguiente elemento priorizado "
                "es **EOS-007 · Medición de carga administrativa**\n"
            ),
        )

        self.write(
            "projects/engineeringos/README.md",
            (
                "W01D04 · Recuperación de contexto\n"
                "36/36 comprobaciones\n"
                "83 segundos\n"
            ),
        )

        self.write(
            ".github/workflows/engineeringos-discovery.yml",
            (
                "Validate context recovery contract\n"
                "python projects/engineeringos/tools/"
                "validate_context_recovery.py\n"
            ),
        )

    def test_valid_contract_passes(self) -> None:
        result = self.run_gate()

        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("Checks: 36/36 passed", result.stdout)

    def test_missing_evidence_fails(self) -> None:
        (
            self.root
            / "projects/engineeringos/docs/evidence/"
            "w01d04-context-recovery.md"
        ).unlink()

        self.assertNotEqual(self.run_gate().returncode, 0)

    def test_network_usage_fails(self) -> None:
        self.replace(
            "projects/engineeringos/docs/evidence/"
            "w01d04-context-recovery.md",
            "| Red utilizada | No |",
            "| Red utilizada | Sí |",
        )

        self.assertNotEqual(self.run_gate().returncode, 0)

    def test_external_source_fails(self) -> None:
        self.replace(
            "projects/engineeringos/docs/evidence/"
            "w01d04-context-recovery.md",
            "| Fuentes externas | 0 |",
            "| Fuentes externas | 1 |",
        )

        self.assertNotEqual(self.run_gate().returncode, 0)

    def test_wrong_elapsed_time_fails(self) -> None:
        self.replace(
            "projects/engineeringos/docs/evidence/"
            "w01d04-context-recovery.md",
            "| Tiempo utilizado (segundos) | 83 |",
            "| Tiempo utilizado (segundos) | 601 |",
        )

        self.assertNotEqual(self.run_gate().returncode, 0)

    def test_wrong_current_focus_fails(self) -> None:
        self.replace(
            "projects/engineeringos/docs/state/current-state.md",
            "EOS-007 · Medición de carga administrativa",
            "EOS-006 · Política de decisiones técnicas",
        )

        self.assertNotEqual(self.run_gate().returncode, 0)

    def test_unfinished_backlog_item_fails(self) -> None:
        relative = (
            "projects/engineeringos/docs/planning/backlog.md"
        )

        self.write(
            relative,
            self.read(relative).replace(
                "Terminado",
                "En validación",
            ),
        )

        self.assertNotEqual(self.run_gate().returncode, 0)

    def test_root_readme_without_next_item_fails(self) -> None:
        self.replace(
            "README.md",
            "EOS-007",
            "EOS-008",
        )

        self.assertNotEqual(self.run_gate().returncode, 0)

    def test_workflow_without_context_gate_fails(self) -> None:
        self.write(
            ".github/workflows/engineeringos-discovery.yml",
            "Validate evidence contract\n",
        )

        self.assertNotEqual(self.run_gate().returncode, 0)


if __name__ == "__main__":
    unittest.main()
