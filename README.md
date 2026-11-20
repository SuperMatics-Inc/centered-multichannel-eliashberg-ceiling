# Centered multichannel Eliashberg branches: a sqrt(341/250)/(2 pi) moment-norm ceiling

Davis Rens  
SuperMatics Inc.  
[ORCID 0000-0001-5839-5197](https://orcid.org/0000-0001-5839-5197)  
Version 1.0.0

Paper DOI: <https://doi.org/10.5281/zenodo.24407691>  
Replay supplement DOI: <https://doi.org/10.5281/zenodo.24407693>  
Source: <https://github.com/SuperMatics-Inc/centered-multichannel-eliashberg-ceiling>

This repository accompanies the preprint *Centered multichannel Eliashberg branches: a sqrt(341/250)/(2 pi) moment-norm ceiling*. The manuscript source and bibliography are in `paper/`. The statement-to-source map is `CLAIMS.md`. The written proof is `replay/RIGOR.md`, the two exact covering programs are `replay/replay.py` and `replay/independent.py`, the driver is `replay/verify.py`, the closure pins are `replay/source-pins.json`, and the execution transcript is `replay/CHECKS.txt`. The independent reviews are in `reviews/`. `MANIFEST.sha256` pins every file in this repository except the two manifests. `ADMITTED.sha256` records the accepted bytes of the manuscript, the proof, the programs and the reviews as shipped here.

## Mathematical scope

The preprint treats a reciprocal multichannel linearised Eliashberg model whose channels carry different bounded, energy-dependent, even densities of states and a common retarded glue, on the centered branch class. It proves that the linear onset temperature obeys

    k_B T_lin < C_rep sqrt(rho),    C_rep = sqrt(6821/5000)/(2 pi),  which rounds to 0.1858913384,

where `rho` is the norm of the glue moment matrix, together with the supremum statement

    S_cent <= C_* = sqrt(341/250)/(2 pi),  which rounds to 0.1858777115,

for the supremum `S_cent` of `k_B T_lin / sqrt(rho)` over the whole centered class. Both constants lie between the exact scalar constant `C_inf = 0.18272624777232952` and the constants `sqrt(683/500)/(2 pi)` and `sqrt(41/30)/(2 pi)` of the preceding preprint in this series, and both are certified by exact rational arithmetic.

Three limits bind the claim.

1. `T_lin` is a linear model onset temperature, derived from the folded stability form with the pairing kernel tested against a fixed positive normal branch. It is not an exact transition temperature, it is not a measurement, and nothing here is a prediction about a material or a claim that any substance is superconducting.
2. Whether the supremum `S_cent` equals `C_inf` or lies strictly above it is open. The paper bounds `C_inf <= S_cent <= C_*` and decides neither direction.
3. The floor `0.185411` is a limit of the edge-reserve method for frozen weight sequences, not a lower bound on `S_cent`. The constant proved here sits above it, consistent with that obstruction.

The finite part of the argument is a rational covering of a compact rectangle in two variables by closed rectangles, carried out twice by independent programs. The analytic statements, namely the Poisson envelope, the Harnack inputs, the sector algebra, the exterior estimates and the reduction to the edge inequality, are proved in `replay/RIGOR.md` and are not machine-checked.

## Contents

| Path | Contents |
|---|---|
| `paper/main.tex` | Manuscript source, 12 pages, with both DOI macros filled in. |
| `paper/refs.bib` | The four cited records, each by DOI. |
| `paper/main.pdf` | The built manuscript, byte-identical to the deposited PDF. |
| `CLAIMS.md` | Claim by claim map to `replay/RIGOR.md` and to checker lines. |
| `replay/RIGOR.md` | The written proof of the reserve argument, its infinite-tail reduction and its conversion to an onset bound. |
| `replay/replay.py` | Primary cover: `[1, 3] x [0, 1/2]` plus channel-exchange symmetry, 159 leaves, maximum depth 20, area 1, 43 head intervals. |
| `replay/independent.py` | Independent cover: `[1/3, 3] x [0, 1/2]` without symmetry reduction, 466 leaves, maximum depth 11, area 4/3, 43 head intervals. |
| `replay/verify.py` | Driver: both covers in base mode and twelve guarded mutants, each of which must exit 1 and print `REJECT`. |
| `replay/source-pins.json` | Thirteen SHA-256 pins of the inherited proofs and arithmetic. |
| `replay/CHECKS.txt` | Execution transcript of `verify.py`, with commands written in repository-relative form. |
| `reviews/PROOF-REVIEW.md` | Independent review of the proof and of the coverings, verdict ACCEPT. |
| `reviews/MANUSCRIPT-REVIEW.md` | Independent review of the manuscript, verdict ACCEPT-WITH-FIXES. |
| `reviews/MANUSCRIPT-REVIEW2.md` | Delta review after the fixes, verdict PASS. |

The thirteen pinned inherited sources are included unmodified under `inherited/`, one file per pin, keyed by the last path segment of the pin name, so the pin check runs on the shipped bytes alone. The pin keys keep the relative names of the working records they came from, as reviewed, and the programs use `inherited/<pin key suffix>` when the key does not resolve next to them. The pinned names are record labels of earlier working records, `inherited/RIGOR.md` is the parent proof of this one, and no pin names a file outside this repository. A few of these inherited texts use em dashes in their own prose; they are byte-for-byte the reviewed pins and were not edited.

The record labels used inside `replay/RIGOR.md`, `replay/source-pins.json` and the reviews are the names of the working records the material came from; they are not paths in this repository. Absolute build directories quoted in the reviews were rewritten to `<build>` or to repository-relative forms, and no other text of those records was changed.

## Replay

The programs use only the Python standard library, with no interval package, no compiled extension and no network access. From the repository root:

```sh
python --version          # Python 3.12 or newer
(cd replay && python -B verify.py)
sha256sum -c MANIFEST.sha256
sha256sum -c ADMITTED.sha256
```

Base mode prints the exact decimal enclosures of the two constants, then `CERTIFIED primary centered cover: reserve=159/500; leaves=159; max_depth=20; area=1; head_intervals=43` and `CERTIFIED independent centered cover: reserve=159/500; leaves=466; max_depth=11; area=4/3; head_intervals=43`. The twelve mutated runs cover a wrong pin hash, a wrong strict reserve ratio, a covering domain shrunk from `r <= 3` to `r <= 2`, a reserve raised past feasibility, an altered infinite-tail cost, a too-steep tangent slope, a corrupted Stage-0 completion sign, a tangent intercept with the wrong sign, and the corresponding cases of the second program. Each must exit 1 with a `REJECT` line rather than crash for a missing dependency, and the driver compares the observed statuses. The whole run takes about two and a half minutes.

CI (`.github/workflows/ci.yml`) verifies both manifests, runs the driver on Python 3.12, applies the public prose safeguards to the manuscript and this README, and builds the manuscript with Tectonic 0.17.0 at `SOURCE_DATE_EPOCH=1795132800`, failing on any overfull box, undefined reference or undefined citation, on a missing DOI, on an em dash and on any internal working name.

## Disclosure and review

AI agents generated the proofs, code, and manuscript drafts under D. Rens' direction. Separate AI agents performed the independent reviews. This preprint has not been peer reviewed.

## Rights

The manuscript text and bibliography in `paper/` are distributed under CC-BY-4.0 through the paper record. The proof, replay code, pins, transcript and other software materials in this repository are distributed under Apache-2.0. The paper's license does not change the software license.
