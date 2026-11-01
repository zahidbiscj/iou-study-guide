# ISGS 101 — Islamic Studies 1: Reorganization Plan

**Status: PLAN v2 (updated with your decisions) — nothing is built yet. Waiting for your "go" to start the Module 1 pilot.**

**Your decisions (locked in):** (1) 5 quiz questions **per module**; (2) **yes** — a printable `.md` study note for every module; (3) **same course** — everything lives inside the existing ISGS 101 section of the site (no separate site/subject).

Goal: turn the ISGS 101 slides + PDFs into a complete, teacher-style, **English + Bangla** course that gets you ready for the midterm — every slide covered, every hard idea explained with an example, every module ending in a quiz.

---

## 1. What I found in `slides/Islamic Studies 1 (ISGS 101)/`

18 PDFs. Text can be extracted directly (no OCR needed), but quality varies.

| File | Pages | What it is |
|---|---|---|
| `Islamic(mod01)` … `Islamic(mod15)` | **292 slides total** | Lecture slides, Dr. Sana Khan, "Islamic Aqeedah" |
| `ISGS 101 Midterm Study questions.pdf` | 3 | The **40 official midterm study questions** |
| `ISGS 101 Midterm Revision Session Spring 2025.pdf` | 24 | Teacher's revision slides (summary of what she stresses) |
| `BIBS 101 Syllabus (1).pdf` | 13 | **Wrong folder** — this is BIBS, not ISGS. I will use it only to double-check the BIBS 101 course already on the site. |

### Module map (from the slide titles)

| Mod | Slides | Topic (as far as titles show) |
|---|---|---|
| 01 | 10 | Definition of Aqeedah, introduction |
| 02 | 22 | Conditions of *Laa ilaaha illallaah* (Hafiz al-Hukmi's poem) |
| 03 | 22 | Same topic continued (opens identically to mod02 — overlap to merge) |
| 04 | 17 | Tawheed al-Asma wa Sifat (Names & Attributes) |
| 05 | 33 | Worship (*'Ibaadah*) — love, trust, fear, etc. |
| 06 | 29 | Belief in the Angels |
| 07 | 4 | Angels continued (short tail of mod06) |
| 08 | 13 | Belief in the Books |
| 09 | 23 | Belief in the Messengers |
| 10 | 11 | Messengers continued |
| 11 | 6 | Belief in the Last Day / Resurrection |
| 12 | 9 | Belief in Qadar (Divine Decree) |
| 13 | 32 | Categories of Shirk |
| 14 | 32 | Categories of Shirk continued (greater vs lesser) |
| 15 | 29 | Fortune-tellers, soothsayers, magic and related topics |

(Titles are what I could read from the first slides; the full list will be confirmed during extraction.)

### Problems I must handle (honest list)

1. **Many slides are only an outline.** Example: mod07 is 4 slides and ~530 characters in total — just bullet headings ("They do not eat or drink"). The slide says *what* but not *why*. A student cannot learn from that alone.
2. **~60+ slides are nearly empty** (title slide, "a 5", a picture only). Mod06 looks especially odd (many "empty" slides — probably diagrams/pictures or unusual text encoding). I will render those pages as images and read them visually.
3. **Arabic text comes out garbled** in plain extraction (reversed letters, missing vowels). I will not trust the raw extraction for Arabic. I will rebuild Arabic phrases/ayat/hadith carefully and show them with transliteration + meaning.
4. **The slides contain typos** ("Adeedah", "Jammah", etc.). I will keep the slide wording as-is in the "slide text" box and use the correct spelling in my own explanation.
5. **Mod02/mod03 overlap** and **mod06/mod07, mod09/mod10, mod13/mod14 are continuations** — I will keep one slide-by-slide record per file but teach them as one flowing topic.
6. **No OCR tool is installed.** For image-only slides I will view the rendered page and transcribe it myself. This is slower but accurate.

---

## 2. What the finished product looks like (what you get)

### 2.1 The menu you will see

Inside **Islamic Studies 1 (ISGS 101)** the menu becomes:

- **Modules** → a list/grid of buttons: **Module 1, Module 2, … Module 15** (each with its topic name, e.g. "Module 6 — Belief in the Angels"). **Click Module 1 → only Module 1 opens**, step by step, with Back/Next, a progress bar, and "resume where I stopped".
- **Midterm Q&A (40 questions)** — rebuilt answers linked to modules.
- **Teacher's Revision Session**
- **Mock Midterm**
- **Glossary & cheat sheet**
- **Assignment** (existing wizard, unchanged)

The side menu also lists Module 1…15 so you can jump directly (`#isgs-mod-01` … `#isgs-mod-15`). The default page when you open ISGS stays **Midterm Q&A** as before (one click on "Modules" to start learning; tell me if you want Modules as the default instead).

### 2.2 The order of teaching INSIDE every module (teacher → student)

Every module is taught in this exact order, so you understand first, then read the slides:

| Part | Name | What it contains |
|---|---|---|
| **A** | **Big picture (teacher to student)** | Before any slide: "What is this module about? Why does it matter? How does it connect to the previous module?" Plain language, simple analogies, English then Bangla. Includes a **"3-minute version"** — the whole module in 6–8 lines. |
| **B** | **Key words** | The Arabic/English terms of this module with meaning in English + Bangla + a one-line example. |
| **C** | **Slide by slide (page by page)** | One step for **every slide** (details below). Nothing skipped. |
| **D** | **Put it together** | Comparison tables, mind-map-style summary, the "if they ask X, write Y" patterns. |
| **E** | **Midterm connection** | Which of the 40 study questions this module answers, with the model answer to write (short + full). Marked ⭐ if the teacher's revision session stresses it. |
| **F** | **Module quiz — 5 questions** | English + Bangla question, 4 options, answer + explanation in both languages. Plus small quick-checks inside Part C. |
| **G** | **Module summary** | One-page recap (also exported as the printable `.md` note). |

### 2.3 Each slide step (Part C) — page by page

For **every slide**, one step (title-only/picture-only slides are shown as their own step too, marked "title slide / diagram", so the slide numbers match your PDF exactly):

| Block | Content |
|---|---|
| **Slide N of M — original text** | Text from the slide, cleaned (English; Arabic rebuilt and checked against the page image) |
| **বাংলা অনুবাদ (translation)** | Proper Bangla translation of that slide text, line by line |
| **Teacher explains** | What the slide means, in simple words, English + Bangla — "like a teacher talking to a student" |
| **Example** | For every hard idea: an everyday example/analogy so it sticks |
| **Exam tip** | How the midterm asks this and a model sentence to write; ⭐ if stressed in the revision session |
| **Open this slide** | Link to the original PDF page |

If a slide only has a heading (e.g. "They do not eat or drink"), I show the slide text exactly, then add the missing explanation. Text I add is labelled **"Added by teacher-explanation (not on the slide)"** so you always know what your lecturer wrote vs what I added.

### 2.4 Quizzes

- **5 questions at the end of every module** (15 × 5 = **75**), English + Bangla, with explanations in both.
- Small **quick-check** questions inside the module after every few slides (as in BIBS/FPEC).
- Mixed difficulty: 2 recall, 2 understanding, 1 "which statement is wrong / apply the idea".

### 2.5 Language rule

Everything is **English + Bangla**: concept explanation, slide text, explanation, example, exam tip, quiz question, options, explanation. Arabic terms stay in Arabic + transliteration, followed by English and Bangla meaning.

### 2.6 "Make sure nothing is missed" — how I guarantee coverage

1. **Slide ledger:** for each module I build a table of slide numbers 1…N. Every slide must have a step. The build **fails** if any slide number is missing or duplicated.
2. **Text coverage check:** a script compares every non-empty line extracted from each slide with the module output; any line not present is reported and fixed (or marked as decorative, e.g. page numbers).
3. **Image slides:** each rendered by me and read; listed in the extraction report with what the picture shows.
4. **Question coverage:** all 40 midterm questions must map to ≥1 module; all 24 revision slides must map to ≥1 module. Unmapped = flagged to you.
5. **Bangla check:** every step has non-empty Bangla; every quiz item has Bangla question, options and explanation.
6. **Final coverage report** (`content/isgs101/COVERAGE.md`): module → slides covered → midterm questions → quiz count. You can verify it at a glance.

---

## 3. Method — how I will do it, step by step

### Phase 0 — Setup (small)
- Pull `master` (done — the slides are now in my checkout).
- Create a working area outside the site (scratch) for extraction and generation scripts, same approach as the BIBS and FPEC builds.

### Phase 1 — Extract (per module)
1. `pdftotext -layout` for every slide, saved as `modNN/slideNN.txt`.
2. Render **every page to PNG** (`pdftoppm`) and look at the near-empty / Arabic-heavy slides myself.
3. Build a clean per-module "source sheet": slide number, English text, Arabic text (rebuilt), notes about images/diagrams.
4. Produce an **extraction report**: slides per module, how many were text-rich vs empty, anything I could not read.

### Phase 2 — Understand & structure
- Group slides into lessons/steps (one or more slides per step).
- Cross-check each module against the **40 midterm questions** and the **revision session**: every question gets mapped to the module/slide that answers it ("this question is answered in Module 2, slides 5–9").
- List the hard concepts per module that need an example.

### Phase 3 — Write the teaching content
- English explanation first, then Bangla — written by me directly, not machine-pasted, with one consistent Bangla glossary (so *Tawheed* is always spelled the same way, etc.).
- Quranic verses and hadith: I will only cite what the slides themselves cite, plus well-known references I am certain of. Where I am not 100% sure of a reference number or wording, I will **say so** and mark it "verify" instead of inventing it.
- Examples for every hard concept, taught like a teacher: "Imagine…", "Think of…", then the rule.

### Phase 4 — Quizzes
- 5 questions per module, mixed difficulty: 2 recall, 2 understanding, 1 "which statement is wrong / apply the idea".
- Distractors are plausible mistakes students actually make (e.g. confusing Rububiyyah with Uluhiyyah).
- Plus inline Quick checks.

### Phase 5 — Build into the site
- New module course engine for ISGS (reuse the FPEC course engine: Back/Next, progress, resume, deep links such as `#isgs-mod-03`), plus a **Modules page with buttons Module 1…15**; clicking a button opens only that module.
- Update ISGS menu: **Modules** | **Midterm Q&A** | **Revision session** | **Mock exam** | **Glossary** | **Assignment**. Default stays **Midterm Q&A** (you can change it).
- **Size control:** `index.html` is already ~1 MB. 292 slides of English + Bangla would add several MB. I will put module content in separate files (`/isgs/mod01.js` …) that load only when you open that module, so the site stays fast on mobile.
- Keep the existing assignment wizard and the 40-card Q&A working (no regressions).

### Phase 6 — Testing
- Headless-browser tests for every module: opens, all steps reachable, Back/Next, quiz scoring, deep links, mobile width, no JavaScript errors.
- Content checks: every slide number 1…N of every module appears exactly once; every module has exactly 5 end-quiz questions; every step has both English and Bangla; every one of the 40 midterm questions links to a module.

### Phase 7 — Review checkpoints and delivery
- **Pilot first:** I build **Module 1 only** (10 slides, smallest), push it, and you check style/language/depth before I do the other 14.
- Then deliver in batches of ~3 modules per commit/deploy (Mods 2–4, 5–7, 8–10, 11–13, 14–15 + Q&A + mock exam + glossary).
- Export each module as a printable `.md` study note in the repo (`content/isgs101/mod01.md` … `mod15.md`) — same content as the site (concept explanation, slide-by-slide, midterm connection, quiz with answers) in English + Bangla.

---

## 4. Midterm focus

- The **40 study questions** are the spine. Every module page ends with "Midterm questions answered by this module: Q3, Q5, Q6…".
- Each of the 40 answers gets: a **short exam answer** (what to write in 3–5 lines), a **full answer** (teacher version), and an **example** where the concept is hard.
- The **revision session PDF** (teacher's own priorities) is used to rank topics: things she repeats are marked ⭐ "very likely in exam".
- The existing 40-card Q&A on the site will be audited against the slides: any answer not supported by the slides gets corrected.

---

## 5. Concepts I expect to need extra examples for

(Final list confirmed after extraction.)

- Tawheed ar-Rububiyyah vs al-Uluhiyyah vs al-Asma wa Sifat (the three types)
- Why even the pagan Arabs who accepted Rububiyyah were still fought (Q8)
- The seven conditions of *Laa ilaaha illallaah* (knowledge, certainty, acceptance, submission, truthfulness, sincerity, love)
- Aqeedah vs Tawheed (Q4)
- Names & Attributes: affirming without distorting, denying resemblance, "nothing is like Him" (Q19)
- Qadar: knowledge, writing, will, creation — and "Allah does whatever He wills" (Q17, Q18, Q31)
- Nabi vs Rasool; infallibility of messengers (Q26, Q27)
- Greater vs lesser shirk; Shirk vs Kufr (Q32–Q34)
- Fortune-telling as shirk; grave worship and which Tawheed it breaks (Q35–Q37)
- Imaan vs Ihsaan (Q39); Angel Jibril's role (Q40)

---

## 6. Deliverables checklist

- [ ] Extraction report (slides per module, empty slides, image slides)
- [ ] 15 modules: Part A teacher-style big picture → key words → slide-by-slide (every slide, English + Bangla, explanation, examples, exam tips) → summary → midterm connection
- [ ] 15 module-end quizzes × 5 questions = **75 quiz questions** (plus inline quick checks)
- [ ] 40 midterm answers rebuilt (short + full) and linked to slides
- [ ] Revision-session explainer (24 slides)
- [ ] Mock midterm paper
- [ ] Glossary / cheat sheet (Arabic + English + Bangla)
- [ ] Site integration + automated tests + deployed to GitHub Pages
- [ ] Printable `.md` notes per module (`content/isgs101/modNN.md`)
- [ ] `COVERAGE.md` proving no slide / question was missed

---

## 7. Effort and order

This is large: 292 slides, ~150,000 characters of source text, two languages. It will take many working turns, not one. Order: **pilot Module 1 → your feedback → Mods 2–4 → 5–7 → 8–10 → 11–13 → 14–15 → Q&A/Revision/Mock/Glossary.** I'll commit and push after each batch so the site always works.

---

## 8. Risks and how I handle them

| Risk | Handling |
|---|---|
| Slide is just a heading and says nothing | I explain it from standard Aqeedah teaching, clearly separated from the slide's own text so you can see what the teacher wrote vs what I added |
| Arabic extraction garbled | Rebuild Arabic manually, view the page image to check |
| I'm not sure of a verse/hadith reference | I will say "verify with your teacher/book" instead of guessing |
| Scholarly differences (e.g. is Khidr alive? Dhul-Qarnayn a prophet?) | I give the position the slide takes, mention the other view in one line, and tell you what to write in the exam (follow your teacher's slide) |
| Site becomes too heavy | Lazy-load module files |
| Bangla spelling/terms inconsistent | One glossary used everywhere |
| Quiz too easy | Mixed difficulty + realistic wrong options |

**Important:** This is religious content. Please let your teacher's slides and textbook remain the final authority; my added explanations are study aids, and anything marked "verify" should be checked with your instructor.

---

## 9. Decisions (resolved)

1. Quizzes: **5 per module** (+ inline quick-checks). ✅
2. Printable `.md` notes per module: **yes**. ✅
3. **Same course** — built inside the existing ISGS 101 section, with Module 1…15 buttons; Midterm Q&A remains the default landing page unless you tell me otherwise. ✅

**Next step:** on your "go" I start Phase 0–1 (extraction + coverage report) and build the **Module 1 pilot** in the new order (big picture → key words → slide by slide → quiz). You review Module 1; then I continue with the rest in batches.
