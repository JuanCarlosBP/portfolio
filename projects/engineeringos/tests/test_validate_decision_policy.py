"""Tests for the EngineeringOS decision-policy validator."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


VALIDATOR = (
    Path(__file__).resolve().parents[1]
    / "tools"
    / "validate_decision_policy.py"
)


class DecisionPolicyValidatorTests(unittest.TestCase):
    """Exercise the valid contract and principal failures."""

    def setUp(self) -> None:
        self.temp_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_directory.cleanup)

        self.root = Path(self.temp_directory.name)
        self._write_valid_fixture()

    def write(
        self,
        relative: str,
        content: str,
    ) -> None:
        path = self.root / relative

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

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

    def run_gate(
        self,
    ) -> subprocess.CompletedProcess[str]:
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

    @staticmethod
    def policy_text() -> str:
        headings = (
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

        metadata = "\n".join(
            (
                "**Proyecto:** EngineeringOS",
                "**Elemento de backlog:** `EOS-006`",
                "**Día de trabajo:** `W01D05`",
                "**Fecha de ejecución:** `2026-08-05`",
                (
                    "**Issue:** [#16]("
                    "https://github.com/JuanCarlosBP/"
                    "portfolio/issues/16)"
                ),
                "**Estado:** Validada",
                "**Versión de la política:** `1.0.0`",
            )
        )

        levels = "\n".join(
            (
                "| `ADR` | decisión | ruta |",
                "| `LOCAL_NOTE` | decisión | ruta |",
                "| `NO_EXTRA_RECORD` | decisión | ruta |",
                "ADR > LOCAL_NOTE > NO_EXTRA_RECORD",
            )
        )

        algorithm = "\n".join(
            f"### Paso {number} · Paso"
            for number in range(1, 7)
        )

        adr_ids = "\n".join(
            f"`ADR-{number:02d}`"
            for number in range(1, 11)
        )

        local_ids = "\n".join(
            f"`LOCAL-{number:02d}`"
            for number in range(1, 7)
        )

        trivial_ids = "\n".join(
            f"`TRIV-{number:02d}`"
            for number in range(1, 8)
        )

        content_ids = "\n".join(
            f"`ADR-CONTENT-{number:02d}`"
            for number in range(1, 9)
        )

        states = "\n".join(
            f"`{state}`"
            for state in (
                "Propuesta",
                "Aceptada",
                "Rechazada",
                "Sustituida",
                "Obsoleta",
            )
        )

        return "\n".join(
            (
                "\n\n".join(headings),
                metadata,
                levels,
                algorithm,
                adr_ids,
                local_ids,
                trivial_ids,
                content_ids,
                states,
                "technical-decision-policy.md",
                "adr-template.md",
                "local-decision-note-template.md",
                "#16",
                "",
            )
        )

    @staticmethod
    def adr_template_text() -> str:
        headings = (
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

        checkboxes = "\n".join(
            f"- [ ] criterio {number}"
            for number in range(1, 11)
        )

        return "\n".join(
            (
                "\n\n".join(headings),
                "**Estado:** {{STATUS}}",
                "**Fecha:** {{DATE}}",
                "TEMPLATE_INSTRUCTION",
                checkboxes,
                "",
            )
        )

    @staticmethod
    def local_template_text() -> str:
        headings = (
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

        checkboxes = "\n".join(
            f"- [ ] criterio {number}"
            for number in range(1, 11)
        )

        return "\n".join(
            (
                "\n\n".join(headings),
                "**Nivel elegido:** `LOCAL_NOTE`",
                "TEMPLATE_INSTRUCTION",
                checkboxes,
                "",
            )
        )

    @staticmethod
    def adr_text() -> str:
        headings = (
            "## Contexto",
            "## Desencadenantes aplicables",
            "## Decisión",
            "## Alternativas consideradas",
            "## Consecuencias",
            "## Trade-off aceptado",
            "## Plan de reversión",
            "## Criterio de revisión",
            (
                "## Compatibilidad con "
                "decisiones anteriores"
            ),
            "## Trazabilidad",
        )

        alternatives = "\n".join(
            f"### Alternativa {letter} · Opción"
            for letter in "ABCD"
        )

        return "\n".join(
            (
                "# ADR-0003 · Política",
                "",
                "**Estado:** Aceptada",
                (
                    "**Decisión relacionada:** "
                    "W01D05 · EOS-006"
                ),
                (
                    "**Issue:** [#16]("
                    "https://github.com/JuanCarlosBP/"
                    "portfolio/issues/16)"
                ),
                "",
                "\n\n".join(headings),
                alternatives,
                "`ADR-01`",
                "`ADR-02`",
                "`ADR-08`",
                "`ADR-10`",
                (
                    "ADR-0001 y ADR-0002 "
                    "conservan su validez histórica."
                ),
                "technical-decision-policy.md",
                "adr-template.md",
                "local-decision-note-template.md",
                "#16",
                "",
            )
        )

    @staticmethod
    def local_note_text() -> str:
        headings = (
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

        rules = "\n".join(
            f"`LOCAL-{number:02d}`"
            for number in range(1, 7)
        )

        checkboxes = "\n".join(
            f"- [x] criterio {number}"
            for number in range(1, 11)
        )

        return "\n".join(
            (
                "# Nota local · Workflow",
                "",
                "**Nivel elegido:** `LOCAL_NOTE`",
                "",
                "\n\n".join(headings),
                rules,
                checkboxes,
                "technical-decision-policy.md",
                "adr-template.md",
                "local-decision-note-template.md",
                "#16",
                "",
            )
        )

    def _write_valid_fixture(self) -> None:
        self.write(
            (
                "projects/engineeringos/docs/standards/"
                "technical-decision-policy.md"
            ),
            self.policy_text(),
        )

        self.write(
            (
                "projects/engineeringos/docs/templates/"
                "adr-template.md"
            ),
            self.adr_template_text(),
        )

        self.write(
            (
                "projects/engineeringos/docs/templates/"
                "local-decision-note-template.md"
            ),
            self.local_template_text(),
        )

        self.write(
            (
                "projects/engineeringos/docs/adr/"
                "ADR-0003-technical-decision-policy.md"
            ),
            self.adr_text(),
        )

        self.write(
            (
                "projects/engineeringos/docs/decisions/"
                "local/"
                "w01d05-reuse-existing-workflow.md"
            ),
            self.local_note_text(),
        )

        self.write(
            (
                "projects/engineeringos/docs/planning/"
                "backlog.md"
            ),
            (
                "| 6 | `EOS-006` | `P1` | "
                "Política de decisiones técnicas | "
                "Terminado | EOS-001 |\n"
                "| 7 | `EOS-007` | `P1` | "
                "Medición | Pendiente | EOS-004 |\n"
            ),
        )

        self.write(
            (
                "projects/engineeringos/docs/state/"
                "current-state.md"
            ),
            "\n".join(
                (
                    "| Día lógico cerrado | `W01D05` |",
                    (
                        "| Foco actual | `EOS-007 · "
                        "Medición de carga administrativa` |"
                    ),
                    (
                        "| Estado del foco actual | "
                        "`Pendiente` |"
                    ),
                    (
                        "| Issue cerrada | [#16]("
                        "https://github.com/JuanCarlosBP/"
                        "portfolio/issues/16) |"
                    ),
                    (
                        "| Último elemento completado | "
                        "`EOS-006 · Política de decisiones técnicas` |"
                    ),
                    "| Rama activa | Ninguna |",
                    "",
                )
            ),
        )

    def test_valid_contract_passes_all_44_checks(
        self,
    ) -> None:
        result = self.run_gate()

        self.assertEqual(
            result.returncode,
            0,
            result.stdout,
        )

        self.assertIn(
            "Checks: 44/44 passed",
            result.stdout,
        )

    def test_missing_policy_fails(self) -> None:
        (
            self.root
            / "projects/engineeringos/docs/standards/"
            "technical-decision-policy.md"
        ).unlink()

        self.assertNotEqual(
            self.run_gate().returncode,
            0,
        )

    def test_missing_adr_trigger_fails(self) -> None:
        self.replace(
            (
                "projects/engineeringos/docs/standards/"
                "technical-decision-policy.md"
            ),
            "`ADR-10`",
            "`ADR-11`",
        )

        self.assertNotEqual(
            self.run_gate().returncode,
            0,
        )

    def test_duplicate_local_rule_fails(self) -> None:
        self.replace(
            (
                "projects/engineeringos/docs/standards/"
                "technical-decision-policy.md"
            ),
            "`LOCAL-06`",
            "`LOCAL-05`",
        )

        self.assertNotEqual(
            self.run_gate().returncode,
            0,
        )

    def test_unresolved_policy_placeholder_fails(
        self,
    ) -> None:
        relative = (
            "projects/engineeringos/docs/standards/"
            "technical-decision-policy.md"
        )

        self.write(
            relative,
            self.read(relative) + "{{UNRESOLVED}}\n",
        )

        self.assertNotEqual(
            self.run_gate().returncode,
            0,
        )

    def test_incomplete_adr_template_fails(
        self,
    ) -> None:
        self.replace(
            (
                "projects/engineeringos/docs/templates/"
                "adr-template.md"
            ),
            "## Criterio de revisión",
            "## Revisión eliminada",
        )

        self.assertNotEqual(
            self.run_gate().returncode,
            0,
        )

    def test_invalid_adr_status_fails(self) -> None:
        self.replace(
            (
                "projects/engineeringos/docs/adr/"
                "ADR-0003-technical-decision-policy.md"
            ),
            "**Estado:** Aceptada",
            "**Estado:** Borrador",
        )

        self.assertNotEqual(
            self.run_gate().returncode,
            0,
        )

    def test_unchecked_real_local_note_fails(
        self,
    ) -> None:
        self.replace(
            (
                "projects/engineeringos/docs/decisions/"
                "local/"
                "w01d05-reuse-existing-workflow.md"
            ),
            "- [x] criterio 1",
            "- [ ] criterio 1",
        )

        self.assertNotEqual(
            self.run_gate().returncode,
            0,
        )

    def test_multiple_active_backlog_items_fail(
        self,
    ) -> None:
        self.replace(
            (
                "projects/engineeringos/docs/planning/"
                "backlog.md"
            ),
            "Medición | Pendiente |",
            "Medición | En curso |",
        )

        self.assertNotEqual(
            self.run_gate().returncode,
            0,
        )

    def test_non_pending_current_state_fails(
        self,
    ) -> None:
        self.replace(
            (
                "projects/engineeringos/docs/state/"
                "current-state.md"
            ),
            (
                "| Estado del foco actual | "
                "`Pendiente` |"
            ),
            (
                "| Estado del foco actual | "
                "`En curso` |"
            ),
        )

        self.assertNotEqual(
            self.run_gate().returncode,
            0,
        )


if __name__ == "__main__":
    unittest.main()
