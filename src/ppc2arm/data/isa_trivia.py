"""
isa_trivia.py — Historical ISA facts, profiles, quotes, and easter egg content
             for PPC2ARM.

Exports
-------
ISA_FACTS          list[dict]   — trivia items (isa, text, category)
ISA_PROFILES       dict[str, dict] — one profile per architecture
COMPILER_QUOTES    list[str]    — memorable quotes from ISA/compiler luminaries
KONAMI_UNLOCK_TEXT str          — secret message revealed by Konami code
HIDDEN_MESSAGES    dict[str, str] — keyed by trigger string
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# ISA PROFILES
# ---------------------------------------------------------------------------

ISA_PROFILES: dict[str, dict] = {

    "arm": {
        "name": "ARM / AArch64",
        "vendor": "Arm Holdings (formerly Advanced RISC Machines / Acorn)",
        "year": 1985,
        "bits": 32,      # AArch64 added in ARMv8-A (2011, products 2013)
        "endian": "Bi-endian (little-endian in practice)",
        "registers": 31,  # AArch64: X0–X30 + XZR/SP
        "description": (
            "Advanced RISC Machine. Born at Acorn Computers in Cambridge in 1985, "
            "ARM was designed by a team of 12 engineers to be small, low-power, and "
            "easy to compile for. The ARMv8-A architecture (2011) added 64-bit "
            "AArch64 execution state while retaining full 32-bit compatibility. "
            "ARMv9 (2021) made SVE2 mandatory and introduced the Realm Management "
            "Extension for confidential computing."
        ),
        "famous_for": (
            "Powering virtually every smartphone and tablet on earth; "
            "Apple Silicon (M1/M2/M3) dominating laptop performance; "
            "AWS Graviton and Ampere Altra reshaping cloud compute; "
            "the most-produced CPU architecture in history with over 250 billion "
            "chips shipped."
        ),
        "died": None,
    },

    "sparc": {
        "name": "SPARC",
        "vendor": "Sun Microsystems (v8) / SPARC International",
        "year": 1987,
        "bits": 32,
        "endian": "Big (v8); Bi-endian (v9)",
        "registers": 32,
        "description": (
            "Scalable Processor ARChitecture. A clean RISC design from Sun "
            "Microsystems, notable for its register-window mechanism that "
            "eliminates most function-call save/restore overhead."
        ),
        "famous_for": (
            "Register windows; open-standard licensing model; "
            "powering Sun workstations and servers from 1987 to the Oracle era."
        ),
        "died": None,
    },

    "alpha": {
        "name": "Alpha AXP",
        "vendor": "Digital Equipment Corporation (DEC)",
        "year": 1992,
        "bits": 64,
        "endian": "Bi-endian",
        "registers": 32,
        "description": (
            "DEC's 64-bit RISC architecture, designed to be the fastest "
            "microprocessor in the world at its launch. Notably, there are no "
            "byte or halfword load/store instructions — all memory ops are "
            "word or doubleword."
        ),
        "famous_for": (
            "Being the first broadly available 64-bit commercial CPU; "
            "Windows NT port; Compaq acquisition; eventual absorption into HP."
        ),
        "died": 2004,
    },

    "mips": {
        "name": "MIPS",
        "vendor": "MIPS Computer Systems / MIPS Technologies",
        "year": 1985,
        "bits": 32,
        "endian": "Bi-endian",
        "registers": 32,
        "description": (
            "Microprocessor without Interlocked Pipeline Stages — the "
            "textbook RISC design. Originated at Stanford under John Hennessy. "
            "Famous for load-delay slots visible to the programmer."
        ),
        "famous_for": (
            "Patterson & Hennessy textbook; SGI workstations; Nintendo 64; "
            "PlayStation 1 & 2; countless embedded controllers."
        ),
        "died": None,
    },

    "pa-risc": {
        "name": "PA-RISC",
        "vendor": "Hewlett-Packard",
        "year": 1986,
        "bits": 32,
        "endian": "Big",
        "registers": 32,
        "description": (
            "Precision Architecture RISC. HP's in-house RISC design, known "
            "for its nullification bits on every branch instruction."
        ),
        "famous_for": (
            "HP 9000 workstations and servers; nullification delay slots; "
            "being the architecture that Itanium was meant to replace."
        ),
        "died": 2008,
    },

    "itanium": {
        "name": "Itanium (IA-64)",
        "vendor": "Intel / Hewlett-Packard",
        "year": 2001,
        "bits": 64,
        "endian": "Bi-endian",
        "registers": 128,
        "description": (
            "Explicitly Parallel Instruction Computing (EPIC). Instructions "
            "are grouped into 128-bit bundles of three, with a template "
            "field telling the processor which units each instruction uses."
        ),
        "famous_for": (
            "EPIC architecture; predicated execution on every instruction; "
            "rotating register file; commercial failure despite extraordinary engineering."
        ),
        "died": 2021,
    },

    "68k": {
        "name": "Motorola 68000",
        "vendor": "Motorola",
        "year": 1979,
        "bits": 32,
        "endian": "Big",
        "registers": 16,
        "description": (
            "A CISC 32-bit microprocessor with a clean, orthogonal instruction "
            "set. Offered a flat address space, making it the favourite of "
            "systems programmers of its era."
        ),
        "famous_for": (
            "Original Apple Macintosh; Amiga; Atari ST; ColdFire derivatives "
            "still manufactured today."
        ),
        "died": None,
    },

    "vax": {
        "name": "VAX",
        "vendor": "Digital Equipment Corporation (DEC)",
        "year": 1977,
        "bits": 32,
        "endian": "Little",
        "registers": 16,
        "description": (
            "Virtual Address eXtension. The pinnacle of CISC design — an "
            "instruction set with over 300 opcodes, arbitrary addressing modes "
            "on every operand."
        ),
        "famous_for": (
            "OpenVMS; scientific computing in the 1980s; inspiring the RISC "
            "movement; DEC's most successful minicomputer line."
        ),
        "died": 2000,
    },

    "ppc": {
        "name": "PowerPC / POWER",
        "vendor": "IBM / Motorola / Apple (AIM alliance)",
        "year": 1992,
        "bits": 32,
        "endian": "Bi-endian",
        "registers": 32,
        "description": (
            "Performance Optimization With Enhanced RISC. Descended from IBM "
            "POWER, the AIM alliance designed PowerPC to challenge Intel's x86. "
            "Used a separate condition register file (CR0–CR7) and link register."
        ),
        "famous_for": (
            "Apple Power Mac and PowerBook (1994–2006); Nintendo GameCube and "
            "Wii; Microsoft Xbox 360; IBM POWER servers; AltiVec SIMD."
        ),
        "died": None,
    },

    "x86": {
        "name": "x86 / x86-64",
        "vendor": "Intel (AMD64 extension by AMD)",
        "year": 1978,
        "bits": 16,
        "endian": "Little",
        "registers": 8,
        "description": (
            "The most commercially successful CPU architecture in history. "
            "Started as the Intel 8086 and grew through decades of extensions."
        ),
        "famous_for": (
            "IBM PC and every descendant; backward compatibility spanning "
            "four decades; surviving every RISC challenge."
        ),
        "died": None,
    },

    "riscv": {
        "name": "RISC-V",
        "vendor": "RISC-V International (open standard)",
        "year": 2010,
        "bits": 32,
        "endian": "Little",
        "registers": 32,
        "description": (
            "An open, royalty-free RISC ISA developed at UC Berkeley. "
            "Modular by design — RV32I is a minimal 40-instruction base with "
            "optional extensions (M, A, F, D, C, V …) added as needed."
        ),
        "famous_for": (
            "Open-source hardware movement; SiFive, StarFive, Alibaba T-Head; "
            "Western Digital storage controllers; growing adoption in HPC and AI."
        ),
        "died": None,
    },
}


# ---------------------------------------------------------------------------
# ISA FACTS
# ---------------------------------------------------------------------------

ISA_FACTS: list[dict] = [

    # ------------------------------------------------------------------ #
    #  ARM (10 facts)                                                       #
    # ------------------------------------------------------------------ #
    {"isa": "arm", "category": "history",
     "text": "ARM began as the Acorn RISC Machine project in 1983 at Acorn Computers "
             "in Cambridge, UK. A small team of 12 engineers — including Sophie Wilson "
             "and Steve Furber — designed the ARM1 chip in just 18 months. The first "
             "silicon arrived working on its very first test, powered by a BBC Micro."},
    {"isa": "arm", "category": "design",
     "text": "The original ARM ISA had a unique 4-bit condition code on EVERY "
             "instruction — any ARM instruction could be made conditional. "
             "AArch32 retains this. AArch64 removed per-instruction conditions "
             "from most instructions (only B.cond and a few others remain), "
             "trading expressiveness for simpler decode pipelines."},
    {"isa": "arm", "category": "history",
     "text": "Apple co-funded Advanced RISC Machines Ltd in 1990 (the spin-off from "
             "Acorn) to get ARM chips for the Newton PDA. ARM Holdings became one "
             "of the most valuable semiconductor IP companies in the world — "
             "ultimately acquired by SoftBank for $32 billion in 2016, then taken "
             "public again in 2023."},
    {"isa": "arm", "category": "design",
     "text": "AArch64 introduced 31 general-purpose 64-bit registers (X0–X30) "
             "plus a dedicated zero register (XZR) and stack pointer (SP). "
             "This was a major upgrade from AArch32's 16 registers — GCC/LLVM "
             "register pressure dropped dramatically, reducing spills on complex code."},
    {"isa": "arm", "category": "benchmark",
     "text": "Apple's M1 chip (2020), based on ARMv8.5-A, outperformed contemporary "
             "Intel Core i9 processors on single-threaded workloads in Geekbench "
             "while using a fraction of the power. It marked the first credible "
             "challenge to x86 in the laptop space since Itanium."},
    {"isa": "arm", "category": "quirk",
     "text": "ARM has a 'Thumb' compressed 16-bit instruction encoding (ARMv4T, 1995) "
             "and Thumb-2 (ARMv6T2, 2003) mixed 16/32-bit encoding, allowing code "
             "density close to x86 CISC. Apple's iOS historically used Thumb-2 for "
             "almost all userspace code to reduce binary sizes."},
    {"isa": "arm", "category": "compiler",
     "text": "LLVM's AArch64 backend is considered one of the cleanest in the "
             "compiler due to ARM's regular 3-operand fixed-width encoding. "
             "The register file is large enough that leaf functions on AArch64 "
             "almost never spill to the stack in practice."},
    {"isa": "arm", "category": "design",
     "text": "ARM's SVE (Scalable Vector Extension, 2016) introduced a revolutionary "
             "predicate-based programming model where vector length is not fixed at "
             "compile time. Code compiled for SVE runs correctly on implementations "
             "with 128-bit, 256-bit, 512-bit, or even 2048-bit vector widths — "
             "without recompilation."},
    {"isa": "arm", "category": "history",
     "text": "AWS launched its Graviton processor (ARMv8 based) in 2018, the first "
             "ARM-based cloud instance for general workloads. Graviton3 (2021, "
             "ARMv8.4-A) offered 25% better performance than Graviton2 and matched "
             "or exceeded equivalent Intel/AMD instances at 20% lower cost. "
             "ARM now powers a significant fraction of AWS infrastructure."},
    {"isa": "arm", "category": "design",
     "text": "AArch64's ADRP+ADD instruction pair is the standard way to reference "
             "global data: ADRP loads the 4 KB page address of a symbol (PC-relative, "
             "±4 GB range), and ADD adds the page offset. This two-instruction "
             "sequence replaced the GOT indirection for position-independent code "
             "on many platforms."},

    # ------------------------------------------------------------------ #
    #  SPARC (8 facts)                                                      #
    # ------------------------------------------------------------------ #
    {"isa": "sparc", "category": "design",
     "text": "SPARC's register windows mean that on a function call, the CPU "
             "simply slides a window pointer — renames registers — rather than "
             "spilling them to memory. A deeply nested call chain can exhaust "
             "all windows, causing a 'window overflow trap'."},
    {"isa": "sparc", "category": "history",
     "text": "The SPARC v8 specification was published as an open standard, "
             "allowing multiple vendors (Fujitsu, Ross Technology, Cypress "
             "Semiconductor) to build competing SPARC CPUs — rare for the era."},
    {"isa": "sparc", "category": "benchmark",
     "text": "SPARC-based Sun workstations dominated CAD and EDA workloads "
             "in the early 1990s. The SPARCstation 1 (1989) at $9,000 offered "
             "12 MIPS, roughly matching a $25,000 VAX 8530."},
    {"isa": "sparc", "category": "design",
     "text": "SPARC v9 made the architecture 64-bit and bi-endian in 1995, "
             "adding 64-bit registers while retaining all v8 integer instructions "
             "unchanged — a notably smooth ISA extension."},
    {"isa": "sparc", "category": "quirk",
     "text": "The SPARC architecture specifies a branch delay slot: the "
             "instruction after a branch always executes before the branch "
             "takes effect. Compilers learned to fill these slots productively, "
             "but it frequently surprises assembly programmers."},
    {"isa": "sparc", "category": "history",
     "text": "Oracle acquired Sun in 2010 and continued shipping SPARC T-series "
             "(Niagara) processors emphasising thread count over single-thread "
             "speed — a controversial strategy that eventually lost to x86 in "
             "the data centre."},
    {"isa": "sparc", "category": "compiler",
     "text": "GCC's SPARC backend has to handle 'leaf function optimisation': "
             "functions that make no calls can skip allocating a register "
             "window entirely, saving the window-slide overhead."},
    {"isa": "sparc", "category": "design",
     "text": "SPARC specifies NO multiply or divide instructions in the v8 "
             "base ISA — they are optional extensions. Early SPARC chips "
             "required a software trap to a firmware routine for integer "
             "multiply/divide."},

    # ------------------------------------------------------------------ #
    #  Alpha (8 facts)                                                      #
    # ------------------------------------------------------------------ #
    {"isa": "alpha", "category": "design",
     "text": "Alpha has no byte or halfword load/store instructions in the "
             "base ISA. All loads return a 64-bit value. Byte manipulation "
             "uses special 'byte zap' (ZAP/ZAPNOT) and 'extract' instructions "
             "to isolate sub-word fields."},
    {"isa": "alpha", "category": "history",
     "text": "Windows NT was ported to Alpha by 1993, making DEC's chip one "
             "of only four architectures NT ever ran on (alongside x86, MIPS, "
             "and PowerPC). NT/Alpha was discontinued in 1999 after the "
             "Compaq acquisition."},
    {"isa": "alpha", "category": "benchmark",
     "text": "The 21064 (EV4) launched in 1992 at 150–200 MHz and was "
             "measurably faster than any x86 processor for floating-point "
             "workloads until the Pentium Pro arrived in 1995."},
    {"isa": "alpha", "category": "design",
     "text": "Alpha's floating-point model explicitly exposes IEEE traps as "
             "software completions — the hardware can optionally deliver FP "
             "exceptions to software, or silently produce the IEEE-defined "
             "result."},
    {"isa": "alpha", "category": "history",
     "text": "Compaq acquired DEC in 1998, then HP acquired Compaq in 2002. "
             "HP killed Alpha development in 2004, directing customers to "
             "migrate to Itanium — a migration that many never completed."},
    {"isa": "alpha", "category": "quirk",
     "text": "Alpha integer registers are strictly 64-bit; there are no 32-bit "
             "register views. A 32-bit ADD instruction (ADDL) produces a "
             "sign-extended 64-bit result."},
    {"isa": "alpha", "category": "compiler",
     "text": "The Alpha AXP port of GCC was notable for aggressive scheduling "
             "optimisations enabled by Alpha's in-order, dual-issue pipeline "
             "and the lack of interlocks — mis-schedule and you stall."},
    {"isa": "alpha", "category": "history",
     "text": "Several Alpha designs (EV6, EV7) were actually fabricated by "
             "Samsung under license. The Samsung Alpha 21264A ran at 1.25 GHz — "
             "among the highest clock rates of any CPU in 2003."},

    # ------------------------------------------------------------------ #
    #  MIPS (8 facts)                                                       #
    # ------------------------------------------------------------------ #
    {"isa": "mips", "category": "history",
     "text": "MIPS stands for Microprocessor without Interlocked Pipeline "
             "Stages. The original R2000 (1985) truly had no interlocks — "
             "if you read a register one cycle after a load, you got garbage."},
    {"isa": "mips", "category": "benchmark",
     "text": "The SGI Indigo² workstation with an R4400 (250 MHz, 1994) "
             "performed Jurassic Park's CGI dinosaur rendering and became "
             "the iconic workstation of the early 3D era."},
    {"isa": "mips", "category": "design",
     "text": "MIPS introduced the HI/LO register pair for multiply/divide — "
             "results land in HI (high word) and LO (low word), then MFHI/MFLO "
             "copy them to general registers."},
    {"isa": "mips", "category": "quirk",
     "text": "The branch delay slot in MIPS means the instruction after every "
             "branch always executes. The MIPS32r6 revision (2014) finally "
             "eliminated delay slots, breaking binary compatibility with all "
             "prior MIPS code."},
    {"isa": "mips", "category": "history",
     "text": "Nintendo used a custom MIPS R4300i (NEC VR4300) in the Nintendo "
             "64 (1996), running at 93.75 MHz. Its 64-bit MIPS core was largely "
             "used in 32-bit mode due to memory constraints."},
    {"isa": "mips", "category": "compiler",
     "text": "MIPS's calling convention assigns $a0–$a3 for function arguments, "
             "$v0–$v1 for return values, and $t0–$t9 as caller-saved temporaries. "
             "The explicit split became a model for subsequent RISC ABIs."},
    {"isa": "mips", "category": "history",
     "text": "Wave Computing acquired the MIPS architecture in 2018 and "
             "briefly open-sourced the MIPS ISA in 2019, before financial "
             "difficulties led to bankruptcy and acquisition by MIPS Tech LLC."},
    {"isa": "mips", "category": "design",
     "text": "MIPS16 and microMIPS are compressed 16-bit instruction encodings "
             "designed for embedded code density, similar in spirit to ARM Thumb. "
             "MicroMIPS can reduce code size by 30–40% vs standard MIPS."},

    # ------------------------------------------------------------------ #
    #  PA-RISC (7 facts)                                                    #
    # ------------------------------------------------------------------ #
    {"isa": "pa-risc", "category": "design",
     "text": "Every PA-RISC branch instruction has a nullification bit. "
             "When set, the instruction in the branch delay slot is annulled "
             "if the branch is not taken — the opposite of SPARC's always-execute model."},
    {"isa": "pa-risc", "category": "history",
     "text": "HP introduced PA-RISC with the HP 9000/840 in 1986. It powered "
             "HP's workstations and servers for over two decades."},
    {"isa": "pa-risc", "category": "design",
     "text": "PA-RISC 2.0 (1996) extended the architecture to 64-bit with a "
             "fully backward-compatible ISA. The PA-RISC 8000 had a 56-entry "
             "reorder buffer — very large for a RISC of that era."},
    {"isa": "pa-risc", "category": "compiler",
     "text": "HP's optimising compiler for PA-RISC pioneered software pipelining, "
             "modulo scheduling, and predicated execution via nullification."},
    {"isa": "pa-risc", "category": "history",
     "text": "PA-RISC was the primary architecture for HP-UX. When HP partnered "
             "with Intel on Itanium, they promised a binary translation layer "
             "— it worked but with significant performance penalties."},
    {"isa": "pa-risc", "category": "quirk",
     "text": "PA-RISC stores function pointers as pointers to a descriptor "
             "structure (a 'plabel'), not directly to code. This surprises C "
             "programmers expecting a function pointer to equal the instruction address."},
    {"isa": "pa-risc", "category": "history",
     "text": "The last PA-RISC processor, the PA-8900, was introduced in 2005 "
             "and produced until 2008."},

    # ------------------------------------------------------------------ #
    #  Itanium (8 facts)                                                    #
    # ------------------------------------------------------------------ #
    {"isa": "itanium", "category": "design",
     "text": "Every Itanium instruction is 41 bits wide. Three instructions "
             "are packed into a 128-bit bundle alongside a 5-bit template "
             "field that tells the processor which execution units each slot targets."},
    {"isa": "itanium", "category": "design",
     "text": "Itanium has 64 integer registers arranged as a rotating register "
             "file for software-pipelined loops — on each BRLC (branch with "
             "loop count), the register base pointer advances."},
    {"isa": "itanium", "category": "history",
     "text": "Intel and HP announced Itanium in 1994, originally called 'Merced'. "
             "It shipped in 2001 — seven years of development. Critics noted "
             "that x86-64 (AMD64) shipped in 2003, two years later, and ran "
             "all existing x86 software natively."},
    {"isa": "itanium", "category": "compiler",
     "text": "Itanium's performance is almost entirely compiler-dependent. "
             "Without a world-class optimising compiler performing EPIC "
             "scheduling, IA-64 hardware idles on NOPs."},
    {"isa": "itanium", "category": "design",
     "text": "Itanium's predication system lets every instruction carry a "
             "1-bit predicate register. If the predicate is false, the "
             "instruction becomes a NOP, enabling if-conversion."},
    {"isa": "itanium", "category": "history",
     "text": "Microsoft dropped Itanium support in Windows Server 2008 R2. "
             "Red Hat dropped it in RHEL 6. The last Itanium chip, the Kittson "
             "(9700 series), shipped in 2017 for HP-UX customers."},
    {"isa": "itanium", "category": "quirk",
     "text": "Itanium's IA-32 compatibility mode (executing legacy x86 code) "
             "was spectacularly slow — 5–10× slower than a contemporary "
             "Pentium 4 on the same workload."},
    {"isa": "itanium", "category": "benchmark",
     "text": "At peak, Itanium 2 Montecito (dual-core, 2006) achieved excellent "
             "floating-point throughput on HPC workloads compiled with Intel's "
             "compiler. The hardware was capable; the ecosystem was not."},

    # ------------------------------------------------------------------ #
    #  68k (8 facts)                                                        #
    # ------------------------------------------------------------------ #
    {"isa": "68k", "category": "design",
     "text": "The 68000 is often called the first 'programmer-friendly' CISC: "
             "8 data registers and 8 address registers, every instruction "
             "working on any register, and a flat 24-bit address space."},
    {"isa": "68k", "category": "history",
     "text": "The original Apple Macintosh (1984) used a Motorola 68000 at 8 MHz. "
             "Apple stuck with the 68k family until 1994, when they switched to PowerPC."},
    {"isa": "68k", "category": "history",
     "text": "The Amiga 1000 (1985) used a 68000 with custom chips (Agnus, Denise, Paula) "
             "for graphics, DMA, and sound — far ahead of contemporary PCs."},
    {"isa": "68k", "category": "design",
     "text": "The 68020 introduced a 32-bit address bus and the BFEXTU/BFINS "
             "bit-field instructions that are still unmatched in expressiveness "
             "in any RISC ISA."},
    {"isa": "68k", "category": "quirk",
     "text": "The 68000 trap mechanism executes a trap handler for almost "
             "everything: divide-by-zero, illegal instruction, privilege "
             "violation, address error."},
    {"isa": "68k", "category": "compiler",
     "text": "GCC's 68k port was one of the first non-VAX targets, written "
             "by Richard Stallman himself."},
    {"isa": "68k", "category": "history",
     "text": "The ColdFire processor family (1994) is a trimmed-down 68k "
             "subset targeting embedded markets, still in production today."},
    {"isa": "68k", "category": "design",
     "text": "The 68k CCR (Condition Code Register) is a clean 5-bit field: "
             "C (carry), V (overflow), Z (zero), N (negative), X (extend). "
             "The X bit acts as a sticky carry for multi-precision arithmetic."},

    # ------------------------------------------------------------------ #
    #  VAX (5 facts)                                                        #
    # ------------------------------------------------------------------ #
    {"isa": "vax", "category": "design",
     "text": "VAX instructions can reference memory operands with any of twelve "
             "addressing modes — including auto-increment, auto-decrement, and "
             "indexed deferred — on every operand of every instruction."},
    {"isa": "vax", "category": "history",
     "text": "VMS (Virtual Memory System), developed by Dave Cutler and his "
             "team at DEC, shipped in 1977. It is still maintained as OpenVMS "
             "and ran on Alpha and Itanium after VAX hardware was discontinued."},
    {"isa": "vax", "category": "benchmark",
     "text": "The VAX 11/780 (1977) was informally defined as '1 MIPS'. "
             "For years, 'VAX MIPS' was used as the baseline unit of compute "
             "across the industry."},
    {"isa": "vax", "category": "quirk",
     "text": "VAX has native hardware support for packed BCD arithmetic, "
             "string operations, and queue manipulation. The MATCHC "
             "instruction finds a substring in memory."},
    {"isa": "vax", "category": "history",
     "text": "The VAX architecture directly inspired the RISC movement: "
             "Patterson and Ditzel's 1980 paper 'The Case for the Reduced "
             "Instruction Set Computer' used VAX as the cautionary CISC example."},

    # ------------------------------------------------------------------ #
    #  PPC / POWER (8 facts)                                                #
    # ------------------------------------------------------------------ #
    {"isa": "ppc", "category": "history",
     "text": "The AIM alliance (Apple, IBM, Motorola) formed in 1991 to create "
             "a common RISC platform that could challenge Intel. The first "
             "PowerPC chip, the 601, shipped in 1993 and powered the first "
             "Power Macintosh in 1994."},
    {"isa": "ppc", "category": "design",
     "text": "PowerPC has eight 4-bit condition register fields (CR0–CR7). "
             "Integer comparisons set CR0 by default; floating-point ops set "
             "CR1. The other six fields are available for arbitrary use, "
             "enabling complex boolean expressions without branches."},
    {"isa": "ppc", "category": "quirk",
     "text": "PPC's load-store architecture means there is no 'ADD [mem], reg' "
             "instruction. Every computation touches registers only. This forced "
             "x86 programmers to rethink idioms but simplified processor design."},
    {"isa": "ppc", "category": "history",
     "text": "Apple's transition from PowerPC to Intel (2006) was announced "
             "at WWDC 2005. Steve Jobs revealed that Mac OS X had been compiled "
             "for x86 since its inception — a 'secret Intel project'."},
    {"isa": "ppc", "category": "design",
     "text": "IBM's AltiVec (VMX) SIMD extension (1999) added 128-bit vector "
             "registers and over 160 new instructions. Apple called it 'Velocity "
             "Engine' in marketing materials. It was a key competitive advantage "
             "over SSE for media processing workloads."},
    {"isa": "ppc", "category": "history",
     "text": "The Microsoft Xbox 360 (2005) and Sony PlayStation 3 (2006) both "
             "used PowerPC-based processors — an IBM Xenon and IBM Cell "
             "respectively. The Cell's 9 cores (1 PPE + 8 SPEs) were PPC-derived."},
    {"isa": "ppc", "category": "design",
     "text": "PowerPC64 added 64-bit registers while keeping the 32-bit "
             "instruction encoding. The 'lwa' (load word algebraic) instruction "
             "was introduced specifically for 64-bit mode to sign-extend a 32-bit "
             "memory value — there is no equivalent in 32-bit PPC."},
    {"isa": "ppc", "category": "benchmark",
     "text": "IBM POWER10 (2021, 7nm) supports up to 15 TB of system memory per "
             "socket and includes the Matrix Math Accelerator unit for AI inference "
             "workloads. It runs IBM i (OS/400), AIX, and Linux."},

    # ------------------------------------------------------------------ #
    #  RISC-V (5 facts)                                                     #
    # ------------------------------------------------------------------ #
    {"isa": "riscv", "category": "history",
     "text": "RISC-V was designed at UC Berkeley in 2010 by Krste Asanović "
             "and his students, originally as a teaching ISA. Its open-source "
             "license made it popular almost immediately with hardware researchers."},
    {"isa": "riscv", "category": "design",
     "text": "The RISC-V base integer ISA (RV32I) has only 40 instructions. "
             "Standard extensions add multiplication (M), atomics (A), "
             "single-precision float (F), double (D), and compressed encoding (C). "
             "An implementation implementing RV64GC supports all of these."},
    {"isa": "riscv", "category": "quirk",
     "text": "RISC-V deliberately omits a link register. The JAL (jump and link) "
             "instruction stores the return address in any general-purpose register "
             "— by convention, x1. This makes the ABI explicit rather than "
             "architecture-mandated."},
    {"isa": "riscv", "category": "history",
     "text": "Western Digital announced in 2019 that it would replace ARM cores "
             "in its storage controller chips with RISC-V, shipping over 1 billion "
             "RISC-V cores per year — the largest single commitment to RISC-V at "
             "the time."},
    {"isa": "riscv", "category": "design",
     "text": "RISC-V's 'V' vector extension (ratified 2021) follows a length-agnostic "
             "model similar to ARM SVE: code specifies a requested vector length "
             "using vsetvl/vsetvli, and the hardware provides up to its maximum "
             "implementation width."},
]


# ---------------------------------------------------------------------------
# COMPILER / ISA QUOTES
# ---------------------------------------------------------------------------

COMPILER_QUOTES: list[str] = [
    # Patterson & Hennessy
    '"The most important computer languages of the future will be those that '
    'emphasize simplicity." — David Patterson',

    '"RISC is not just a style; it is a discipline." — John Hennessy',

    '"A computer is a machine that can be instructed to carry out sequences '
    'of arithmetic or logical operations automatically. The amazing thing '
    'is how much humans disagree about how those instructions should look." '
    '— Andrew Tanenbaum',

    '"Compatibility means deliberately repeating other people\'s mistakes." '
    '— David Wheeler',

    '"Premature optimization is the root of all evil." — Donald Knuth',

    '"The most effective debugging tool is still careful thought, coupled '
    'with judiciously placed print statements." — Brian Kernighan',

    '"There are only two kinds of programming languages: those that people '
    'always complain about and those that nobody uses." — Bjarne Stroustrup',

    # Jim Keller (chip architect)
    '"We kept adding complexity to x86 and then hiding it. Microcode, '
    'out-of-order engines, reorder buffers — all to make a 1978 ISA run '
    'fast in 2005. That\'s both an impressive engineering achievement and '
    'a profound architectural tragedy." — Jim Keller (paraphrased)',

    '"Every instruction set extension is a mortgage on future chip area." '
    '— Jim Keller',

    # Sophie Wilson (ARM architect)
    '"We were trying to make the simplest thing that worked. The first ARM '
    'chip cost about £26 in 1985 prices. Nobody imagined it would end up in '
    'ten billion devices a year." — Sophie Wilson, on designing the ARM1',

    '"Low power was not a goal for the original ARM. It was an accident — '
    'we couldn\'t afford a good power supply for the BBC Micro lab, so the '
    'chip had to run on what the micro could provide." — Sophie Wilson',

    # Steve Furber (ARM architect)
    '"The ARM processor is a lesson in the power of constraints. Limited '
    'transistor budget, limited power, limited time. Every constraint made '
    'the design cleaner." — Steve Furber',

    # Dave Cutler
    '"A good operating system is one that doesn\'t get in your way." '
    '— Dave Cutler, architect of VMS and Windows NT',

    '"I designed NT to be portable because I\'d learned that no '
    'architecture is right forever." — Dave Cutler',

    # Fred Brooks
    '"There is no single development, in either technology or management '
    'technique, which by itself promises even one order of magnitude '
    'improvement within a decade in productivity, in reliability, in '
    'simplicity." — Fred Brooks, "No Silver Bullet" (1986)',

    '"The programmer, like the poet, works only slightly removed from pure '
    'thought-stuff." — Fred Brooks, "The Mythical Man-Month"',

    # General ISA wisdom
    '"An instruction set is a contract between hardware and software that '
    'outlasts both." — Anonymous',

    '"The tragedy of Itanium was not that it failed. The tragedy was that '
    'it worked exactly as designed — and the design was wrong." — Anonymous',

    '"Every RISC architecture is a reaction to VAX. Every CISC defence '
    'is a concession to compatibility." — Anonymous',

    '"Delay slots are the assembly programmer\'s way of saying: \'I noticed '
    'you were about to waste a cycle, so I moved my problem forward in '
    'time.\'" — Anonymous',

    '"Endianness is not a religious war. It is an engineering error that '
    'metastasized into a religious war." — Anonymous',

    '"ARM won not by being the fastest or the most powerful, but by being '
    'the most affordable to license. The business model was the innovation." '
    '— Anonymous chip industry observer',

    '"If PowerPC had Apple in its corner for another decade, you would be '
    'reading this on a PowerPC chip right now." — Anonymous',

    '"The condition register file is what PowerPC got right that x86 still '
    'hasn\'t copied." — Anonymous',
]


# ---------------------------------------------------------------------------
# EASTER EGG CONTENT
# ---------------------------------------------------------------------------

KONAMI_UNLOCK_TEXT: str = """\
╔══════════════════════════════════════════════════════════════════╗
║          ★  KONAMI CODE ACCEPTED  ★                              ║
║                                                                  ║
║   You have unlocked the ISA GRAVEYARD.                           ║
║                                                                  ║
║   Here lie the architectures that dared to challenge all:        ║
║                                                                  ║
║   † Alpha AXP     (1992–2004)  "Fastest ever. Gone too soon."   ║
║   † PA-RISC       (1986–2008)  "Precision was its middle name." ║
║   † Itanium       (2001–2021)  "Explicitly parallel in failure."║
║   † MIPS (desktop)(1985–2002)  "Textbook perfect, market lost." ║
║   † VAX           (1977–2000)  "CISC pinnacle. RISC casualty."  ║
║                                                                  ║
║   Still alive (and thriving):                                    ║
║   ♥ ARM / AArch64  (in your pocket, your laptop, the cloud)     ║
║   ♥ PowerPC / POWER (in IBM cloud, game consoles, your car)     ║
║   ♥ RISC-V          (the open challenger, rising fast)           ║
║   ♥ x86-64          (the immortal cockroach of ISAs)             ║
║                                                                  ║
║   "Any sufficiently successful ISA is indistinguishable          ║
║    from a mistake that won." — PPC2ARM Fortune Cookie            ║
╚══════════════════════════════════════════════════════════════════╝
"""

HIDDEN_MESSAGES: dict[str, str] = {

    "title_7clicks": (
        "You clicked the title 7 times.\n\n"
        "Congratulations. You have discovered the ISA Graveyard.\n"
        "A place where retired architectures rest in silicon peace.\n\n"
        "Alpha. PA-RISC. Itanium. They all believed they would win.\n"
        "They were not wrong about performance. They were wrong about timing.\n\n"
        "ARM was right about both."
    ),

    "status_bar_quote": (
        '"The best ISA is the one that ships — and ships a billion units." — Anonymous chipmaker'
    ),

    "about_hidden_zone": (
        "══════════════════════════════════════\n"
        "  HALL OF FAME: ISA LUMINARIES\n"
        "══════════════════════════════════════\n"
        "  Sophie Wilson    — ARM1 ISA designer (Acorn, 1985)\n"
        "  Steve Furber     — ARM1 chip architect (Acorn, 1985)\n"
        "  John Cocke       — RISC pioneer, IBM 801\n"
        "  David Patterson  — Berkeley RISC, SPARC\n"
        "  John Hennessy    — Stanford MIPS\n"
        "  Jim Keller       — Alpha EV6, K8, Apple A4/A5, Tesla FSD\n"
        "  Dave Cutler      — VMS, Windows NT\n"
        "  Fred Brooks      — OS/360, Mythical Man-Month\n"
        "  Krste Asanović   — RISC-V (UC Berkeley)\n"
        "  Bob Colwell      — Intel P6 microarchitect\n"
        "  Eric Traut       — Apple Rosetta (PPC→x86 translation)\n"
        "  Mike Muller      — ARM CTO, first commercial ARM chips\n"
        "══════════════════════════════════════\n"
        '  "An ISA is forever. Choose wisely."\n'
        "══════════════════════════════════════"
    ),

    "compiler_quotes_unlock": (
        "Secret menu unlocked: Show Compiler Quotes.\n"
        "Check the Help menu."
    ),

    "random_instruction_fact": (
        "Did you know? AArch64's NOP instruction is encoded as 0xD503201F. "
        "It is a hint instruction (HINT #0) rather than a separate opcode — "
        "the same encoding space that carries WFE, WFI, SEV, and other "
        "micro-architectural hints."
    ),

    "isa_graveyard_epitaphs": (
        "ALPHA  : 'I computed π to 50 decimal places before your JVM loaded.'\n"
        "ITANIUM: 'The compiler was supposed to do this part.'\n"
        "PA-RISC: 'HP promised Itanium would be better. HP was wrong.'\n"
        "VAX    : 'MATCHC, LOCC, MOVC5 — features ARM still doesn\\'t have.'\n"
        "MIPS   : 'I taught a generation of CS students. Then they all bought ARM.'"
    ),

    "arm_fun_fact": (
        "ARM originally stood for Acorn RISC Machine. After the spin-off in 1990 "
        "it was renamed Advanced RISC Machines. After Arm Holdings went public "
        "in 1998 the letters no longer officially stand for anything — "
        "it is just 'Arm' (lower-case A, per the current brand guidelines)."
    ),
}
