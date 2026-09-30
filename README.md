# PPC2ARM — PowerPC ↔ ARM/AArch64 Instruction Picker

### *From the minds of IBM Bob & Daneyand*

[![Release](https://img.shields.io/github/v/release/007Style/PPC2ARM?label=latest%20release&color=brightgreen)](https://github.com/007Style/PPC2ARM/releases/latest)
[![Platform](https://img.shields.io/badge/platform-macOS%20arm64-blue)](https://github.com/007Style/PPC2ARM/releases/latest)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

```
  ██████╗ ██████╗  ██████╗██████╗  █████╗ ██████╗ ███╗   ███╗
  ██╔══██╗██╔══██╗██╔════╝╚════██╗██╔══██╗██╔══██╗████╗ ████║
  ██████╔╝██████╔╝██║      █████╔╝███████║██████╔╝██╔████╔██║
  ██╔═══╝ ██╔═══╝ ██║     ██╔═══╝ ██╔══██║██╔══██╗██║╚██╔╝██║
  ██║     ██║     ╚██████╗███████╗██║  ██║██║  ██║██║ ╚═╝ ██║
  ╚═╝     ╚═╝      ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝

         PowerPC  ↔  ARM / AArch64   ISA Translation Station
              Retro Museum Edition  •  v1.0.0
```

> *"Any sufficiently successful ISA is indistinguishable from a mistake that won."*
> — PPC2ARM Fortune Cookie

---

## What Is This Thing?

PPC2ARM is a **fully self-contained Python tool** that answers the age-old question every systems programmer eventually screams at their monitor:

> *"OK so `lwz` loads a word on PowerPC — what in the HECK is the ARM equivalent?!"*

The answer, dear friend, is `LDR`. And PPC2ARM will tell you that, along with the syntax, the semantics, a confidence rating, and a detailed note explaining exactly where the two architectures diverge — because they always diverge somewhere, and that somewhere will absolutely ruin your Tuesday if you don't know about it.

This tool maps **PowerPC** (PPC32, PPC64, AltiVec/VMX) instructions to their **ARM / AArch64** equivalents, and vice-versa. When no direct analogue exists — and sometimes it really doesn't — the tool suggests the closest approximation and stamps it clearly with a `[SUGGESTION]` badge so you don't accidentally assume that `VPERM` and `TBL` are the same instruction. (They're close. They're not the same. Endianness is involved. We're sorry.)

All instruction data is **embedded directly in Python source files**. No internet connection. No database. No cloud. No subscriptions. No telemetry. No AI-generated hallucinations about fictional mnemonics. Just cold, hard, manually-researched ISA facts, lovingly compiled and cross-referenced from the actual architecture manuals.

Oh, and there's a **retro phosphor-green wxPython GUI** with an ISA Museum, a scrolling trivia ticker, and a Konami code easter egg. Because why not.

---

## The Origin Story

Once upon a time, a developer was porting PowerPC assembly to AArch64. They opened seventeen browser tabs, three PDF copies of the ARM Architecture Reference Manual, two copies of the IBM POWER ISA spec, and one very strong coffee.

Four hours later, they had translated twelve instructions and developed a nervous tic every time they saw the word "endianness."

PPC2ARM was built so that never happens to anyone again.

---

## Features

### 🔍 Bidirectional Instruction Lookup
Look up any PowerPC mnemonic and get its ARM/AArch64 analogue. Or go the other way — look up an ARM mnemonic and find out what PPC instruction it corresponds to. Both directions. All day. No fuss.

### 🎯 Four Confidence Levels
Not all analogues are created equal. PPC2ARM is honest about this:

| Badge | Meaning |
|-------|---------|
| `[DIRECT]` | Near-identical semantics. Safe 1-to-1 substitution. You're golden. |
| `[CLOSE]` | Same intent, minor differences in flag behavior, register model, or operand order. Read the notes. |
| `[SUGGESTION]` | Closest we've got. Programmer must verify. Endianness may be involved. Good luck. |
| `[NO MATCH]` | Nothing reasonable exists. We're telling you this so you don't waste three hours looking. |

### 🤖 Fuzzy Search
Typo in your mnemonic? Type `lwzz` instead of `lwz`? PPC2ARM's Levenshtein-powered fuzzy matcher will gently suggest what you probably meant, ranked by similarity score. No judgment.

### 📖 Comprehensive ISA Coverage

**PowerPC side:**
- PPC32 integer arithmetic — `add`, `subf`, `mullw`, `divw`, `neg`, all the dot-forms, all the overflow forms, the whole family
- PPC64 extensions — `ld`, `std`, `mulld`, `divd`, `extsw`, `cntlzd`, and friends
- Load/store with update forms — `lwzu`, `stwu`, `ldu`, `stdu` (the ARM equivalents involve pre/post-index addressing and we explain exactly how)
- Condition register instructions — `mfcr`, `mtcr`, `crand`, `cror`, `crxor`
- AltiVec/VMX — `vaddubm` through `vrsqrtefp`, vector permute, splat, merge, compare, and more
- Floating point — `fadd`, `fsub`, `fmul`, `fdiv`, `fmadd`, `fnmadd`, `fabs`, `fsqrt`, `fctiw`, `fcfid`, all of it
- System/privileged — `sc`, `mtspr`, `mfspr`, `mflr`, `mtlr`, `rfi`, `tlbie`, `isync`, `sync`, `lwsync`, `icbi`, `dcbf`
- Branch family — `b`, `bl`, `blr`, `bctr`, `bc`, `beq`, `bne`, `blt`, `bgt`, `bdz`, `bdnz`

**ARM / AArch64 side:**
- Base integer — `ADD`/`ADDS`/`SUB`/`SUBS`/`ADC`/`SBC`, `MUL`/`MADD`/`MSUB`, `SMULL`/`UMULL`/`SMULH`/`UMULH`, `SDIV`/`UDIV`
- Logic — `AND`/`ANDS`/`ORR`/`ORN`/`EOR`/`EON`/`BIC`/`BICS`/`MVN`/`TST`
- Move — `MOV`/`MOVZ`/`MOVK`/`MOVN`
- Shifts — `LSL`/`LSR`/`ASR`/`ROR`/`EXTR`/`UBFM`/`SBFM`/`BFM`
- Bit ops — `CLZ`/`CLS`/`RBIT`/`REV`/`REV16`/`REV32`
- Sign/zero extend — `SXTB`/`SXTH`/`SXTW`/`UXTB`/`UXTH`
- Compare & select — `CMP`/`CMN`/`CSEL`/`CSINC`/`CSET`/`CINC`
- Address — `ADR`/`ADRP`
- Load/store — `LDR`/`LDRB`/`LDRSB`/`LDRH`/`LDRSH`/`LDRSW`/`STR`/`STRB`/`STRH`/`LDP`/`STP`, pre/post-index forms
- Exclusives & atomics — `LDXR`/`STXR`, LSE atomics (`LDADD`/`STADD`/`CAS`) for ARMv8.1-A
- Branch — `B`/`BL`/`BR`/`BLR`/`RET`/`B.cond`/`CBZ`/`CBNZ`/`TBZ`/`TBNZ`
- System — `SVC`/`HVC`/`SMC`/`ERET`/`MRS`/`MSR`/`ISB`/`DSB`/`DMB`/`NOP`/`WFE`/`WFI`/`TLBI`/`DC`/`IC`
- FP scalar — `FADD`/`FSUB`/`FMUL`/`FDIV`/`FMADD`/`FMSUB`/`FNMADD`/`FABS`/`FNEG`/`FSQRT`/`FCVTZS`/`SCVTF`/`FCMP`/`FCVT`/`FMOV`
- NEON/ASIMD — `ADD`/`SUB`/`MUL` (vec), `AND`/`ORR`/`EOR` (vec), `BSL`/`BIF`/`BIT`, `FADD`/`FMUL`/`FMLA`/`FMLS` (vec), `ADDV`, `ZIP1`/`ZIP2`/`UZP1`, `TBL`/`TBX`, `DUP`/`INS`, `LD1`/`ST1`/`LD2`/`ST2`, `CMGE`/`CMEQ`, `FRECPE`/`FRSQRTE`
- SVE — `ADD`/`LD1W`/`ST1W`/`WHILELT`/`PTRUE`/`FMAD`

### 🗺️ Detailed Porting Notes
Every single mapping entry comes with a human-written note explaining the architectural differences. Register model differences. Flag behavior differences. Operand order gotchas (`subf` is `rD = rB - rA` — note the reversed operand order!). Endianness implications for vector operations. Update-form addressing idioms. These notes are the thing that would have saved you three hours.

### 🏛️ ISA Museum (GUI)
A browsable, interactive reference of historical CPU architectures — because context matters, history is fascinating, and sometimes you just want to know why Alpha has no byte load instructions. The Museum covers:

- **ARM / AArch64** — from Acorn's BBC Micro lab to Apple Silicon dominating the laptop market
- **PowerPC / POWER** — from the AIM alliance to IBM POWER10 running your cloud
- **SPARC** — register windows, Sun workstations, Oracle, the end
- **Alpha AXP** — the fastest CPU of its era, killed by corporate acquisition
- **MIPS** — the textbook RISC, the SGI workstations, the Nintendo 64
- **PA-RISC** — HP's precision architecture and its nullification delay slots
- **Itanium (IA-64)** — the most expensively engineered commercial failure in CPU history
- **Motorola 68000** — the original Mac, the Amiga, the Atari ST, and ColdFire still shipping today
- **VAX** — the CISC pinnacle that accidentally invented the RISC movement
- **RISC-V** — the open challenger, rising fast

Each architecture gets a full museum placard: vendor, birth year, death year (if applicable), bit width, endianness, register count, description, and a "Famous For" section. Plus a Random Fact button. Plus a side-by-side comparison panel.

### 📜 75+ Historical ISA Facts
Trivia items covering history, design decisions, compiler implications, benchmarks, and delightful quirks. Did you know:

- The original ARM chip ran on a BBC Micro's power supply because the Acorn lab couldn't afford a better one, and the low power consumption was an *accident*?
- SPARC has no multiply or divide in the base ISA — early chips needed a firmware trap to do multiplication?
- The VAX 11/780 was literally defined as "1 MIPS" and became the industry baseline unit of compute?
- Alpha has no byte load instructions — you have to extract bytes with special ZAP instructions?
- Itanium's IA-32 compatibility mode ran x86 code 5-10× slower than a contemporary Pentium 4?

The ticker bar at the bottom of the GUI scrolls through these facts continuously. Right-click it to filter by ISA.

### 💬 24 Compiler & ISA Quotes
From the luminaries who built these machines:
- David Patterson and John Hennessy on RISC
- Sophie Wilson and Steve Furber on accidentally inventing the world's most-used CPU
- Jim Keller on the architectural tragedy of x86
- Fred Brooks on software engineering
- Dave Cutler on operating systems
- And several anonymous observations from the trenches that are uncomfortably accurate

### 🎮 Easter Eggs
Because life is short and assembly is hard:

- **Konami Code** (↑↑↓↓←→←→BA) — Unlocks the ISA Graveyard, complete with silicon tombstones for Alpha, PA-RISC, Itanium, desktop MIPS, and VAX
- **Click the title 7 times** — Discovers what happens when architectures retire
- **Right-click the status bar** — Random compiler quote
- **Right-click the ticker** — Filter trivia by ISA
- **The About dialog** has a hidden click zone — find it
- **Help menu** gets a secret "Show Compiler Quotes" item after the Konami code
- **Extras menu** — ISA Timeline, Instruction Count Stats, Benchmark Trivia

---

## Download

> **[⬇ Download PPC2ARM v1.0.0 for macOS (Apple Silicon)](https://github.com/007Style/PPC2ARM/releases/latest)**

| Platform | File | Size |
|----------|------|------|
| macOS (Apple Silicon / arm64) | [`PPC2ARM-1.0.0-macos-arm64.zip`](https://github.com/007Style/PPC2ARM/releases/download/v1.0.0/PPC2ARM-1.0.0-macos-arm64.zip) | ~41 MB |

**To install the macOS app:**
1. Download `PPC2ARM-1.0.0-macos-arm64.zip` from the link above
2. Unzip it (double-click or `unzip PPC2ARM-1.0.0-macos-arm64.zip`)
3. Drag `PPC2ARM.app` to your `/Applications` folder
4. **First launch:** Right-click → Open (bypasses the Gatekeeper "unidentified developer" warning — the app is unsigned but safe)
5. Double-click to open normally from then on

No Python installation required. No dependencies. It just runs.

---

## Requirements (running from source)

- **Python 3.10+**
- **wxPython >= 4.2** (GUI only — CLI and REPL work without it)

```bash
pip install wxPython
```

The CLI and REPL have **zero external dependencies**. Pure stdlib Python.

---

## Installation (from source)

```bash
git clone https://github.com/007Style/PPC2ARM.git
cd PPC2ARM
pip install -r requirements.txt   # only needed for GUI
```

That's it. There's no build step, no compiled extension, no C code, no Rust. Just Python files.

---

## Usage

### Single-Shot CLI Lookup

```bash
# PPC → ARM
python ppc2arm.py --from ppc --instr lwz
python ppc2arm.py --from ppc --instr add
python ppc2arm.py --from ppc --instr fmadd --mode 64
python ppc2arm.py --from ppc --instr vaddubm
python ppc2arm.py --from ppc --instr blr
python ppc2arm.py --from ppc --instr sc
python ppc2arm.py --from ppc --instr bdnz

# ARM → PPC
python ppc2arm.py --from arm --instr LDR
python ppc2arm.py --from arm --instr FMADD
python ppc2arm.py --from arm --instr ZIP1
python ppc2arm.py --from arm --instr SVC
python ppc2arm.py --from arm --instr CAS
```

Example output for `--from ppc --instr fmadd --mode 64`:
```
  FMADD  [DIRECT]
  Floating-Point Multiply-Add
  Syntax : frD, frA, frC, frB
  Computes frA*frC+frB in double-precision and places result in frD.

  → ARM analogues:
    FMADD                   Floating-point Fused Multiply-Add (scalar)
                            Syntax: Sd/Dd, Sn/Dn, Sm/Dm, Sa/Da
                            Computes Sn*Sm + Sa in a single fused operation.

  ℹ  FP fused multiply-add double; AArch64 FMADD Dd,Dn,Dm,Da — exact equivalent.
```

Example output for `--from ppc --instr bdnz` (a suggestion):
```
  BDNZ  [SUGGESTION]

  → ARM analogues:
    CBNZ                    Compare and Branch if Non-Zero
    SUBS                    Subtract, setting flags

  ⚠  Branch if CTR not zero after decrement; SUBS Xn,Xn,#1 + CBNZ.
```

### Interactive REPL

```bash
python ppc2arm.py          # no args drops you into REPL
python ppc2arm.py --repl   # explicit flag
```

The REPL greets you with a random compiler quote and a prompt that shows your current direction and mode:

```
  PPC2ARM — ISA Translation Station  PowerPC ↔ ARM/AArch64  v1.0.0

  Direction: PPC → ARM   Mode: 32-bit
  Type 'help' for commands, 'quit' to exit.

  "Low power was not a goal for the original ARM. It was an accident." — Sophie Wilson

ppc2arm[ppc/32]>
```

Full command reference:

```
ppc2arm[ppc/32]> lookup lwz             # translate lwz PPC→ARM
ppc2arm[ppc/32]> search vector          # full-text search in PPC instruction set
ppc2arm[ppc/32]> set dir arm            # switch to ARM→PPC direction
ppc2arm[arm/32]> lookup LDR             # translate LDR ARM→PPC
ppc2arm[arm/32]> set mode 64            # switch to 64-bit mode
ppc2arm[arm/64]> lookup SMULH           # 64-bit ARM multiply high
ppc2arm[arm/64]> list categories        # see all instruction categories
ppc2arm[arm/64]> info arm               # full ARM ISA museum placard
ppc2arm[arm/64]> info ppc               # full PPC museum placard
ppc2arm[arm/64]> info alpha             # Alpha AXP — RIP 2004
ppc2arm[arm/64]> random fact            # random fact from any ISA
ppc2arm[arm/64]> random fact arm        # random fact about ARM specifically
ppc2arm[arm/64]> help                   # full command reference
ppc2arm[arm/64]> quit                   # or just Ctrl+D
```

You can also just type a mnemonic directly without `lookup`:
```
ppc2arm[ppc/32]> vaddubm
```

### GUI

```bash
python ppc2arm.py --gui
python ppc2arm.py --gui --mode 64
```

The GUI opens the **ISA Translation Station** window with:
- **Lookup tab** — searchable instruction list on the left, full detail panel on the right
- **ISA Museum tab** — browse all 11 ISA profiles with timeline graphics and random facts
- **History Log tab** — every lookup you've done this session, timestamped
- **Mode bar** — toggle PPC→ARM / ARM→PPC direction and 32/64-bit mode
- **Ticker bar** — scrolling ISA trivia at the bottom (right-click to filter)
- **Status bar** — instruction counts and last operation (right-click for a quote)

---

## Architecture

```
PPC2ARM/
├── ppc2arm.py                 # CLI entry point (single-shot, REPL) & GUI launcher
├── requirements.txt           # wxPython >= 4.2
├── README.md                  # You are here
│
├── core/
│   ├── __init__.py
│   ├── engine.py              # InstructionEngine — lookup, search, categories,
│   │                          #   ISA profiles, random facts, compiler quotes
│   ├── registry.py            # ISARegistry — pluggable ISA tables, version/
│   │                          #   capability filtering, mode compatibility
│   └── fuzzy.py               # Levenshtein fuzzy matcher — no external deps,
│                              #   prefix/substring/edit-distance scoring
│
├── data/
│   ├── __init__.py
│   ├── isa_schema.py          # Dataclasses: Instruction, MappingEntry,
│   │                          #   ISACapability; well-known capability constants
│   │                          #   (ARMv8.0-A → ARMv9.2-A, NEON, SVE, SME,
│   │                          #    PowerISA-2.07 → PowerISA-3.1)
│   ├── ppc_instructions.py    # 423 PPC mnemonics: PPC32, PPC64, AltiVec/VMX,
│   │                          #   all dot-forms, overflow forms, update forms
│   ├── arm_instructions.py    # 164 ARM mnemonics: AArch64 base, FP scalar,
│   │                          #   NEON/ASIMD, SVE, SVE2, LSE atomics
│   ├── mappings.py            # 256 PPC_TO_ARM entries + auto-generated
│   │                          #   ARM_TO_PPC reverse table; full porting notes
│   └── isa_trivia.py          # 75 ISA facts, 11 profiles, 24 quotes,
│                              #   Konami unlock text, hidden messages
│
└── gui/
    ├── __init__.py
    ├── app.py                 # PPC2ARMApp (wx.App) + MainFrame + HistoryPanel
    ├── theme.py               # Retro phosphor-green colour palette, fonts,
    │                          #   apply_theme(), confidence_colour()
    ├── mode_bar.py            # Direction toggle (PPC↔ARM) + mode selector (32/64)
    │                          #   emits EVT_DIRECTION_CHANGED, EVT_MODE_CHANGED
    ├── main_panel.py          # SplitterWindow: SearchableList + ResultPanel
    ├── result_panel.py        # RichTextCtrl-based instruction detail renderer
    ├── isa_museum.py          # ISAMuseumPanel + ISATimelineDialog
    ├── easter_eggs.py         # EasterEggManager: Konami code, title clicks,
    │                          #   graveyard dialog, secret menu items
    └── widgets/
        ├── __init__.py
        ├── searchable_list.py # SearchCtrl + ListCtrl with live filtering
        ├── ticker_bar.py      # wx.Timer-driven scrolling trivia ticker
        └── about_dialog.py    # About dialog + hidden Easter egg click zone
```

---

## The Mapping Table — A Philosophical Note

Instruction set mapping is not a pure function. Two mnemonics from different ISAs can have the same *name*, similar *syntax*, identical *behavior in the common case*, and still behave differently at the edges in ways that will destroy your program if you're not careful.

A few examples of things PPC2ARM tracks so you don't have to discover them the hard way:

**`subf` is not `SUB`** — PowerPC's `subf rD,rA,rB` computes `rD = rB - rA`. Note the reversed operands. ARM's `SUB Xd,Xn,Xm` computes `Xd = Xn - Xm`. If you translate naively without swapping operands, you will get the wrong sign. Confidence: `close`.

**`lwzu` is not a simple `LDR`** — The PPC update-form `lwzu rD,d(rA)` loads from memory AND writes the updated address back into rA. ARM's post-index `LDR Wt,[Xn],#imm` and pre-index `LDR Wt,[Xn,#imm]!` cover this idiom, but the encoding and assembly syntax are different. Confidence: `close`.

**`vaddubm` is `ADD Vd.16B`** — This one actually maps directly. PPC AltiVec adds sixteen unsigned bytes modulo 256; AArch64 NEON does exactly the same thing. Confidence: `direct`. (Enjoy it. These are rare.)

**`vperm` is not `TBL`** — Both are byte-shuffle instructions that use a separate index vector. But PPC AltiVec `vperm` is big-endian by design (element 0 is at the high byte), while AArch64 `TBL` is little-endian. If you're doing vector permutations and your results look reversed, this is why. Confidence: `close`, with a note.

**`bdnz` has no ARM equivalent** — PowerPC has a dedicated Count Register (CTR) and `bdnz` decrements it and branches if non-zero, in a single instruction. ARM has no CTR. You need `SUBS Xn,Xn,#1` followed by `CBNZ Xn,label`. Two instructions. Confidence: `suggestion`.

This is the level of detail throughout the entire mapping table.

---

## Data Sources

Every instruction definition and mapping was researched against the official architecture documentation:

| Source | Document |
|--------|----------|
| IBM POWER ISA v3.1 | IBM OpenPOWER Foundation (public PDF) |
| IBM POWER ISA v2.07 | IBM OpenPOWER Foundation (public PDF) |
| Arm Architecture Reference Manual (ARMv8, for A-profile) | developer.arm.com |
| Arm Architecture Reference Manual Supplement — SVE | developer.arm.com |
| Arm Neon Intrinsics Reference | developer.arm.com |
| Arm A64 Instruction Set Architecture | developer.arm.com |
| SPARC v8/v9 Architecture Manual | SPARC International / IEEE Std 1754 |
| Alpha Architecture Reference Manual | Digital Equipment Corporation |
| MIPS32/64 Architecture Reference Manual | MIPS Technologies |
| PA-RISC 2.0 Architecture Reference Manual | Hewlett-Packard |
| IA-64 Application Developer's Architecture Guide | Intel Corporation |
| M68000 Family Programmer's Reference Manual | Motorola |
| VAX Architecture Reference Manual | Digital Equipment Corporation |

---

## Non-Goals

To keep the scope honest, PPC2ARM intentionally does NOT:

- Assemble or disassemble actual machine code bytes
- Decode binary instruction encodings
- Emulate PowerPC or ARM execution
- Cover every POWER10 / AMX / AVX-512 / SME2 extension in depth
- Make network calls, phone home, or collect telemetry
- Package as a macOS .app bundle or .dmg (just run the Python script)
- Replace reading the actual architecture manuals (seriously, read them)

---

## A Love Letter to the ISAs That Didn't Make It

This tool was built partly out of genuine respect for the architectures that lost the market wars but won the engineering argument. Alpha was faster than everything. PA-RISC had nullification. Itanium had predication on literally every instruction. VAX had MATCHC — a single instruction that finds a substring in memory.

They lost to x86 not because they were worse, but because compatibility, economics, and timing matter more than elegance.

ARM won not because it was the most powerful, but because it was cheap to license, simple to implement, and drew almost no power. Sophie Wilson and Steve Furber designed it in eighteen months with a team of twelve. The chip ran off a BBC Micro's leftover power supply. The low power consumption was, famously, an accident.

That chip now runs in over 250 billion devices.

Architecture is humbling.

---

## Acknowledgments

Built with:
- **Python 3.10+** — the language that outlasted every framework war
- **wxPython 4.2** — the GUI toolkit that refuses to die, and we love it for that
- **IBM POWER ISA specification** — thank you IBM for making it public
- **Arm Architecture Reference Manual** — available free at developer.arm.com
- **The entire history of computer architecture** — standing on the shoulders of giants

*From the minds of IBM Bob & Daneyand — two entities who spent way too long thinking about instruction sets so you don't have to.*

---

## License

MIT. Do whatever you want with it. Port it to RISC-V. We dare you.

```
  † Alpha AXP     (1992–2004)  "Fastest ever. Gone too soon."
  † PA-RISC       (1986–2008)  "Precision was its middle name."
  † Itanium       (2001–2021)  "Explicitly parallel in failure."
  † MIPS (desktop)(1985–2002)  "Textbook perfect, market lost."
  † VAX           (1977–2000)  "CISC pinnacle. RISC casualty."

  ♥ ARM           still alive (in your pocket right now)
  ♥ PowerPC/POWER still alive (in your cloud, your car, your console)
  ♥ RISC-V        rising fast (open, free, unstoppable)
```
