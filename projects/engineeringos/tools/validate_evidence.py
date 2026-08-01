#!/usr/bin/env python3
"""Validate the reusable EngineeringOS evidence contract."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ISSUE_URL = "https://github.com/JuanCarlosBP/portfolio/issues/12"
BRANCH = "docs/p01-w01d03-evidence-template"
AM_SHA = "376d9263e4b2a91f2e10e9f4ae87c4ca86e2b50d"
PM_COMMIT_MESSAGE = "test(w0013pm): discovery engineeringos"

EXPECTED_TEMPLATE_PLACEHOLDERS = Counter(
    {
        "PROJECT": 1,
        "DAY_ID": 2,
        "EXECUTION_DATE": 1,
        "ISSUE_URL": 1,
        "BRANCH": 1,
        "AM_COMMIT": 1,
        "PM_COMMIT_MESSAGE": 1,
        "STATUS": 1,
    }
)

ALLOWED_METRIC_CLASSES = {
    "Observada",
    "Objetivo",
    "No medida",
}

COMMAND_TABLE_HEADER = (
    "| Orden | Comando | Código de salida | "
    "Resultado observado | Evidencia |"
)

METRIC_TABLE_HEADER = (
    "| Clase | Señal | Valor | Fuente | Interpretación |"
)

IMPACT_TABLE_HEADER = (
    "| Superficie revisada | Decisión | Resultado |"
)

RISK_TABLE_HEADER = (
    "| Tipo | Descripción | Mitigación o tratamiento | Estado |"
)


@dataclass(frozen=True)
class Check:
    """One deterministic evidence validation result."""

    document: str
    requirement: str
    passed: bool


def read_text(path: Path) -> str:
    """Read UTF-8 text or return an empty string for an absent file."""

    if not path.is_file():
        return ""

    return path.read_text(encoding="utf-8")


def extract_section(content: str, heading: str) -> str:
    """Return the body following one level-two Markdown heading."""

    pattern = re.compile(
        rf"^{re.escape(heading)}\n"
        rf"(?P<body>.*?)(?=^## |\Z)",
        flags=re.MULTILINE | re.DOTALL,
    )

    match = pattern.search(content)

    if match is None:
        return ""

    return match.group("body").strip()


def parse_table_rows(
    section: str,
    expected_header: str,
) -> list[list[str]]:
    """Parse data rows from one Markdown table."""

    lines = section.splitlines()

    try:
        header_index = lines.index(expected_header)
    except ValueError:
        return []

    if header_index + 1 >= len(lines):
        return []

    separator = lines[header_index + 1].strip()

    if not separator.startswith("|---"):
        return []

    rows: list[list[str]] = []

    for line in lines[header_index + 2 :]:
        stripped = line.strip()

        if not stripped:
            if rows:
                break

            continue

        if not stripped.startswith("|"):
            if rows:
                break

            continue

        cells = [
            cell.strip()
            for cell in stripped.strip("|").split("|")
        ]

        rows.append(cells)

    return rows


def heading_titles(content: str) -> list[str]:
    """Return all level-one to level-three Markdown heading titles."""

    return re.findall(
        r"^#{1,3}\s+(.+)$",
        content,
        flags=re.MULTILINE,
    )


def contains_substantive_bullet(section: str) -> bool:
    """Return whether a section contains at least one non-empty bullet."""

    return bool(
        re.search(
            r"^- \S.+$",
            section,
            flags=re.MULTILINE,
        )
    )


def canonical_urls(content: str) -> list[str]:
    """Extract canonical HTTPS URLs from Markdown and plain text."""

    return re.findall(
        r"https://[^\s|)>]+",
        content,
    )


def strip_code(value: str) -> str:
    """Remove inline-code delimiters from one table-cell value."""

    return value.replace("`", "").strip()


def readme_impact_is_complete(rows: list[list[str]]) -> bool:
    """Require completed decisions for both affected README files."""

    expected = {
        "README.md raíz",
        "projects/engineeringos/README.md",
    }

    completed: set[str] = set()

    for row in rows:
        if len(row) != 3:
            continue

        surface = strip_code(row[0])
        decision = row[1].strip()
        result = row[2].strip()

        if (
            surface in expected
            and decision
            and result
        ):
            completed.add(surface)

    return completed == expected


def validate_evidence(project_root: Path) -> list[Check]:
    """Return all 46 deterministic evidence-contract checks."""

    template_path = (
        project_root
        / "docs"
        / "templates"
        / "increment-evidence-template.md"
    )

    evidence_path = (
        project_root
        / "docs"
        / "evidence"
        / "w01d03-validation.md"
    )

    template = read_text(template_path)
    evidence = read_text(evidence_path)

    placeholder_counts = Counter(
        re.findall(
            r"\{\{([A-Z0-9_]+)\}\}",
            template,
        )
    )

    risk_rows = parse_table_rows(
        extract_section(
            evidence,
            "## Riesgos y limitaciones",
        ),
        RISK_TABLE_HEADER,
    )

    checks: list[Check] = [
        Check(
            "increment-evidence-template.md",
            "file exists",
            template_path.is_file(),
        ),
        Check(
            "increment-evidence-template.md",
            "contains the reusable evidence title",
            "# Evidencia de incremento · {{DAY_ID}}" in template,
        ),
        Check(
            "increment-evidence-template.md",
            "contains metadata",
            "## Metadatos" in template,
        ),
        Check(
            "increment-evidence-template.md",
            "uses the exact placeholder contract",
            placeholder_counts == EXPECTED_TEMPLATE_PLACEHOLDERS,
        ),
        Check(
            "increment-evidence-template.md",
            "contains purpose",
            "## Propósito" in template,
        ),
        Check(
            "increment-evidence-template.md",
            "contains scope",
            "## Alcance" in template,
        ),
        Check(
            "increment-evidence-template.md",
            "contains observed facts",
            "## Hechos observados" in template,
        ),
        Check(
            "increment-evidence-template.md",
            "contains unverified objectives",
            "## Objetivos aún no verificados" in template,
        ),
        Check(
            "increment-evidence-template.md",
            "contains commands and results",
            "## Comandos y resultados" in template,
        ),
        Check(
            "increment-evidence-template.md",
            "contains the command table contract",
            COMMAND_TABLE_HEADER in template,
        ),
        Check(
            "increment-evidence-template.md",
            "contains metrics",
            "## Métricas" in template,
        ),
        Check(
            "increment-evidence-template.md",
            "contains the metric table contract",
            METRIC_TABLE_HEADER in template,
        ),
        Check(
            "increment-evidence-template.md",
            "documents all allowed metric classes",
            all(
                f"`{metric_class}`" in template
                for metric_class in ALLOWED_METRIC_CLASSES
            ),
        ),
        Check(
            "increment-evidence-template.md",
            "contains decision and trade-off",
            "## Decisión y trade-off" in template,
        ),
        Check(
            "increment-evidence-template.md",
            "contains risks and limitations",
            "## Riesgos y limitaciones" in template,
        ),
        Check(
            "increment-evidence-template.md",
            "contains documentary impact",
            "## Impacto documental" in template,
        ),
        Check(
            "increment-evidence-template.md",
            "lists both affected README files",
            (
                "`README.md` raíz" in template
                and "`projects/engineeringos/README.md`" in template
            ),
        ),
        Check(
            "increment-evidence-template.md",
            "contains canonical traceability",
            "## Trazabilidad y enlaces canónicos" in template,
        ),
        Check(
            "increment-evidence-template.md",
            "contains the next action",
            "## Siguiente acción" in template,
        ),
        Check(
            "increment-evidence-template.md",
            "contains rules and explicit instructions",
            (
                "## Reglas de uso" in template
                and template.count("TEMPLATE_INSTRUCTION") >= 10
            ),
        ),
        Check(
            "increment-evidence-template.md",
            "places every placeholder in metadata or title",
            all(
                f"{{{{{placeholder}}}}}" in template
                for placeholder in EXPECTED_TEMPLATE_PLACEHOLDERS
            ),
        ),
        Check(
            "increment-evidence-template.md",
            "forbids unnecessary canonical-content duplication",
            (
                "No copiar información extensa que ya tenga una "
                "fuente canónica enlazable."
            )
            in template,
        ),
        Check(
            "w01d03-validation.md",
            "file exists",
            evidence_path.is_file(),
        ),
        Check(
            "w01d03-validation.md",
            "contains the W01D03 evidence title",
            "# Evidencia de incremento · W01D03" in evidence,
        ),
        Check(
            "w01d03-validation.md",
            "contains project, day and execution date metadata",
            all(
                marker in evidence
                for marker in (
                    "| Proyecto | EngineeringOS |",
                    "| Día de trabajo | W01D03 |",
                    "| Fecha de ejecución | 2026-08-01 |",
                )
            ),
        ),
        Check(
            "w01d03-validation.md",
            "identifies issue 12",
            ISSUE_URL in evidence,
        ),
        Check(
            "w01d03-validation.md",
            "identifies the working branch",
            f"| Rama | `{BRANCH}` |" in evidence,
        ),
        Check(
            "w01d03-validation.md",
            "identifies the AM commit",
            AM_SHA in evidence,
        ),
        Check(
            "w01d03-validation.md",
            "identifies the PM commit message",
            PM_COMMIT_MESSAGE in evidence,
        ),
        Check(
            "w01d03-validation.md",
            "uses the En validación state",
            "| Estado | En validación |" in evidence,
        ),
        Check(
            "w01d03-validation.md",
            "contains purpose",
            "## Propósito" in evidence,
        ),
        Check(
            "w01d03-validation.md",
            "contains scope",
            "## Alcance" in evidence,
        ),
        Check(
            "w01d03-validation.md",
            "contains observed facts",
            "## Hechos observados" in evidence,
        ),
        Check(
            "w01d03-validation.md",
            "contains unverified objectives",
            "## Objetivos aún no verificados" in evidence,
        ),
        Check(
            "w01d03-validation.md",
            "contains commands and metrics",
            (
                "## Comandos y resultados" in evidence
                and "## Métricas" in evidence
            ),
        ),
        Check(
            "w01d03-validation.md",
            "contains complete closure and traceability sections",
            (
                all(
                    marker in evidence
                    for marker in (
                        "## Decisión y trade-off",
                        "## Riesgos y limitaciones",
                        "## Impacto documental",
                        "## Trazabilidad y enlaces canónicos",
                        "## Siguiente acción",
                        "## Reglas de uso",
                    )
                )
                and bool(risk_rows)
                and all(
                    len(row) == 4
                    and all(
                        cell.strip()
                        for cell in row
                    )
                    for row in risk_rows
                )
            ),
        ),
    ]

    command_rows = parse_table_rows(
        extract_section(
            evidence,
            "## Comandos y resultados",
        ),
        COMMAND_TABLE_HEADER,
    )

    metric_rows = parse_table_rows(
        extract_section(
            evidence,
            "## Métricas",
        ),
        METRIC_TABLE_HEADER,
    )

    impact_rows = parse_table_rows(
        extract_section(
            evidence,
            "## Impacto documental",
        ),
        IMPACT_TABLE_HEADER,
    )

    titles = heading_titles(evidence)
    title_counts = Counter(titles)

    urls = canonical_urls(evidence)
    url_counts = Counter(urls)

    facts = extract_section(
        evidence,
        "## Hechos observados",
    )

    objectives = extract_section(
        evidence,
        "## Objetivos aún no verificados",
    )

    checks.extend(
        [
            Check(
                "w01d03-validation.md",
                "contains no unresolved placeholders",
                not bool(
                    re.search(
                        r"\{\{[A-Z0-9_]+\}\}",
                        evidence,
                    )
                ),
            ),
            Check(
                "w01d03-validation.md",
                "uses unique required headings",
                bool(titles)
                and all(
                    count == 1
                    for count in title_counts.values()
                ),
            ),
            Check(
                "w01d03-validation.md",
                "contains complete command rows",
                bool(command_rows)
                and all(
                    len(row) == 5
                    and all(cell.strip() for cell in row)
                    for row in command_rows
                ),
            ),
            Check(
                "w01d03-validation.md",
                "uses integer command exit codes",
                bool(command_rows)
                and all(
                    len(row) == 5
                    and bool(
                        re.fullmatch(
                            r"-?\d+",
                            row[2].strip(),
                        )
                    )
                    for row in command_rows
                ),
            ),
            Check(
                "w01d03-validation.md",
                "uses only allowed metric classes",
                bool(metric_rows)
                and all(
                    len(row) == 5
                    and row[0].strip()
                    in ALLOWED_METRIC_CLASSES
                    for row in metric_rows
                ),
            ),
            Check(
                "w01d03-validation.md",
                "contains at least one observed metric",
                any(
                    len(row) == 5
                    and row[0].strip() == "Observada"
                    for row in metric_rows
                ),
            ),
            Check(
                "w01d03-validation.md",
                "contains substantive observed facts",
                contains_substantive_bullet(facts),
            ),
            Check(
                "w01d03-validation.md",
                "contains substantive unverified objectives",
                contains_substantive_bullet(objectives),
            ),
            Check(
                "w01d03-validation.md",
                "uses canonical URLs without duplication",
                bool(urls)
                and all(
                    count == 1
                    for count in url_counts.values()
                ),
            ),
            Check(
                "w01d03-validation.md",
                "records completed impact decisions for both README files",
                readme_impact_is_complete(impact_rows),
            ),
        ]
    )

    if len(checks) != 46:
        raise RuntimeError(
            f"Evidence contract must contain 46 checks, got {len(checks)}"
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
        "EngineeringOS evidence quality gate",
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
            "Validate the W01D03 reusable EngineeringOS "
            "evidence contract."
        )
    )

    parser.add_argument(
        "--root",
        type=Path,
        default=default_root,
        help=(
            "EngineeringOS project root containing docs/templates "
            "and docs/evidence."
        ),
    )

    return parser


def main() -> int:
    """Run the quality gate and expose success through the exit code."""

    args = build_parser().parse_args()
    checks = validate_evidence(args.root)

    print(render_summary(checks))

    return 1 if failures(checks) else 0


if __name__ == "__main__":
    raise SystemExit(main())
