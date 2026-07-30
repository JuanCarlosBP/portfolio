"""Tests for the EngineeringOS planning quality gate."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

from validate_planning import (  # noqa: E402
    BACKLOG_MARKERS,
    DOD_MARKERS,
    EXPECTED_CORE_ITEMS,
    failures,
    validate_planning,
)


def build_valid_backlog() -> str:
    """Return a minimal backlog satisfying the executable contract."""

    rows = [
        "| 1 | `EOS-001` | `P0` | Contract | Terminado | W01D01 |",
        "| 2 | `EOS-002` | `P0` | Validator | Terminado | EOS-001 |",
        "| 3 | `EOS-003` | `P0` | Tests and CI | Terminado | EOS-002 |",
        "| 4 | `EOS-004` | `P1` | Evidence | Pendiente | EOS-001 |",
        "| 5 | `EOS-005` | `P1` | Context | Pendiente | EOS-001 |",
        "| 6 | `EOS-006` | `P1` | Decisions | Pendiente | EOS-001 |",
        "| 7 | `EOS-007` | `P1` | Overhead | Pendiente | EOS-004 |",
        "| 8 | `EOS-008` | `P2` | CLI | Pendiente | EOS-002 |",
        "| 9 | `EOS-009` | `P2` | Release | Pendiente | EOS-003 |",
        "| 10 | `EOS-010` | `P3` | GUI | Aparcada | Nueva evidencia |",
    ]

    headings = [
        f"## EOS-{number:03d} · Element"
        for number in range(1, 11)
    ]

    return (
        "\n\n".join(BACKLOG_MARKERS)
        + "\n\n"
        + "\n".join(rows)
        + "\n\n"
        + "\n\n".join(headings)
        + "\n"
    )


def build_valid_dod() -> str:
    """Return a minimal DoD satisfying the executable contract."""

    prefix = list(DOD_MARKERS[:9])
    suffix = list(DOD_MARKERS[9:])

    core = [
        f"- [ ] {item}"
        for item in EXPECTED_CORE_ITEMS
    ]

    return (
        "\n\n".join(prefix)
        + "\n"
        + "\n".join(core)
        + "\n\n"
        + "\n\n".join(suffix)
        + "\n"
    )


class PlanningValidationTests(unittest.TestCase):
    """Protect planning, WIP and closure from becoming manual claims."""

    def setUp(self) -> None:
        self._temporary_directory = tempfile.TemporaryDirectory()
        self.project_root = Path(self._temporary_directory.name)

        self.backlog_path = (
            self.project_root
            / "docs"
            / "planning"
            / "backlog.md"
        )

        self.dod_path = (
            self.project_root
            / "docs"
            / "standards"
            / "definition-of-done.md"
        )

        self.backlog_path.parent.mkdir(parents=True)
        self.dod_path.parent.mkdir(parents=True)

        self.backlog_path.write_text(
            build_valid_backlog(),
            encoding="utf-8",
        )

        self.dod_path.write_text(
            build_valid_dod(),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self._temporary_directory.cleanup()

    def test_complete_contract_passes_all_39_checks(self) -> None:
        checks = validate_planning(self.project_root)

        self.assertEqual(39, len(checks))
        self.assertEqual([], failures(checks))

    def test_missing_backlog_is_detected(self) -> None:
        self.backlog_path.unlink()

        failed = failures(
            validate_planning(self.project_root)
        )

        self.assertTrue(
            any(
                check.document == "backlog.md"
                and check.requirement == "file exists"
                for check in failed
            )
        )

    def test_missing_priority_policy_is_detected(self) -> None:
        content = self.backlog_path.read_text(encoding="utf-8")

        self.backlog_path.write_text(
            content.replace(
                "## Política de prioridad",
                "## Otra política",
            ),
            encoding="utf-8",
        )

        failed = failures(
            validate_planning(self.project_root)
        )

        self.assertTrue(
            any(
                "## Política de prioridad"
                in check.requirement
                for check in failed
            )
        )

    def test_invalid_priority_is_detected(self) -> None:
        content = self.backlog_path.read_text(encoding="utf-8")

        self.backlog_path.write_text(
            content.replace(
                "`P0`",
                "`PX`",
                1,
            ),
            encoding="utf-8",
        )

        failed = failures(
            validate_planning(self.project_root)
        )

        self.assertTrue(
            any(
                check.requirement
                == "uses only allowed priorities"
                for check in failed
            )
        )

    def test_multiple_active_items_fail_the_wip_rule(self) -> None:
        content = self.backlog_path.read_text(encoding="utf-8")

        content = content.replace(
            "| 1 | `EOS-001` | `P0` | Contract | "
            "Terminado | W01D01 |",
            "| 1 | `EOS-001` | `P0` | Contract | "
            "En curso | W01D01 |",
        )

        content = content.replace(
            "| 2 | `EOS-002` | `P0` | Validator | "
            "Terminado | EOS-001 |",
            "| 2 | `EOS-002` | `P0` | Validator | "
            "En validación | EOS-001 |",
        )

        self.backlog_path.write_text(
            content,
            encoding="utf-8",
        )

        failed = failures(
            validate_planning(self.project_root)
        )

        self.assertTrue(
            any(
                check.requirement
                == "respects WIP by having at most one active item"
                for check in failed
            )
        )

    def test_missing_mandatory_dod_item_is_detected(self) -> None:
        content = self.dod_path.read_text(encoding="utf-8")

        self.dod_path.write_text(
            content.replace(
                "- [ ] CI verde.\n",
                "",
            ),
            encoding="utf-8",
        )

        failed = failures(
            validate_planning(self.project_root)
        )

        self.assertTrue(
            any(
                check.requirement
                == "contains the exact six mandatory route criteria"
                for check in failed
            )
        )


if __name__ == "__main__":
    unittest.main()
