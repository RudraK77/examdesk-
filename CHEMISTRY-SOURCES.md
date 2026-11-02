# Chemistry source and answer ledger

CHBSC1001 — Electrochemistry, Battery Science and Engineering Materials, first year.

## Paper coverage

| Paper | Collection / PDF pages | Questions | Marks |
|---|---|---:|---:|
| ISE-I, October 2023 | FY question papers 2K23.pdf, p. 7 | 5 | 15 |
| ISE-II, November 2023 | Same, p. 8 | 5 | 15 |
| End semester, 20 December 2023 | Same, pp. 9–10 | 15 | 60 |
| ISE-I, October 2024 | FY pyq 2K24.pdf, p. 16 | 6 | 15 |
| End semester, 5 January 2025 | Same, pp. 17–18 | 15 | 60 |

All optional questions are included. Combined prompts retain their total marks. The nine subparts on the 2023 end-semester second page have inferred 6-mark allocations: the marks column is cropped, but the matching groups allow any two and the paper totals 60. These entries carry an asterisk. No missing 2024 chemistry ISE-II is invented. Dates use printed headers/stamps, not collection names.

46 source-specific records use 43 answer modules. Answers are study material, not an official marking scheme. Scans preserve the source print; normalized wording is identified in the app.

## Uploaded references

All seven original PDFs are preserved in assets/notes/chem and embedded in the standalone HTML. Each answer lists its relevant PDF pages; a background-only citation is labelled as such. The Papers view includes the full note shelf.

- Electrochemistry.pdf — 9 pages: galvanic cells, potentials, series, Nernst equation and battery background.
- Fuel technology.pdf — 16 pages: fuel classes and calorimetry; pp. 13–15 are the main numerical references.
- Advance Engineering Materials.pdf — 43 scanned pages: conducting polymers and doping (9–17), biodegradation/PLA (18–29), liquid crystals (29–42).
- polymer classification.pdf — 23 pages: supplementary polymer classifications.
- green chemistry.pdf — 38 pages: principles (1–12), atom economy (18–20), solvents (21–24). Some later pages are blank.
- Nano chemistry notes.pdf — 7 scanned pages: nanotubes (1), fullerene figure (5), properties (6), dimensional descriptions (7).
- Nano notes.pdf — 3 scanned pages: size effects and top-down/bottom-up methods.

Supplementary primary references are attached directly to relevant answer modules for Li-ion/Ni-Cd batteries, fuel cells, solar cells, flame photometry, microwave/ultrasound synthesis, CVD and PLA synthesis. Explanatory expansions are distinguished from content explicitly present in the uploaded notes.

## Science and source corrections

- Electrochemistry p. 1 labels zinc oxidation as cathode; answers correctly use anode. Reduction/oxidation potential sign conventions are stated consistently.
- Fuel cells convert energy electrochemically; they are not described as ordinary combustion devices.
- October 2023 Q1(C): literal latent heat is 587 kJ/kg; the alternative 587 cal/g convention is shown separately.
- December 2023 Q3(a): literal latent heat is 580 cal/kg; conditional 580 cal/g interpretation is separate.
- December 2023 Q1(c): the prompt alternates between gaseous fuel and coal; mass-based data are retained.
- October 2024 Q1(A): Fe³⁺ equation is unbalanced and its supplied potential conflicts with the usual Fe²⁺ value. Formal supplied-data result is labelled; copper/iron emf uses printed oxidation potentials.
- January 2025 Q4(C): the Cu²⁺ concentration is unspecified, so the standard calculation and the general Nernst expression are both given.
- January 2025 Q5(C): desired products are unspecified. H₂ and Fe are the main assumptions; whole-syngas atom economy is also shown.
- Notes mix small-molecule liquid crystals with LCPs; answers distinguish them. Some handwritten thermotropic/lyotropic descriptions are reversed; answers use temperature-controlled and solvent/concentration-controlled definitions respectively.
- Biomedical fullerene suggestions are presented as research, without repeating unsupported claims of universal nontoxicity or cures.

## Diagrams

15 scalable, labelled diagrams. Bomb calorimeter, Daniell cell, liquid-crystal phases, polyacetylene, PLA and carbon structures follow reviewed note figures/descriptions. Additional cell/instrument schematics are labelled supplementary. C60 uses an actual 60-vertex, 90-edge truncated-icosahedron graph. Expand controls and horizontal scrolling preserve legibility on phones. Diagram captions identify their basis.

## Maintenance

Edit assets/chem-data.json; keep section text and search text consistent. Run sync_data.py then make_standalone.py. The standalone embeds notes as PDF bytes and opens them through local Blob URLs; there is also a save option if a browser lacks a PDF viewer. Original subjects retain their question IDs and content. A separate file location has separate browser storage.

Run tests/verify_chem.py and tests/chemistry.cjs from the project root, plus existing data validators. Browser tests require Playwright and Chrome. Android includes the new asset directories but has not been compiled or device-tested.
