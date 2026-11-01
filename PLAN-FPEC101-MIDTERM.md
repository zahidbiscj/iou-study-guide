# FPEC 101 — Principles of Economics: Midterm Course Plan (Modules 1–15)

**Status: PLAN v2 — files received and analysed; building.** You uploaded the 15 lecture PPTX files, the 20 midterm study questions and the revised syllabus (on the `feature` branch). I copied them to this branch, extracted every slide (376 slides), and Module 1 is built. Progress per module is in `content/fpec101/COVERAGE.md`.

**Goal:** make FPEC 101 a complete **English + Bangla** midterm course for **Modules 1–15**. I go through every slide of every module, one at a time, and explain it the way a local tutor would: simple words, real-life examples from Bangladesh, small number examples, graphs drawn step by step, and what to write in the exam. The course ends with the official midterm questions answered and a mock exam.

---

## 1. What I found and what I still need from you

### Already on the site (I will keep and reuse it)
| Part | What it is | What happens to it |
|---|---|---|
| **FPEC 101 · Midterm Q&A (20 questions)** | 20 microeconomics midterm questions, each answered in EN + বাংলা | **Kept.** I check every answer against your slides, fix anything the slides say differently, and link each question to the module and slide it comes from. |
| **FPEC 101 · Final exam course (18 lessons)** | Macroeconomics, for the final exam | **Unchanged.** It is for the final, not the midterm. |
| **Module engine from ISGS 101** (`isgs/index.js`, `isgs/mod01.js`) | Module 1…15 buttons, Back/Next, progress, resume, quizzes, lazy-loading | **Reused**, so FPEC looks and works like ISGS. |

### Missing (this blocks the slide-by-slide work)
I searched **every branch** (`master`, `feature`, and all `claude/*` branches). `slides/` only has **Islamic Studies (ISGS 101)** and **English Language Studies (ENES 101)**. There are **no Principles of Economics files**:

| Needed | Why |
|---|---|
| **Module 1 … Module 15 slides/notes** (PDF / PPTX / DOCX / images) | To go slide by slide and leave nothing out |
| **Midterm study questions / past papers** (if they differ from the 20 already on the site) | Model answers |
| Midterm revision session slides (if your teacher gave one) | To mark ⭐ the topics your teacher stresses |
| Syllabus / course outline | To confirm module titles, the textbook (McConnell? Mankiw? Sloman?) and the exam format |

**Please upload them to:** `slides/Principles of Economics (FPEC 101)/`
Suggested names: `FPEC(mod01).pdf` … `FPEC(mod15).pdf`, `FPEC 101 Midterm Study questions.pdf`, `FPEC 101 Midterm Revision.pdf`, `FPEC 101 Syllabus.pdf`. Any names work, as long as I can tell which file belongs to which module.

> If the files are on Google Drive, in another repo, or inside a ZIP, tell me where and I'll take them from there.

---

## 2. Real module map (from your files)

Lecturer: **Salimah Musharrif**. Textbook: **McConnell, Brue & Flynn, _Economics_ (20th ed.)**. Assessment: unit tests 15%, assignment 15%, **midterm 30%**, final 40%. The midterm covers **Unit 1 (Lectures 1–5)** and **Unit 2 (Lectures 6–15)**. The 20 official midterm study questions are the **same 20 already on the site**.

| Mod | Lecture topic (syllabus) | Slides | Midterm Qs |
|---|---|---|---|
| 1 | Definitions, micro/macro, positive/normative, scarcity, opportunity cost, PPC | 13 | Q1, Q2, Q3 |
| 2 | Market systems (command, market, mixed) and circular flow of income | 20 | Q4, Q5 |
| 3 | Demand and supply analysis, market failure and government intervention | 38 | Q6, Q7 |
| 4 | Demand and supply analysis, elasticity of demand | 21 | Q7, Q8 |
| 5 | PED and total revenue, elasticity of supply, income and cross elasticity | 26 | Q8, Q9, Q10 |
| 6 | Economic costs, short-run and long-run costs | 35 | Q11, Q12 |
| 7 | Economic costs, short-run and long-run costs (economies of scale, business growth) | 19 | Q13, Q14 |
| 8 | Perfect competition | 30 | Q15 |
| 9 | Pure monopoly | 31 | Q15 |
| 10 | Pure monopoly (cont.), monopolistic competition | 24 | Q15 |
| 11 | Oligopoly | 27 | Q15 |
| 12 | Competition policy and regulation | 19 | Q16 |
| 13 | Wage determination | 27 | Q17, Q18 |
| 14 | Income inequality, poverty and discrimination | 19 | Q19 |
| 15 | Government and market failure | 27 | Q20 |

What the files look like: all text is extractable from the PPTX; graphs are drawn as PowerPoint shapes or pictures, so I render every slide to an image and redraw each graph as a labelled diagram. A few slides have speaker notes (Lectures 4, 5, 8); those are shown too.

## 3. What you will see (UI layout)

### 3.1 FPEC 101 home screen
```
┌──────────────────────────────────────────────────┐
│ FPEC 101 · Principles of Economics                │
│ Midterm: Modules 1–15   ▓▓▓▓▓░░░░░ 34% done        │
├──────────────────────────────────────────────────┤
│ [▶ Continue: Module 5, slide 9]                    │
├──────────────────────────────────────────────────┤
│ 📚 Modules 1–15         │ ❓ Midterm Q&A (20)       │
│ 📈 Graph Gym            │ 🧮 Formula & Numbers      │
│ 📝 Mock Midterm         │ ⚡ Last-night cheat sheet │
│ 🎓 Final exam course (separate, unchanged)          │
└──────────────────────────────────────────────────┘
```
The side menu lists **Module 1 … Module 15** (`#fpec-mod-01` … `#fpec-mod-15`), so you can jump straight to any module.

### 3.2 Modules grid
15 cards: **Module 5 — Demand & Supply · চাহিদা ও যোগান**. Each card shows ✓ done / % progress, how many slides it has, and ⭐ if the topic is a likely exam question. Clicking a card opens **only that module**, with **◀ Back / Next ▶**, a progress bar, and "resume where I stopped".

### 3.3 Language switch (already on the site)
- **EN + বাং** (default): each English paragraph, then the Bangla explanation in a shaded box.
- **English**: English only, which is how you will write in the exam.
- **বাংলা**: Bangla only, for when a topic feels hard.

Rule: technical words stay in English with a Bangla gloss, e.g. *Elasticity (স্থিতিস্থাপকতা)*, *Opportunity cost (সুযোগ ব্যয়)*, so you can recognise them in the question paper. One glossary keeps every Bangla term the same everywhere.

---

## 4. How every module is taught (tutor → student order)

| Part | Name | What's in it |
|---|---|---|
| **A** | **Tutor's intro** | "What is this module about? Why does it matter? How does it connect to the last module?" in plain English plus Bangla, around one everyday story (a tea stall, rice prices in Karwan Bazar, Pathao fares when it rains). Ends with a **2-minute version**: the whole module in 6–8 lines. |
| **B** | **Key terms** | Each term: English definition · বাংলা meaning · one-line example. |
| **C** | **Slide by slide** | **One card for every slide**, none skipped (see 4.1). |
| **D** | **Put it together** | Comparison tables (e.g. *movement vs shift*, *perfect competition vs monopoly*), a short "how one idea leads to the next" summary, and common mistakes (✗ wrong / ✓ right). |
| **E** | **Numbers & graphs** | Worked calculations (elasticity, costs, profit), each done one step at a time, plus every graph from the module drawn step by step (see Section 5). |
| **F** | **Midterm link** | The midterm questions this module answers, each with a **short answer** (what to write in 5–8 lines) and a **full answer** (for long questions), plus the graph to draw. ⭐ = stressed by your teacher. |
| **G** | **Module quiz** | 5 MCQs (EN + বাংলা) with explanations, plus quick checks between slides. |

### 4.1 One slide = one card
```
┌ Module 7 · Slide 6 / 21 ─────────────────────────────┐
│ 📄 Slide says:   (the slide text, word for word)        │
│ 🇧🇩 বাংলা অনুবাদ:  line-by-line Bangla translation       │
│ 🧑‍🏫 In simple words (EN):  what it really means          │
│ 🧑‍🏫 সহজ কথায় (বাংলা):  same explanation in Bangla        │
│ 🛒 Real life:  a Bangladesh example (rice, petrol,       │
│               mobile data, garments, Eid shopping…)      │
│ 🧮 Numbers / 📈 Graph:  if the slide has any             │
│ ⚠️ Exam tip:  how it is asked + a model sentence         │
│ [ ✓ I understood this ]          [ Open original slide ] │
└───────────────────────────────────────────────────────┘
```
- **Title or blank slides** get one line ("Title slide: Module 7 starts here"), so slide numbers match your PDF exactly.
- **Graph or picture slides:** I render the page as an image, read it myself, and redraw the graph as a clean, labelled diagram that works in both light and dark mode.
- **Bullet-only slides:** I add the explanation your teacher would give in class, marked clearly as **Tutor's note (not on the slide)**, so you always know what the slide says and what I added.
- **Formula slides:** the formula, what each letter means, then one worked example with real numbers.

### 4.2 Real-life examples (how I make hard topics easy)
Every hard idea gets an everyday example before the theory. For example:

| Concept | Real-life example |
|---|---|
| Opportunity cost | Choosing between a part-time job and studying for the midterm: the job's pay is the cost of studying |
| PPC | A farmer in Bogura with one field: more rice means less potato |
| Law of demand | Hilsa price falls in season, so more people buy hilsa |
| Shift vs movement | Onion price rises (movement) vs Eid comes and everyone wants more beef at every price (shift) |
| Price elasticity | Salt (inelastic: you buy it anyway) vs restaurant biryani (elastic) |
| Cross elasticity | Tea and sugar (complements); Grameenphone vs Robi data (substitutes) |
| Price ceiling | Government sets a maximum price for rice or fuel, and queues/shortage appear |
| Economies of scale | Big garment factory vs a small tailor: cost per shirt falls as size grows |
| Monopoly / oligopoly | Electricity supply (monopoly); mobile operators, cement companies (oligopoly) |
| Market failure | Factory smoke on the Buriganga (externality); street lights (public good) |
| Minimum wage | The RMG minimum wage debate |

---

## 5. Economics-specific features

1. **📈 Graph Gym**: every graph in Modules 1–15 (PPC, demand/supply, equilibrium, shifts, ceiling/floor, elasticity, cost curves (TC/AVC/ATC/MC), MR=MC, the four market structures, labour market, externalities). Each one is built **in steps**: axes → first curve → second curve → equilibrium → what changes. You click "Next" and watch it form, then practise "which way does it shift?" questions.
2. **🧮 Formula & Numbers**: every formula on one page (opportunity cost, PED midpoint formula, PES, YED, XED, TR/TC/profit, AFC/AVC/ATC/MC, MP/AP), each with a worked example and 2–3 practice problems with answers hidden.
3. **"How to draw this in the exam"** box under every graph: which labels and arrows you need so you don't lose marks.
4. **Common-mistake alerts**, e.g. "a price change does **not** shift the demand curve"; "elastic means |PED| > 1"; "normal profit is a cost".

---

## 6. Other sections

1. **Midterm Q&A (20)**: the existing answers, checked against your slides, with links to module/slide, a **short answer + full answer + diagram** for each, search, self-test mode (answers hidden), and an "I've learned this" counter.
2. **Mock Midterm**: a full practice paper in your real exam format (I'll match it to the syllabus), with a timer and the answers shown at the end.
3. **Last-night cheat sheet**: one printable page with definitions, formulas, the 10 must-know graphs and the 4 market structures table.
4. **Printable notes**: `content/fpec101/mod01.md` … `mod15.md`, with the same content as the site.

---

## 7. How I'll build it (step by step)

1. **Extract**: get the text of every slide (`pdftotext`), render every page to PNG, and look myself at graph and picture slides. Save the raw text in `content/fpec101/source/`.
2. **Inventory**: slides per module, real module titles, which slides are graph-only or empty. This replaces the guessed map in Section 2.
3. **Map the questions**: link each midterm question to its module and slides, and mark the ⭐ topics from the revision slides.
4. **Pilot: Module 1 only**, built fully (Parts A–G), then pushed. **You review it** and tell me what to change: more or less Bangla, longer or shorter, more examples, harder quiz.
5. **Modules 2–15** in the same style, pushed in batches (2–4, 5–7, 8–10, 11–13, 14–15) so you can start studying early. Modules load as separate files (`fpec/modNN.js`) only when you open them, so the site stays fast on mobile.
6. **Graph Gym, Formula page, Q&A audit, Mock Midterm, Cheat sheet.**
7. **Coverage check** (`content/fpec101/COVERAGE.md`): every slide number of every module mapped to its card. The build **fails** if a slide is missing or a card has no Bangla, so **nothing is missed**.
8. **Testing**: a headless browser opens every module, clicks through all steps, checks quizzes, deep links, phone width, light and dark mode, and that the console has no errors. Then I push to `claude/dazzling-faraday-35ajwk`.

---

## 8. Risks and how I handle them

| Risk | Handling |
|---|---|
| Slides are only headings or bullet points | I explain them from the standard textbook topic and label it *Tutor's note* |
| Graphs exist only as images | I redraw them as clean SVG diagrams, checked against the slide image |
| Slide numbers or formulas look wrong | I show the slide as it is, note the correction, and say what to write in the exam |
| Too much content for a phone | Lazy-loaded module files and short cards (one idea per screen) |
| Bangla terms inconsistent | One FPEC glossary used everywhere |

---

## 9. Questions for you (answer when you upload the files)

1. **Exam format:** MCQ, short answer, long answer with graphs, numerical problems, or a mix? How many marks, and how long is the exam?
2. **Midterm questions:** are the **20 questions already on the site** the official study questions for this semester, or is there a new list?
3. **Default screen** for FPEC 101: **Modules** (my suggestion for the midterm) or **Midterm Q&A**?
4. **Quiz size:** 5 MCQs per module, or 10?
5. **Bangla level:** full Bangla for every slide (my default), or only for hard parts?
6. Your message said "good result in **English** studies." I've taken that to mean Principles of Economics, the subject you asked for. ENES 101 (English) has its own plan in `PLAN-ENES101-MIDTERM.md` on another branch, and its notes are on the `feature` branch. Tell me if you meant English instead.

---

*Next step: upload the FPEC 101 files to `slides/Principles of Economics (FPEC 101)/` (or tell me where they are) and say **"go"**. I'll start with the inventory and the Module 1 pilot.*
