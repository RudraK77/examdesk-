# Retro Exam Arcade — Subject screen review

Stage 1 is ready for feedback. Home/onboarding and other new screens have not been built; the existing navigation remains intact. Shared visual tokens also style the existing answer and source windows so the Subject page works end to end.

## Applied

- Indigo desktop, faint background-only scanlines, cream windows, teal title bar, pink answer bar and yellow marks.
- Hard borders and offset shadows, raised/pressed buttons, no rounded corners or gradients.
- Offline Press Start 2P for short UI labels; IBM Plex Mono for readable questions and answers. Font licenses are bundled.
- Question cards with verified marks, exam type, year and one recorded source. Star bookmarks retain existing behavior.
- Segmented revision bar derives only from the existing revised-question set.
- Desktop taskbar and mobile bottom navigation use the existing Study, Saved, Papers and About views.
- Working window minimize/restore, Calm mode, answer font-size control and stepped motion under 300ms. Existing reduced-motion support remains.

## Assumptions and preserved behavior

The request is a presentation redesign. The original six-paper bank and all 34 questions, answers, diagrams and provenance remain byte-for-byte unchanged. Existing marks-high-to-low sorting, filters, bookmark/revision storage and navigation logic remain in place. No difficulty scores, exact-repeat frequency, priority predictions, XP, streaks or exam countdown were fabricated. The existing answer view remains the interaction target for question cards. Home and additional screen flows await your feedback on this stage.

## Files touched

- assets/theme.css: new centralized design tokens and offline fonts.
- assets/style.css: replaced accumulated styles with the shared retro component styles.
- assets/components.js: presentation-only QuestionCard and RetroProgress.
- assets/index.html: window frame, subject heading and UI controls.
- assets/app.js: component rendering, icons, motion and presentation controls; existing content/filter algorithms retained.
- assets/fonts/: requested fonts plus SIL Open Font License files.
- make_standalone.py: embeds theme, components and fonts in the single-file offline app.
- pubspec.yaml: includes bundled font assets.

## Verification

Content checksums match the pre-redesign copies. Offline checks passed for font loading, all 34 cards, marks order, exam/year filters, search, minimize/restore via title bar and taskbar, answers, revised progress, saved-state persistence, Calm mode, font size, diagram windows and reduced motion. No remote requests or JavaScript errors. All 34 answer screens passed phone-overflow checks. Desktop/390px screenshots visually reviewed; 320px layout checked. Flutter/APK compilation remains unavailable here.


## Stage 2: Home/Desktop

Added Home to the taskbar and made the brand open it. Existing Study remains the initial screen. Two subject folders open the existing OS/DS question banks. Overall and per-subject progress use actual revised flags; the Continue shortcut uses the last question opened in this session and is absent before one is opened. No countdown, XP or streak is inferred.

Changed presentation files: assets/app.js, assets/index.html and assets/style.css. No question data, answer content or persistent storage schema changed. Shared RetroProgress renders the progress displays. Version labels were updated.

Verified both folders, real progress, resume across subjects, retained Study filters when returning via the Study tab, 44px targets, 320–1440px layouts, offline operation and no JavaScript errors. The next screen remains pending review, following the requested one-screen-at-a-time process.
