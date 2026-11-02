# Exam Desk

A warm retro study app for Government College of Engineering Aurangabad / Chhatrapati Sambhajinagar, second-year CSE: Operating Systems (CSPCC2003), Data Structure (CSPCC2002), and Mathematics III (CSPCC2001).

## Use it now — no installation or internet

Open `assets/index.html` in Chrome, Edge or another modern browser. Keep the assets folder intact. The separate `Exam-Desk-Offline.html` deliverable is a self-contained version with all scans embedded; it can be copied and opened directly. Bookmark/progress storage belongs to each browser/file location and is not synchronized between copies.

The app includes three subject folders, a second-year CSE course header, exam and paper-year filters, answer search, topic sorting, bookmarks, revision flags, source evidence and local scans. No account or backend is needed. There are no remote fonts, analytics, CDNs or API requests.

## Android build

This is a Flutter Android wrapper around a bundled HTML/CSS/JavaScript application. It is not a fully native Flutter widget implementation. The same local assets are used by the browser and Android versions. JSON is the content source; localStorage stores bookmarks and revision flags. SQLite is unnecessary for this small immutable bank.

Flutter/Dart and the Android SDK were not installed in the authoring environment. No APK was compiled or device-tested. Use current stable Flutter (at least 3.38 / Dart 3.10), Android SDK, JDK and a current Android System WebView. The pinned WebView plugin requires Android API 24 or newer.

From this project directory:

```sh
flutter doctor
python3 bootstrap_android.py
flutter analyze
flutter build apk --debug
```

On Windows use `python` instead of `python3` if needed. The bootstrap script generates the Android shell in a temporary directory, copies only its Android platform folder, sets minimum SDK 24 and the display label, and fetches packages. It preserves the provided application sources. An internet connection is needed for initial Flutter/Gradle/dependency downloads, not for studying after installation.

Debug APK output: `build/app/outputs/flutter-apk/app-debug.apk`.

For a connected Android device:

```sh
flutter devices
flutter run
```

For release distribution, configure your own signing key before `flutter build apk --release`. A generated Flutter template may use debug signing by default; do not treat that as production signing. The app requests no storage permissions and has no runtime network dependency. The default Flutter debug manifest may include Internet permission for development tooling.

Android checks still required: install on a physical device; launch in airplane mode; open every paper and an answer; save/revise a question; force-stop and reopen; verify Android back closes the source viewer, then answer, then exits; test system text scaling and a current WebView. There is a local-load error screen with retry.

## Operating Systems evidence rules

Four uploads contain six actual papers:

| ID | Paper | Date | Marks | Source |
|---|---|---|---|---|
| ct1-u | CT1 main, year unknown | Unverified | 15 | Os ct1.png; cropped header |
| ct1-r25 | 2025 CT1, uploader-identified retest | 13/10/2025 | 15 | Os re ct 1.png |
| ct2-25 | 2025 CT2 | 07/10/2025 | 15 | Os ct 2.png |
| ct1-24 | 2024 CT1 | 04/09/2024 | 15 | PDF page 1 |
| ct2-24 | 2024 CT2 | 24/10/2024 | 15 | PDF page 2 |
| end-24 | 2024 End Semester | December; day disputed | 60 | PDF pages 3–4, ONE paper |

The end-sem stamp appears to read **18 DEC 2024**, while the request describes **8 December**. The exact date is null in the data. The undated CT1 is never assigned to 2025. Retest identity is attributed to the uploader because the printed header only says Class Test I.

There are 34 question records and 34 question-focused answer modules. Original wording is transcribed with whitespace/punctuation cleanup; tables are serialized into labeled values. Scans are authoritative. Combined questions retain their printed total marks, not one allocation per subtopic. All optional questions are included; their marks do not sum to the paper maximum because exams allow choices.

Topic normalization groups related concepts and spelling variants, while preserving distinct prompts and numerical inputs. Topic coverage = number of unique paper IDs containing that topic, across the whole library. It is not an exact-repeat count or probability of appearing in an exam. Each individual prompt has one recorded source occurrence. The app exposes related variants and their individual marks/source references instead of inventing exact repetition statistics.

No official syllabus or marking scheme was uploaded. Answers are curated study material, not college-approved solutions. Coverage is limited to the supplied papers. Numerical assumptions are explicit: handwritten LRU frame count, priority tie rule, ambiguous “SJF primitive”, missing SCAN limits/directions and missing seek-time model.

## Maintain content

Edit `assets/data.json`, then run:

```sh
python3 sync_data.py
python3 tests/verify_data.py
```

`data.js` mirrors JSON so the app also works under local file URLs without fetch permissions. The self-contained HTML is a distribution snapshot; regenerate it after changing assets with `python3 make_standalone.py`. Stable question IDs preserve bookmarks across updates. Adding another course/academic year requires extending the data model and course chooser; this MVP shows its one available course in the header.

## Verification

See `TEST-REPORT.md`. Data/numerical tests use standard Python 3.9+. Browser checks use Playwright and Chrome; install `playwright` with npm, then run `node tests/ui.cjs` from the project directory. Set `CHROME_PATH` if Chrome is installed elsewhere, or install Playwright Chromium. Screenshots are written under `test-results/`.

## Technical references

- [Official Flutter WebView package and API](https://pub.dev/packages/webview_flutter): bundled asset loading, controller and navigation delegate.
- [Android Developers: Data and file storage overview](https://developer.android.com/training/data-storage/): reference for the Android file-system answer. This link is for maintainers; the answer remains bundled offline.

## Simplified interface update

The main screen now prioritizes questions, with exam/year selectors and search. Topic and sort are collapsible. Active filter chips can be removed individually; Clear all filters restores the full list. Study and Saved retain separate filter settings. Search trims surrounding whitespace. Missing papers have an explicit empty-state explanation.

## Pointwise answer update

All answers now use numbered points in simple language, with definitions, examples and worked steps. PCB/IPC, multiprocessing, paging hardware and the combined distributed-OS/spooling question have dedicated answers to avoid unrelated material. Sources and related questions are collapsed below the answer. Marks high-to-low is the default for Study and Saved; filtering and searching preserve this order unless you explicitly choose another sort. Reset also restores marks high-to-low.

## Question-led answer structure

The latest version replaces the flat numbered list with sections matching the requested subquestions. Definitions are separate from functions, features, comparisons and calculations. Worked answers use given-data tables, methods, calculations and final results. Only sequential procedures use numbered steps. Twenty-six bundled SVG diagrams illustrate the concepts and numerical routes, without network requests. Figure captions identify illustrative examples and assumed disk limits. No official subpart mark allocation is invented.

Answers now use a `sections` schema (paragraphs, bullets, ordered steps, code, tables and optional diagram reference). SVG diagrams are stored in the JSON `diagrams` map. Update the plain-text `text` field too when editing content, because search uses it. Run `node tests/answers.cjs` for the current section/diagram reader checks.

## UI refinement (v1.1)

Bundled line icons, hover/press/focus feedback, filter-result transitions and a subtle answer-panel entrance. Saved and revised actions show clear selected states. Search has a clear button that preserves input focus. Answers include a scroll-progress line, back-to-top and Previous/Next within the filtered result sequence. Figures can be expanded in a separate dialog. All effects are local; reduced-motion preferences suppress animations, including the backdrop. Keyboard Escape closes the top dialog and focus returns to the question after closing the answer.

Run `node tests/polish.cjs` to check the new interactions and reduced-motion mode. No Android build was performed in this environment.

## Retro Exam Arcade: Subject-page review

The current UI is the first screen of the requested redesign. See `DESIGN-REVIEW.md` for scope, assumptions, changed files and checks. Content is unchanged. The requested fonts are bundled offline with their licenses; `make_standalone.py` embeds them in the portable HTML. Home and other new screen flows await feedback.


## Data Structure update (v1.2)

Use the Subject selector to switch between Operating Systems (CSPCC2003) and Data Structure (CSPCC2002). OS content and existing bookmark/revision IDs are preserved. DS adds 38 source-question records, 26 shared answer modules and 10 SVG diagrams. It includes all six distinct papers from the four DS uploads. All scans are bundled, including the original PDF.

CT filters use printed academic-year labels (AY 2024–25 / AY 2025–26), not assumed calendar years. The end-sem exam has a verified 16 December 2024 date. CT1 semester IV conflicts with CT2 semester III; the printed labels remain in provenance. Two different AY 2024–25 CT1 sets are variants A/B, without inventing main/retest identities. Wording is normalised for readability; use the included scans to inspect exact print. End-sem source pages are displayed in reading order: original PDF page 3, then page 2.

Each card remains a source-specific question with its own marks. Equivalent prompts share an answer family; appearance badges count distinct papers in that family across the whole subject. Different scopes (strict binary trees, B-tree insertion, DFS applications) retain separate families. Broad topic coverage is separately labelled.

Default ordering remains marks high to low. Changing subject resets filters and scrolls to the top. Bookmarks and progress are displayed per subject and persist with the existing local-storage keys.

Data files: assets/ds-data.json and assets/ds-data.js (window.DS_DATA). When editing JSON, regenerate JS with `python3 sync_data.py`, then run `python3 make_standalone.py`. The Flutter assets list includes assets/papers/ds/. No APK was compiled; Android build instructions above still apply.

Validation: `python3 tests/verify_ds.py`, `python3 tests/verify_data.py`, and `node tests/data-structure.cjs` (install Playwright; set CHROME_PATH if needed). The browser checks cover all year/exam combinations, all 38 DS answer screens, every DS scan, bookmarks/progress, mobile layouts, and no remote requests.


## Home/Desktop (v1.3)

Tap Home or the Exam Desk brand to open the subject folders. Continue returns to the last question opened in the current session; it is not retained after a reload. Revision progress and bookmarks retain their existing device storage. Study remains the initial screen.


## Mathematics III (v1.4)

M3 adds 4 distinct papers and 37 solved source questions. The full library has 109 questions across 16 papers and 3 subjects. CT1/ISE-I and CT2/ISE-II are paired in the exam dropdown; the source keeps its printed exam label. Maths ct1.jpg is correctly classified as ISE-II/CT2 from its 06/10/2025 header. No 2025 M3 CT1 is invented. The mixed PDF’s OS pages are excluded.

An asterisk on M3 end-sem marks identifies equal subpart allocations inferred from 12-mark groups and their choice rules. Printed invalid densities/moments are flagged, and conditional corrections are separated from source facts. Answers include worked tables, calculations, final results, CDF/normal-tail diagrams, and explicit statistical assumptions. No official syllabus or marking scheme is available.

See M3-SOURCES.md for the paper ledger. Data lives in assets/m3-data.json and m3-data.js, with five scan images under assets/papers/m3/. Use sync_data.py and make_standalone.py after editing. Verify with `python3 tests/verify_m3.py`; browser checks are in `node tests/m3.cjs` and expect the standalone HTML beside the project folder. Flutter assets include the new source folder. APK compilation/device testing is still outstanding.

## Chemistry (v1.5)

Added **Electrochemistry, Battery Science and Engineering Materials (CHBSC1001)** as a first-year subject. The library now contains **155 questions across 21 papers and four subjects**. Chemistry contributes 46 source questions, 43 answer modules and 15 labelled diagrams. All optional questions are answered.

The subject selector includes Chemistry; Home now covers Years 1 and 2. Seven original note PDFs appear under Chemistry → Papers, with page-level references below each answer. Supplementary web references are labelled and require internet; answers, diagrams, scans and uploaded notes are offline. `Exam-Desk-Offline.html` beside the project folder is the portable version and contains all note PDFs.

See CHEMISTRY-SOURCES.md for provenance, conditional calculations, inferred marks and corrections to source-note typos. Chemistry files are assets/chem-data.json and chem-data.js. After changes, run sync_data.py and make_standalone.py. Validate with `python3 tests/verify_chem.py` and `node tests/chemistry.cjs` (Playwright and Chrome required). Android compilation/device testing remains outstanding.


## PPS addition
60 solved source questions across five papers, with numbered algorithms, 30 complete C programs, sample outputs and four flowcharts. Select PPS · First year. See PPS-SOURCES.md for provenance and validation.


## IKS addition
36 question records across six papers, including four paired MCQ sets, simple structured answers, examples and three study diagrams. Select IKS · First year. See IKS-SOURCES.md for provenance.
