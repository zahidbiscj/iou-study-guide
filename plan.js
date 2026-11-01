/* Study planner for the home page: 1 Nov – 30 Nov, one subject per day. Self-contained; uses only localStorage. */
(function () {
  'use strict';
  var START = '2026-11-01', END = '2026-11-30', REVISION_DAYS = 4;
  var KEY = 'plan-done-v1';
  var SUBJ = {
    isgs: { name: 'ISGS 101', full: 'Islamic Studies 1', bn: 'ইসলামিক স্টাডিজ ১', icon: '☪️', color: '#2f7d5b' },
    fpec: { name: 'FPEC 101', full: 'Principles of Economics', bn: 'অর্থনীতির মূলনীতি', icon: '📈', color: '#b5651d' },
    enes: { name: 'ENES 101', full: 'English Language Studies', bn: 'ইংরেজি ভাষা শিক্ষা', icon: '✍️', color: '#3b6ea8' },
    bibs: { name: 'BIBS 101', full: 'Introduction to Business', bn: 'ব্যবসায়ের ভূমিকা', icon: '💼', color: '#8a4f9e' }
  };
  var ORDER = ['isgs', 'fpec', 'enes', 'bibs'];
  var ENES_T = ['Academic Study & Learning Styles', 'Developing Vocabulary', 'Skimming, Scanning & SQ3R', 'Annotating a Text', 'Note Taking', 'Note-Taking for Presentations', 'Mind Mapping', 'Outline Note Taking', 'Understanding Academic Arguments', 'Plagiarism & Paraphrasing', 'The Writing Process', 'Pre-writing', 'Pre-writing for an Assignment', 'Rough Draft, Topic Sentences & Thesis', 'Revising'];

  /* ---------- helpers ---------- */
  function $(s, r) { return (r || document).querySelector(s); }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function iso(d) { return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()); }
  function parse(s) { var p = s.split('-'); return new Date(+p[0], +p[1] - 1, +p[2]); }
  function addDays(d, n) { var x = new Date(d.getTime()); x.setDate(x.getDate() + n); return x; }
  function diffDays(a, b) { return Math.round((parse(a) - parse(b)) / 86400000); }
  function todayStr() {
    var m = /[?&]plan-today=(\d{4}-\d{2}-\d{2})/.exec(location.search);
    return m ? m[1] : iso(new Date());
  }
  function load() { try { var v = JSON.parse(localStorage.getItem(KEY) || '{}'); return v && typeof v === 'object' ? v : {}; } catch (e) { return {}; } }
  function save(v) { try { localStorage.setItem(KEY, JSON.stringify(v)); } catch (e) { /* storage unavailable */ } }
  function seenOf(k) { try { return JSON.parse(localStorage.getItem(k + '-mod-seen') || '{}') || {}; } catch (e) { return {}; } }
  function hrs(min) { var h = min / 60; return (Math.round(h * 10) / 10).toString().replace(/\.0$/, '') + ' h'; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;'); }
  var DAYN = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  function nice(s) { var d = parse(s); return DAYN[d.getDay()] + ' ' + d.getDate() + ' ' + MON[d.getMonth()]; }

  /* ---------- modules ---------- */
  function modules() {
    var out = { isgs: [], fpec: [], enes: [], bibs: [] };
    var reg = { isgs: window.ISGS_MODS, fpec: window.FPEC_MODS, bibs: window.BIBS_MODS };
    ['isgs', 'fpec', 'bibs'].forEach(function (k) {
      (reg[k] || []).forEach(function (m) {
        out[k].push({ id: k + '-' + m.n, sub: k, n: m.n, title: m.t, mins: Math.round(12 + 3.5 * (m.slides || 10)),
          href: '#' + k + '-mod-' + pad(m.n), slides: m.slides });
      });
    });
    ENES_T.forEach(function (t, i) { out.enes.push({ id: 'enes-' + (i + 1), sub: 'enes', n: i + 1, title: t, mins: 50, href: '#ecourse-E' + (i + 1) }); });
    return out;
  }

  /* ---------- schedule ---------- */
  function buildPlan(mods) {
    var total = 0, tm = {};
    ORDER.forEach(function (k) { tm[k] = mods[k].reduce(function (a, m) { return a + m.mins; }, 0); total += tm[k]; });
    var totalDays = diffDays(END, START) + 1, studyDays = totalDays - REVISION_DAYS;
    /* days per subject: largest remainder */
    var days = {}, used = 0, rem = [];
    ORDER.forEach(function (k) { var x = studyDays * tm[k] / total; days[k] = Math.max(1, Math.floor(x)); used += days[k]; rem.push({ k: k, r: x - Math.floor(x) }); });
    rem.sort(function (a, b) { return b.r - a.r; });
    for (var i = 0; used < studyDays; i = (i + 1) % rem.length) { days[rem[i].k]++; used++; }
    for (i = 0; used > studyDays; i = (i + 1) % ORDER.length) { if (days[ORDER[i]] > 1) { days[ORDER[i]]--; used--; } }
    /* spread subject-days evenly */
    var slots = [];
    ORDER.forEach(function (k, oi) { for (var j = 0; j < days[k]; j++) slots.push({ k: k, j: j, t: (j + 0.5) / days[k] + oi * 0.001 }); });
    slots.sort(function (a, b) { return a.t - b.t; });
    /* contiguous module chunks per subject, balanced by minutes */
    var chunks = {};
    ORDER.forEach(function (k) {
      var list = mods[k], d = days[k], sum = tm[k], acc = 0, c = [], cur = [], day = 0;
      list.forEach(function (m, idx) {
        var left = list.length - idx, daysLeft = d - day;
        cur.push(m); acc += m.mins;
        var target = sum * (day + 1) / d;
        var mustClose = left - 1 <= daysLeft - 1 && daysLeft > 1;   /* keep >=1 module for every remaining day */
        if (day < d - 1 && (acc >= target - m.mins / 2 || mustClose)) { c.push(cur); cur = []; day++; }
      });
      if (cur.length) c.push(cur);
      chunks[k] = c;
    });
    var plan = [], d0 = parse(START), idxBy = {};
    slots.forEach(function (s, n) {
      var list = (chunks[s.k][idxBy[s.k] = (idxBy[s.k] === undefined ? 0 : idxBy[s.k] + 1)]) || [];
      plan.push({ date: iso(addDays(d0, n)), sub: s.k, mods: list, rev: false, mins: list.reduce(function (a, m) { return a + m.mins; }, 0) });
    });
    ORDER.forEach(function (k, n) {
      plan.push({ date: iso(addDays(d0, studyDays + n)), sub: k, mods: [], rev: true, mins: 150 });
    });
    return plan;
  }

  /* ---------- render ---------- */
  var root, mods, plan, ALL;
  function css() {
    var s = document.createElement('style');
    s.textContent = '.plan{margin:34px 0 8px}.plan h2{font-size:22px;margin:0 0 4px;color:var(--brand)}.plan .sub{color:var(--muted);font-size:14px;margin-bottom:14px}' +
      '.pl-card{background:var(--paper);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:16px;margin:12px 0}' +
      '.pl-top{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}' +
      '.pl-stat{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:12px}.pl-stat b{display:block;font-size:24px;color:var(--brand)}.pl-stat span{font-size:12px;color:var(--muted)}' +
      '.pl-bar{height:10px;background:var(--line);border-radius:99px;overflow:hidden;margin:6px 0}.pl-bar i{display:block;height:100%;background:var(--brand-2,#2f7d5b);border-radius:99px}.pl-bar i.exp{background:transparent}' +
      '.pl-status{font-weight:700;padding:10px 14px;border-radius:12px;margin:10px 0}.pl-ok{background:#e3f4e8;color:#17623a}.pl-warn{background:#fff1da;color:#8a5200}.pl-bad{background:#fde5e3;color:#9b1f16}' +
      '[data-theme="dark"] .pl-ok{background:#16352a;color:#8fdcb0}[data-theme="dark"] .pl-warn{background:#3a2e14;color:#f0c670}[data-theme="dark"] .pl-bad{background:#3d1d1b;color:#f4a49c}' +
      '.pl-chip{display:inline-block;font-size:12px;font-weight:700;color:#fff;border-radius:99px;padding:2px 10px;white-space:nowrap}' +
      '.pl-mod{display:flex;gap:10px;align-items:flex-start;padding:8px 0;border-top:1px solid var(--line)}.pl-mod:first-child{border-top:0}.pl-mod input{margin-top:4px;width:18px;height:18px;flex:none}' +
      '.pl-mod a{color:var(--ink);text-decoration:none;font-weight:600}.pl-mod a:hover{color:var(--brand)}.pl-mod small{display:block;color:var(--muted);font-size:12px}.pl-mod.done a{text-decoration:line-through;color:var(--muted)}' +
      '.pl-days{display:grid;gap:6px}.pl-day{display:grid;grid-template-columns:92px 1fr auto;gap:10px;align-items:center;padding:8px 10px;border:1px solid var(--line);border-radius:10px;background:var(--paper);font-size:13px}' +
      '.pl-day.today{border:2px solid var(--brand-2,#2f7d5b)}.pl-day .dd{font-weight:700}.pl-day .ml{color:var(--muted);font-size:12px}.pl-day a{color:var(--brand)}' +
      '.pl-sp{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}.pl-sp div{font-size:13px}' +
      '.pl-chart{display:flex;align-items:flex-end;gap:2px;height:70px;margin-top:6px}.pl-chart div{flex:1;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;height:100%;position:relative}.pl-chart i{width:100%;border-radius:3px 3px 0 0;min-height:2px}.pl-chart .p{background:var(--line)}.pl-chart .d{background:var(--brand-2,#2f7d5b);position:absolute;bottom:0;left:15%;width:70%}' +
      '.pl-btn{font:inherit;font-size:12px;color:var(--muted);background:none;border:1px solid var(--line);border-radius:8px;padding:5px 10px;cursor:pointer}' +
      '@media(max-width:560px){.pl-day{grid-template-columns:78px 1fr}.pl-day .st{grid-column:1/-1}}';
    document.head.appendChild(s);
  }
  function doneMap() { return load(); }
  function isDone(m, dm) { return !!dm[m.id]; }
  function pctRead(m) { var s = seenOf(m.sub)[m.n]; return s && s.t ? Math.min(100, Math.round(s.v / s.t * 100)) : 0; }

  function modRow(m, dm, today) {
    var d = isDone(m, dm), p = pctRead(m), sb = SUBJ[m.sub];
    return '<label class="pl-mod' + (d ? ' done' : '') + '"><input type="checkbox" data-id="' + m.id + '"' + (d ? ' checked' : '') + '><div><a href="' + m.href + '">Module ' + m.n + ' · ' + esc(m.title) + '</a>' +
      '<small>' + (m.slides ? m.slides + ' slides · ' : '') + '≈ ' + hrs(m.mins) + (p ? ' · 📖 read ' + p + '%' : '') + (d ? ' · ✅ done ' + dm[m.id] : '') + '</small></div></label>';
  }
  function chip(k) { return '<span class="pl-chip" style="background:' + SUBJ[k].color + '">' + SUBJ[k].icon + ' ' + SUBJ[k].name + '</span>'; }
  function dayCard(day, dm, title, today) {
    if (!day) return '';
    var h = '<div class="pl-card"><b>' + title + '</b> · ' + nice(day.date) + ' ' + chip(day.sub) + ' <span class="ml">≈ ' + hrs(day.mins) + '</span>';
    if (day.rev) {
      h += '<p style="margin:10px 0 0">🔁 <b>Revision day · রিভিশন</b> — retake the 5-question module quizzes you got wrong, then read the <a href="#subject-' + day.sub + '">' + SUBJ[day.sub].name + ' midterm Q&amp;A</a> aloud once.</p>';
    } else {
      day.mods.forEach(function (m) { h += modRow(m, dm, today); });
    }
    return h + '</div>';
  }

  function render() {
    var dm = doneMap(), today = todayStr();
    var totalDays = plan.length;
    var dayNo = diffDays(today, START) + 1;
    var before = dayNo < 1, after = dayNo > totalDays;
    var allMods = ALL, doneN = allMods.filter(function (m) { return isDone(m, dm); }).length, totalN = allMods.length;
    var plannedThrough = function (dateStr) { var n = 0; plan.forEach(function (d) { if (d.date <= dateStr) n += d.mods.length; }); return n; };
    var yesterday = iso(addDays(parse(today), -1));
    var expStart = plannedThrough(yesterday), expEnd = plannedThrough(today);
    var doneMins = 0, totMins = 0; allMods.forEach(function (m) { totMins += m.mins; if (isDone(m, dm)) doneMins += m.mins; });
    var daysLeft = Math.max(0, diffDays(END, today) + 1);
    var studyLeft = plan.filter(function (d) { return d.date >= today && !d.rev; }).length;
    var remN = totalN - doneN;
    var status, cls;
    if (before) { status = '🗓 Plan starts on ' + nice(START) + ' (' + (-dayNo + 1) + ' day' + (dayNo < 0 ? 's' : '') + ' to go) · পরিকল্পনা শুরু হবে ' + nice(START); cls = 'pl-ok'; }
    else if (doneN >= totalN) { status = '🎉 All ' + totalN + ' modules done! Use the remaining days for revision and the midterm Q&A. · সব মডিউল শেষ!'; cls = 'pl-ok'; }
    else if (after) { status = '⏰ The 30 November target has passed — ' + remN + ' modules still open. Finish them as fast as you can. · লক্ষ্য তারিখ পেরিয়ে গেছে'; cls = 'pl-bad'; }
    else if (doneN >= expEnd) { status = '✅ Ahead of plan' + (doneN > expEnd ? ' by ' + (doneN - expEnd) + ' module(s)' : ' — today\'s work is done') + ' · পরিকল্পনার আগে/সঠিক'; cls = 'pl-ok'; }
    else if (doneN >= expStart) { status = '🟢 On track — finish today\'s modules (' + (expEnd - doneN) + ' to go). · ঠিক পথে'; cls = 'pl-ok'; }
    else {
      var behind = expStart - doneN;
      var perDay = studyLeft ? Math.ceil(remN / studyLeft * 10) / 10 : remN;
      status = (behind > 3 ? '🔴' : '🟠') + ' Behind by ' + behind + ' module(s). To finish by 30 Nov do about ' + perDay + ' modules/day (≈ ' + hrs(Math.round((totMins - doneMins) / Math.max(1, studyLeft))) + ' per day). · ' + behind + 'টি মডিউল পিছিয়ে';
      cls = behind > 3 ? 'pl-bad' : 'pl-warn';
    }
    var idx = plan.map(function (d) { return d.date; }).indexOf(today);
    var tDay = idx >= 0 ? plan[idx] : (before ? plan[0] : null), nDay = idx >= 0 ? plan[idx + 1] : (before ? plan[1] : null);
    var h = '<h2>🗓 My November study plan · আমার নভেম্বরের পড়ার পরিকল্পনা</h2><div class="sub">1 → 30 November · one subject a day · ' + totalN + ' modules + quizzes · tick a module when you finish it <b>and</b> its 5-question quiz · প্রতিদিন একটি বিষয়</div>';
    h += '<div class="pl-top">' +
      '<div class="pl-stat"><b>' + (before ? '—' : after ? 'Done' : 'Day ' + dayNo + '/' + totalDays) + '</b><span>Today · ' + nice(today) + '</span></div>' +
      '<div class="pl-stat"><b>' + doneN + '/' + totalN + '</b><span>Modules completed (' + Math.round(doneN / totalN * 100) + '%)</span></div>' +
      '<div class="pl-stat"><b>' + expEnd + '</b><span>Planned by end of today</span></div>' +
      '<div class="pl-stat"><b>' + daysLeft + '</b><span>Days left to 30 Nov</span></div>' +
      '<div class="pl-stat"><b>' + hrs(Math.max(0, totMins - doneMins)) + '</b><span>Study time still needed</span></div></div>';
    h += '<div class="pl-status ' + cls + '">' + status + '</div>';
    h += '<div class="pl-card"><div style="display:flex;justify-content:space-between;font-size:13px"><b>Overall progress</b><span>' + doneN + ' done · plan says ' + expEnd + '</span></div>' +
      '<div class="pl-bar" style="position:relative"><i style="width:' + Math.round(doneN / totalN * 100) + '%"></i></div>' +
      '<div class="pl-bar"><i style="width:' + Math.round(expEnd / totalN * 100) + '%;background:#c9b458"></i></div><div style="font-size:11px;color:var(--muted)">green = you · yellow = where the plan says you should be · সবুজ = তুমি, হলুদ = পরিকল্পনা</div></div>';
    h += dayCard(tDay, dm, before ? 'First day' : 'Today · আজ', today) + dayCard(nDay, dm, before ? 'Day 2' : 'Tomorrow · আগামীকাল', today);
    h += '<div class="pl-card"><b>By subject · বিষয় অনুযায়ী</b><div class="pl-sp" style="margin-top:8px">';
    ORDER.forEach(function (k) {
      var l = mods[k], dn = l.filter(function (m) { return isDone(m, dm); }).length, exp = 0;
      plan.forEach(function (d) { if (d.sub === k && d.date <= today) exp += d.mods.length; });
      var rd = l.reduce(function (a, m) { return a + pctRead(m); }, 0) / l.length;
      h += '<div>' + chip(k) + ' ' + dn + '/' + l.length + ' <span class="ml" style="color:var(--muted)">(plan: ' + exp + ')</span><div class="pl-bar"><i style="width:' + Math.round(dn / l.length * 100) + '%;background:' + SUBJ[k].color + '"></i></div>' +
        '<span style="color:var(--muted);font-size:12px">📖 avg. read ' + Math.round(rd) + '% · ' + SUBJ[k].full + '</span></div>';
    });
    h += '</div></div>';
    /* daily chart */
    var perDate = {}; Object.keys(dm).forEach(function (id) { perDate[dm[id]] = (perDate[dm[id]] || 0) + 1; });
    var mx = Math.max.apply(null, plan.map(function (d) { return Math.max(d.mods.length, perDate[d.date] || 0); }).concat([1]));
    h += '<div class="pl-card"><b>Daily progress · প্রতিদিনের অগ্রগতি</b> <span style="font-size:12px;color:var(--muted)">grey = planned, green = done</span><div class="pl-chart">';
    plan.forEach(function (d) {
      h += '<div title="' + nice(d.date) + ': planned ' + d.mods.length + ', done ' + (perDate[d.date] || 0) + '"><i class="p" style="height:' + Math.round(d.mods.length / mx * 100) + '%"></i><i class="d" style="height:' + Math.round((perDate[d.date] || 0) / mx * 100) + '%"></i></div>';
    });
    h += '</div></div>';
    /* timeline */
    h += '<details class="pl-card"' + (after ? ' open' : '') + '><summary style="cursor:pointer;font-weight:700">Full 30-day timetable · সম্পূর্ণ সময়সূচি</summary><div class="pl-days" style="margin-top:10px">';
    plan.forEach(function (d) {
      var dn = d.mods.filter(function (m) { return isDone(m, dm); }).length, st;
      if (d.rev) st = d.date < today ? '🔁 revision' : d.date === today ? '🟢 revision today' : '🔁 revision';
      else if (dn === d.mods.length) st = '✅ done';
      else if (d.date < today) st = '⚠️ ' + (d.mods.length - dn) + ' left';
      else if (d.date === today) st = '🟢 today ' + dn + '/' + d.mods.length;
      else st = '⏳ ' + dn + '/' + d.mods.length;
      h += '<div class="pl-day' + (d.date === today ? ' today' : '') + '"><span class="dd">' + nice(d.date) + '</span><span>' + chip(d.sub) + ' <span class="ml">' +
        (d.rev ? 'Revision + quiz retakes' : d.mods.map(function (m) { return '<a href="' + m.href + '">M' + m.n + '</a>'; }).join(' · ') + ' · ≈ ' + hrs(d.mins)) + '</span></span><span class="st">' + st + '</span></div>';
    });
    h += '</div></details>';
    h += '<div style="text-align:right"><button class="pl-btn" id="plReset" type="button">Reset my ticks</button></div>';
    root.innerHTML = h;
    var boxes = root.querySelectorAll('input[data-id]');
    Array.prototype.forEach.call(boxes, function (b) {
      b.addEventListener('change', function () {
        var m = load(); if (b.checked) m[b.getAttribute('data-id')] = todayStr(); else delete m[b.getAttribute('data-id')];
        save(m); render();
      });
    });
    var r = $('#plReset'); if (r) r.addEventListener('click', function () { if (confirm('Clear all ticks on the study plan?')) { save({}); render(); } });
  }

  function init() {
    root = $('#plan'); if (!root) return;
    mods = modules(); plan = buildPlan(mods);
    ALL = []; ORDER.forEach(function (k) { ALL = ALL.concat(mods[k]); });
    css(); render();
    window.addEventListener('hashchange', render);
    window.addEventListener('focus', render);
    window.PLAN_DEBUG = { plan: plan, mods: mods };
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
