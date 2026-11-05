// Builds qn/data.js for quick-notes.html from the module files (summary, key words, every MCQ).
// Run: node content/quicknotes/build.js
const fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..', '..');
global.window = {};
const out = {};
function strip(h) { return (h || '').replace(/<div class="mod-fig[\s\S]*?<\/div>/g, ''); }
function mcq(it, src) {
  return { q: it.q, qb: it.qbn || '', o: it.opts, a: it.ans, e: it.exp || '', eb: it.expbn || '', s: src };
}
for (const [key, name] of [['isgs', 'ISGS 101 · Islamic Studies 1'], ['fpec', 'FPEC 101 · Principles of Economics'], ['bibs', 'BIBS 101 · Introduction to Business']]) {
  const mods = [];
  global[key.toUpperCase() + '_REG'] = (n, d) => {
    const m = { n, t: d.t, tb: d.tb, sum: '', words: '', q: [] };
    for (const st of d.steps) {
      if (st.k === 'summary') m.sum = strip(st.h);
      if (st.k === 'words' && !m.words) m.words = strip(st.h);
      if (st.z && st.z.items) st.z.items.forEach(it => m.q.push(mcq(it, st.k === 'quiz' ? 'quiz' : 'check')));
    }
    mods.push(m);
  };
  fs.readdirSync(path.join(ROOT, key)).filter(f => /^mod\d+\.js$/.test(f)).sort()
    .forEach(f => eval(fs.readFileSync(path.join(ROOT, key, f), 'utf8')));
  mods.sort((a, b) => a.n - b.n);
  out[key] = { name, mods };
}
// ENES: hand-written summaries + MCQs from index.html
const html = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
const line = html.split('\n').find(l => l.includes('var MINIQ_ENES'));
const EQ = eval('(' + line.slice(line.indexOf('{'), line.lastIndexOf('}') + 1) + ')');
const EN = require('./enes-notes.js');
const emods = [];
for (let n = 1; n <= 15; n++) {
  const [t, tb, en, bn] = EN[n];
  emods.push({ n, t, tb, sum: '<div class="pair"><div class="en"><span class="tag">English</span>' + en + '</div><div class="bn-box"><span class="tag">বাংলা</span>' + bn + '</div></div>', words: '',
    q: ((EQ['EN' + n] || {}).items || []).map(it => mcq(it, 'quiz')) });
}
if (EQ.ENA) emods.push({ n: 16, t: 'Study questions: True / False (from the official list)', tb: 'স্টাডি কোয়েশ্চন: সত্য / মিথ্যা', sum: '', words: '', q: EQ.ENA.items.map(it => mcq(it, 'quiz')) });
out.enes = { name: 'ENES 101 · English Language Studies', mods: emods };
fs.mkdirSync(path.join(ROOT, 'qn'), { recursive: true });
fs.writeFileSync(path.join(ROOT, 'qn', 'data.js'), 'var QN=' + JSON.stringify(out) + ';\n');
for (const k in out) console.log(k, out[k].mods.length, 'modules,', out[k].mods.reduce((a, m) => a + m.q.length, 0), 'MCQs');
