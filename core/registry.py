"""
registry.py — ISA registry for PPC2ARM.

Provides a central place to query:
  - Which instructions belong to a given ISA / capability / version tag.
  - Whether a given mnemonic is available for a requested mode/capability.
  - Fast iteration for the engine's search and list_categories methods.

The registry does NOT hold the instruction data itself; it imports from
data.ppc_instructions and data.arm_instructions.
"""

from __future__ import annotations

from typing import Optional

from data.isa_schema import ISACapability, MappingEntry


class ISARegistry:
    """
    Central registry for ISA instruction sets and capability queries.

    Usage
    -----
    reg = ISARegistry()
    ppc_instrs = reg.get_table("ppc")
    arm_instrs = reg.get_table("arm")
    ok = reg.mode_ok(entry_mode="both", requested_mode="64")
    cats = reg.categories("arm")
    """

    def __init__(self) -> None:
        # Lazy-import to keep module load fast
        from data.ppc_instructions import PPC_INSTRUCTIONS
        from data.arm_instructions import ARM_INSTRUCTIONS

        self._tables: dict[str, dict[str, dict]] = {
            "ppc": PPC_INSTRUCTIONS,
            "arm": ARM_INSTRUCTIONS,
        }

        # Registered capabilities by name
        self._capabilities: dict[str, ISACapability] = {}

    # ------------------------------------------------------------------
    # Table access
    # ------------------------------------------------------------------

    def get_table(self, isa: str) -> dict[str, dict]:
        """Return the instruction dict for *isa* ('ppc' or 'arm')."""
        isa = isa.lower()
        if isa not in self._tables:
            raise KeyError(f"Unknown ISA {isa!r}. Available: {list(self._tables)}")
        return self._tables[isa]

    def register_capability(self, cap: ISACapability) -> None:
        """Register an ISACapability so it can be queried by name."""
        self._capabilities[cap.name] = cap

    def get_capability(self, name: str) -> Optional[ISACapability]:
        """Return a registered ISACapability by name, or None."""
        return self._capabilities.get(name)

    # ------------------------------------------------------------------
    # Mode / variant filtering
    # ------------------------------------------------------------------

    @staticmethod
    def mode_ok(entry_mode: str, requested_mode: str) -> bool:
        """
        Return True when *entry_mode* is compatible with *requested_mode*.

        entry_mode   | requested_mode | result
        -------------|----------------|-------
        "both"       | any            | True
        any          | "both"         | True
        "32"         | "32"           | True
        "64"         | "64"           | True
        "32"         | "64"           | False
        """
        if entry_mode == "both" or requested_mode == "both":
            return True
        return entry_mode == requested_mode

    # ------------------------------------------------------------------
    # Category enumeration
    # ------------------------------------------------------------------

    def categories(self, isa: str) -> list[str]:
        """Return sorted unique category names for *isa*."""
        table = self.get_table(isa)
        return sorted({r.get("category", "other") for r in table.values()})

    # ------------------------------------------------------------------
    # Version / capability filtering
    # ------------------------------------------------------------------

    def instructions_for_version(
        self, isa: str, version_tag: str
    ) -> dict[str, dict]:
        """
        Return instructions from *isa* whose isa_versions list includes
        *version_tag* (or whose isa_versions list is empty, meaning 'all versions').
        """
        table = self.get_table(isa)
        result: dict[str, dict] = {}
        for mnemonic, record in table.items():
            vers = record.get("isa_versions", [])
            if not vers or version_tag in vers:
                result[mnemonic] = record
        return result

    # ------------------------------------------------------------------
    # Summary stats
    # ------------------------------------------------------------------

    def stats(self) -> dict[str, int]:
        """Return instruction counts keyed by ISA name."""
        return {isa: len(tbl) for isa, tbl in self._tables.items()}
