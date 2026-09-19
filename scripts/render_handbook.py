#!/usr/bin/env python3
"""
render_handbook.py — Render sss_database.json as a browsable, game-style Hero Handbook.

The JSON is built for machines; this renders the same data the way the in-game
Hero Handbook presents it: one card per hero with role badge, attack type, stat
ratings, skill panels with their per-tier names/descriptions, and a readable
augment-cost table using real item names.

Usage:
    python3 scripts/render_handbook.py [--out docs/heroes.html]

Output is a single self-contained HTML file (no network calls, no build step).
"""
import json, os, sys, collections

EX = os.path.join(os.path.dirname(__file__), '..', 'extracted')
ROLE_COLOR = {
    'Ranger': '#4ade80', 'Striker': '#f87171', 'Protector': '#60a5fa',
    'Destroyer': '#fbbf24', 'Rover': '#a78bfa', 'Flagship': '#f472b6',
}
ROLE_ORDER = ['Ranger', 'Striker', 'Protector', 'Destroyer', 'Rover', 'Flagship']


def main():
    out = 'docs/heroes.html'
    if '--out' in sys.argv:
        out = sys.argv[sys.argv.index('--out') + 1]
    out_path = os.path.join(os.path.dirname(__file__), '..', out)

    with open(os.path.join(EX, 'sss_database.json'), encoding='utf-8') as f:
        db = json.load(f)

    counts = collections.Counter(h['role'] for h in db)
    gen = collections.Counter(h['generation'] for h in db)

    # slim the payload: assets are not rendered prominently, keep the rest intact
    payload = []
    for h in db:
        d = {k: v for k, v in h.items() if k != 'assets'}
        d['assets'] = h['assets']
        payload.append(d)

    data_js = json.dumps(payload, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

    html = TEMPLATE.replace('/*__DATA__*/null', data_js)
    html = html.replace('__N__', str(len(db)))
    html = html.replace('__GEN__', f"{gen['latest']} new-gen / {gen['old']} old-gen")
    chips = ''.join(
        f'<button class="chip" data-role="{r}" style="--c:{ROLE_COLOR[r]}">'
        f'{r} <span class="n">{counts[r]}</span></button>'
        for r in ROLE_ORDER
    )
    html = html.replace('__CHIPS__', chips)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'{len(db)} heroes -> {out_path} ({os.path.getsize(out_path)/1e6:.2f} MB)')


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Galaxy Legends — SSS Hero Handbook</title>
<style>
:root{
  --bg:#0f1115; --panel:#171a21; --panel2:#1d2129; --line:#272c37;
  --tx:#e6e8ee; --dim:#98a1b3; --dim2:#6b7488; --acc:#7dd3fc;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);
  font:14px/1.5 ui-sans-serif,system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px 80px}
header{position:sticky;top:0;z-index:20;background:rgba(15,17,21,.94);
  backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.hd{max-width:1180px;margin:0 auto;padding:14px 20px}
h1{margin:0;font-size:17px;letter-spacing:.2px}
h1 small{color:var(--dim);font-weight:400;font-size:12px;margin-left:8px}
.toolbar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-top:10px}
input[type=search]{flex:1;min-width:200px;background:var(--panel);border:1px solid var(--line);
  color:var(--tx);border-radius:8px;padding:8px 12px;font-size:13px;outline:none}
input[type=search]:focus{border-color:var(--acc)}
.chip{background:var(--panel);border:1px solid var(--line);color:var(--dim);
  border-radius:999px;padding:6px 13px;font-size:12px;cursor:pointer;transition:.15s}
.chip .n{color:var(--dim2);margin-left:4px;font-size:11px}
.chip:hover{border-color:var(--c);color:var(--tx)}
.chip.on{background:color-mix(in srgb,var(--c) 18%,transparent);border-color:var(--c);color:var(--c)}
.chip.on .n{color:var(--c)}
.count{color:var(--dim2);font-size:12px;padding:6px 2px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;
  margin:14px 0;overflow:hidden}
.ch{display:flex;align-items:center;gap:12px;padding:13px 16px;cursor:pointer;
  border-left:3px solid var(--c,var(--line))}
.ch:hover{background:var(--panel2)}
.badge{font-size:11px;font-weight:600;padding:3px 9px;border-radius:999px;
  background:color-mix(in srgb,var(--c) 20%,transparent);color:var(--c);
  border:1px solid color-mix(in srgb,var(--c) 40%,transparent);white-space:nowrap}
.nm{font-size:15px;font-weight:600}
.cn{color:var(--dim);font-size:12.5px}
.iid{color:var(--dim2);font-size:11px;font-variant-numeric:tabular-nums}
.spacer{flex:1}
.rt{display:flex;gap:12px;color:var(--dim);font-size:11.5px}
.rt b{color:var(--tx);font-weight:600}
.tog{color:var(--dim2);font-size:11px;white-space:nowrap}
.body{display:none;border-top:1px solid var(--line);padding:6px 16px 16px}
.card.open .body{display:block}
.card.open .tog::after{content:" ▲"}
.tog::after{content:" ▼"}
h4{margin:16px 0 8px;font-size:11px;letter-spacing:.9px;text-transform:uppercase;color:var(--dim2)}
.skill{background:var(--panel2);border:1px solid var(--line);border-radius:9px;
  padding:11px 13px;margin-bottom:9px}
.skill .sh{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap}
.slot{color:var(--dim2);font-size:11px;font-variant-numeric:tabular-nums}
.sn{font-weight:600;font-size:13.5px}
.unl{color:var(--dim);font-size:11.5px}
.tier{border-top:1px dashed var(--line);margin-top:9px;padding-top:9px}
.tier:first-of-type{border-top:0;margin-top:7px;padding-top:0}
.th{display:flex;gap:9px;align-items:baseline;flex-wrap:wrap}
.tl{font-size:11px;font-weight:700;color:var(--acc);min-width:16px}
.tat{font-size:11px;color:var(--dim);background:#0f1115;border:1px solid var(--line);
  border-radius:5px;padding:1px 7px;font-variant-numeric:tabular-nums}
.tnm{font-size:12.5px;color:#cbd2e0}
.td{color:var(--dim);font-size:12.5px;margin-top:4px;white-space:pre-wrap}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th,td{text-align:left;padding:6px 10px;border-bottom:1px solid var(--line)}
th{color:var(--dim2);font-size:10.5px;text-transform:uppercase;letter-spacing:.6px;
  font-weight:600;position:sticky;top:0;background:var(--panel)}
td.lv{color:var(--tx);font-weight:600;font-variant-numeric:tabular-nums;white-space:nowrap}
td.mn{color:#fbbf24;font-variant-numeric:tabular-nums;white-space:nowrap}
.tw{max-height:340px;overflow:auto;border:1px solid var(--line);border-radius:9px}
.none{color:var(--dim2);font-size:12.5px;font-style:italic}
.empty{color:var(--dim2);text-align:center;padding:60px 0}
</style>
</head>
<body>
<header><div class="hd">
  <h1>Galaxy Legends — SSS Hero Handbook <small>__N__ heroes · __GEN__ · v2.6.2</small></h1>
  <div class="toolbar">
    <input type="search" id="q" placeholder="Search name, id, skill or description…">
    <button class="chip on" data-role="*">All</button>__CHIPS__
  </div>
  <div class="count" id="cnt"></div>
</div></header>
<div class="wrap" id="list"></div>
<script id="data" type="application/json">/*__DATA__*/null</script>
<script>
const DB = JSON.parse(document.getElementById('data').textContent);
const ROLE = {Ranger:'#4ade80',Striker:'#f87171',Protector:'#60a5fa',
              Destroyer:'#fbbf24',Rover:'#a78bfa',Flagship:'#f472b6'};
const esc = s => String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
let role='*', q='';

function costRow(s){
  const items=(s.items||[]).map(i=>`${i.qty}× ${esc(i.name||('#'+i.id))}`).join(', ')||'—';
  const money=s.money?`<span style="color:#fbbf24">${s.money.toLocaleString()}</span>`:'—';
  return `<tr><td class="lv">${esc(s.to)}</td><td>${items}</td><td class="mn">${money}</td></tr>`;
}
function oldSkills(sk){
  const base=(sk[0]&&sk[0].name_en)||'—';
  let h=`<div class="skill"><div class="sh"><span class="sn">${esc(base)}</span>`+
     `<span class="unl">signature skill · ${sk.length} version${sk.length>1?'s':''}</span></div>`;
  sk.forEach(t=>{
    h+=`<div class="tier"><div class="th"><span class="tl">${t.tier_label||''}</span>`+
       `<span class="tat">${esc(t.from_augment||'')}</span>`+
       `<span class="tnm">${esc(t.name_en||'—')}${t.name_cn?` <span class="cn">${esc(t.name_cn)}</span>`:''}</span></div>`+
       (t.description_en?`<div class="td">${esc(t.description_en)}</div>`:
        `<div class="td none">no English description shipped</div>`)+`</div>`;
  });
  return h+`</div>`;
}
function card(h){
  const c=ROLE[h.role]||'#888';
  let b=`<h4>Ratings <span style="text-transform:none;letter-spacing:0">(1–10)</span></h4>`+
    `<div class="rt" style="margin-bottom:4px">`+
    `<span>Damage <b>${h.ratings.damage}</b></span><span>Defence <b>${h.ratings.defence}</b></span>`+
    `<span>Assist <b>${h.ratings.assist}</b></span></div>`;
  b+=`<h4>Skills</h4>`;
  if(h.generation==='latest'){
    h.skills.forEach(s=>{
      b+=`<div class="skill"><div class="sh"><span class="slot">Slot ${s.slot}</span>`+
         `<span class="sn">${esc(s.name_en)||'—'}</span>`+
         `<span class="unl">unlocks at ${esc(s.unlocks_at)}</span></div>`;
      s.tiers.forEach(t=>{
        b+=`<div class="tier"><div class="th"><span class="tl">${t.tier_label}</span>`+
           `<span class="tat">${esc(t.from_augment)}</span>`+
           `<span class="tnm">${esc(t.name_en||'—')}</span></div>`+
           (t.description_en?`<div class="td">${esc(t.description_en)}</div>`:
            `<div class="td none">no English description shipped</div>`)+`</div>`;
      });
      b+=`</div>`;
    });
  } else { b+=oldSkills(h.skills); }
  if(h.transform){
    b+=`<h4>Transform form</h4><div class="skill"><div class="sh"><span class="sn">`+
       `${esc(h.transform.name_cn||'')}</span><span class="unl">id ${h.transform.id}</span></div>`+
       oldSkills(h.transform.skills)+`</div>`;
  }
  if(h.augment&&h.augment.length){
    b+=`<h4>Augment cost</h4><div class="tw"><table><thead><tr><th>To</th><th>Materials</th><th>Money</th>`+
       `</tr></thead><tbody>${h.augment.map(costRow).join('')}</tbody></table></div>`;
  }
  return `<div class="card" data-role="${h.role}" data-id="${h.id}" style="--c:${c}">`+
    `<div class="ch"><span class="badge">${h.role}</span>`+
    `<span class="nm">${esc(h.name_en||'(no English name)')}</span>`+
    `<span class="cn">${esc(h.name_cn)}</span><span class="iid">#${h.id}</span>`+
    `<span class="spacer"></span>`+
    `<span class="rt"><span>DMG <b>${h.ratings.damage}</b></span>`+
    `<span>DEF <b>${h.ratings.defence}</b></span><span>AST <b>${h.ratings.assist}</b></span></span>`+
    `<span class="tog"></span></div><div class="body">${b}</div></div>`;
}
function draw(){
  const ql=q.toLowerCase();
  const rows=DB.filter(h=>{
    if(role!=='*'&&h.role!==role) return false;
    if(!ql) return true;
    if(String(h.id).includes(ql)) return true;
    if((h.name_en||'').toLowerCase().includes(ql)) return true;
    if((h.name_cn||'').includes(ql)) return true;
    const blob=JSON.stringify(h.skills)+(h.augment?JSON.stringify(h.augment):'');
    return blob.toLowerCase().includes(ql);
  });
  document.getElementById('list').innerHTML = rows.length
    ? rows.map(card).join('')
    : `<div class="empty">No hero matches “${esc(q)}”.</div>`;
  document.getElementById('cnt').textContent = `${rows.length} of ${DB.length} heroes`;
  document.querySelectorAll('.ch').forEach(el=>el.onclick=()=>
    el.parentElement.classList.toggle('open'));
}
document.getElementById('q').oninput=e=>{q=e.target.value;draw()};
document.querySelectorAll('.chip').forEach(el=>el.onclick=()=>{
  document.querySelectorAll('.chip').forEach(c=>c.classList.remove('on'));
  el.classList.add('on'); role=el.dataset.role; draw();
});
draw();
</script>
</body>
</html>
"""

if __name__ == '__main__':
    main()
