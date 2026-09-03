from pathlib import Path

# Design V5 updater
p = Path('index.html')
s = p.read_text(encoding='utf-8')

css = r'''
<style id="blaskos-allergen-design-v5">
#docsAllergens{padding-bottom:10px}
#docsAllergens .card{border-radius:20px;box-shadow:0 5px 18px rgba(20,88,78,.055)}
#docsAllergens .eyebrow{color:#2f6e64}
#docsAllergens h2{font-family:Georgia,serif;font-size:40px;letter-spacing:-1.2px;color:#124f47;margin-bottom:8px}
#docsAllergens>p.muted{font-size:13px;margin-top:0;max-width:720px}
#docsAllergens .allergen-hero{margin-top:18px;border-radius:20px;padding:19px 20px;background:linear-gradient(135deg,#0f5d52,#0d4b43);box-shadow:0 8px 22px rgba(20,88,78,.12);min-height:104px}
#docsAllergens .allergen-hero h3{font-family:Georgia,serif;font-size:23px;letter-spacing:-.2px}
#docsAllergens .allergen-hero p{font-size:12px;line-height:1.45}
#docsAllergens .allergen-score{background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.18);border-radius:15px;padding:10px 12px;min-width:70px}
#docsAllergens .allergen-score b{font-size:27px}
#docsAllergens .allergen-score span{font-size:9px}
#docsAllergens .allergen-note{margin-top:12px;border-radius:17px;padding:15px 16px;background:#fffaf0;border:1px solid #ead9a8;box-shadow:none}
#docsAllergens .allergen-note b{font-size:12px;color:#6e5918;white-space:normal}
#docsAllergens .allergen-note p{margin:4px 0 0;color:#75683f}
#docsAllergens .allergen-add-card{background:#f1f8f6;border:1px solid #c7ddd7;border-radius:18px;padding:15px 16px;margin:12px 0 15px;display:flex;align-items:center;justify-content:space-between;gap:12px}
#docsAllergens .allergen-add-card h3{font-family:Inter,system-ui,sans-serif;font-size:15px;margin:0 0 3px;font-weight:850}
#docsAllergens .allergen-add-card p{font-size:12px;margin:0;color:#58716c;line-height:1.35}
#docsAllergens .allergen-add-card .allergen-add{background:#14584e;color:#fff;border-radius:12px;padding:11px 14px;box-shadow:0 4px 10px rgba(20,88,78,.14)}
#docsAllergens .allergen-legend{margin:12px 0 9px;gap:13px;color:#48645f}
#docsAllergens .allergen-legend b{width:24px;height:24px;border-radius:7px}
#docsAllergens .a-c{background:#f5cbc7;color:#9b4d47}
#docsAllergens .a-m{background:#ffeab0;color:#8a6916}
#docsAllergens .a-n{background:#edf2f0;color:#70817c}
#docsAllergens .allergen-table-wrap{border:1px solid #d8e1dd;border-radius:17px;background:#fff;box-shadow:0 5px 18px rgba(20,88,78,.045)}
#docsAllergens .allergen-table th,#docsAllergens .allergen-table td{padding:9px 7px;height:49px;border-bottom:1px solid #e5ebe8;background:#fff}
#docsAllergens .allergen-table th{height:58px;background:#f1f7f5;color:#1d5a52;font-weight:850;font-size:9px;vertical-align:middle}
#docsAllergens .allergen-table th:first-child{background:#f1f7f5;min-width:145px}
#docsAllergens .allergen-table td:first-child{min-width:145px;max-width:155px;padding-left:12px;background:#fff}
#docsAllergens .allergen-table td:first-child b{font-size:11px;color:#173d38}
#docsAllergens .allergen-cell{font-size:11px!important;border-radius:0}
#docsAllergens .allergen-cell.c{background:#f6d9d6!important;color:#a4524b}
#docsAllergens .allergen-cell.m{background:#fff0c8!important;color:#876914}
#docsAllergens .allergen-cell.n{background:#f3f6f5!important;color:#9ba8a5}
#docsAllergens .allergen-status{font-size:8px;padding:3px 6px;background:#e6f2ed;color:#24665b}
#docsAllergens .allergen-status.unverified{background:#fff0c6;color:#765d13}
#docsAllergens .allergen-actions{justify-content:flex-start;margin-top:5px}
#docsAllergens .allergen-actions button{font-size:9px;padding:5px 7px;background:#fff;border-color:#d7e0dc}
#docsAllergens .allergen-guidance{margin-top:13px!important;border-radius:18px!important}
#docsAllergens .allergen-guidance h3{font-family:Georgia,serif;font-size:19px;color:#14584e}
#docsAllergens .allergen-toolbar{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0 0}
#docsAllergens .allergen-toolbar button{background:#fff;border:1px solid #d7e0dc;border-radius:11px;padding:10px 12px;color:#14584e;font-size:11px;font-weight:800}
#docsAllergens .allergen-toolbar button.danger{color:#a14b45;border-color:#e6c8c4}
@media(max-width:520px){#docsAllergens h2{font-size:36px}#docsAllergens .allergen-hero{padding:17px 16px}#docsAllergens .allergen-hero h3{font-size:21px}#docsAllergens .allergen-add-card{align-items:flex-start}#docsAllergens .allergen-add-card .allergen-add{flex:0 0 auto}}
@media(max-width:390px){#docsAllergens h2{font-size:32px}#docsAllergens .allergen-add-card{padding:13px}#docsAllergens .allergen-add-card p{max-width:180px}#docsAllergens .allergen-add-card .allergen-add{padding:10px 11px;font-size:11px}}
</style>
'''

js = r'''
<script id="blaskos-allergen-design-v5-js">
(function(){
  function enhance(){
    const panel=document.getElementById('docsAllergens');
    if(!panel) return;
    const hero=panel.querySelector('.allergen-hero');
    if(hero && !panel.querySelector('.allergen-add-card')){
      const card=document.createElement('div');
      card.className='allergen-add-card';
      card.innerHTML='<div><h3>Add something new to the menu</h3><p>New pizzas stay private until their allergen record is verified.</p></div><button class="allergen-add" onclick="openAllergenPizzaModal()">＋ Add new pizza</button>';
      hero.insertAdjacentElement('afterend',card);
    }
    const wrap=panel.querySelector('#allergenTableWrap');
    if(wrap && !panel.querySelector('.allergen-toolbar')){
      const bar=document.createElement('div');
      bar.className='allergen-toolbar';
      bar.innerHTML='<button onclick="printAllergenMatrix()">▣ Print matrix</button><button onclick="exportAllergenMatrix()">⇩ Export matrix</button><button class="danger" onclick="clearAllergenMatrix()">♲ Clear matrix</button>';
      wrap.insertAdjacentElement('afterend',bar);
    }
  }
  window.printAllergenMatrix=function(){window.print()};
  window.exportAllergenMatrix=function(){
    const key='blaskosPizzaAppV2'; let data=[];
    try{const db=JSON.parse(localStorage.getItem(key)||'{}');data=db.allergenPizzas||[]}catch(e){}
    const head=['Pizza','Celery','Gluten cereals','Crustaceans','Eggs','Fish','Lupin','Milk','Molluscs','Mustard','Peanuts','Sesame','Soya','Sulphites','Tree nuts','Review','Verified'];
    const codes=['Ce','Gl','Cr','Eg','Fi','Lu','Mi','Mo','Mu','Pe','Se','So','Su','Nu'];
    const rows=[head].concat(data.map(p=>[p.name,...codes.map(k=>p.allergens&&p.allergens[k]||'n'),p.date||'',p.verified?'Yes':'No']));
    const csv=rows.map(r=>r.map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(',')).join('\n');
    const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));a.download='blaskos-pizza-allergen-matrix.csv';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),500);
  };
  window.clearAllergenMatrix=function(){
    if(!confirm('Clear the entire allergen matrix? This cannot be undone.')) return;
    try{const db=JSON.parse(localStorage.getItem('blaskosPizzaAppV2')||'{}');db.allergenPizzas=[];localStorage.setItem('blaskosPizzaAppV2',JSON.stringify(db));if(window.renderAllergenMatrix)window.renderAllergenMatrix();if(window.toast)toast('Allergen matrix cleared')}catch(e){}
  };
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',enhance);else enhance();
  setTimeout(enhance,500);
})();
</script>
'''

head = s.find('<head>')
if head < 0:
    raise SystemExit('Could not find real <head> tag')
insert_at = head + len('<head>')
if 'blaskos-allergen-design-v5' not in s:
    s = s[:insert_at] + css + js + s[insert_at:]

p.write_text(s, encoding='utf-8')
print('Applied allergen design V5')
