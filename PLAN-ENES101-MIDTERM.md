# ENES 101 — English Language Studies: Midterm Course (Modules 1–15)

**Status: BUILT (v1).** Open the site → **ENES 101 · English Language Studies**.

## What was built
- **Source:** `slides/English Language Studies (ENES 101)/English Notes 1 to 15.pdf` (main), checked against the syllabus, curriculum outline, *Lecture 9–15 Notes*, Durrian Qadri's 231-page midterm notes and `ENES101Study questions.pdf`.
- **Module course** (`#enes-course`, `#ecourse-E1` … `#ecourse-E15`): "Start here" + 15 modules, 64 teaching steps. Every heading and table from the notes is explained in English with **Bangla side by side**; True/False study-question traps are flagged in the lesson they belong to.
- **MCQ quick check after every module**: 106 questions, each with a bilingual explanation for the right answer.
- **Midterm Q&A** (`#enes-midterm`): all **25 short** (T/F, Yes/No) and **34 long** study questions answered (the English model answer to write + a Bangla explanation + a link to the module), with search, self-test, "learned" ticks and a 25-question T/F MCQ quiz.
- Same look and controls as the other courses: EN+বাং / English / বাংলা switch, dark mode, progress saved, phone layout.

---

## Original plan (kept for reference)


## 1. What I found and what I still need from you

### Found
- `index.html` already has an **ENES 101** subject card and an empty section (`data-subject="enes"`) that says *"Study notes for this subject are coming soon."* I will fill this section.
- The site already has what this course needs: the **EN + বাং / English / বাংলা** language switch, dark mode, progress tracking, and mini-quizzes (used for ISGS 101 and FPEC 101). ENES will use the same parts, so it looks and works like the other courses.

### Not found (this blocks me)
The repo has **no English Language Studies files**. On every branch, `slides/` only holds `Islamic Studies 1 (ISGS 101)/`. I could not find:

| Needed | Why |
|---|---|
| Module 1 … Module 15 slides/notes (PDF / PPTX / DOCX / images) | To cover every slide, page by page |
| **Midterm study questions / past midterm paper** | To build the "Midterm Q&A" with model answers |
| Midterm revision session slides (if the teacher gave one) | To mark ⭐ the topics the teacher stresses |
| Syllabus / course outline (optional) | To confirm the module titles and the exam format (MCQ? short answer? essay?) |

**Please upload them to:** `slides/English Language Studies (ENES 101)/`
Suggested names: `ENES(mod01).pdf` … `ENES(mod15).pdf`, `ENES 101 Midterm Study questions.pdf`, `ENES 101 Midterm Revision.pdf`, `ENES 101 Syllabus.pdf`. Any names work, as long as I can tell which module each file is.

> If the files are in a different branch, a Google Drive folder, or another repo, tell me where and I'll pull them from there.

---

## 2. What you will see (UI layout)

### 2.1 The ENES 101 home screen
When you click **ENES 101 · English Language Studies** on the main page:

```
┌──────────────────────────────────────────────┐
│ ENES 101 · English Language Studies           │
│ Midterm: Modules 1–15   ▓▓▓▓▓░░░░░ 34% done    │
├──────────────────────────────────────────────┤
│ [▶ Continue: Module 4, slide 7]                │
├──────────────────────────────────────────────┤
│ 📚 Modules        │ ❓ Midterm Q&A             │
│ 📝 Mock Midterm   │ 📖 Grammar & Word Bank     │
│ ⚡ Last-night cheat sheet                       │
└──────────────────────────────────────────────┘
```

### 2.2 Modules grid
15 cards: **Module 1 — <topic>**, **Module 2 — <topic>** … each one shows ✓ done / % progress and a ⭐ if the teacher stressed it. Clicking a card opens **only that module**, with **◀ Back / Next ▶** buttons, a progress bar, and "resume where I stopped". The side menu also lists Module 1–15 (`#enes-mod-01` … `#enes-mod-15`) so you can jump straight to one.

### 2.3 Language switch (already on the site)
- **EN + বাং** (default): each English paragraph is followed by its Bangla explanation in a lightly shaded box.
- **English**: English only, which is how you will write in the exam.
- **বাংলা**: Bangla only, for when a topic is hard to follow.

**Rule for an English course:** the Bangla part *explains*, it doesn't replace. Example sentences, grammar rules, definitions and model answers always stay in **English** (that's what the exam marks). The Bangla says what they mean and when to use them. Word lists show the **English word + বাংলা meaning + an English example sentence**.

---

## 3. How every module is taught (teacher → student order)

| Part | Name | What's in it |
|---|---|---|
| **A** | **Tutor's intro** | "What is this module about, why does it matter in the exam, and how does it link to the last module?" in simple English plus Bangla. Ends with a **2-minute version**: the whole module in 5–8 lines. |
| **B** | **Key terms** | Each term with its English definition, বাংলা meaning, and one example (e.g. *Noun — a naming word — নামবাচক শব্দ — "Dhaka is a city."*). |
| **C** | **Slide by slide** | One step for **every slide**, none skipped (details in 3.1). |
| **D** | **Put it together** | Rule tables, comparison charts (e.g. *its vs it's*, *Present Perfect vs Past Simple*), and a list of common mistakes Bangladeshi students make, with a ✗ wrong / ✓ right example for each. |
| **E** | **Practice** | 5–10 exercises in the exam's own style (fill in the blank, correct the sentence, MCQ, short answer, a short writing task), with answers hidden behind "Show answer" and a short reason for each. |
| **F** | **Midterm link** | The official midterm questions this module answers, each with a **model answer** (a short version and a full version). ⭐ marks the ones the teacher stressed. |

### 3.1 One slide = one card
```
┌ Module 3 · Slide 5 / 18 ─────────────────────┐
│ 📄 Slide says:  (the slide text, word for word) │
│ 🧑‍🏫 In simple words (EN):  explanation          │
│ 🇧🇩 বাংলায় বুঝি:  same idea in Bangla           │
│ ✏️ Example:  2–3 English sentences, key part bold│
│ ⚠️ Exam tip / common mistake                     │
│ [ ✓ I understood this ]                          │
└──────────────────────────────────────────────┘
```
- **Title or blank slides** get one line ("Title slide: the topic starts here") so nothing looks skipped.
- **Picture-only slides:** I render the page as an image, read it myself, and write out what it shows.
- **Outline-only slides** (bullet points only): I add the explanation the teacher would give in class, and I mark it clearly as *tutor's note*, so you can tell slide content from my additions.
- **Slide typos** stay as they are in "Slide says", and my explanation uses the correct form. In an English course that's a useful lesson too.

---

## 4. Other sections

1. **Midterm Q&A**: every official study question with a model answer you can write in the exam (EN), a Bangla explanation, and a link to the module and slide it comes from. Includes search, *expand all*, *self-test* (answers hidden), and an "I've learned this" counter, the same as ISGS 101.
2. **Mock Midterm**: one full practice paper in the real exam format (I'll match the format once I see the questions/syllabus), with a timer and the answers revealed at the end.
3. **Grammar & Word Bank**: every grammar rule and vocabulary word from Modules 1–15 in one searchable table, sortable by module.
4. **Last-night cheat sheet**: one printable page with the must-know rules, definitions and formats (letter/email/paragraph structure if they're in the syllabus).
5. **Printable notes:** an optional `.md`/print view for each module.

---

## 5. How I'll build it (step by step)

1. **Read all the files.** Extract the text of every slide. Turn image-only or low-text pages into images and read them visually. Write up a short inventory: slides per module, module titles, which slides are empty or image-only.
2. **Read the midterm questions and revision slides.** Match each question to a module and slide, and mark the ⭐ topics.
3. **Pilot: Module 1 only.** Build it fully (Parts A–F) and push. **You review it and tell me what to change** (more or less Bangla, longer or shorter, harder or easier examples).
4. **Modules 2–15**, built in the same style. I'll push in batches (for example 2–5, 6–10, 11–15) so you can start studying early.
5. **Midterm Q&A, Mock Midterm, Word Bank, Cheat sheet.**
6. **Coverage check:** a table that maps every slide number in every module to its card, so you can see that **nothing was missed**.
7. Test on a phone-width screen, and in light and dark mode, then push to branch `claude/vigilant-hamilton-1nc7rg`.

---

## 6. Questions for you (answer when you upload the files)

1. **Exam format:** MCQ, short answer, writing (paragraph/letter/essay), or a mix? How long is the exam?
2. **Default screen:** when you open ENES 101, should it show **Modules** or **Midterm Q&A** first?
3. **Practice per module:** is 5 questions enough, or do you want 10?
4. **Bangla level:** full Bangla explanation for every slide (my default), or Bangla only for the hard parts?
5. Does your teacher have a fixed answer style or format for writing tasks that I should follow?

---

*Next step: upload the ENES 101 files to `slides/English Language Studies (ENES 101)/` (or tell me where they are) and say **"go"**. I'll start with the inventory and the Module 1 pilot.*
