"""
isa_schema.py — Dataclass definitions for PPC2ARM.

All instruction records, mapping entries, and ISA capability descriptors
are validated against these schemas.  The registry and engine import from
here so there is a single source of truth.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Instruction:
    """A single ISA instruction record."""
    mnemonic:     str
    full_name:    str
    syntax:       str
    description:  str
    flags:        list[str]       = field(default_factory=list)
    variants:     str             = "both"   # "32" | "64" | "both"
    category:     str             = "integer"
    encoding:     str             = ""
    isa_versions: list[str]       = field(default_factory=list)
    # e.g. ["ARMv8.0-A", "ARMv8.2-A"] or ["PowerISA-2.07", "PowerISA-3.1"]


@dataclass
class MappingEntry:
    """Bidirectional translation mapping between two ISA mnemonics."""
    source:     str              # canonical mnemonic of the source ISA
    targets:    list[str]        # one or more destination mnemonics
    confidence: str              # "direct" | "close" | "suggestion" | "none"
    notes:      str              # human-readable porting notes
    mode:       str = "both"     # "32" | "64" | "both"


@dataclass
class ISACapability:
    """
    Describes an ISA extension or version gate.
    Used by the registry to answer capability queries like
    "does this instruction require SVE?" or "is this PowerISA 3.0+?"
    """
    name:         str            # e.g. "ARMv8.2-A", "NEON", "SVE", "SME", "PowerISA-3.1"
    display_name: str
    description:  str
    parent:       Optional[str] = None   # parent capability/version, if any
    since_year:   Optional[int] = None


# ---------------------------------------------------------------------------
# Well-known capability constants
# ---------------------------------------------------------------------------

# ARM
CAP_AARCH32    = ISACapability("AArch32",    "AArch32",    "32-bit ARM execution state (ARMv7-A compatible)", None, 2011)
CAP_AARCH64    = ISACapability("AArch64",    "AArch64",    "64-bit ARM execution state, introduced in ARMv8-A", None, 2013)
CAP_ARMV8_0    = ISACapability("ARMv8.0-A",  "ARMv8.0-A",  "Baseline ARMv8-A: AArch32 + AArch64", "AArch64", 2011)
CAP_ARMV8_1    = ISACapability("ARMv8.1-A",  "ARMv8.1-A",  "ARMv8.1: LSE atomics, limited SIMD enhancements", "ARMv8.0-A", 2016)
CAP_ARMV8_2    = ISACapability("ARMv8.2-A",  "ARMv8.2-A",  "ARMv8.2: FP16, dot product, statistical profiling", "ARMv8.1-A", 2017)
CAP_ARMV8_3    = ISACapability("ARMv8.3-A",  "ARMv8.3-A",  "ARMv8.3: pointer auth, JSConv", "ARMv8.2-A", 2018)
CAP_ARMV8_4    = ISACapability("ARMv8.4-A",  "ARMv8.4-A",  "ARMv8.4: nested virtualization, MPAM, DIT", "ARMv8.3-A", 2019)
CAP_ARMV8_5    = ISACapability("ARMv8.5-A",  "ARMv8.5-A",  "ARMv8.5: MTE, BTI, RNG", "ARMv8.4-A", 2019)
CAP_ARMV9_0    = ISACapability("ARMv9.0-A",  "ARMv9.0-A",  "ARMv9: mandatory SVE2, realm management extension", "ARMv8.5-A", 2021)
CAP_ARMV9_2    = ISACapability("ARMv9.2-A",  "ARMv9.2-A",  "ARMv9.2: RME, Confidential Compute Architecture", "ARMv9.0-A", 2022)
CAP_NEON       = ISACapability("NEON",        "NEON/ASIMD", "Advanced SIMD (NEON/ASIMD): 128-bit SIMD for ARM", "AArch64", 2011)
CAP_SVE        = ISACapability("SVE",         "SVE",        "Scalable Vector Extension: variable-width vectors", "ARMv8.2-A", 2016)
CAP_SVE2       = ISACapability("SVE2",        "SVE2",       "SVE2: extended predication and crypto", "ARMv9.0-A", 2021)
CAP_SME        = ISACapability("SME",         "SME",        "Scalable Matrix Extension: matrix outer-product tiles", "ARMv9.2-A", 2022)

# Power
CAP_POWER_207  = ISACapability("PowerISA-2.07", "PowerISA 2.07", "Power ISA 2.07 (POWER8 era)", None, 2013)
CAP_POWER_300  = ISACapability("PowerISA-3.00", "PowerISA 3.00", "Power ISA 3.00 (POWER9 era)", "PowerISA-2.07", 2017)
CAP_POWER_310  = ISACapability("PowerISA-3.1",  "PowerISA 3.1",  "Power ISA 3.1 (POWER10 era)", "PowerISA-3.00", 2020)
