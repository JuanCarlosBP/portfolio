"""Tests for the executable EngineeringOS discovery quality gate."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

from validate_discovery import (  # noqa: E402
    COMMON_MARKERS,
    DOCUMENT_RULES,
    failures,
    validate_discovery,
)


class DiscoveryValidationTests(unittest.TestCase):
    """Protect the main risk: documentation without a verifiable contract."""

    def setUp(self) -> None:
        self._temporary_directory = tempfile.TemporaryDirectory()
        self.discovery_dir = Path(self._temporary_directory.name)
        self._write_complete_discovery()

    def tearDown(self) -> None:
        self._temporary_directory.cleanup()

    def _write_complete_discovery(self) -> None:
        for filename, specific_markers in DOCUMENT_RULES.items():
            content = "\n\n".join((*COMMON_MARKERS, *specific_markers))
            (self.discovery_dir / filename).write_text(
                f"{content}\n", encoding="utf-8"
            )

    def test_complete_discovery_passes_all_40_checks(self) -> None:
        checks = validate_discovery(self.discovery_dir)

        self.assertEqual(40, len(checks))
        self.assertEqual([], failures(checks))

    def test_missing_document_fails_its_10_checks(self) -> None:
        (self.discovery_dir / "success-metrics.md").unlink()

        failed = failures(validate_discovery(self.discovery_dir))

        self.assertEqual(10, len(failed))
        self.assertTrue(
            all(check.document == "success-metrics.md" for check in failed)
        )

    def test_missing_required_section_is_detected(self) -> None:
        path = self.discovery_dir / "problem-statement.md"
        content = path.read_text(encoding="utf-8")
        path.write_text(
            content.replace("## Problema principal", "## Otro apartado"),
            encoding="utf-8",
        )

        failed = failures(validate_discovery(self.discovery_dir))

        self.assertEqual(1, len(failed))
        self.assertIn("## Problema principal", failed[0].requirement)

    def test_draft_status_cannot_pass_the_gate(self) -> None:
        path = self.discovery_dir / "users-and-needs.md"
        content = path.read_text(encoding="utf-8")
        path.write_text(
            content.replace(
                "**Estado:** Validado en W01D01",
                "**Estado:** Borrador inicial",
            ),
            encoding="utf-8",
        )

        failed = failures(validate_discovery(self.discovery_dir))

        self.assertEqual(1, len(failed))
        self.assertEqual("users-and-needs.md", failed[0].document)
        self.assertIn("Validado en W01D01", failed[0].requirement)


if __name__ == "__main__":
    unittest.main()
