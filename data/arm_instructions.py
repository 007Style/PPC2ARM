"""
arm_instructions.py — ARM / AArch64 instruction database for PPC2ARM.

Keys are canonical uppercase mnemonics (e.g. "ADD", "LDR", "FMADD").
Values are dicts conforming to the Instruction schema from data.isa_schema.

Coverage
--------
- AArch64 base (ARMv8.0-A): integer, load/store, branch, system
- AArch32 legacy aliases where relevant
- FP (scalar, ARMv8-A VFPv4/FPv5)
- NEON / Advanced SIMD (128-bit vector)
- SVE / SVE2 (scalable vector)
- LSE atomics (ARMv8.1-A)
- Selected ARMv8.3–ARMv9 extensions
"""

from __future__ import annotations

ARM_INSTRUCTIONS: dict[str, dict] = {

    # ------------------------------------------------------------------ #
    #  INTEGER ARITHMETIC — AArch64                                        #
    # ------------------------------------------------------------------ #

    "ADD": {
        "mnemonic": "ADD", "full_name": "Add",
        "syntax": "Xd, Xn, Xm | Xd, Xn, #imm",
        "description": "Adds two registers or a register and an immediate; places the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (register/immediate)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "ADDS": {
        "mnemonic": "ADDS", "full_name": "Add, setting flags",
        "syntax": "Xd, Xn, Xm | Xd, Xn, #imm",
        "description": "Adds two values, sets NZCV condition flags, and places result in Xd.",
        "flags": ["N", "Z", "C", "V"], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "SUB": {
        "mnemonic": "SUB", "full_name": "Subtract",
        "syntax": "Xd, Xn, Xm | Xd, Xn, #imm",
        "description": "Subtracts the second operand from the first and places the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "SUBS": {
        "mnemonic": "SUBS", "full_name": "Subtract, setting flags",
        "syntax": "Xd, Xn, Xm | Xd, Xn, #imm",
        "description": "Subtracts and sets NZCV flags.",
        "flags": ["N", "Z", "C", "V"], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "ADC": {
        "mnemonic": "ADC", "full_name": "Add with Carry",
        "syntax": "Xd, Xn, Xm",
        "description": "Adds two registers and the carry flag (C) and places the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "ADCS": {
        "mnemonic": "ADCS", "full_name": "Add with Carry, setting flags",
        "syntax": "Xd, Xn, Xm",
        "description": "Add with carry, sets NZCV.",
        "flags": ["N", "Z", "C", "V"], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "SBC": {
        "mnemonic": "SBC", "full_name": "Subtract with Carry",
        "syntax": "Xd, Xn, Xm",
        "description": "Subtracts Xm and the inverse of the carry flag from Xn; places result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "SBCS": {
        "mnemonic": "SBCS", "full_name": "Subtract with Carry, setting flags",
        "syntax": "Xd, Xn, Xm",
        "description": "Subtract with carry, sets NZCV.",
        "flags": ["N", "Z", "C", "V"], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "NEG": {
        "mnemonic": "NEG", "full_name": "Negate",
        "syntax": "Xd, Xm",
        "description": "Negates Xm (two's complement) and places the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (alias SUB Xd,XZR,Xm)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "NEGS": {
        "mnemonic": "NEGS", "full_name": "Negate, setting flags",
        "syntax": "Xd, Xm",
        "description": "Negates Xm and sets NZCV flags.",
        "flags": ["N", "Z", "C", "V"], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "MUL": {
        "mnemonic": "MUL", "full_name": "Multiply",
        "syntax": "Xd, Xn, Xm",
        "description": "Multiplies Xn and Xm, places the lower bits of the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (3-source, alias MADD Xd,Xn,Xm,XZR)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "MADD": {
        "mnemonic": "MADD", "full_name": "Multiply-Add",
        "syntax": "Xd, Xn, Xm, Xa",
        "description": "Multiplies Xn and Xm, adds Xa, places the lower bits in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (3-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "MSUB": {
        "mnemonic": "MSUB", "full_name": "Multiply-Subtract",
        "syntax": "Xd, Xn, Xm, Xa",
        "description": "Multiplies Xn and Xm, subtracts from Xa, places the lower bits in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (3-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "SMULL": {
        "mnemonic": "SMULL", "full_name": "Signed Multiply Long",
        "syntax": "Xd, Wn, Wm",
        "description": "Multiplies two 32-bit signed integers and writes a 64-bit signed result to Xd.",
        "flags": [], "variants": "64", "category": "integer", "encoding": "Data-processing (3-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "UMULL": {
        "mnemonic": "UMULL", "full_name": "Unsigned Multiply Long",
        "syntax": "Xd, Wn, Wm",
        "description": "Multiplies two 32-bit unsigned integers and writes a 64-bit unsigned result to Xd.",
        "flags": [], "variants": "64", "category": "integer", "encoding": "Data-processing (3-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "SMULH": {
        "mnemonic": "SMULH", "full_name": "Signed Multiply High",
        "syntax": "Xd, Xn, Xm",
        "description": "Multiplies two 64-bit signed integers and writes the high 64 bits of the 128-bit result to Xd.",
        "flags": [], "variants": "64", "category": "integer", "encoding": "Data-processing (3-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "UMULH": {
        "mnemonic": "UMULH", "full_name": "Unsigned Multiply High",
        "syntax": "Xd, Xn, Xm",
        "description": "Multiplies two 64-bit unsigned integers and writes the high 64 bits of the 128-bit result to Xd.",
        "flags": [], "variants": "64", "category": "integer", "encoding": "Data-processing (3-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "SDIV": {
        "mnemonic": "SDIV", "full_name": "Signed Divide",
        "syntax": "Xd, Xn, Xm",
        "description": "Divides Xn by Xm (signed) and places the quotient in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (2-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "UDIV": {
        "mnemonic": "UDIV", "full_name": "Unsigned Divide",
        "syntax": "Xd, Xn, Xm",
        "description": "Divides Xn by Xm (unsigned) and places the quotient in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (2-source)",
        "isa_versions": ["ARMv8.0-A"],
    },

    # ------------------------------------------------------------------ #
    #  INTEGER LOGICAL                                                      #
    # ------------------------------------------------------------------ #

    "AND": {
        "mnemonic": "AND", "full_name": "Bitwise AND",
        "syntax": "Xd, Xn, Xm | Xd, Xn, #imm",
        "description": "Performs a bitwise AND of Xn and Xm (or immediate) and places the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing / logical immediate",
        "isa_versions": ["ARMv8.0-A"],
    },
    "ANDS": {
        "mnemonic": "ANDS", "full_name": "Bitwise AND, setting flags",
        "syntax": "Xd, Xn, Xm | Xd, Xn, #imm",
        "description": "Bitwise AND, sets N and Z flags (C and V cleared).",
        "flags": ["N", "Z", "C", "V"], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "ORR": {
        "mnemonic": "ORR", "full_name": "Bitwise OR",
        "syntax": "Xd, Xn, Xm | Xd, Xn, #imm",
        "description": "Performs a bitwise OR of Xn and Xm (or immediate) and places the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "ORN": {
        "mnemonic": "ORN", "full_name": "Bitwise OR NOT",
        "syntax": "Xd, Xn, Xm",
        "description": "Performs a bitwise OR of Xn with the inverse of Xm and places the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "EOR": {
        "mnemonic": "EOR", "full_name": "Exclusive OR",
        "syntax": "Xd, Xn, Xm | Xd, Xn, #imm",
        "description": "Performs a bitwise exclusive OR of Xn and Xm (or immediate) and places the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "EON": {
        "mnemonic": "EON", "full_name": "Exclusive OR NOT",
        "syntax": "Xd, Xn, Xm",
        "description": "Performs a bitwise XNOR of Xn and Xm and places the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "BIC": {
        "mnemonic": "BIC", "full_name": "Bit Clear (AND NOT)",
        "syntax": "Xd, Xn, Xm",
        "description": "Performs a bitwise AND of Xn with the inverse of Xm and places the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "BICS": {
        "mnemonic": "BICS", "full_name": "Bit Clear, setting flags",
        "syntax": "Xd, Xn, Xm",
        "description": "AND of Xn with ~Xm, sets N and Z flags.",
        "flags": ["N", "Z", "C", "V"], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "MVN": {
        "mnemonic": "MVN", "full_name": "Move NOT (bitwise complement)",
        "syntax": "Xd, Xm",
        "description": "Places the bitwise complement of Xm into Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (alias ORN Xd,XZR,Xm)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "TST": {
        "mnemonic": "TST", "full_name": "Test bits (AND, setting flags, discard result)",
        "syntax": "Xn, Xm | Xn, #imm",
        "description": "Performs a bitwise AND and sets N and Z flags; result is discarded.",
        "flags": ["N", "Z", "C", "V"], "variants": "both", "category": "integer", "encoding": "Data-processing (alias ANDS XZR,...)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "MOV": {
        "mnemonic": "MOV", "full_name": "Move register or immediate",
        "syntax": "Xd, Xm | Xd, #imm16",
        "description": "Copies a register to another or loads a 16-bit immediate (zero-extended or with shift).",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (alias ORR/MOVZ)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "MOVZ": {
        "mnemonic": "MOVZ", "full_name": "Move wide with zero",
        "syntax": "Xd, #imm16{, LSL #shift}",
        "description": "Moves a 16-bit immediate (optionally shifted by 0/16/32/48) into Xd, zeroing other bits.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Move wide immediate",
        "isa_versions": ["ARMv8.0-A"],
    },
    "MOVK": {
        "mnemonic": "MOVK", "full_name": "Move wide with keep",
        "syntax": "Xd, #imm16{, LSL #shift}",
        "description": "Inserts a 16-bit immediate into Xd at the specified bit position; other bits unchanged.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Move wide immediate",
        "isa_versions": ["ARMv8.0-A"],
    },
    "MOVN": {
        "mnemonic": "MOVN", "full_name": "Move wide with NOT",
        "syntax": "Xd, #imm16{, LSL #shift}",
        "description": "Moves the bitwise complement of a 16-bit immediate (optionally shifted) into Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Move wide immediate",
        "isa_versions": ["ARMv8.0-A"],
    },

    # ------------------------------------------------------------------ #
    #  SHIFTS & ROTATES                                                     #
    # ------------------------------------------------------------------ #

    "LSL": {
        "mnemonic": "LSL", "full_name": "Logical Shift Left",
        "syntax": "Xd, Xn, Xm | Xd, Xn, #imm",
        "description": "Shifts Xn left by a register or immediate amount, filling with zeros.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (alias LSLV / UBFM)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "LSR": {
        "mnemonic": "LSR", "full_name": "Logical Shift Right",
        "syntax": "Xd, Xn, Xm | Xd, Xn, #imm",
        "description": "Shifts Xn right logically by a register or immediate amount, filling with zeros.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (alias LSRV / UBFM)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "ASR": {
        "mnemonic": "ASR", "full_name": "Arithmetic Shift Right",
        "syntax": "Xd, Xn, Xm | Xd, Xn, #imm",
        "description": "Shifts Xn right arithmetically by a register or immediate amount, preserving sign.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (alias ASRV / SBFM)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "ROR": {
        "mnemonic": "ROR", "full_name": "Rotate Right",
        "syntax": "Xd, Xn, Xm | Xd, Xn, #imm",
        "description": "Rotates Xn right by the specified amount.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (alias RORV / EXTR)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "EXTR": {
        "mnemonic": "EXTR", "full_name": "Extract register",
        "syntax": "Xd, Xn, Xm, #lsb",
        "description": "Extracts a register from a pair of registers: {Xn:Xm} >> lsb, places 64 bits in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Extract",
        "isa_versions": ["ARMv8.0-A"],
    },
    "UBFM": {
        "mnemonic": "UBFM", "full_name": "Unsigned Bit Field Move",
        "syntax": "Xd, Xn, #immr, #imms",
        "description": "Copies a bit field from Xn into Xd with zero extension; used by LSR/LSL/UBFIZ/UBFX.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Bitfield",
        "isa_versions": ["ARMv8.0-A"],
    },
    "SBFM": {
        "mnemonic": "SBFM", "full_name": "Signed Bit Field Move",
        "syntax": "Xd, Xn, #immr, #imms",
        "description": "Copies a bit field from Xn into Xd with sign extension; used by ASR/SBFIZ/SBFX/SXTB/SXTH/SXTW.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Bitfield",
        "isa_versions": ["ARMv8.0-A"],
    },
    "BFM": {
        "mnemonic": "BFM", "full_name": "Bit Field Move",
        "syntax": "Xd, Xn, #immr, #imms",
        "description": "Copies a bit field from Xn into Xd without changing the remaining bits.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Bitfield",
        "isa_versions": ["ARMv8.0-A"],
    },
    "CLZ": {
        "mnemonic": "CLZ", "full_name": "Count Leading Zeros",
        "syntax": "Xd, Xn",
        "description": "Counts the number of leading zero bits in Xn and places the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (1-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "CLS": {
        "mnemonic": "CLS", "full_name": "Count Leading Sign bits",
        "syntax": "Xd, Xn",
        "description": "Counts the number of leading bits equal to the sign bit of Xn.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (1-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "RBIT": {
        "mnemonic": "RBIT", "full_name": "Reverse Bits",
        "syntax": "Xd, Xn",
        "description": "Reverses the bit order of Xn and places the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (1-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "REV": {
        "mnemonic": "REV", "full_name": "Reverse Bytes",
        "syntax": "Xd, Xn",
        "description": "Reverses the byte order (endian swap) of Xn and places the result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (1-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "REV16": {
        "mnemonic": "REV16", "full_name": "Reverse bytes in 16-bit halfwords",
        "syntax": "Xd, Xn",
        "description": "Reverses the byte order within each 16-bit halfword of Xn.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (1-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "REV32": {
        "mnemonic": "REV32", "full_name": "Reverse bytes in 32-bit words",
        "syntax": "Xd, Xn",
        "description": "Reverses the byte order within each 32-bit word of Xn.",
        "flags": [], "variants": "64", "category": "integer", "encoding": "Data-processing (1-source)",
        "isa_versions": ["ARMv8.0-A"],
    },

    # sign / zero extend
    "SXTB": {
        "mnemonic": "SXTB", "full_name": "Sign Extend Byte",
        "syntax": "Xd, Wn",
        "description": "Sign-extends the least significant byte of Wn to 64 bits and places result in Xd.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Bitfield (alias SBFM)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "SXTH": {
        "mnemonic": "SXTH", "full_name": "Sign Extend Halfword",
        "syntax": "Xd, Wn",
        "description": "Sign-extends the least significant 16 bits of Wn to 64 bits.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Bitfield (alias SBFM)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "SXTW": {
        "mnemonic": "SXTW", "full_name": "Sign Extend Word",
        "syntax": "Xd, Wn",
        "description": "Sign-extends the 32-bit value in Wn to 64 bits and places result in Xd.",
        "flags": [], "variants": "64", "category": "integer", "encoding": "Bitfield (alias SBFM)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "UXTB": {
        "mnemonic": "UXTB", "full_name": "Unsigned Extend Byte",
        "syntax": "Wd, Wn",
        "description": "Zero-extends the least significant byte of Wn.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Bitfield (alias UBFM)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "UXTH": {
        "mnemonic": "UXTH", "full_name": "Unsigned Extend Halfword",
        "syntax": "Wd, Wn",
        "description": "Zero-extends the least significant 16 bits of Wn.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Bitfield (alias UBFM)",
        "isa_versions": ["ARMv8.0-A"],
    },

    # compare
    "CMP": {
        "mnemonic": "CMP", "full_name": "Compare",
        "syntax": "Xn, Xm | Xn, #imm",
        "description": "Subtracts and sets NZCV flags; result is discarded. Alias for SUBS XZR,...",
        "flags": ["N", "Z", "C", "V"], "variants": "both", "category": "integer", "encoding": "Data-processing (alias SUBS XZR,...)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "CMN": {
        "mnemonic": "CMN", "full_name": "Compare Negative",
        "syntax": "Xn, Xm | Xn, #imm",
        "description": "Adds and sets NZCV flags; result is discarded. Alias for ADDS XZR,...",
        "flags": ["N", "Z", "C", "V"], "variants": "both", "category": "integer", "encoding": "Data-processing (alias ADDS XZR,...)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "CSEL": {
        "mnemonic": "CSEL", "full_name": "Conditional Select",
        "syntax": "Xd, Xn, Xm, cond",
        "description": "Places Xn or Xm in Xd depending on the condition code.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (1-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "CSINC": {
        "mnemonic": "CSINC", "full_name": "Conditional Select Increment",
        "syntax": "Xd, Xn, Xm, cond",
        "description": "Places Xn or Xm+1 in Xd depending on the condition code.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "CSET": {
        "mnemonic": "CSET", "full_name": "Conditional Set",
        "syntax": "Xd, cond",
        "description": "Sets Xd to 1 if the condition is true, 0 otherwise.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing (alias CSINC Xd,XZR,XZR,~cond)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "CINC": {
        "mnemonic": "CINC", "full_name": "Conditional Increment",
        "syntax": "Xd, Xn, cond",
        "description": "Places Xn or Xn+1 in Xd depending on the condition code.",
        "flags": [], "variants": "both", "category": "integer", "encoding": "Data-processing",
        "isa_versions": ["ARMv8.0-A"],
    },

    # ------------------------------------------------------------------ #
    #  ADDRESS COMPUTATION                                                  #
    # ------------------------------------------------------------------ #

    "ADR": {
        "mnemonic": "ADR", "full_name": "Form PC-relative address",
        "syntax": "Xd, label",
        "description": "Adds a signed immediate to the PC and writes the result to Xd.",
        "flags": [], "variants": "64", "category": "integer", "encoding": "PC-rel addressing",
        "isa_versions": ["ARMv8.0-A"],
    },
    "ADRP": {
        "mnemonic": "ADRP", "full_name": "Form PC-relative address to 4KB page",
        "syntax": "Xd, label",
        "description": "Shifts a 21-bit signed immediate left by 12, adds to the PC (page-aligned), writes to Xd.",
        "flags": [], "variants": "64", "category": "integer", "encoding": "PC-rel addressing",
        "isa_versions": ["ARMv8.0-A"],
    },

    # ------------------------------------------------------------------ #
    #  LOAD / STORE — AArch64                                              #
    # ------------------------------------------------------------------ #

    "LDR": {
        "mnemonic": "LDR", "full_name": "Load Register",
        "syntax": "Xt, [Xn{, #offset}] | Xt, label",
        "description": "Loads a 32 or 64-bit value from memory into a register.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store register (unsigned offset / PC-rel)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "LDRB": {
        "mnemonic": "LDRB", "full_name": "Load Register Byte",
        "syntax": "Wt, [Xn{, #offset}]",
        "description": "Loads a byte from memory and zero-extends it into Wt.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store register",
        "isa_versions": ["ARMv8.0-A"],
    },
    "LDRSB": {
        "mnemonic": "LDRSB", "full_name": "Load Register Signed Byte",
        "syntax": "Xt, [Xn{, #offset}]",
        "description": "Loads a byte from memory and sign-extends it into Xt.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store register",
        "isa_versions": ["ARMv8.0-A"],
    },
    "LDRH": {
        "mnemonic": "LDRH", "full_name": "Load Register Halfword",
        "syntax": "Wt, [Xn{, #offset}]",
        "description": "Loads a 16-bit halfword from memory and zero-extends it into Wt.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store register",
        "isa_versions": ["ARMv8.0-A"],
    },
    "LDRSH": {
        "mnemonic": "LDRSH", "full_name": "Load Register Signed Halfword",
        "syntax": "Xt, [Xn{, #offset}]",
        "description": "Loads a 16-bit halfword from memory and sign-extends it into Xt.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store register",
        "isa_versions": ["ARMv8.0-A"],
    },
    "LDRSW": {
        "mnemonic": "LDRSW", "full_name": "Load Register Signed Word",
        "syntax": "Xt, [Xn{, #offset}]",
        "description": "Loads a 32-bit word from memory and sign-extends it into Xt (64-bit).",
        "flags": [], "variants": "64", "category": "load_store", "encoding": "Load/store register",
        "isa_versions": ["ARMv8.0-A"],
    },
    "STR": {
        "mnemonic": "STR", "full_name": "Store Register",
        "syntax": "Xt, [Xn{, #offset}]",
        "description": "Stores a 32 or 64-bit register value to memory.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store register",
        "isa_versions": ["ARMv8.0-A"],
    },
    "STRB": {
        "mnemonic": "STRB", "full_name": "Store Register Byte",
        "syntax": "Wt, [Xn{, #offset}]",
        "description": "Stores the least significant byte of Wt to memory.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store register",
        "isa_versions": ["ARMv8.0-A"],
    },
    "STRH": {
        "mnemonic": "STRH", "full_name": "Store Register Halfword",
        "syntax": "Wt, [Xn{, #offset}]",
        "description": "Stores the least significant 16 bits of Wt to memory.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store register",
        "isa_versions": ["ARMv8.0-A"],
    },
    "LDP": {
        "mnemonic": "LDP", "full_name": "Load Pair of Registers",
        "syntax": "Xt1, Xt2, [Xn{, #offset}]",
        "description": "Loads two consecutive values from memory into a pair of registers.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store pair",
        "isa_versions": ["ARMv8.0-A"],
    },
    "STP": {
        "mnemonic": "STP", "full_name": "Store Pair of Registers",
        "syntax": "Xt1, Xt2, [Xn{, #offset}]",
        "description": "Stores two registers to consecutive memory locations.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store pair",
        "isa_versions": ["ARMv8.0-A"],
    },
    "LDUR": {
        "mnemonic": "LDUR", "full_name": "Load Register (unscaled offset)",
        "syntax": "Xt, [Xn, #simm9]",
        "description": "Loads a register from memory using a 9-bit signed unscaled offset.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store register (unscaled)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "STUR": {
        "mnemonic": "STUR", "full_name": "Store Register (unscaled offset)",
        "syntax": "Xt, [Xn, #simm9]",
        "description": "Stores a register to memory using a 9-bit signed unscaled offset.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store register (unscaled)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "LDXR": {
        "mnemonic": "LDXR", "full_name": "Load Exclusive Register",
        "syntax": "Xt, [Xn]",
        "description": "Loads a value from a memory location and marks it as exclusive (for LL/SC atomics).",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store exclusive",
        "isa_versions": ["ARMv8.0-A"],
    },
    "STXR": {
        "mnemonic": "STXR", "full_name": "Store Exclusive Register",
        "syntax": "Ws, Xt, [Xn]",
        "description": "Conditionally stores to memory if the exclusive reservation is still held. Ws receives 0 (success) or 1 (failure).",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store exclusive",
        "isa_versions": ["ARMv8.0-A"],
    },
    # LSE atomics (ARMv8.1-A)
    "LDADD": {
        "mnemonic": "LDADD", "full_name": "Atomic Add",
        "syntax": "Xs, Xt, [Xn]",
        "description": "Atomically adds Xs to the memory value at [Xn]; original value loaded into Xt.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Atomic memory operation",
        "isa_versions": ["ARMv8.1-A"],
    },
    "STADD": {
        "mnemonic": "STADD", "full_name": "Atomic Add (store only)",
        "syntax": "Xs, [Xn]",
        "description": "Atomically adds Xs to the memory value at [Xn]; no load result.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Atomic memory operation",
        "isa_versions": ["ARMv8.1-A"],
    },
    "CAS": {
        "mnemonic": "CAS", "full_name": "Compare and Swap",
        "syntax": "Xs, Xt, [Xn]",
        "description": "Atomically compares [Xn] with Xs; if equal, stores Xt; loads old value into Xs.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Compare and swap",
        "isa_versions": ["ARMv8.1-A"],
    },
    "LDR_PRE": {
        "mnemonic": "LDR_PRE", "full_name": "Load Register (pre-index update)",
        "syntax": "Xt, [Xn, #simm]!",
        "description": "Adds simm to Xn first (pre-index), then loads from the updated address. Xn is updated.",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store register (pre-indexed)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "LDR_POST": {
        "mnemonic": "LDR_POST", "full_name": "Load Register (post-index update)",
        "syntax": "Xt, [Xn], #simm",
        "description": "Loads from [Xn], then adds simm to Xn (post-index update).",
        "flags": [], "variants": "both", "category": "load_store", "encoding": "Load/store register (post-indexed)",
        "isa_versions": ["ARMv8.0-A"],
    },

    # ------------------------------------------------------------------ #
    #  BRANCH & CONTROL                                                     #
    # ------------------------------------------------------------------ #

    "B": {
        "mnemonic": "B", "full_name": "Branch",
        "syntax": "label",
        "description": "Unconditional branch to a PC-relative target within ±128 MB.",
        "flags": [], "variants": "both", "category": "branch", "encoding": "Unconditional branch (immediate)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "BL": {
        "mnemonic": "BL", "full_name": "Branch with Link",
        "syntax": "label",
        "description": "Branches to a target and stores the return address in X30 (LR).",
        "flags": [], "variants": "both", "category": "branch", "encoding": "Unconditional branch (immediate)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "BR": {
        "mnemonic": "BR", "full_name": "Branch to Register",
        "syntax": "Xn",
        "description": "Unconditional branch to the address in Xn.",
        "flags": [], "variants": "both", "category": "branch", "encoding": "Unconditional branch (register)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "BLR": {
        "mnemonic": "BLR", "full_name": "Branch with Link to Register",
        "syntax": "Xn",
        "description": "Branches to the address in Xn and stores the return address in X30 (LR).",
        "flags": [], "variants": "both", "category": "branch", "encoding": "Unconditional branch (register)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "RET": {
        "mnemonic": "RET", "full_name": "Return from subroutine",
        "syntax": "{Xn}",
        "description": "Branches to the address in X30 (LR) by default, or Xn if specified.",
        "flags": [], "variants": "both", "category": "branch", "encoding": "Unconditional branch (register)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "B_COND": {
        "mnemonic": "B.cond", "full_name": "Branch conditionally",
        "syntax": "B.EQ / B.NE / B.LT / B.LE / B.GT / B.GE / B.CS / B.CC / ..., label",
        "description": "Branches to a PC-relative target if the specified condition code is true.",
        "flags": [], "variants": "both", "category": "branch", "encoding": "Conditional branch (immediate)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "CBZ": {
        "mnemonic": "CBZ", "full_name": "Compare and Branch if Zero",
        "syntax": "Xt, label",
        "description": "Branches to label if Xt is zero (does not set flags).",
        "flags": [], "variants": "both", "category": "branch", "encoding": "Compare and branch (immediate)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "CBNZ": {
        "mnemonic": "CBNZ", "full_name": "Compare and Branch if Non-Zero",
        "syntax": "Xt, label",
        "description": "Branches to label if Xt is non-zero (does not set flags).",
        "flags": [], "variants": "both", "category": "branch", "encoding": "Compare and branch (immediate)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "TBZ": {
        "mnemonic": "TBZ", "full_name": "Test bit and Branch if Zero",
        "syntax": "Xt, #imm, label",
        "description": "Tests bit #imm of Xt and branches if it is zero.",
        "flags": [], "variants": "both", "category": "branch", "encoding": "Test and branch (immediate)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "TBNZ": {
        "mnemonic": "TBNZ", "full_name": "Test bit and Branch if Non-Zero",
        "syntax": "Xt, #imm, label",
        "description": "Tests bit #imm of Xt and branches if it is non-zero.",
        "flags": [], "variants": "both", "category": "branch", "encoding": "Test and branch (immediate)",
        "isa_versions": ["ARMv8.0-A"],
    },

    # ------------------------------------------------------------------ #
    #  SYSTEM / PRIVILEGED                                                  #
    # ------------------------------------------------------------------ #

    "SVC": {
        "mnemonic": "SVC", "full_name": "Supervisor Call",
        "syntax": "#imm16",
        "description": "Generates a synchronous exception (software interrupt / system call) to EL1.",
        "flags": [], "variants": "both", "category": "system", "encoding": "Exception generation",
        "isa_versions": ["ARMv8.0-A"],
    },
    "HVC": {
        "mnemonic": "HVC", "full_name": "Hypervisor Call",
        "syntax": "#imm16",
        "description": "Generates a synchronous exception to EL2 (hypervisor).",
        "flags": [], "variants": "both", "category": "system", "encoding": "Exception generation",
        "isa_versions": ["ARMv8.0-A"],
    },
    "SMC": {
        "mnemonic": "SMC", "full_name": "Secure Monitor Call",
        "syntax": "#imm16",
        "description": "Generates a synchronous exception to EL3 (secure monitor).",
        "flags": [], "variants": "both", "category": "system", "encoding": "Exception generation",
        "isa_versions": ["ARMv8.0-A"],
    },
    "ERET": {
        "mnemonic": "ERET", "full_name": "Exception Return",
        "syntax": "",
        "description": "Returns from exception level, restoring PC from ELR_ELn and PSTATE from SPSR_ELn.",
        "flags": [], "variants": "both", "category": "system", "encoding": "Exception return",
        "isa_versions": ["ARMv8.0-A"],
    },
    "MRS": {
        "mnemonic": "MRS", "full_name": "Move System Register to general register",
        "syntax": "Xt, sysreg",
        "description": "Reads a system register into Xt.",
        "flags": [], "variants": "64", "category": "system", "encoding": "System register move",
        "isa_versions": ["ARMv8.0-A"],
    },
    "MSR": {
        "mnemonic": "MSR", "full_name": "Move general register to System Register",
        "syntax": "sysreg, Xt",
        "description": "Writes Xt into a system register.",
        "flags": [], "variants": "64", "category": "system", "encoding": "System register move",
        "isa_versions": ["ARMv8.0-A"],
    },
    "ISB": {
        "mnemonic": "ISB", "full_name": "Instruction Synchronization Barrier",
        "syntax": "{option}",
        "description": "Flushes the pipeline and causes subsequent instructions to be fetched after the barrier.",
        "flags": [], "variants": "both", "category": "system", "encoding": "Barriers",
        "isa_versions": ["ARMv8.0-A"],
    },
    "DSB": {
        "mnemonic": "DSB", "full_name": "Data Synchronization Barrier",
        "syntax": "option",
        "description": "Ensures all explicit memory accesses before this instruction complete before any after.",
        "flags": [], "variants": "both", "category": "system", "encoding": "Barriers",
        "isa_versions": ["ARMv8.0-A"],
    },
    "DMB": {
        "mnemonic": "DMB", "full_name": "Data Memory Barrier",
        "syntax": "option",
        "description": "Ensures ordering of memory accesses relative to other memory accesses.",
        "flags": [], "variants": "both", "category": "system", "encoding": "Barriers",
        "isa_versions": ["ARMv8.0-A"],
    },
    "NOP": {
        "mnemonic": "NOP", "full_name": "No Operation",
        "syntax": "",
        "description": "Does nothing. Used for alignment, timing, and patching.",
        "flags": [], "variants": "both", "category": "system", "encoding": "Hints",
        "isa_versions": ["ARMv8.0-A"],
    },
    "WFE": {
        "mnemonic": "WFE", "full_name": "Wait For Event",
        "syntax": "",
        "description": "Causes the processor to enter a low-power state until an event is signaled.",
        "flags": [], "variants": "both", "category": "system", "encoding": "Hints",
        "isa_versions": ["ARMv8.0-A"],
    },
    "WFI": {
        "mnemonic": "WFI", "full_name": "Wait For Interrupt",
        "syntax": "",
        "description": "Causes the processor to enter a low-power state until an interrupt is pending.",
        "flags": [], "variants": "both", "category": "system", "encoding": "Hints",
        "isa_versions": ["ARMv8.0-A"],
    },
    "SEV": {
        "mnemonic": "SEV", "full_name": "Send Event",
        "syntax": "",
        "description": "Sends an event to all PEs in the multiprocessor system.",
        "flags": [], "variants": "both", "category": "system", "encoding": "Hints",
        "isa_versions": ["ARMv8.0-A"],
    },
    "TLBI": {
        "mnemonic": "TLBI", "full_name": "TLB Invalidate",
        "syntax": "op, Xt",
        "description": "Invalidates TLB entries by operand type (e.g. VMALLE1IS, VAE1IS).",
        "flags": [], "variants": "64", "category": "system", "encoding": "System instruction",
        "isa_versions": ["ARMv8.0-A"],
    },
    "DC": {
        "mnemonic": "DC", "full_name": "Data Cache operation",
        "syntax": "op, Xt",
        "description": "Performs a data cache operation (clean, invalidate, zero) on the cache line for Xt.",
        "flags": [], "variants": "64", "category": "system", "encoding": "System instruction",
        "isa_versions": ["ARMv8.0-A"],
    },
    "IC": {
        "mnemonic": "IC", "full_name": "Instruction Cache operation",
        "syntax": "op{, Xt}",
        "description": "Performs an instruction cache operation (typically IALLU or IVAU).",
        "flags": [], "variants": "64", "category": "system", "encoding": "System instruction",
        "isa_versions": ["ARMv8.0-A"],
    },

    # ------------------------------------------------------------------ #
    #  FLOATING POINT — Scalar (VFPv4 / ARMv8 FP)                         #
    # ------------------------------------------------------------------ #

    "FADD": {
        "mnemonic": "FADD", "full_name": "Floating-point Add (scalar)",
        "syntax": "Sd/Dd, Sn/Dn, Sm/Dm",
        "description": "Adds two floating-point scalar values and places the result in the destination.",
        "flags": [], "variants": "both", "category": "float", "encoding": "Floating-point data-processing (2-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FSUB": {
        "mnemonic": "FSUB", "full_name": "Floating-point Subtract (scalar)",
        "syntax": "Sd/Dd, Sn/Dn, Sm/Dm",
        "description": "Subtracts one floating-point scalar from another and places the result in the destination.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP data-processing (2-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FMUL": {
        "mnemonic": "FMUL", "full_name": "Floating-point Multiply (scalar)",
        "syntax": "Sd/Dd, Sn/Dn, Sm/Dm",
        "description": "Multiplies two floating-point scalar values and places the result in the destination.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP data-processing (2-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FDIV": {
        "mnemonic": "FDIV", "full_name": "Floating-point Divide (scalar)",
        "syntax": "Sd/Dd, Sn/Dn, Sm/Dm",
        "description": "Divides one floating-point scalar by another.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP data-processing (2-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FMADD": {
        "mnemonic": "FMADD", "full_name": "Floating-point Fused Multiply-Add (scalar)",
        "syntax": "Sd/Dd, Sn/Dn, Sm/Dm, Sa/Da",
        "description": "Computes Sn*Sm + Sa in a single fused operation (no intermediate rounding) into Sd.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP data-processing (3-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FMSUB": {
        "mnemonic": "FMSUB", "full_name": "Floating-point Fused Multiply-Subtract",
        "syntax": "Sd/Dd, Sn/Dn, Sm/Dm, Sa/Da",
        "description": "Computes -(Sn*Sm) + Sa in a fused operation.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP data-processing (3-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FNMADD": {
        "mnemonic": "FNMADD", "full_name": "Floating-point Negated Fused Multiply-Add",
        "syntax": "Sd/Dd, Sn/Dn, Sm/Dm, Sa/Da",
        "description": "Computes -(Sn*Sm + Sa) in a fused operation.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP data-processing (3-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FABS": {
        "mnemonic": "FABS", "full_name": "Floating-point Absolute value",
        "syntax": "Sd/Dd, Sn/Dn",
        "description": "Places the absolute value of the floating-point source in the destination.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP data-processing (1-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FNEG": {
        "mnemonic": "FNEG", "full_name": "Floating-point Negate",
        "syntax": "Sd/Dd, Sn/Dn",
        "description": "Negates the floating-point source and places it in the destination.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP data-processing (1-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FSQRT": {
        "mnemonic": "FSQRT", "full_name": "Floating-point Square Root",
        "syntax": "Sd/Dd, Sn/Dn",
        "description": "Computes the square root of the floating-point source.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP data-processing (1-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FRINTA": {
        "mnemonic": "FRINTA", "full_name": "Floating-point Round to Nearest with Ties Away",
        "syntax": "Sd/Dd, Sn/Dn",
        "description": "Rounds a floating-point value to an integer (ties round away from zero).",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP data-processing (1-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FRINTZ": {
        "mnemonic": "FRINTZ", "full_name": "Floating-point Round towards Zero",
        "syntax": "Sd/Dd, Sn/Dn",
        "description": "Rounds a floating-point value towards zero (truncate).",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP data-processing (1-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FCVTZS": {
        "mnemonic": "FCVTZS", "full_name": "Floating-point Convert to Signed integer, rounding toward Zero",
        "syntax": "Xd/Wd, Sn/Dn",
        "description": "Converts a floating-point value to a signed integer by rounding toward zero.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP conversion",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FCVTZU": {
        "mnemonic": "FCVTZU", "full_name": "Floating-point Convert to Unsigned integer, rounding toward Zero",
        "syntax": "Xd/Wd, Sn/Dn",
        "description": "Converts a floating-point value to an unsigned integer by rounding toward zero.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP conversion",
        "isa_versions": ["ARMv8.0-A"],
    },
    "SCVTF": {
        "mnemonic": "SCVTF", "full_name": "Signed integer Convert to Floating-point",
        "syntax": "Sd/Dd, Xn/Wn",
        "description": "Converts a signed integer register to a floating-point value.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP conversion",
        "isa_versions": ["ARMv8.0-A"],
    },
    "UCVTF": {
        "mnemonic": "UCVTF", "full_name": "Unsigned integer Convert to Floating-point",
        "syntax": "Sd/Dd, Xn/Wn",
        "description": "Converts an unsigned integer register to a floating-point value.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP conversion",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FCMP": {
        "mnemonic": "FCMP", "full_name": "Floating-point Compare",
        "syntax": "Sn/Dn, Sm/Dm | Sn/Dn, #0.0",
        "description": "Sets the NZCV flags based on the comparison of two floating-point values.",
        "flags": ["N", "Z", "C", "V"], "variants": "both", "category": "float", "encoding": "FP comparison",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FCVT": {
        "mnemonic": "FCVT", "full_name": "Floating-point Convert precision",
        "syntax": "Sd/Dd/Hd, Sn/Dn/Hn",
        "description": "Converts between single, double, and half precision floating-point values.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP data-processing (1-source)",
        "isa_versions": ["ARMv8.0-A"],
    },
    "FMOV": {
        "mnemonic": "FMOV", "full_name": "Floating-point Move",
        "syntax": "Sd/Dd, Sn/Dn | Sd, Xn | Xd, Sn",
        "description": "Copies a floating-point value, or moves between integer and FP registers.",
        "flags": [], "variants": "both", "category": "float", "encoding": "FP move",
        "isa_versions": ["ARMv8.0-A"],
    },

    # ------------------------------------------------------------------ #
    #  FP / SIMD LOAD-STORE                                                #
    # ------------------------------------------------------------------ #

    "LDR_FP": {
        "mnemonic": "LDR (FP)", "full_name": "Load FP/SIMD Register",
        "syntax": "St/Dt/Qt, [Xn{, #offset}]",
        "description": "Loads a scalar FP or SIMD register from memory.",
        "flags": [], "variants": "both", "category": "float", "encoding": "Load/store SIMD and FP",
        "isa_versions": ["ARMv8.0-A"],
    },
    "STR_FP": {
        "mnemonic": "STR (FP)", "full_name": "Store FP/SIMD Register",
        "syntax": "St/Dt/Qt, [Xn{, #offset}]",
        "description": "Stores a scalar FP or SIMD register to memory.",
        "flags": [], "variants": "both", "category": "float", "encoding": "Load/store SIMD and FP",
        "isa_versions": ["ARMv8.0-A"],
    },

    # ------------------------------------------------------------------ #
    #  NEON / Advanced SIMD — 128-bit vector                               #
    # ------------------------------------------------------------------ #

    "ADD_VEC": {
        "mnemonic": "ADD (vec)", "full_name": "Add (vector)",
        "syntax": "Vd.<T>, Vn.<T>, Vm.<T>",
        "description": "Adds corresponding elements of two NEON vectors.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "SUB_VEC": {
        "mnemonic": "SUB (vec)", "full_name": "Subtract (vector)",
        "syntax": "Vd.<T>, Vn.<T>, Vm.<T>",
        "description": "Subtracts corresponding elements of two NEON vectors.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "MUL_VEC": {
        "mnemonic": "MUL (vec)", "full_name": "Multiply (vector)",
        "syntax": "Vd.<T>, Vn.<T>, Vm.<T>",
        "description": "Multiplies corresponding integer elements of two NEON vectors.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "AND_VEC": {
        "mnemonic": "AND (vec)", "full_name": "Bitwise AND (vector)",
        "syntax": "Vd.16B, Vn.16B, Vm.16B",
        "description": "Performs a bitwise AND of two 128-bit NEON registers.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "ORR_VEC": {
        "mnemonic": "ORR (vec)", "full_name": "Bitwise OR (vector)",
        "syntax": "Vd.16B, Vn.16B, Vm.16B",
        "description": "Performs a bitwise OR of two 128-bit NEON registers.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "EOR_VEC": {
        "mnemonic": "EOR (vec)", "full_name": "Bitwise XOR (vector)",
        "syntax": "Vd.16B, Vn.16B, Vm.16B",
        "description": "Performs a bitwise XOR of two 128-bit NEON registers.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "BIF": {
        "mnemonic": "BIF", "full_name": "Bitwise Insert if False",
        "syntax": "Vd.16B, Vn.16B, Vm.16B",
        "description": "Inserts bits from Vn into Vd where corresponding bits of Vm are 0.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "BIT": {
        "mnemonic": "BIT", "full_name": "Bitwise Insert if True",
        "syntax": "Vd.16B, Vn.16B, Vm.16B",
        "description": "Inserts bits from Vn into Vd where corresponding bits of Vm are 1.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "BSL": {
        "mnemonic": "BSL", "full_name": "Bitwise Select",
        "syntax": "Vd.16B, Vn.16B, Vm.16B",
        "description": "Selects bits from Vn where Vd bits are 1, and from Vm where Vd bits are 0.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "FADD_VEC": {
        "mnemonic": "FADD (vec)", "full_name": "Floating-point Add (vector)",
        "syntax": "Vd.<T>, Vn.<T>, Vm.<T>",
        "description": "Adds corresponding FP elements of two NEON vectors.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "FMUL_VEC": {
        "mnemonic": "FMUL (vec)", "full_name": "Floating-point Multiply (vector)",
        "syntax": "Vd.<T>, Vn.<T>, Vm.<T>",
        "description": "Multiplies corresponding FP elements of two NEON vectors.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "FMLA": {
        "mnemonic": "FMLA", "full_name": "Floating-point Multiply-Add to accumulator (vector)",
        "syntax": "Vd.<T>, Vn.<T>, Vm.<T>",
        "description": "Multiplies corresponding FP elements of Vn and Vm and adds to Vd (fused).",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "FMLS": {
        "mnemonic": "FMLS", "full_name": "Floating-point Multiply-Subtract from accumulator (vector)",
        "syntax": "Vd.<T>, Vn.<T>, Vm.<T>",
        "description": "Multiplies Vn and Vm elements and subtracts the product from Vd.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "ADDV": {
        "mnemonic": "ADDV", "full_name": "Add across vector",
        "syntax": "Bd/Hd/Sd, Vn.<T>",
        "description": "Adds all integer elements of a vector and places the scalar result in the destination.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD across lanes",
        "isa_versions": ["NEON"],
    },
    "ZIP1": {
        "mnemonic": "ZIP1", "full_name": "Zip vectors (primary)",
        "syntax": "Vd.<T>, Vn.<T>, Vm.<T>",
        "description": "Interleaves the lower half elements of Vn and Vm into Vd.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD permute",
        "isa_versions": ["NEON"],
    },
    "ZIP2": {
        "mnemonic": "ZIP2", "full_name": "Zip vectors (secondary)",
        "syntax": "Vd.<T>, Vn.<T>, Vm.<T>",
        "description": "Interleaves the upper half elements of Vn and Vm into Vd.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD permute",
        "isa_versions": ["NEON"],
    },
    "UZP1": {
        "mnemonic": "UZP1", "full_name": "Unzip vectors (primary)",
        "syntax": "Vd.<T>, Vn.<T>, Vm.<T>",
        "description": "Extracts even-numbered elements from Vn and Vm into Vd.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD permute",
        "isa_versions": ["NEON"],
    },
    "TBL": {
        "mnemonic": "TBL", "full_name": "Table vector Lookup",
        "syntax": "Vd.8B/16B, {Vn.16B, ...}, Vm.8B/16B",
        "description": "Performs a table lookup: each byte in Vm indexes into a 1–4 register table.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD table lookup",
        "isa_versions": ["NEON"],
    },
    "TBX": {
        "mnemonic": "TBX", "full_name": "Table vector lookup eXtension",
        "syntax": "Vd.8B/16B, {Vn.16B, ...}, Vm.8B/16B",
        "description": "Like TBL but out-of-range indices leave the destination element unchanged.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD table lookup",
        "isa_versions": ["NEON"],
    },
    "DUP": {
        "mnemonic": "DUP", "full_name": "Duplicate scalar to vector",
        "syntax": "Vd.<T>, Rn | Vd.<T>, Vn.<Ts>[index]",
        "description": "Broadcasts a scalar value or element across all lanes of a vector.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD copy",
        "isa_versions": ["NEON"],
    },
    "INS": {
        "mnemonic": "INS", "full_name": "Insert vector element from general register or element",
        "syntax": "Vd.<Ts>[index], Rn | Vd.<Ts>[idx1], Vn.<Ts>[idx2]",
        "description": "Inserts a value from a general-purpose register or another vector element into a lane.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD copy",
        "isa_versions": ["NEON"],
    },
    "LD1": {
        "mnemonic": "LD1", "full_name": "Load single structure to one/two/three/four registers",
        "syntax": "{ Vt.<T> }, [Xn]",
        "description": "Loads one or more sequential NEON registers from memory.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD load/store single",
        "isa_versions": ["NEON"],
    },
    "ST1": {
        "mnemonic": "ST1", "full_name": "Store single structure from one/two/three/four registers",
        "syntax": "{ Vt.<T> }, [Xn]",
        "description": "Stores one or more NEON registers to sequential memory locations.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD load/store single",
        "isa_versions": ["NEON"],
    },
    "LD2": {
        "mnemonic": "LD2", "full_name": "Load 2-element structures to two registers (de-interleave)",
        "syntax": "{ Vt.<T>, Vt2.<T> }, [Xn]",
        "description": "Loads pairs of elements, de-interleaving them into two NEON registers.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD load/store multiple",
        "isa_versions": ["NEON"],
    },
    "ST2": {
        "mnemonic": "ST2", "full_name": "Store 2-element structures from two registers (interleave)",
        "syntax": "{ Vt.<T>, Vt2.<T> }, [Xn]",
        "description": "Stores two NEON registers interleaved as pairs to memory.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD load/store multiple",
        "isa_versions": ["NEON"],
    },
    "LDR_VEC": {
        "mnemonic": "LDR (SIMD)", "full_name": "Load SIMD/FP register",
        "syntax": "Qt, [Xn{, #offset}]",
        "description": "Loads a 128-bit NEON register from memory.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Load/store SIMD and FP",
        "isa_versions": ["NEON"],
    },
    "STR_VEC": {
        "mnemonic": "STR (SIMD)", "full_name": "Store SIMD/FP register",
        "syntax": "Qt, [Xn{, #offset}]",
        "description": "Stores a 128-bit NEON register to memory.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Load/store SIMD and FP",
        "isa_versions": ["NEON"],
    },
    "CMGE": {
        "mnemonic": "CMGE", "full_name": "Compare signed Greater than or Equal (vector)",
        "syntax": "Vd.<T>, Vn.<T>, Vm.<T>",
        "description": "Compares signed elements; sets corresponding result lanes to all-ones if ≥, all-zeros otherwise.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },
    "CMEQ": {
        "mnemonic": "CMEQ", "full_name": "Compare Equal (vector)",
        "syntax": "Vd.<T>, Vn.<T>, Vm.<T>",
        "description": "Compares elements for equality; sets all-ones or all-zeros per lane.",
        "flags": [], "variants": "both", "category": "vector", "encoding": "Advanced SIMD three-register same",
        "isa_versions": ["NEON"],
    },

    # ------------------------------------------------------------------ #
    #  SVE — Scalable Vector Extension                                     #
    # ------------------------------------------------------------------ #

    "ADD_SVE": {
        "mnemonic": "ADD (SVE)", "full_name": "Add (SVE predicated / unpredicated)",
        "syntax": "Zd.<T>, Zn.<T>, Zm.<T> | Zd.<T>, Pg/M, Zd.<T>, Zn.<T>",
        "description": "Adds corresponding elements of two SVE vectors, optionally predicated.",
        "flags": [], "variants": "64", "category": "vector", "encoding": "SVE integer arithmetic",
        "isa_versions": ["SVE"],
    },
    "LD1_SVE": {
        "mnemonic": "LD1W/LD1D (SVE)", "full_name": "Contiguous load SVE (predicated)",
        "syntax": "Zt.<T>, Pg/Z, [Xn, Xm, LSL #s]",
        "description": "Loads active elements (selected by predicate) from contiguous memory into a scalable vector register.",
        "flags": [], "variants": "64", "category": "vector", "encoding": "SVE load and store",
        "isa_versions": ["SVE"],
    },
    "ST1_SVE": {
        "mnemonic": "ST1W/ST1D (SVE)", "full_name": "Contiguous store SVE (predicated)",
        "syntax": "Zt.<T>, Pg, [Xn, Xm, LSL #s]",
        "description": "Stores active elements from a scalable vector register to contiguous memory.",
        "flags": [], "variants": "64", "category": "vector", "encoding": "SVE load and store",
        "isa_versions": ["SVE"],
    },
    "WHILELT": {
        "mnemonic": "WHILELT", "full_name": "While Less Than (SVE)",
        "syntax": "Pd.<T>, Xn, Xm",
        "description": "Sets predicate lanes to true while index (Xn+lane) < Xm; generates vectorization loop masks.",
        "flags": [], "variants": "64", "category": "vector", "encoding": "SVE while",
        "isa_versions": ["SVE"],
    },
    "PTRUE": {
        "mnemonic": "PTRUE", "full_name": "Initialise predicate as True (SVE)",
        "syntax": "Pd.<T>{, pattern}",
        "description": "Sets all active predicate elements to true, according to an optional element count pattern.",
        "flags": [], "variants": "64", "category": "vector", "encoding": "SVE predicate logical",
        "isa_versions": ["SVE"],
    },
    "FMAD_SVE": {
        "mnemonic": "FMAD (SVE)", "full_name": "FP Multiply-Add, addend first (SVE)",
        "syntax": "Zdn.<T>, Pg/M, Zm.<T>, Za.<T>",
        "description": "Fused multiply-add Zdn = Za + Zm*Zdn, predicated over active lanes.",
        "flags": [], "variants": "64", "category": "vector", "encoding": "SVE floating-point multiply-add",
        "isa_versions": ["SVE"],
    },
    "FRECPE": {
        "mnemonic": "FRECPE", "full_name": "FP Reciprocal Estimate",
        "syntax": "Vd.<T>, Vn.<T>",
        "description": "Provides a floating-point reciprocal estimate for each element.",
        "flags": [], "variants": "both", "category": "float", "encoding": "Advanced SIMD two-register misc",
        "isa_versions": ["NEON"],
    },
    "FRSQRTE": {
        "mnemonic": "FRSQRTE", "full_name": "FP Reciprocal Square Root Estimate",
        "syntax": "Vd.<T>, Vn.<T>",
        "description": "Provides a floating-point reciprocal square root estimate for each element.",
        "flags": [], "variants": "both", "category": "float", "encoding": "Advanced SIMD two-register misc",
        "isa_versions": ["NEON"],
    },
}
