# Verification report

Verified on 22 October 2026 using headless Google Chrome and Python 3.9 on macOS.

## Passed

- All 34 question records reference one of six valid paper IDs, with valid answer modules and scans.
- Source marks are 5 for CT questions and 6 for end-sem questions; unknown CT1 year/date remain null.
- The end-sem two-page source is one paper; disputed exact date remains null.
- JSON and JavaScript content bundles match exactly.
- Independent numerical simulations verify priority TAT 8.2 / WT 5.2, LRU 11 faults, SSTF 236 cylinders, paging physical address 10, FCFS TAT 9.8, nonpreemptive SJF TAT 8.0 and SRTF TAT 7.0.
- Browser launched with networking disabled from a local file URL.
- All 34 questions loaded; 2025 filters return eight questions; 2025 CT1 returns four retest questions; unknown-year CT1 returns four questions.
- Search finds LRU; answer opens with its worked result.
- Bookmark and revision flags survive page reload; saved-only view works.
- Source disclosure and viewer work; all seven scanned page images load.
- Empty search and reset filters work.
- JavaScript back handler closes the reader.
- Desktop, 390px and 320px layouts checked; no document-level horizontal overflow. Main and answer screens visually inspected.
- No JavaScript runtime errors in the tested flows.
- Self-contained HTML separately launches offline, shows all questions and renders both embedded end-sem scans with zero HTTP requests.

## Not verified here

Flutter compilation, Android installation, WebView persistence across force-stop, Android system back integration, OS text scaling and physical-device performance. Flutter/Dart and Android build tooling were unavailable. The wrapper is supplied as source with a bootstrap script, not as a claimed working APK.

No official academic review or syllabus-completeness verification has occurred. Scan ambiguities and numerical assumptions are documented in the app and README.

## Simplified UI regression checks

Passed 12 exam/year combinations, topic intersections, All options, individual filter removal, clear-all restoration to 34 questions, whitespace-tolerant search, separate Saved/Study filters, reader return and 320px/390px layouts. Tests ran offline with zero JavaScript errors. Data and independent numerical tests passed again.

## Pointwise answers and marks sorting

Passed: all 34 question readers render numbered points, source/related sections start collapsed, paging hardware excludes the unrelated CT2 numerical, and no reader overflow occurs at phone width. Marks descend on initial load, year/exam/topic combinations, search and reset. Checked 320px/390px layouts and visually reviewed home/answer screenshots. All checks ran offline with zero JavaScript errors. Independent numerical/data checks passed again.

## Question-led sections and diagrams

All 34 readers passed section rendering checks; the former flat answer list is absent. All diagram references and table row widths validated. Twenty-six SVGs are bundled locally. Visually reviewed phone screenshots for a definition/functions answer, priority Gantt chart, process states and directory structure. No page/reader horizontal overflow; wide diagrams and tables scroll inside their own containers. Marks sorting, filters and reset passed again with networking disabled and zero JavaScript errors. Independent numerical/data tests still pass.

## v1.1 UI interactions

Passed offline checks for bundled icons, clear-search focus, persistent saved state, Previous/Next restricted to filtered results, diagram expansion and Escape, scroll-progress/back-to-top, revision state, focus restoration, 320px layout and reduced-motion mode. Fixed backdrop animation under reduced motion and expand-icon overflow. Rechecked all 34 answers for section rendering and phone overflow, plus default marks sorting, filter/search/reset behavior. Visually inspected answer and diagram screens. No JavaScript errors. Android device behavior remains unverified.

## Retro Exam Arcade — Subject page

Content JSON/JS hashes match pre-redesign. Offline tests passed for fonts, cards/marks ordering, filters/search, minimize/title/taskbar restore, answers, revision progress and saved persistence, Calm mode, font-size control, diagrams, reduced motion and 320px layout. All 34 answer readers checked for overflow and section retention. No remote requests or JS errors. See DESIGN-REVIEW.md.


## v1.2 Data Structure

Passed: all 16 DS year/exam filter combinations; trimmed search with combined filters; highest marks first (13 six-mark prompts followed by 25 five-mark prompts); all 38 reader screens; four expression trees; all seven scan images across six papers; subject-specific bookmarks and revision progress with persistence; layout widths 320, 390, 768 and 1440; no remote requests or JavaScript errors under offline browser mode.

The OS UI regression and independent dataset checks passed. OS data.json/data.js SHA-256 checksums are unchanged. DS references, marks, dates, repeat families and worked traversal/B-tree examples passed independent checks. The rational ADT C program compiled with warnings treated as errors and produced 5/6, 1/6 and equality=true. The circular-stack C function passed empty/single/multiple-node invariant checks. Mobile Subject, Answer and expanded-expression views were visually inspected.

Validation is in desktop Chrome with mobile viewport emulation. No physical Android device or compiled APK was tested.

The final packaged-project run also passed after adding navigation scroll reset and bottom scroll clearance so paper buttons remain reachable above the navigation bar.


## v1.4 Mathematics III

Passed all 37 M3 answer screens, all 12 year/exam combinations, highest-marks-first ordering, 19 inferred-mark badges, ISE-II search, all five scan images, three-subject navigation, bookmark/revision persistence, 320–1440px layouts, and offline operation with no remote requests or JavaScript errors. Long equations wrap within phone readers. Mobile subject and normal-tail answer screenshots were visually inspected.

Independent arithmetic checks cover invalid density masses, moment inequalities, regression residuals, binomial fit and chi-square statistic, Poisson and normal tails, family counts and source/marks provenance. Existing OS checksum and DS data checks pass. Source corrections are conditional, never silent. No physical Android/APK validation was performed.

## Chemistry v1.5 verification — 28 October 2026

- All 46 chemistry source records present: 5 + 5 + 15 + 6 + 15 across the five supplied papers.
- Chemistry data validator passed: references, question IDs, marks/inference flags, all scan and note files, JSON/JS agreement, independent calorimeter/atom-economy/emf results, and Ni-Cd / alkaline fuel-cell half-reaction balances.
- Existing OS, DS and M3 Python validators passed. Their source JSON files are byte-identical to the supplied project.
- Headless Chrome checks passed on both the folder HTML and portable standalone: all 46 answers, 15 expandable diagrams, 16 exam/year combinations, search, seven paper-scan images, seven note controls, subject switching, saved/revised state, and 320/390/768/1440-pixel layouts. No application page errors or remote HTTP requests were observed in these flows.
- Original note PDFs embedded in the standalone were decoded and compared byte-for-byte: all seven match. Folder PDFs exist. Browser checks verify iframe/link creation; PDF display depends on the host browser's PDF support, with save/open alternatives provided.
- All 15 SVG diagrams were rendered for visual inspection; CVD/solar/bomb labels were adjusted and re-rendered. Mobile answer and desktop overview screenshots were inspected.
- The initial persistence assertion toggled an already-saved bookmark off because local-file storage was shared between the two builds. The test now explicitly sets the saved/revised states before checking persistence; the application required no change for this.
- Android build and physical-device checks were not performed.


## Chemistry answer-opening fix

The reference renderer now handles answer modules without reference lists and skips empty reference groups. It also handles missing note records without stopping the answer reader.

Browser verification: clicked all 46 Chemistry questions in both assets/index.html and Exam-Desk-Offline.html at a 390 × 844 viewport. Each answer dialog opened with answer sections; no JavaScript page errors occurred.
