# Centered multichannel Eliashberg branches: a sqrt(341/250)/(2 pi) moment-norm ceiling

Davis Rens  
SuperMatics Inc.  
[ORCID 0000-0001-5839-5197](https://orcid.org/0000-0001-5839-5197)  
Version 2.0.0

Paper DOI: <https://doi.org/10.5281/zenodo.24410276>  
Replay supplement DOI: <https://doi.org/10.5281/zenodo.24410275>  
Source: <https://github.com/SuperMatics-Inc/centered-multichannel-eliashberg-ceiling>

This repository accompanies the preprint *Centered multichannel Eliashberg branches: a sqrt(341/250)/(2 pi) moment-norm ceiling*, version 2. The manuscript source and bibliography are in `paper/`. The statement-to-source map is `CLAIMS.md`. Version 1 holds the written proof `replay/RIGOR.md`, the two exact covering programs `replay/replay.py` and `replay/independent.py`, the driver `replay/verify.py`, the closure pins `replay/source-pins.json` and the execution transcript `replay/CHECKS.txt`. Version 2 adds the close-out record of the sharper result under `records/aniso-close/`, which holds the proof record `RIGOR.md`, the two exact covering programs `replay.py` and `independent.py`, and the execution transcript `CHECKS.txt` with its mutation receipts and source hashes. `MANIFEST.sha256` pins every file in this repository except the two manifests. `ADMITTED.sha256` records the accepted bytes of the manuscript, the two proof records, the four programs and the two transcripts as shipped here.

## Mathematical scope

The preprint treats a reciprocal multichannel linearised Eliashberg model whose channels carry different bounded, energy-dependent, even densities of states and a common retarded glue, on the centered branch class. It proves that the linear onset temperature obeys the strict bound

    k_B T_lin < C_* sqrt(rho),    C_* = sqrt(341/250)/(2 pi),  which rounds to 0.1858777115,

where `rho` is the norm of the glue moment matrix, together with the supremum statement

    S_cent <= C_3 = sqrt(6811/5000)/(2 pi),  which rounds to 0.1857550244,

for the supremum `S_cent` of `k_B T_lin / sqrt(rho)` over the whole centered class. The first is a bound on a supremum and is not strict; the second is the strict statement one would quote, and the exact slack at the reported temperature is the rational `9/6820`. Both numbers lie between the exact scalar constant `C_inf = 0.18272624777232952` and the constants `sqrt(683/500)/(2 pi)` and `sqrt(41/30)/(2 pi)` of the preceding preprints in this series, and both are certified by exact rational arithmetic. The finite part of the argument is a continuum reserve `d_3 = 3189/10000`, raised from the `159/500` of version 1, and the two-stage cascade with the head criterion evaluated at every pairwise crossing of the envelope lines.

Three limits bind the claim.

1. `T_lin` is a linear model onset temperature, derived from the folded stability form with the pairing kernel tested against a fixed positive normal branch. It is not an exact transition temperature, it is not a measurement, and nothing here is a prediction about a material or a claim that any substance is superconducting.
2. Whether the supremum `S_cent` equals `C_inf` or lies strictly above it is open. The paper proves `C_inf <= S_cent <= C_3` and decides neither direction. Nor does it decide whether `S_cent` equals `C_3`.
3. The floor `0.185411` is a limit of the edge-reserve method for frozen weight sequences, not a lower bound on `S_cent`. The constant proved here sits above it, consistent with that obstruction.

The finite part of the argument is a rational covering of a compact rectangle in two variables by closed rectangles, carried out twice by independent programs. The analytic statements, namely the Poisson envelope, the Harnack inputs, the width cone, the sector algebra, the exterior estimates and the reduction to the edge inequality, are proved in `records/aniso-close/RIGOR.md` and in `replay/RIGOR.md`, and are not machine-checked.

## Contents

| Path | Contents |
|---|---|
| `paper/main.tex` | Manuscript source, 14 pages, with both DOI macros filled in. |
| `paper/refs.bib` | The four cited records, each by DOI. |
| `paper/main.pdf` | The built manuscript, byte-identical to the deposited PDF. |
| `CLAIMS.md` | Claim by claim map to the proof records and to the checker lines. |
| `records/aniso-close/RIGOR.md` | The written proof record of the version 2 result: the three-stage reserve, the exterior regions, the edge inequality and the open coupled question. |
| `records/aniso-close/replay.py` | Primary cover: symmetric cover, 367 leaves, maximum depth 24, area 1, 43 head intervals. |
| `records/aniso-close/independent.py` | Independent cover: full-domain quadtree cover, 1036 leaves, maximum depth 13, area 4/3, 43 head intervals. |
| `records/aniso-close/CHECKS.txt` | Execution transcript of the twenty-two checker runs, with exit codes, wall times, mutation outcomes, endpoint enclosures, reserve search receipts and source hashes. |
| `replay/RIGOR.md` | The version 1 written proof of the reserve argument, its infinite-tail reduction and its conversion to an onset bound. |
| `replay/replay.py` | Version 1 primary cover: `[1, 3] x [0, 1/2]` plus channel-exchange symmetry, 159 leaves, maximum depth 20, area 1, 43 head intervals. |
| `replay/independent.py` | Version 1 independent cover: `[1/3, 3] x [0, 1/2]` without symmetry reduction, 466 leaves, maximum depth 11, area 4/3, 43 head intervals. |
| `replay/verify.py` | Version 1 driver: both covers in base mode and twelve guarded mutants, each of which must exit 1 and print `REJECT`. |
| `replay/source-pins.json` | Thirteen SHA-256 pins of the inherited proofs and arithmetic. |
| `replay/CHECKS.txt` | Execution transcript of `verify.py`, with commands written in repository-relative form. |

The thirteen pinned inherited sources are included unmodified under `inherited/`, one file per pin, keyed by the last path segment of the pin name, so the pin check runs on the shipped bytes alone. The pin keys keep the relative names of the working records they came from, as reviewed, and the programs use `inherited/<pin key suffix>` when the key does not resolve next to them. The pinned names are record labels of earlier working records, `inherited/RIGOR.md` is the parent proof of `replay/RIGOR.md`, and no pin names a file outside this repository. A few of these inherited texts use em dashes in their own prose and quote working locations; they are byte-for-byte the reviewed pins, they are hashed by the checkers, and they were not edited.

The record labels used inside the two proof records and the two transcripts are the names of the working records the material came from; they are not paths in this repository. Working locations quoted in the transcripts, the transcription runner sources and one process sentence of `records/aniso-close/RIGOR.md` are rewritten in repository-relative form, in the form `<tmp>`, or as `python`; no command, exit code, number or piece of prose logic was changed.

## What version 2 adds

Version 2 supersedes version 1 and leaves both of its statements intact as weaker bounds. It is a new version of the same preprint, with the same model class, the same method and the same labels.

- The reserve rises from `159/500` to `d_3 = 3189/10000`, so the supremum bound moves from `sqrt(341/250)/(2 pi)` to `C_3 = sqrt(6811/5000)/(2 pi)`, a reduction of `0.066%`.
- The version 1 strict constant `sqrt(6821/5000)/(2 pi)` is replaced by the strict bound at `sqrt(341/250)/(2 pi)`, which version 1 held only as the supremum constant, with the exact bare gap `9/6820`.
- The cascade gains a second completion stage, the head criterion is evaluated at all pairwise crossings of the envelope lines, and the head intervals are verified to cover the head weight exactly once.
- The two coverings grow from 159 and 466 leaves to 367 and 1036 leaves. Both programs are re-run from scratch at `d = 3189/10000`, with ten guarded mutants each, and all twenty exit 1 at a documented mathematical guard.
- The manuscript grows from 12 to 14 pages.
- The next grid point `d = 3190/10000` remains unresolved, neither rejected nor excluded; the paper draws no conclusion from it.
- Review records removed from the tree; available in version 1 history. This repository ships the manuscript, the proof records, the programs and the transcripts only, so the version 2 tree carries no review-cycle file.
- `CITATION.cff` records version 2.0.0 and the two version 2 DOIs.

The version 1 constants remain quoted in the paper as the weaker bounds they are. Nothing in version 2 upgrades a label: `C_3` and `C_*` bound the model onset temperature `T_lin` only, and no statement here concerns a measured transition temperature.

## Replay

The programs use only the Python standard library, with no interval package, no compiled extension and no network access. From the repository root:

```sh
python --version          # Python 3.12 or newer
(cd replay && python -B verify.py)
python -B records/aniso-close/replay.py
python -B records/aniso-close/independent.py
sha256sum -c MANIFEST.sha256
sha256sum -c ADMITTED.sha256
```

The two version 2 programs take no required argument. The primary cover exits 0 after about three minutes and prints `EXACT primary three-stage cover: d=3189/10000; leaves=367; depth=24; area=1; heads=43`; the independent cover exits 0 after about seven minutes and prints `EXACT independent three-stage cover: d=3189/10000; leaves=1036; depth=13; area=4/3; heads=43`. Both print `C_bound = sqrt(6811/5000)/(2*pi)` and `C_report = sqrt(341/250)/(2*pi)`. Each program also accepts `--mutant NAME` for the ten documented deliberate corruptions, `--reserve P/Q` for a different reserve, and the driver that ran the twenty-two commands and compared every observed exit with its expectation is reproduced in `records/aniso-close/CHECKS.txt` together with its output. Every mutated run must exit 1 and print a line beginning `REJECT` at its mathematical guard; an exception, a timeout or an argument error does not count as a rejection.

Version 1 base mode prints the exact decimal enclosures of its two constants, then `CERTIFIED primary centered cover: reserve=159/500; leaves=159; max_depth=20; area=1; head_intervals=43` and `CERTIFIED independent centered cover: reserve=159/500; leaves=466; max_depth=11; area=4/3; head_intervals=43`. Its twelve mutated runs cover a wrong pin hash, a wrong strict reserve ratio, a covering domain shrunk from `r <= 3` to `r <= 2`, a reserve raised past feasibility, an altered infinite-tail cost, a too-steep tangent slope, a corrupted Stage-0 completion sign, a tangent intercept with the wrong sign, and the corresponding cases of the second program.

CI (`.github/workflows/ci.yml`) verifies both manifests, runs the version 1 driver on Python 3.12, runs both version 2 programs and their twenty guarded mutants and compares every exit code with `records/aniso-close/CHECKS.txt`, applies the public prose safeguards to the manuscript, this README, `CLAIMS.md`, the citation file and both transcripts, and builds the manuscript with Tectonic 0.17.0 at `SOURCE_DATE_EPOCH=1795132800`, failing on any overfull box, undefined reference or undefined citation, on a missing DOI, on an em dash and on any internal working location.

## Disclosure and review

AI agents generated the proofs, code, and manuscript drafts under D. Rens' direction. Separate AI agents performed the independent reviews. This preprint has not been peer reviewed.

## Rights

The manuscript text and bibliography in `paper/` are distributed under CC-BY-4.0 through the paper record. The proof, replay code, pins and transcripts in this repository are distributed under Apache-2.0. The paper's license does not change the software license.
