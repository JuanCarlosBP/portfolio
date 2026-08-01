"""Tests for the reusable EngineeringOS evidence quality gate."""

from __future__ import annotations

import re
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = PROJECT_ROOT / "tools"
CANONICAL_TEMPLATE = (
    PROJECT_ROOT
    / "docs"
    / "templates"
    / "increment-evidence-template.md"
)

sys.path.insert(0, str(TOOLS_DIR))

from validate_evidence import (  # noqa: E402
    failures,
    validate_evidence,
)


VALID_COMMAND_ROW = (
    "| 1 | `python3 -B -m unittest` | 0 | "
    "21/21 | Salida local |"
)

VALID_METRIC_ROW = (
    "| Observada | Pruebas | 21/21 | "
    "Ejecución local | Suite completa verde |"
)


def build_valid_evidence() -> str:
    """Return one complete evidence document."""

    return """# Evidencia de incremento · W01D03

## Metadatos

| Campo | Valor |
|---|---|
| Proyecto | EngineeringOS |
| Día de trabajo | W01D03 |
| Fecha de ejecución | 2026-08-01 |
| Issue | https://github.com/JuanCarlosBP/portfolio/issues/12 |
| Rama | `docs/p01-w01d03-evidence-template` |
| Commit AM | `376d9263e4b2a91f2e10e9f4ae87c4ca86e2b50d` |
| Commit PM | `test(w0013pm): discovery engineeringos` |
| Estado | En validación |
| Versión de la plantilla | `1.0.0` |

## Propósito

**Problema:** Evidencias sin estructura común.

**Usuario o destinatario:** Responsable de EngineeringOS.

**Resultado empresarial perseguido:** Reducir pérdida de contexto.

**Resultado observable esperado:** Contrato reutilizable validado.

## Alcance

### Incluido

- Plantilla, validador, pruebas y documentación.

### Fuera de alcance

- CLI, release e interfaz gráfica.

## Hechos observados

- La plantilla existe y el incremento AM está publicado.

## Objetivos aún no verificados

- Crear el commit PM, la PR y verificar la CI.

## Comandos y resultados

| Orden | Comando | Código de salida | Resultado observado | Evidencia |
|---:|---|---:|---|---|
| 1 | `python3 -B -m unittest` | 0 | 21/21 | Salida local |

## Métricas

| Clase | Señal | Valor | Fuente | Interpretación |
|---|---|---|---|---|
| Observada | Pruebas | 21/21 | Ejecución local | Suite completa verde |
| Objetivo | CI remota | Pendiente | Issue 12 | Requiere PR |

## Decisión y trade-off

| Campo | Contenido |
|---|---|
| Decisión | Plantilla Markdown con validador Python |
| Alternativa descartada | Formulario externo |
| Ventaja obtenida | Versionado y reproducibilidad |
| Coste o inconveniente aceptado | Cumplimentación manual |
| Criterio de revisión | Fricción repetida y medida |

## Riesgos y limitaciones

| Tipo | Descripción | Mitigación o tratamiento | Estado |
|---|---|---|---|
| Limitación | La semántica requiere revisión humana | Revisión en PR | Conocida |

## Impacto documental

| Superficie revisada | Decisión | Resultado |
|---|---|---|
| `README.md` raíz | Actualizar | Reflejar W01D03 y EOS-005 |
| `projects/engineeringos/README.md` | Actualizar | Documentar el nuevo gate |
| Changelog | Actualizar | Registrar W01D03 |
| Backlog | Actualizar | EOS-004 terminado |
| Definition of Done | Actualizar | Incorporar plantilla |

## Trazabilidad y enlaces canónicos

| Elemento | URL o ruta canónica | Finalidad |
|---|---|---|
| Issue | Metadatos superiores | Contrato del incremento |
| Pull request | Pendiente de creación | Integración |
| CI | Pendiente de ejecución | Validación remota |
| Commit AM | Historial Git | Incremento de documentación |
| Commit PM | Mensaje registrado | Incremento de validación |
| Archivo o evidencia principal | `docs/evidence/w01d03-validation.md` | Evidencia |

## Siguiente acción

- Ejecutar EOS-005 mediante un ejercicio real de recuperación de contexto.

## Reglas de uso

1. No presentar objetivos como resultados observados.
2. No duplicar fuentes canónicas.
"""


class EvidenceValidationTests(unittest.TestCase):
    """Protect evidence from becoming an unverifiable manual claim."""

    def setUp(self) -> None:
        self._temporary_directory = tempfile.TemporaryDirectory()
        self.project_root = Path(self._temporary_directory.name)

        self.template_path = (
            self.project_root
            / "docs"
            / "templates"
            / "increment-evidence-template.md"
        )

        self.evidence_path = (
            self.project_root
            / "docs"
            / "evidence"
            / "w01d03-validation.md"
        )

        self.template_path.parent.mkdir(parents=True)
        self.evidence_path.parent.mkdir(parents=True)

        self.template_path.write_text(
            CANONICAL_TEMPLATE.read_text(encoding="utf-8"),
            encoding="utf-8",
        )

        self.evidence_path.write_text(
            build_valid_evidence(),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self._temporary_directory.cleanup()

    def test_complete_contract_passes_all_46_checks(self) -> None:
        checks = validate_evidence(self.project_root)

        self.assertEqual(46, len(checks))
        self.assertEqual([], failures(checks))

    def test_missing_contract_files_are_detected(self) -> None:
        cases = [
            (
                self.template_path,
                "increment-evidence-template.md",
            ),
            (
                self.evidence_path,
                "w01d03-validation.md",
            ),
        ]

        for path, document in cases:
            with self.subTest(document=document):
                original = path.read_text(encoding="utf-8")
                path.unlink()

                failed = failures(
                    validate_evidence(self.project_root)
                )

                self.assertTrue(
                    any(
                        check.document == document
                        and check.requirement == "file exists"
                        for check in failed
                    )
                )

                path.write_text(
                    original,
                    encoding="utf-8",
                )

    def test_unresolved_placeholder_is_detected(self) -> None:
        content = self.evidence_path.read_text(encoding="utf-8")

        self.evidence_path.write_text(
            content.replace(
                "| Proyecto | EngineeringOS |",
                "| Proyecto | {{PROJECT}} |",
                1,
            ),
            encoding="utf-8",
        )

        failed = failures(
            validate_evidence(self.project_root)
        )

        self.assertTrue(
            any(
                check.requirement
                == "contains no unresolved placeholders"
                for check in failed
            )
        )

    def test_duplicate_heading_is_detected(self) -> None:
        content = self.evidence_path.read_text(encoding="utf-8")

        self.evidence_path.write_text(
            content + "\n## Propósito\n\nDuplicado.\n",
            encoding="utf-8",
        )

        failed = failures(
            validate_evidence(self.project_root)
        )

        self.assertTrue(
            any(
                check.requirement
                == "uses unique required headings"
                for check in failed
            )
        )

    def test_incomplete_command_or_risk_row_is_detected(self) -> None:
        original = self.evidence_path.read_text(encoding="utf-8")

        cases = [
            (
                VALID_COMMAND_ROW,
                (
                    "| 1 | `python3 -B -m unittest` | "
                    "0 | | Salida local |"
                ),
                "contains complete command rows",
            ),
            (
                (
                    "| Limitación | La semántica requiere revisión humana "
                    "| Revisión en PR | Conocida |"
                ),
                (
                    "| Limitación | La semántica requiere revisión humana "
                    "| | Conocida |"
                ),
                (
                    "contains complete closure and "
                    "traceability sections"
                ),
            ),
        ]

        for source, replacement, requirement in cases:
            with self.subTest(requirement=requirement):
                mutated = original.replace(
                    source,
                    replacement,
                    1,
                )

                self.assertNotEqual(
                    original,
                    mutated,
                )

                self.evidence_path.write_text(
                    mutated,
                    encoding="utf-8",
                )

                failed = failures(
                    validate_evidence(self.project_root)
                )

                self.assertTrue(
                    any(
                        check.requirement == requirement
                        for check in failed
                    )
                )

        self.evidence_path.write_text(
            original,
            encoding="utf-8",
        )

    def test_invalid_exit_code_is_detected(self) -> None:
        content = self.evidence_path.read_text(encoding="utf-8")

        self.evidence_path.write_text(
            content.replace(
                VALID_COMMAND_ROW,
                (
                    "| 1 | `python3 -B -m unittest` | "
                    "success | 21/21 | Salida local |"
                ),
                1,
            ),
            encoding="utf-8",
        )

        failed = failures(
            validate_evidence(self.project_root)
        )

        self.assertTrue(
            any(
                check.requirement
                == "uses integer command exit codes"
                for check in failed
            )
        )

    def test_invalid_metric_class_is_detected(self) -> None:
        content = self.evidence_path.read_text(encoding="utf-8")

        self.evidence_path.write_text(
            content.replace(
                VALID_METRIC_ROW,
                (
                    "| Medida | Pruebas | 21/21 | "
                    "Ejecución local | Suite completa verde |"
                ),
                1,
            ),
            encoding="utf-8",
        )

        failed = failures(
            validate_evidence(self.project_root)
        )

        self.assertTrue(
            any(
                check.requirement
                == "uses only allowed metric classes"
                for check in failed
            )
        )

    def test_missing_observed_metric_is_detected(self) -> None:
        content = self.evidence_path.read_text(encoding="utf-8")

        self.evidence_path.write_text(
            content.replace(
                "| Observada | Pruebas |",
                "| Objetivo | Pruebas |",
                1,
            ),
            encoding="utf-8",
        )

        failed = failures(
            validate_evidence(self.project_root)
        )

        self.assertTrue(
            any(
                check.requirement
                == "contains at least one observed metric"
                for check in failed
            )
        )

    def test_empty_fact_or_objective_section_is_detected(self) -> None:
        cases = [
            (
                "## Hechos observados",
                "contains substantive observed facts",
            ),
            (
                "## Objetivos aún no verificados",
                "contains substantive unverified objectives",
            ),
        ]

        original = self.evidence_path.read_text(encoding="utf-8")

        for heading, requirement in cases:
            with self.subTest(heading=heading):
                pattern = re.compile(
                    rf"({re.escape(heading)}\n)"
                    rf".*?"
                    rf"(?=\n## )",
                    flags=re.DOTALL,
                )

                mutated, count = pattern.subn(
                    rf"\1\n",
                    original,
                    count=1,
                )

                self.assertEqual(1, count)

                self.evidence_path.write_text(
                    mutated,
                    encoding="utf-8",
                )

                failed = failures(
                    validate_evidence(self.project_root)
                )

                self.assertTrue(
                    any(
                        check.requirement == requirement
                        for check in failed
                    )
                )

                self.evidence_path.write_text(
                    original,
                    encoding="utf-8",
                )

    def test_duplicate_canonical_url_is_detected(self) -> None:
        content = self.evidence_path.read_text(encoding="utf-8")

        self.evidence_path.write_text(
            content.replace(
                "| Pull request | Pendiente de creación |",
                (
                    "| Pull request | "
                    "https://github.com/JuanCarlosBP/portfolio/issues/12 |"
                ),
                1,
            ),
            encoding="utf-8",
        )

        failed = failures(
            validate_evidence(self.project_root)
        )

        self.assertTrue(
            any(
                check.requirement
                == "uses canonical URLs without duplication"
                for check in failed
            )
        )

    def test_missing_readme_impact_is_detected(self) -> None:
        content = self.evidence_path.read_text(encoding="utf-8")

        self.evidence_path.write_text(
            content.replace(
                (
                    "| `README.md` raíz | Actualizar | "
                    "Reflejar W01D03 y EOS-005 |"
                ),
                "| `README.md` raíz | | |",
                1,
            ),
            encoding="utf-8",
        )

        failed = failures(
            validate_evidence(self.project_root)
        )

        self.assertTrue(
            any(
                check.requirement
                == (
                    "records completed impact decisions "
                    "for both README files"
                )
                for check in failed
            )
        )


if __name__ == "__main__":
    unittest.main()
