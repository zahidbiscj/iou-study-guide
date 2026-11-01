/* Study planner for the home page: 1 Nov – 30 Nov, one subject per day. Self-contained; uses only localStorage. */
(function () {
  'use strict';
  var START = '2026-11-01', END = '2026-11-30', REVISION_DAYS = 4, REST = ['2026-11-12', '2026-11-13', '2026-11-14'];
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

  /* ---------- modules + automatic progress ---------- */
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
  function jget(k) { try { return JSON.parse(localStorage.getItem(k) || '{}') || {}; } catch (e) { return {}; } }
  function count(sel) { return document.querySelectorAll(sel).length; }
  /* progress of one module: reading (steps opened) and quiz (all questions answered) */
  function info(m, cache) {
    var read = 0, qDone = false, qScore = null;
    if (m.sub === 'enes') {
      var key = 'E' + m.n, seen = (cache.eseen[key] || []).length, total = count('#ecourse .cstep[data-lesson="' + key + '"]');
      read = total ? Math.min(1, seen / total) : 0;
      var need = count('#ecourse .cstep[data-lesson="' + key + '"] .miniquiz'), qs = cache.equiz[key] || {}, got = Object.keys(qs);
      qDone = need === 0 ? read >= 1 : got.length >= need;
      if (got.length) { var c = 0, t = 0; got.forEach(function (q) { c += qs[q].b || 0; t += qs[q].t || 0; }); qScore = { c: c, t: t }; }
    } else {
      var sn = (cache[m.sub].seen[m.n]) || {}, v = sn.v && sn.v.length ? sn.v.length : 0;
      read = sn.t ? Math.min(1, v / sn.t) : 0;
      var q = cache[m.sub].quiz[m.n] && cache[m.sub].quiz[m.n].main;
      qDone = !!q; if (q) qScore = { c: q.b || q.c, t: q.t };
    }
    var complete = read >= 1 && qDone;
    var frac = complete ? 1 : Math.min(0.99, 0.8 * read + (qDone ? 0.2 : 0));
    return { read: read, qDone: qDone, qScore: qScore, complete: complete, frac: frac, state: complete ? 'done' : (read > 0 || qDone ? 'part' : 'none') };
  }
  function makeCache() {
    return { eseen: jget('enes-seen'), equiz: jget('enes-quiz'),
      isgs: { seen: jget('isgs-mod-seen'), quiz: jget('isgs-quiz') }, fpec: { seen: jget('fpec-mod-seen'), quiz: jget('fpec-quiz') }, bibs: { seen: jget('bibs-mod-seen'), quiz: jget('bibs-quiz') } };
  }

  /* ---------- schedule: 2 subjects a day (one main, one lighter); Fri & Sat lightest ---------- */
  function buildPlan(mods) {
    var d0 = parse(START), totalDays = diffDays(END, START) + 1, studyDays = totalDays - REVISION_DAYS;
    var left = {}, total = 0, i, k;
    ORDER.forEach(function (x) { left[x] = mods[x].slice(); mods[x].forEach(function (m) { total += m.mins; }); });
    function rem(x) { return left[x].reduce(function (a, m) { return a + m.mins; }, 0); }
    function light(date) { var w = parse(date).getDay(); return w === 5 || w === 6; }   /* Fri, Sat */
    var weights = [], sumW = 0;
    var activeIdx = [];
    for (i = 0; i < studyDays; i++) { var dd0 = iso(addDays(d0, i)), w = REST.indexOf(dd0) >= 0 ? 0 : (light(dd0) ? 0.4 : 1); weights.push(w); sumW += w; if (w) activeIdx.push(i); }
    var plan = [], assigned = 0, cum = 0, prevPair = '';
    function pre(x, n) { var t = 0; for (var j = 0; j < n; j++) t += left[x][j].mins; return t; }
    for (i = 0; i < studyDays; i++) {
      var date = iso(addDays(d0, i)), lt = light(date);
      if (!weights[i]) { plan.push({ date: date, sub: 'isgs', parts: [], mods: [], rev: false, rest: true, light: false, mins: 0 }); continue; }
      cum += weights[i];
      var cap = total * weights[i] / sumW, debt = total * (cum - weights[i]) / sumW - assigned;
      var T = Math.max(0.3 * cap, cap + 0.35 * debt), last = i === activeIdx[activeIdx.length - 1], L = activeIdx.filter(function (x) { return x > i; }).length;
      var have = ORDER.filter(function (x) { return left[x].length; }), pick = null;
      if (last) {
        pick = { parts: have.map(function (x) { return [x, left[x].length]; }) };
      } else {
        var maxRem = Math.max.apply(null, have.map(rem).concat([1])), best = 1e18;
        have.forEach(function (x) {
          have.concat(have.length === 1 ? [null] : []).forEach(function (y) {
            if (y === x) return;
            for (var na = 1; na <= (lt ? 1 : 3) && na <= left[x].length; na++) {
              for (var nb = (y ? 1 : 0); nb <= (y ? (lt ? 1 : 2) : 0) && (!y || nb <= left[y].length); nb++) {
                if (y && na < nb) continue;
                var sx = pre(x, na), sy = y ? pre(y, nb) : 0, sum = sx + sy;
                if (y && sx < sy * 0.9 && na === nb) continue;          /* main subject should carry more */
                var cost = (lt ? 2.5 : 1) * Math.pow((sum - T) / 60, 2) + (sum - cap > 0 && lt ? 0 : 0) + 0.15 * Math.pow((maxRem - rem(x)) / 60, 2);
                if (x + y === prevPair || y + x === prevPair) cost += 4;
                var remAfter = ORDER.reduce(function (a, z) { return a + rem(z); }, 0) - sum, capAfter = total * (sumW - cum) / sumW;
                if (remAfter < 0.9 * capAfter) cost += 0.8 * Math.pow((0.9 * capAfter - remAfter) / 60, 2);   /* do not run out of work before the last day */
                /* every subject must still be finishable in the days that remain */
                ORDER.forEach(function (z) {
                  var r = left[z].length - (z === x ? na : 0) - (z === y ? nb : 0);
                  if (r > L * 1.6) cost += 1e6 * (r - L * 1.6);
                });
                if (cost < best) { best = cost; pick = { parts: y ? [[x, na], [y, nb]] : [[x, na]] }; }
              }
            }
          });
        });
      }
      var parts = [], flat = [];
      if (!pick) pick = { parts: [] };
      pick.parts.forEach(function (pp) {
        var mm = left[pp[0]].splice(0, pp[1]); parts.push({ sub: pp[0], mods: mm }); flat = flat.concat(mm);
      });
      var mins = flat.reduce(function (a, m) { return a + m.mins; }, 0); assigned += mins;
      prevPair = parts.map(function (x) { return x.sub; }).join('');
      plan.push({ date: date, sub: parts.length ? parts[0].sub : 'isgs', parts: parts, mods: flat, rev: false, light: lt, mins: mins });
    }
    var rev = [['isgs', 'fpec'], ['enes', 'bibs'], ['isgs', 'enes'], ['fpec', 'bibs']];
    rev.forEach(function (pair, n) {
      var date = iso(addDays(d0, studyDays + n)), lt = light(date);
      plan.push({ date: date, sub: pair[0], parts: pair.map(function (x) { return { sub: x, mods: [] }; }), mods: [], rev: true, light: lt, mins: lt ? 90 : 150 });
    });
    return plan;
  }

  /* ---------- render ---------- */
  var root, mods, plan, ALL, INFO = {};
  function css() {
    var st = document.createElement('style');
    st.textContent = '.plan{margin:34px 0 8px}.plan h2{font-size:22px;margin:0 0 4px;color:var(--brand)}.plan .sub{color:var(--muted);font-size:14px;margin-bottom:14px}' +
      '.pl-card{background:var(--paper);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:16px;margin:12px 0}' +
      '.pl-top{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px}' +
      '.pl-stat{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:12px}.pl-stat b{display:block;font-size:24px;color:var(--brand)}.pl-stat span{font-size:12px;color:var(--muted)}' +
      '.pl-bar{height:10px;background:var(--line);border-radius:99px;overflow:hidden;margin:6px 0}.pl-bar i{display:block;height:100%;background:var(--brand-2,#2f7d5b);border-radius:99px}' +
      '.pl-status{font-weight:700;padding:10px 14px;border-radius:12px;margin:10px 0}.pl-ok{background:#e3f4e8;color:#17623a}.pl-warn{background:#fff1da;color:#8a5200}.pl-bad{background:#fde5e3;color:#9b1f16}' +
      '[data-theme="dark"] .pl-ok{background:#16352a;color:#8fdcb0}[data-theme="dark"] .pl-warn{background:#3a2e14;color:#f0c670}[data-theme="dark"] .pl-bad{background:#3d1d1b;color:#f4a49c}' +
      '.pl-chip{display:inline-block;font-size:12px;font-weight:700;color:#fff;border-radius:99px;padding:2px 10px;white-space:nowrap}' +
      '.pl-st{display:inline-block;font-size:11px;font-weight:700;border-radius:99px;padding:2px 8px;white-space:nowrap}.pl-st.done{background:#d6f0de;color:#17623a}.pl-st.part{background:#fff1da;color:#8a5200}.pl-st.none{background:var(--line);color:var(--muted)}' +
      '.pl-mod{display:grid;grid-template-columns:1fr auto;gap:8px 12px;align-items:center;padding:9px 0;border-top:1px solid var(--line)}.pl-mod:first-child{border-top:0}' +
      '.pl-mod a.t{color:var(--ink);text-decoration:none;font-weight:600}.pl-mod a.t:hover{color:var(--brand)}.pl-mod small{display:block;color:var(--muted);font-size:12px}' +
      '.pl-go{font-size:12px;font-weight:700;color:var(--brand);text-decoration:none;border:1px solid var(--brand-2,#2f7d5b);border-radius:8px;padding:4px 10px;white-space:nowrap}' +
      '.pl-days{display:grid;gap:6px}.pl-day{display:grid;grid-template-columns:92px 1fr auto;gap:10px;align-items:center;padding:8px 10px;border:1px solid var(--line);border-radius:10px;background:var(--paper);font-size:13px}' +
      '.pl-day.today{border:2px solid var(--brand-2,#2f7d5b)}.pl-day .dd{font-weight:700}.pl-day .ml{color:var(--muted);font-size:12px}.pl-day a{color:var(--brand)}' +
      '.pl-sp{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}' +
      '.pl-chart{display:flex;align-items:flex-end;gap:2px;height:70px;margin-top:6px}.pl-chart div{flex:1;position:relative;height:100%}.pl-chart i{position:absolute;bottom:0;left:0;width:100%;border-radius:3px 3px 0 0;min-height:2px}.pl-chart .p{background:var(--line)}.pl-chart .d{background:var(--brand-2,#2f7d5b);left:20%;width:60%}' +
      '.pl-log{width:100%;border-collapse:collapse;font-size:13px;margin-top:8px}.pl-log td,.pl-log th{padding:5px 8px;border-top:1px solid var(--line);text-align:left}.pl-log th{color:var(--muted);font-weight:600;font-size:12px}' +
      '.plan details summary{cursor:pointer;font-weight:700}' +
      '@media print{body *{visibility:hidden}.plan,.plan *{visibility:visible}.plan{position:absolute;left:0;top:0;width:100%}.pl-go,#plName,#plTime{display:none}}@media(max-width:560px){.pl-day{grid-template-columns:78px 1fr}.pl-day .st{grid-column:1/-1}}';
    document.head.appendChild(st);
  }
  function chip(k) { return '<span class="pl-chip" style="background:' + SUBJ[k].color + '">' + SUBJ[k].icon + ' ' + SUBJ[k].name + '</span>'; }
  var LBL = { done: '✅ Completed', part: '🟡 In progress', none: '⚪ Not started' };
  function scoreTxt(i) { return i.qScore ? i.qScore.c + '/' + i.qScore.t : '—'; }
  function modRow(m) {
    var i = INFO[m.id];
    var det = (m.slides ? m.slides + ' slides · ' : '') + '≈ ' + hrs(m.mins) + ' · 📖 read ' + Math.round(i.read * 100) + '% · 📝 quiz ' + (i.qDone ? 'finished (' + scoreTxt(i) + ')' : 'not done');
    var go = i.complete ? 'Review' : (i.state === 'none' ? 'Start →' : 'Continue →');
    return '<div class="pl-mod"><div><a class="t" href="' + m.href + '">Module ' + m.n + ' · ' + esc(m.title) + '</a><small>' + det + '</small>' +
      '<div class="pl-bar"><i style="width:' + Math.round(i.frac * 100) + '%"></i></div></div><div style="text-align:right"><span class="pl-st ' + i.state + '">' + LBL[i.state] + '</span><br><a class="pl-go" href="' + m.href + '">' + go + '</a></div></div>';
  }
  function dayCard(day, title) {
    if (!day) return '';
    if (day.rest) return '<div class="pl-card"><b>' + title + '</b> · ' + nice(day.date) + ' <span class="pl-st none">😴 Rest day · বিশ্রামের দিন</span><p style="margin:8px 0 0;color:var(--muted)">No study today — recharge. · আজ পড়া নেই, বিশ্রাম নাও।</p></div>';
    var h = '<div class="pl-card"><b>' + title + '</b> · ' + nice(day.date) + (day.light ? ' <span class="pl-st none">light day · হালকা দিন</span>' : '') + ' <span style="color:var(--muted);font-size:12px">≈ ' + hrs(day.mins) + '</span>';
    day.parts.forEach(function (pt, pi) {
      h += '<div style="margin-top:10px">' + chip(pt.sub) + ' <span style="font-size:12px;color:var(--muted)">' + (day.rev ? 'revision' : (day.parts.length > 1 ? (pi === 0 ? 'main subject · প্রধান' : 'lighter subject · হালকা') : '')) + '</span>';
      if (day.rev) h += '<p style="margin:6px 0 0">🔁 Redo the module quizzes you missed, then read the <a href="#subject-' + pt.sub + '">' + SUBJ[pt.sub].name + ' midterm Q&amp;A</a> once.</p>';
      else pt.mods.forEach(function (m) { h += modRow(m); });
      h += '</div>';
    });
    return h + '</div>';
  }

  /* recompute everything from what the student actually did; stamp dates & daily log */
  function compute() {
    var cache = makeCache(); INFO = {};
    ALL.forEach(function (m) { INFO[m.id] = info(m, cache); });
    var S = 0, Q = 0;
    ['isgs', 'fpec', 'bibs'].forEach(function (k) {
      Object.keys(cache[k].seen).forEach(function (n) { S += (cache[k].seen[n].v || []).length; });
      Object.keys(cache[k].quiz).forEach(function (n) { if (cache[k].quiz[n].main) Q++; });
    });
    Object.keys(cache.eseen).forEach(function (k) { S += cache.eseen[k].length; });
    Object.keys(cache.equiz).forEach(function (k) { Q += Object.keys(cache.equiz[k]).length; });
    return { S: S, Q: Q };
  }
  function sync() {
    if (!ALL) return;
    var tot = compute(), today = todayStr(), lg = jget('plan-log-v2');
    lg.done = lg.done || {}; lg.days = lg.days || {};
    var dd = lg.days[today] = lg.days[today] || { s: 0, q: 0, m: 0 };
    if (lg.last) { dd.s += Math.max(0, tot.S - lg.last.s); dd.q += Math.max(0, tot.Q - lg.last.q); }
    lg.last = { s: tot.S, q: tot.Q };
    ALL.forEach(function (m) { if (INFO[m.id].complete && !lg.done[m.id]) { lg.done[m.id] = today; dd.m++; } });
    try { localStorage.setItem('plan-log-v2', JSON.stringify(lg)); } catch (e) { /* storage unavailable */ }
    return lg;
  }

  function render() {
    var lg = sync() || jget('plan-log-v2'), today = todayStr(), totalDays = plan.length;
    var dayNo = diffDays(today, START) + 1, before = dayNo < 1, after = dayNo > totalDays;
    var totalN = ALL.length, doneN = 0, qN = 0, eq = 0, totMins = 0, doneMins = 0;
    ALL.forEach(function (m) { var i = INFO[m.id]; if (i.complete) doneN++; if (i.qDone && i.read > 0) qN++; eq += i.frac; totMins += m.mins; doneMins += m.mins * i.frac; });
    var overall = Math.round(doneMins / totMins * 100);
    function plannedThrough(ds) { var n = 0; plan.forEach(function (d) { if (d.date <= ds) n += d.mods.length; }); return n; }
    var expStart = plannedThrough(iso(addDays(parse(today), -1))), expEnd = plannedThrough(today);
    var daysLeft = Math.max(0, diffDays(END, today) + 1), studyLeft = plan.filter(function (d) { return d.date >= today && !d.rev && !d.rest; }).length;
    var remMins = Math.max(0, totMins - doneMins), r1 = function (x) { return Math.round(x * 10) / 10; };
    var status, cls;
    if (before) { status = '🗓 Plan starts on ' + nice(START) + '. Open any module to begin — progress is recorded automatically. · ' + nice(START) + ' থেকে শুরু'; cls = 'pl-ok'; }
    else if (doneN >= totalN) { status = '🎉 All ' + totalN + ' modules and quizzes finished! Use the last days for revision and the midterm Q&A.'; cls = 'pl-ok'; }
    else if (after) { status = '⏰ The 30 November target has passed — ' + (totalN - doneN) + ' modules still open.'; cls = 'pl-bad'; }
    else if (eq >= expEnd) { status = '✅ Ahead of plan' + (eq - expEnd >= 0.5 ? ' by ' + r1(eq - expEnd) + ' module(s)' : ' — today\'s target is met') + ' · পরিকল্পনার আগে'; cls = 'pl-ok'; }
    else if (eq >= expStart) { status = '🟢 On track — finish today\'s modules (' + r1(expEnd - eq) + ' module(s) to go). · ঠিক পথে'; cls = 'pl-ok'; }
    else {
      var behind = r1(expStart - eq), perDay = studyLeft ? r1((totalN - eq) / studyLeft) : 0;
      status = (behind > 3 ? '🔴' : '🟠') + ' Behind by ' + behind + ' module(s). To finish by 30 Nov: about ' + perDay + ' modules/day (≈ ' + hrs(remMins / Math.max(1, studyLeft)) + ' a day). · ' + behind + 'টি মডিউল পিছিয়ে';
      cls = behind > 3 ? 'pl-bad' : 'pl-warn';
    }
    var forecast = '';
    if (!before && !after && eq > 0 && doneN < totalN) {
      var pace = eq / Math.max(1, dayNo), need = Math.ceil((totalN - eq) / pace), fin = addDays(parse(today), need), late = diffDays(iso(fin), END);
      forecast = '📈 At your pace (' + r1(pace) + ' modules/day) you will finish about <b>' + nice(iso(fin)) + '</b> — ' + (late <= 0 ? (-late) + ' day(s) before the target ✅' : late + ' day(s) after the target ⚠️') + '.';
    } else if (!before && !after && eq === 0) forecast = '📈 No progress recorded yet — open today\'s first module below.';
    var idx = plan.map(function (d) { return d.date; }).indexOf(today);
    var tDay = idx >= 0 ? plan[idx] : (before ? plan[0] : null), nDay = idx >= 0 ? plan[idx + 1] : (before ? plan[1] : null);

    var h = '<h2>📊 Student Progress Report · শিক্ষার্থীর অগ্রগতি রিপোর্ট</h2><div class="sub">Updates by itself as you study — no ticking. A module counts as <b>completed</b> only when you have opened <b>every step</b> and <b>finished its 5-question quiz</b>. · নিজে নিজেই আপডেট হয়; মডিউল শেষ = সব ধাপ + কুইজ শেষ।</div>';
    h += '<!--PL:REST-->' + '<div class="pl-top">' +
      '<div class="pl-stat"><b>' + overall + '%</b><span>Overall progress</span></div>' +
      '<div class="pl-stat"><b>' + doneN + '/' + totalN + '</b><span>Modules completed</span></div>' +
      '<div class="pl-stat"><b>' + qN + '/' + totalN + '</b><span>Quizzes finished</span></div>' +
      '<div class="pl-stat"><b>' + (before ? '—' : after ? 'Ended' : 'Day ' + dayNo + '/' + totalDays) + '</b><span>' + nice(today) + ' · ' + daysLeft + ' days left</span></div>' +
      '<div class="pl-stat"><b>' + hrs(remMins) + '</b><span>Study time still needed</span></div></div>';
    h += '<div class="pl-status ' + cls + '">' + status + '</div>' + (forecast ? '<div style="font-size:13px;margin:0 2px 8px">' + forecast + '</div>' : '');
    /* motivation: countdown, today's goal ring, streak, badges */
    var dayz = lg.days || {}, act = function (d) { return dayz[d] && (dayz[d].s || dayz[d].q || dayz[d].m); };
    var streak = 0, cd = act(today) ? today : iso(addDays(parse(today), -1));
    while (act(cd)) { streak++; cd = iso(addDays(parse(cd), -1)); }
    var best = 0, run = 0, prevD = null;
    Object.keys(dayz).sort().forEach(function (d) { if (!act(d)) return; run = prevD && diffDays(d, prevD) === 1 ? run + 1 : 1; best = Math.max(best, run); prevD = d; });
    var tmods = tDay && !tDay.rev && !tDay.rest ? tDay.mods : [], gF = tmods.length ? tmods.reduce(function (a, m) { return a + INFO[m.id].frac; }, 0) / tmods.length : 0;
    var perfect = ALL.some(function (m) { var q = INFO[m.id].qScore; return q && q.c === q.t && q.t > 0; });
    var msg;
    if (before) msg = '🚀 Day 1 is ' + nice(START) + '. Start early — every module you finish now is a day saved later!';
    else if (doneN >= totalN) msg = '🏆 You did it! Every module and quiz is finished. Now polish with the midterm Q&A.';
    else if (after) msg = '⏰ Time is up — finish what is left today.';
    else if (tDay && tDay.rest) msg = '😴 Rest day — enjoy it. The plan restarts on the next study day.';
    else if (cls === 'pl-bad' || cls === 'pl-warn') msg = '🔥 You are slipping behind — ' + daysLeft + ' days left! Finish today\'s goal and add one extra module to catch up.';
    else if (gF >= 1) msg = '🎉 Today\'s goal is complete! Start tomorrow\'s first module to get ahead.';
    else if (streak >= 3) msg = '💪 ' + streak + '-day streak! Don\'t break the chain — study today.';
    else msg = '🎯 Finish today\'s goal and you stay on track. Small steps every day win the month.';
    var urgent = !before && !after && doneN < totalN && daysLeft <= 7;
    var ring = 'background:conic-gradient(var(--brand-2,#2f7d5b) ' + Math.round(gF * 360) + 'deg,var(--line) 0)';
    h += '<div class="pl-card" style="display:grid;grid-template-columns:auto 1fr;gap:14px;align-items:center"><div style="width:84px;height:84px;border-radius:50%;' + ring + ';display:grid;place-items:center"><div style="width:62px;height:62px;border-radius:50%;background:var(--paper);display:grid;place-items:center;font-weight:800;color:var(--brand)">' + Math.round(gF * 100) + '%</div></div>' +
      '<div><b>🎯 Today\'s goal · আজকের লক্ষ্য</b><div style="font-size:14px;margin-top:4px">' + msg + '</div><div style="font-size:13px;margin-top:6px;color:var(--muted)">🔥 Streak: <b>' + streak + '</b> day' + (streak === 1 ? '' : 's') + ' · best ' + best + '</div></div></div>';
    if (!before && !after) h += '<div class="pl-status ' + (urgent ? 'pl-bad' : 'pl-ok') + '" style="text-align:center">⏳ ' + daysLeft + ' day' + (daysLeft === 1 ? '' : 's') + ' left to 30 November · ' + (totalN - doneN) + ' module' + (totalN - doneN === 1 ? '' : 's') + ' to go' + (urgent ? ' — final sprint! 🏁' : '') + '</div>';
    var BG = [['🌱', 'First module', doneN >= 1], ['📘', '5 modules', doneN >= 5], ['⭐', '25% done', overall >= 25], ['🔥', '50% done', overall >= 50], ['🚀', '75% done', overall >= 75], ['🏆', 'All 54 done', doneN >= totalN],
      ['🔥', '3-day streak', best >= 3], ['⚡', '7-day streak', best >= 7], ['💯', 'Perfect quiz', perfect], ['📚', 'Subject master', ORDER.some(function (k) { return mods[k].every(function (m) { return INFO[m.id].complete; }); })]];
    h += '<div class="pl-card"><b>🏅 Achievements · অর্জন</b> <span style="font-size:12px;color:var(--muted)">' + BG.filter(function (b) { return b[2]; }).length + '/' + BG.length + ' unlocked</span><div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:8px">' +
      BG.map(function (b) { return '<span class="pl-st ' + (b[2] ? 'done' : 'none') + '" style="font-size:12px;padding:5px 10px;' + (b[2] ? '' : 'opacity:.55;filter:grayscale(1)') + '">' + b[0] + ' ' + b[1] + '</span>'; }).join('') + '</div></div>';
    h += '<div class="pl-card"><div style="display:flex;justify-content:space-between;font-size:13px"><b>You vs the plan</b><span>you ' + r1(eq) + ' · plan ' + expEnd + ' of ' + totalN + ' modules</span></div>' +
      '<div class="pl-bar"><i style="width:' + Math.round(eq / totalN * 100) + '%"></i></div><div class="pl-bar"><i style="width:' + Math.round(expEnd / totalN * 100) + '%;background:#c9b458"></i></div>' +
      '<div style="font-size:11px;color:var(--muted)">green = you · yellow = where the plan says you should be today · সবুজ = তুমি, হলুদ = পরিকল্পনা</div></div>';
    h += '<!--PL:TOP-->' + '<div class="pl-card" style="border-color:var(--brand-2,#2f7d5b);background:var(--paper)"><b>👇 এখান থেকে শুরু · Start here</b><div style="font-size:14px;margin-top:4px">আজ ও আগামীকালের পড়া নিচে। মডিউলের নাম বা <b>Start / Continue →</b> বোতামে ক্লিক করো। মডিউলের সব ধাপ ও ৫-প্রশ্নের কুইজ শেষ হলে অগ্রগতি নিজে থেকে আপডেট হবে।<br><span style="color:var(--muted)">Click a module name or the Start / Continue → button. Finish every step and its 5-question quiz — your progress updates by itself.</span></div></div>' + dayCard(tDay, before ? 'First day' : 'Today · আজ') + dayCard(nDay, before ? 'Day 2' : 'Tomorrow · আগামীকাল');
    /* by subject */
    h += '<!--PL:SUBJ-->' + '<div class="pl-card"><b>By subject · বিষয় অনুযায়ী</b> <span style="font-size:12px;color:var(--muted)">(tap a subject to see every module)</span><div class="pl-sp" style="margin-top:8px">';
    ORDER.forEach(function (k) {
      var l = mods[k], dn = 0, f = 0, ex = 0, mm = 0, dm = 0;
      l.forEach(function (m) { var i = INFO[m.id]; if (i.complete) dn++; f += i.frac; mm += m.mins; dm += m.mins * i.frac; });
      plan.forEach(function (d) { if (d.date <= today) d.parts.forEach(function (pt) { if (pt.sub === k) ex += pt.mods.length; }); });
      h += '<div>' + chip(k) + ' <b>' + Math.round(dm / mm * 100) + '%</b> · ' + dn + '/' + l.length + ' <span style="color:var(--muted);font-size:12px">(plan: ' + ex + ')</span><div class="pl-bar"><i style="width:' + Math.round(dm / mm * 100) + '%;background:' + SUBJ[k].color + '"></i></div><span style="color:var(--muted);font-size:12px">' + SUBJ[k].full + '</span></div>';
    });
    h += '</div></div>';
    ORDER.forEach(function (k) {
      h += '<details class="pl-card"><summary>' + SUBJ[k].icon + ' ' + SUBJ[k].name + ' — all modules · সব মডিউল</summary>';
      mods[k].forEach(function (m) { h += modRow(m); });
      h += '</details>';
    });
    /* daily log */
    var days = lg.days || {}, doneBy = {};
    Object.keys(lg.done || {}).forEach(function (id) { doneBy[lg.done[id]] = (doneBy[lg.done[id]] || 0) + 1; });
    var mx = Math.max.apply(null, plan.map(function (d) { return Math.max(d.mods.length, doneBy[d.date] || 0); }).concat([1]));
    h += '<!--PL:CHART-->' + '<div class="pl-card"><b>Daily progress · প্রতিদিনের অগ্রগতি</b> <span style="font-size:12px;color:var(--muted)">grey = planned modules, green = modules you completed</span><div class="pl-chart">';
    plan.forEach(function (d) { h += '<div title="' + nice(d.date) + ': planned ' + d.mods.length + ', completed ' + (doneBy[d.date] || 0) + '"><i class="p" style="height:' + Math.round(d.mods.length / mx * 100) + '%"></i><i class="d" style="height:' + Math.round((doneBy[d.date] || 0) / mx * 100) + '%"></i></div>'; });
    h += '</div>';
    var ds = Object.keys(days).filter(function (d) { return days[d].s || days[d].q || days[d].m; }).sort().reverse();
    h += ds.length ? '<table class="pl-log"><tr><th>Date</th><th>Steps studied</th><th>Quizzes finished</th><th>Modules completed</th></tr>' + ds.slice(0, 14).map(function (d) { return '<tr><td>' + nice(d) + '</td><td>' + days[d].s + '</td><td>' + days[d].q + '</td><td>' + days[d].m + '</td></tr>'; }).join('') + '</table>' :
      '<p style="color:var(--muted);font-size:13px;margin:8px 0 0">Your daily activity will appear here after you study.</p>';
    h += '</div>';
    /* timetable */
    h += '<!--PL:REST-->' + '<details class="pl-card"' + (after ? ' open' : '') + '><summary>Full 30-day timetable · সম্পূর্ণ সময়সূচি</summary><div class="pl-days" style="margin-top:10px">';
    plan.forEach(function (d) {
      var dn = d.mods.filter(function (m) { return INFO[m.id].complete; }).length, st;
      if (d.rest) st = '😴 rest';
      else if (d.rev) st = d.date === today ? '🟢 revision today' : '🔁 revision';
      else if (dn === d.mods.length) st = '✅ done';
      else if (d.date < today) st = '⚠️ ' + (d.mods.length - dn) + ' left';
      else if (d.date === today) st = '🟢 today ' + dn + '/' + d.mods.length;
      else st = '⏳ ' + dn + '/' + d.mods.length;
      h += '<div class="pl-day' + (d.date === today ? ' today' : '') + '"><span class="dd">' + nice(d.date) + '</span><span>' + chip(d.sub) + ' <span class="ml">' +
        (d.rest ? 'Rest day · বিশ্রাম' : d.rev ? 'Revision + quiz retakes' : d.mods.map(function (m) { return '<a href="' + m.href + '">M' + m.n + '</a>'; }).join(' · ') + ' · ≈ ' + hrs(d.mins)) + '</span></span><span class="st">' + st + '</span></div>';
    });
    h += '</div></details>';
    var nm = ''; try { nm = localStorage.getItem('plan-name') || ''; } catch (e) { /* storage unavailable */ }
    var rt = ''; try { rt = localStorage.getItem('plan-remind-time') || '20:00'; } catch (e) { rt = '20:00'; }
    h += '<div class="pl-card"><b>📤 Share, print & remind · শেয়ার, প্রিন্ট ও রিমাইন্ডার</b>' +
      '<div style="margin-top:8px;display:flex;flex-wrap:wrap;gap:8px;align-items:center"><input id="plName" placeholder="Your name · তোমার নাম" value="' + esc(nm) + '" style="padding:7px 10px;border:1px solid var(--line);border-radius:8px;background:var(--paper);color:var(--ink);font:inherit;min-width:180px">' +
      '<button class="pl-go" id="plCard" type="button">🖼 Download progress card</button><button class="pl-go" id="plPrint" type="button">🖨 Print / Save PDF</button><button class="pl-go" id="plWa" type="button">💬 Share on WhatsApp</button></div>' +
      '<div style="margin-top:10px;display:flex;flex-wrap:wrap;gap:8px;align-items:center"><span style="font-size:13px">⏰ Daily reminder at</span><input id="plTime" type="time" value="' + rt + '" style="padding:6px 8px;border:1px solid var(--line);border-radius:8px;background:var(--paper);color:var(--ink);font:inherit">' +
      '<button class="pl-go" id="plIcs" type="button">📅 Add to phone calendar (.ics)</button><button class="pl-go" id="plNote" type="button">🔔 Notify me when I open the site</button></div>' +
      '<p style="font-size:12px;color:var(--muted);margin:8px 0 0">The calendar file adds one reminder per study day (1–30 Nov, skipping rest days) with that day\'s subjects and modules — import it into Google/Apple Calendar and your phone will remind you. The browser notification works only when the site is open. · ক্যালেন্ডার ফাইল ইমপোর্ট করলে প্রতিদিন ফোনে রিমাইন্ডার আসবে।</p></div>';
    h += '<p style="font-size:12px;color:var(--muted)">ℹ️ The report is saved in <b>this browser</b> and is private to whoever is using it — each student sees their own progress. Opening the site on another phone or computer starts a fresh report. · রিপোর্টটি এই ব্রাউজারে সংরক্ষিত।</p>';
    var seg = h.split(/<!--PL:(TOP|CHART|SUBJ|REST)-->/), out = { TOP: seg[0], CHART: '', SUBJ: '', REST: '' };
    for (var q = 1; q < seg.length; q += 2) out[seg[q]] += seg[q + 1];
    $('#plTop', root).innerHTML = out.TOP; $('#plChart', root).innerHTML = out.CHART;
    $('#plSubj', root).innerHTML = out.SUBJ; $('#plRest', root).innerHTML = out.REST;
    var nameEl = $('#plName', root), who = function () { return (nameEl && nameEl.value.trim()) || 'Student'; };
    var summary = function () { return '📊 ' + who() + ' — IOU study progress\n' + overall + '% overall · ' + doneN + '/' + totalN + ' modules + quizzes done\n🔥 streak ' + streak + ' day(s) · ' + daysLeft + ' days left to 30 Nov\n' + (eq >= expEnd ? '✅ on/ahead of plan' : '⚠️ behind plan') + '\n' + location.origin + location.pathname; };
    nameEl.addEventListener('change', function () { try { localStorage.setItem('plan-name', nameEl.value.trim()); } catch (e) { /* storage unavailable */ } });
    $('#plWa', root).addEventListener('click', function () { window.open('https://wa.me/?text=' + encodeURIComponent(summary()), '_blank'); });
    $('#plPrint', root).addEventListener('click', function () { var ds = document.querySelectorAll('.plan details'); Array.prototype.forEach.call(ds, function (d) { d.open = true; }); window.print(); });
    $('#plCard', root).addEventListener('click', function () {
      var c = document.createElement('canvas'); c.width = 900; c.height = 500; var g = c.getContext('2d');
      g.fillStyle = '#10372a'; g.fillRect(0, 0, 900, 500); g.fillStyle = '#e9c46a'; g.fillRect(0, 0, 900, 8);
      g.fillStyle = '#fff'; g.font = 'bold 40px sans-serif'; g.fillText(who(), 50, 90); g.font = '22px sans-serif'; g.fillStyle = '#bfe3d0'; g.fillText('IOU Study Guide · Student Progress Card · ' + nice(today), 50, 130);
      g.fillStyle = '#e9c46a'; g.font = 'bold 120px sans-serif'; g.fillText(overall + '%', 50, 280); g.fillStyle = '#fff'; g.font = '28px sans-serif'; g.fillText('overall progress', 60, 320);
      g.fillStyle = '#2a5a47'; g.fillRect(50, 345, 800, 26); g.fillStyle = '#6fd39a'; g.fillRect(50, 345, 8 * overall, 26);
      g.fillStyle = '#fff'; g.font = '26px sans-serif'; g.fillText('✔ ' + doneN + '/' + totalN + ' modules + quizzes     🔥 ' + streak + '-day streak     ⏳ ' + daysLeft + ' days left', 50, 425);
      g.fillStyle = '#bfe3d0'; g.font = '20px sans-serif'; g.fillText(eq >= expEnd ? 'On / ahead of plan' : 'Catching up — keep going!', 50, 465);
      var a = document.createElement('a'); a.download = 'progress-card.png'; a.href = c.toDataURL('image/png'); a.click();
    });
    $('#plIcs', root).addEventListener('click', function () {
      var t = $('#plTime', root).value || '20:00'; try { localStorage.setItem('plan-remind-time', t); } catch (e) { /* storage unavailable */ }
      var hh = t.replace(':', '') + '00', E = function (x) { return String(x).replace(/\\/g, '\\\\').replace(/;/g, '\;').replace(/,/g, '\\,').replace(/\n/g, '\\n'); };
      var L = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//IOU Study Guide//EN'];
      plan.forEach(function (d) {
        if (d.rest) return;
        var desc = d.parts.map(function (pt) { return SUBJ[pt.sub].name + (d.rev ? ': revision + quiz retakes' : ': ' + pt.mods.map(function (m) { return 'M' + m.n + ' ' + m.title; }).join('; ')); }).join('\n') + '\nOpen: ' + location.origin + location.pathname;
        L.push('BEGIN:VEVENT', 'UID:' + d.date + '@iou-study-guide', 'DTSTAMP:20261101T000000Z', 'DTSTART:' + d.date.replace(/-/g, '') + 'T' + hh, 'DURATION:PT30M',
          'SUMMARY:' + E('📚 Study: ' + d.parts.map(function (pt) { return SUBJ[pt.sub].name; }).join(' + ')), 'DESCRIPTION:' + E(desc), 'BEGIN:VALARM', 'ACTION:DISPLAY', 'DESCRIPTION:Study time', 'TRIGGER:PT0M', 'END:VALARM', 'END:VEVENT');
      });
      L.push('END:VCALENDAR');
      var a = document.createElement('a'); a.download = 'study-plan-reminders.ics'; a.href = URL.createObjectURL(new Blob([L.join('\r\n')], { type: 'text/calendar' })); a.click();
    });
    $('#plNote', root).addEventListener('click', function () {
      if (!('Notification' in window)) { alert('This browser does not support notifications.'); return; }
      Notification.requestPermission().then(function (r) { if (r === 'granted') { try { localStorage.setItem('plan-notify', '1'); } catch (e) { /* storage unavailable */ } alert('Done ✅ — you will get a reminder each day you open the site.'); } });
    });
    try {
      if (localStorage.getItem('plan-notify') === '1' && window.Notification && Notification.permission === 'granted' && localStorage.getItem('plan-notified') !== today && tDay && !tDay.rest) {
        localStorage.setItem('plan-notified', today);
        new Notification('📚 Today: ' + tDay.parts.map(function (pt) { return SUBJ[pt.sub].name; }).join(' + '), { body: (tDay.rev ? 'Revision day' : tDay.mods.length + ' module(s), about ' + hrs(tDay.mins)) + ' · ' + daysLeft + ' days left' });
      }
    } catch (e) { /* notifications unavailable */ }
  }

  function init() {
    root = $('#plan'); if (!root) return;
    mods = modules(); plan = buildPlan(mods);
    ALL = []; ORDER.forEach(function (k) { ALL = ALL.concat(mods[k]); });
    css(); render();
    window.planSync = function () { sync(); };
    window.addEventListener('hashchange', render);
    window.addEventListener('focus', render);
    window.PLAN_DEBUG = { plan: plan, mods: mods, info: function () { return INFO; } };
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
