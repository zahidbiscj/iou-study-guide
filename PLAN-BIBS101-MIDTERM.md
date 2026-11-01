# BIBS 101 — Introduction to Business: Midterm Course Plan

**Status: DONE — all 9 modules built (see `content/bibs101/COVERAGE.md`).**

Goal: turn the BIBS 101 slides into a complete **English + Bangla** midterm course, taught the way a tutor would teach it. Every slide is covered, every hard idea gets an example, every study question gets a model answer, and every module ends with a quiz. It follows the same method as the ISGS 101 rebuild ([PLAN-ISGS101-REORGANIZE.md](PLAN-ISGS101-REORGANIZE.md)).

---

## 1. What I found (research)

The BIBS slides are on the **`feature`** branch in `slides/Introduction to Business (BIBS 101)/`. They are not on `master` or on this branch yet. That folder is 12 MB and holds 11 PDFs.

| File | Slides | Study questions | Syllabus units |
|---|---|---|---|
| Unit 1 and 2 - Role of Business | 52 | 1.1 – 1.6 | 1 (s1–23), 2 (s24–52) |
| Unit 3 and 4 - EconEnvironment | 64 | 2.1 – 2.7 | 3 (s1–22), 4 (s23–64) |
| Unit 5 and 6 - GlobalEnvironment | 78 | 3.1 – 3.6 | 5 (s1–42), 6 (s43–78) |
| Unit 7 - FinancialMarketsandSystem | 47 | 4.1 – 4.3 | 7 |
| Unit 8 - LegalEnvironment | 57 | 5.1 – 5.7 | 8 |
| Unit 9 - BusinessEthics | 34 | 6.1 – 6.4 | 9 |
| Unit 10 and 11 - BusinessOwnership | 57 | 7.1 – 7.7 | 10 (s1–32), 11 (s33–57) |
| Unit 12 and 13 - Entrepreneurship | 42 | 8.1 – 8.5 | 12 (s1–17), 13 (s18–42) |
| Unit 14 and 15 - Management | 74 | 9.1 – 9.6 | 14 (s1–30), 15 (s31–74) |
| **Total** | **555** | **51** | **Units 1–15** |
| BIBS 101 Study Qs | 3 pages | the 51 official questions, "Units covered 1–15" | — |
| BIBS 101 Syllabus | 7 pages | assessment, unit-to-slide map (Units 1–30) | — |

### What this means

1. **The midterm covers Units 1–15, which is all 9 slide decks.** The syllabus runs to Unit 30 (motivation, marketing, HR, accounting and so on), but the study-questions sheet says "Units covered 1–15". Units 16–30 are final-exam material and are out of scope here.
2. **The slides follow the study questions exactly.** Every deck opens with "Module Learning Outcomes", which lists the study questions, and each question then has its own block of slides. For example, Q2.3 "Law of demand" is Econ slides 24–32. There are also **~160 sub-outcomes** (1.1.1, 1.1.2 …), and they make natural lesson steps. So the course can follow the 51 questions directly.

   Where each question starts (slide number in its deck):
   - 1.x: 4, 14, 20, 25, 36, 41
   - 2.x: 4, 18, 24, 33, 41, 48, 57
   - 3.x: 4, 19, 26, 44, 58, 67
   - 4.x: 4, 18, 38
   - 5.x: 4, 9, 14, 28, 36, 41, 49
   - 6.x: 4, 9, 18, 27
   - 7.x: 4, 9, 14, 23, 34, 42, 49
   - 8.x: 4, 9, 19, 29, 36
   - 9.x: 4, 15, 25, 32, 44, 59
3. **The text is clean English.** Unlike ISGS, there is no Arabic and no garbled extraction, so `pdftotext` gives usable text.
4. **About 76 slides (~14%) have almost no text, and the decks contain about 200 embedded images.** I rendered samples and checked them. These are section-divider slides ("Supply", "Equilibrium") and **graphs or tables that exist only as pictures**, such as the supply curve, the shifts-in-supply diagram, the business cycle, org charts and trade tables. They carry exam content, so I will read each one visually. Key graphs will be redrawn as clean labelled diagrams, and the rest will be shown as the slide image.
5. **The slides are US-centric** (the Fed, the FDIC, U.S. law and U.S. small business). The exam will ask these as written, so I keep the US facts. Where it helps understanding, I add a one-line Bangladesh comparison, such as the Federal Reserve ↔ Bangladesh Bank.
6. **The existing BIBS section on the site (51 Q&A cards + quiz) was written before the slides were available.** It is generic textbook content and does not cite slides. Some answers may use different lists or terms from what your lecturer's slides use. **All 51 answers will be checked against the slides and rewritten where they differ.** For example, the slide's exact list of stakeholders, the slide's "four factors of production", and the slide's names for the four economic stages.
7. **The syllabus has small errors.** Unit 12 says "Slides -17", meaning 1–17. Unit 13 says "Global Environment" but means Entrepreneurship. The header says "ISLAMIC STUDIES 3". None of these affect the course.

### Assessment (from the syllabus)

| Component | Weight |
|---|---|
| Unit tests (**MCQ**) | 15% |
| Research assignment | 15% |
| **Mid-semester exam** | **30%** |
| Final exam | 40% |

The unit tests are MCQ and the 51 study questions are "explain / list / distinguish" questions. The course therefore trains **both**: written answers *and* a lot of MCQ practice.

---

## 2. How the course is organized

**Course = 9 modules → 51 lessons (one per study question) → 555 slides.**

| Module | Units | Topic | Lessons | Slides |
|---|---|---|---|---|
| 1 | 1–2 | Role of Business | 6 | 52 |
| 2 | 3–4 | Economic Environment | 7 | 64 |
| 3 | 5–6 | Global Environment | 6 | 78 |
| 4 | 7 | Financial Markets & System | 3 | 47 |
| 5 | 8 | Legal Environment | 7 | 57 |
| 6 | 9 | Business Ethics | 4 | 34 |
| 7 | 10–11 | Business Ownership | 7 | 57 |
| 8 | 12–13 | Entrepreneurship | 5 | 42 |
| 9 | 14–15 | Management | 6 | 74 |

I chose decks rather than syllabus units because the syllabus unit boundaries cut through the middle of questions. For example, Unit 1 ends at slide 23 in the middle of Q1.3. Each module still shows its unit numbers and slide ranges, so you can match it to the syllabus.

### 2.1 What you see on the site

Everything goes **inside the existing BIBS 101 section**, as was done for ISGS:

- **Modules**: buttons for Module 1 … 9, each with its topic, slide count and a progress bar. Click one and only that module opens, step by step, with Back/Next and "resume where I stopped". Deep links: `#bibs-mod-01` … `#bibs-mod-09`.
- **Study Questions (51)**: the existing Q&A cards, rewritten from the slides. Each card links to "learn this in Module X, slides a–b".
- **Mock midterm** (written + MCQ, with answer key).
- **Glossary & cheat sheet** (English + Bangla).
- **Quiz**: the existing quiz, rebuilt from the slides.

### 2.2 Teaching order inside every module

| Part | What it contains |
|---|---|
| **A · Big picture** | What this module is about and why business people care, in plain language with an everyday Bangladeshi example (tea stall, bKash, Aarong, garments factory). Includes a **3-minute version** of the whole module. |
| **B · Key words** | Every term from the module, with an English definition, Bangla meaning and a one-line example. Examples: *tort*, *GDP*, *franchise*, *span of control*. |
| **C · Lessons (one per study question)** | Every slide of that question, one by one (see 2.3). |
| **D · Put it together** | Comparison tables (sole proprietorship vs partnership vs corporation; statutory vs common law; the four economic systems), flow diagrams and "if they ask X, write Y". |
| **E · Exam answers** | For each study question in the module: a **short answer** (what to write in 4–6 lines), a **full answer**, and an example, all citing the slides. |
| **F · Module quiz** | 10 MCQs (see 2.4). |
| **G · Summary** | A one-page recap, also saved as a printable note (`content/bibs101/modNN.md`). |

### 2.3 Each slide (inside Part C)

| Block | Content |
|---|---|
| **Slide N of M: original text** | The slide's text, cleaned. For picture slides, a description of the graph/table, or a redrawn diagram. |
| **বাংলা** | A Bangla translation of the slide. |
| **Tutor explains** | What it means in simple words, in English then Bangla. |
| **Example** | A concrete example for every hard idea. For instance, rising onion prices in Ramadan for demand and supply. |
| **Exam tip** | How the midterm or MCQ test asks this point, and a model sentence. |
| **Open slide** | A link to the original PDF page. |

Divider slides that contain only a title (for example "Supply") become one short step, so slide numbers still match your PDF. Text I add beyond the slide is labelled **"Tutor's addition (not on the slide)"**.

### 2.4 Practice

- **Quick check after every study question:** 2–3 MCQs, about 130 in total.
- **Module quiz:** 10 MCQs per module, 90 in total. The mix is recall, understanding, "which is NOT…", and small scenarios such as "A shop owner and her brother share profits and unlimited liability. Which ownership form is this?"
- **Mock midterm:** one full paper with written questions from the 51 plus an MCQ section, and an answer key.
- Every question, option and explanation is in **English + Bangla**.

---

## 3. Method, step by step

**Phase 0: Setup.** Bring `slides/Introduction to Business (BIBS 101)/` from the `feature` branch into this branch so the site's "Open slide" links work. Keep the extraction scripts in scratch, outside the site.

**Phase 1: Extract.**
- `pdftotext -layout` for each slide.
- `pdftoppm` renders every slide.
- I read every picture or graph slide visually.
- The output is a source sheet per module (slide number → text → picture notes → which study question / sub-outcome it belongs to) and an extraction report.

**Phase 2: Map.**
- Slide → sub-outcome → study question → module. This is already mostly known from the table above.
- Audit the 51 existing answers against the slides and list every mismatch.

**Phase 3: Write.**
- Big picture, key words, slide-by-slide explanations and examples, English first then Bangla.
- One Bangla glossary so terms stay consistent everywhere, e.g. *supply = যোগান*, *demand = চাহিদা*, *liability = দায়*.

**Phase 4: Quizzes and the mock exam.** Wrong options are based on real confusions, such as:
- shortage vs surplus
- trade deficit vs budget deficit
- general vs limited partner
- S-corp vs LLC
- express vs implied warranty
- line vs line-and-staff structure

**Phase 5: Build into the site.**
- Generalize the ISGS module engine (Back/Next, progress, resume, lazy loading) so ISGS and BIBS share one engine instead of a copy.
- Add `bibs/index.js` plus `bibs/mod01.js` … `mod09.js`, each loaded only when opened. `index.html` is already ~1 MB, and the full BIBS content will be ~4 MB, so it must not go into the page.
- Redrawn graphs are inline SVG. Slide images are compressed WebP and are used only where needed.

**Phase 6: Test** with headless Chromium:
- every module opens and every step is reachable
- quizzes score correctly and deep links work
- phone width works, with no JS errors
- ISGS still works, since the engine is shared

**Phase 7: Deliver in batches.**
- Pilot **Module 1** (Role of Business, 52 slides) first, and you check style and depth.
- Then Modules 2–3 → 4–6 → 7–9 → Q&A rewrite, mock, glossary.
- Commit and push after each batch so the site always works.

### Guaranteeing nothing is missed

1. **Slide ledger:** each module must contain steps for slides 1…N exactly once. The build fails otherwise.
2. **Text coverage script:** every non-empty slide line must appear in the module output, or be marked decorative.
3. **Picture slides:** each is listed with what it shows and how it is presented (redrawn / image / described).
4. **Question coverage:** all 51 study questions and all ~160 sub-outcomes map to a lesson.
5. **Bangla check:** no step, question or option is missing its Bangla.
6. **`content/bibs101/COVERAGE.md`:** a final table of module → slides → questions → quiz count.

---

## 4. Concepts that need extra teaching (and examples)

- Profit vs loss vs value, and goods vs services (1.1); for-profit vs nonprofit (1.2)
- The four factors of production, including entrepreneurship as a factor (1.3)
- Stakeholders vs shareholders (1.5); the external forces in PESTLE-style form (1.6)
- Economic systems: capitalism, socialism, communism, mixed (2.2)
- **Demand/supply curves, shifts vs movements, equilibrium, surplus, shortage (2.3–2.5)**: redrawn graphs and a worked example
- GDP, unemployment, inflation/CPI, and the business cycle's four stages (2.6–2.7)
- Absolute vs comparative advantage; balance of trade vs balance of payments; exporting → licensing → franchising → contract manufacturing → joint venture → FDI (3.1–3.3)
- Tariffs, quotas, embargoes, dumping; WTO, NAFTA/USMCA, EU, IMF, World Bank (3.4–3.5)
- Functions and characteristics of money; M1 vs M2; the Fed's tools; debt vs equity financing (4.1–4.3)
- Statutory vs common law; tort, negligence, strict product liability; patents, copyrights, trademarks; express vs implied warranties; the elements of a contract and breach (5.x)
- Ethical vs legal (the four-box grid); codes of ethics; the CSR pyramid (6.x)
- Sole proprietorship / partnership / corporation / S-corp / LLC / franchise; unlimited vs limited liability; horizontal vs vertical vs conglomerate mergers (7.x)
- Entrepreneur traits; the steps to start a business; the parts of a business plan (8.x)
- Top / middle / first-line managers; technical, human and conceptual skills; Taylor → Fayol → Weber → Hawthorne; strategic, tactical, operational and contingency plans; line vs line-and-staff vs matrix structures; autocratic vs democratic vs free-rein leadership; the control process (9.x)

(These come from the study questions. The exact lists and terms will follow the slides once they are extracted.)

---

## 5. Size and effort

555 slides × English + Bangla works out to roughly 4–5 MB of course text, loaded per module, and many working turns. That is about twice the size of ISGS. The order is: **pilot Module 1 → your feedback → batches**.

## 6. Risks

| Risk | Handling |
|---|---|
| Graphs/tables exist only as images | View every one; redraw key graphs as SVG and describe the rest |
| A slide is only a heading | Explain it from the prescribed textbook (OpenStax *Introduction to Business*, listed in the syllabus), labelled as a tutor's addition |
| US-specific facts (laws, agencies, figures) | Keep them as the slides state them, since that is what is examined, with a Bangladesh comparison for understanding only |
| Old Q&A conflicts with the slides | The slides win; I note every change in COVERAGE.md |
| Site gets heavy | Lazy-load per module; WebP images only where needed |

---

## 7. Decisions I need from you

1. **Modules = 9 (one per slide deck, aligned to the study questions)**, as I recommend, or 15 separate syllabus units?
2. **Quiz size:** 10 MCQs per module + 2–3 quick checks per question (my suggestion, because unit tests are MCQ), or 5 per module as in ISGS?
3. **Exam format:** do you know the midterm format (MCQ only, short answers, essays, how many questions, time)? The mock paper will follow it if you tell me. Otherwise I use the mixed format above.
4. **Landing page:** keep "Study Questions" as the default BIBS page, or open "Modules" first?

**Next step:** on your "go" (with answers, or "use your defaults"), I do Phase 0–1 for all decks and build the **Module 1 pilot**.
