from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

if 'id="blaskos-allergen-v4"' in s:
    raise SystemExit('Allergen V4 already installed')

# Replace the existing Docs > Allergens panel by matching balanced div tags.
marker = '<div id="docsAllergens"'
start = s.find(marker)
if start < 0:
    raise SystemExit('docsAllergens panel not found')

pos = start
level = 0
pattern = re.compile(r'<div\b[^>]*>|</div\s*>', re.I)
end = None
for m in pattern.finditer(s, start):
    if m.group(0).lower().startswith('<div'):
        level += 1
    else:
        level -= 1
        if level == 0:
            end = m.end()
            break
if end is None:
    raise SystemExit('Could not find end of docsAllergens panel')

panel = r'''<div id="docsAllergens" class="docs-panel">
  <div class="allergen-hero" id="blaskos-allergen-v4">
    <div>
      <div class="eyebrow" style="color:#cce6df">Menu safety</div>
      <h3>Allergen register</h3>
      <p>Keep a verified record of the 14 regulated allergens for every pizza on your menu.</p>
    </div>
    <div class="allergen-score"><b id="allergenVerifiedCount">0</b><span>verified</span></div>
  </div>

  <div class="card allergen-note">
    <b>Important</b>
    <span>Use your current ingredient labels and supplier specifications when completing this register. Always confirm allergen information before serving a customer with an allergy.</span>
  </div>

  <div class="card">
    <div class="row">
      <div><h3 style="margin-bottom:3px">Pizza menu</h3><div class="muted" id="allergenRegisterSummary">No pizzas added yet.</div></div>
      <button class="primary allergen-add" onclick="openAllergenPizzaModal()">＋ Add pizza</button>
    </div>
    <div class="allergen-legend"><span><b class="a-c">C</b> Contains</span><span><b class="a-m">M</b> May contain</span><span><b class="a-n">—</b> Not listed</span></div>
    <div class="allergen-table-wrap" id="allergenTableWrap"></div>
  </div>

  <div class="card allergen-guidance">
    <h3>How to use this register</h3>
    <p class="muted">Record allergens from the ingredients and supplier specifications for each recipe. “May contain” should only be used where there is a genuine unavoidable cross-contamination risk that cannot be adequately controlled.</p>
    <p class="small muted">For loose/non-prepacked food, written allergen information is best practice and should be supported by a conversation with the customer.</p>
  </div>
</div>'''
s = s[:start] + panel + s[end:]

css = r'''
<style id="blaskos-allergen-css-v4">
.allergen-hero{background:var(--green);color:#fff;border-radius:24px;padding:20px;margin:14px 0;display:flex;justify-content:space-between;gap:16px;align-items:center}.allergen-hero h3{font-size:27px;margin:3px 0 5px;color:#fff}.allergen-hero p{margin:0;color:#d7ebe6;font-size:13px}.allergen-score{min-width:78px;text-align:center;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:18px;padding:12px 9px}.allergen-score b{display:block;font-size:30px;line-height:1}.allergen-score span{font-size:10px;text-transform:uppercase;letter-spacing:1px}.allergen-note{display:flex;gap:10px;align-items:flex-start;background:#fff8e9;border-color:#e9d69d;font-size:12px;line-height:1.4}.allergen-note b{color:#765d13;white-space:nowrap}.allergen-add{width:auto;padding:11px 13px;white-space:nowrap}.allergen-legend{display:flex;gap:14px;flex-wrap:wrap;margin:18px 0 10px;font-size:11px;color:var(--muted)}.allergen-legend b{display:inline-grid;place-items:center;width:23px;height:23px;border-radius:7px;margin-right:4px;font-size:10px}.a-c{background:var(--green);color:#fff}.a-m{background:#fff0c6;color:#765d13}.a-n{background:#edf1ef;color:#65736f}.allergen-table-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:16px;-webkit-overflow-scrolling:touch}.allergen-table{border-collapse:collapse;width:max-content;min-width:100%}.allergen-table th,.allergen-table td{border-bottom:1px solid var(--line);padding:10px 7px;text-align:center;font-size:10px;white-space:nowrap;background:#fff}.allergen-table th{position:sticky;top:0;background:var(--mint);font-size:9px;color:var(--green);z-index:1}.allergen-table th:first-child,.allergen-table td:first-child{position:sticky;left:0;text-align:left;z-index:2;background:var(--paper);min-width:130px;max-width:150px}.allergen-table th:first-child{background:var(--mint);z-index:3}.allergen-cell{font-weight:900}.allergen-cell.c{background:#e5f2ed!important;color:var(--green)}.allergen-cell.m{background:#fff5d7!important;color:#7a610e}.allergen-cell.n{color:#a0aaa7}.allergen-status{display:inline-block;margin-top:4px;padding:4px 7px;border-radius:999px;font-size:9px;font-weight:900}.allergen-status.verified{background:var(--mint);color:var(--green)}.allergen-status.unverified{background:#fff0c6;color:#765d13}.allergen-actions{display:flex;gap:5px;justify-content:flex-end;margin-top:7px}.allergen-actions button{padding:7px 9px;font-size:10px}.allergen-guidance{font-size:13px}.allergen-guidance h3{font-size:19px}.allergen-field{margin-bottom:8px}.allergen-field label{margin-bottom:4px}.allergen-choice-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}.allergen-choice{border:1px solid var(--line);border-radius:12px;padding:9px;background:#fff}.allergen-choice label{display:flex;align-items:center;gap:7px;font-size:12px;font-weight:700}.allergen-choice input{width:18px;height:18px;margin:0}.allergen-check{display:flex;align-items:center;gap:9px;padding:11px;border:1px solid var(--line);border-radius:12px;background:#fff;margin:8px 0 14px}.allergen-check input{width:20px;height:20px;margin:0}.allergen-modal-actions{display:flex;gap:8px}.allergen-modal-actions button{flex:1}.allergen-empty{padding:25px 10px;text-align:center;color:var(--muted);font-size:13px}.allergen-date{font-size:16px!important}
@media(max-width:390px){.allergen-hero{padding:17px}.allergen-score{min-width:68px}.allergen-add{padding:10px 11px;font-size:12px}}
</style>
'''

js = r'''
<script id="blaskos-allergen-js-v4">
(function(){
const A=[['Ce','Celery'],['Gl','Gluten cereals'],['Cr','Crustaceans'],['Eg','Eggs'],['Fi','Fish'],['Lu','Lupin'],['Mi','Milk'],['Mo','Molluscs'],['Mu','Mustard'],['Pe','Peanuts'],['Se','Sesame'],['So','Soya'],['Su','Sulphites'],['Nu','Tree nuts']];
const KEY='blaskosPizzaAppV2';
function getDb(){try{return JSON.parse(localStorage.getItem(KEY))||{}}catch(e){return {}}}
function saveDb(db){localStorage.setItem(KEY,JSON.stringify(db))}
function getPizzas(){const db=getDb();return Array.isArray(db.allergenPizzas)?db.allergenPizzas:[]}
function setPizzas(p){const db=getDb();db.allergenPizzas=p;saveDb(db)}
function esc(v){return String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function statusLabel(v){return v==='c'?'C':v==='m'?'M':'—'}
function render(){const pizzas=getPizzas();const verified=pizzas.filter(x=>x.verified).length;const vc=document.getElementById('allergenVerifiedCount');if(vc)vc.textContent=verified;
const sum=document.getElementById('allergenRegisterSummary');if(sum)sum.textContent=pizzas.length?(pizzas.length+' pizza'+(pizzas.length===1?'':'s')+' · '+verified+' verified'):'No pizzas added yet.';
const wrap=document.getElementById('allergenTableWrap');if(!wrap)return;if(!pizzas.length){wrap.innerHTML='<div class="allergen-empty">Add your first pizza to build the allergen matrix.</div>';return}
let h='<table class="allergen-table"><thead><tr><th>Pizza</th>'+A.map(a=>'<th>'+a[0]+'<br>'+esc(a[1])+'</th>').join('')+'<th>Review</th></tr></thead><tbody>';
pizzas.forEach((p,i)=>{h+='<tr><td><b>'+esc(p.name)+'</b><br><span class="allergen-status '+(p.verified?'verified':'unverified')+'">'+(p.verified?'Verified':'Not verified')+'</span><div class="allergen-actions"><button class="secondary" onclick="editAllergenPizza('+i+')">Edit</button><button class="secondary danger" onclick="deleteAllergenPizza('+i+')">Delete</button></div></td>';A.forEach(a=>{const v=p.allergens&&p.allergens[a[0]]||'n';h+='<td class="allergen-cell '+v+'">'+statusLabel(v)+'</td>'});h+='<td>'+esc(p.date||'—')+'</td></tr>'});h+='</tbody></table>';wrap.innerHTML=h}
window.openAllergenPizzaModal=function(index){const p=index==null?null:getPizzas()[index];const selected=p&&p.allergens?p.allergens:{};let fields=A.map(a=>'<div class="allergen-field"><label>'+esc(a[1])+' ('+a[0]+')</label><div class="allergen-choice-grid"><div class="allergen-choice"><label><input type="radio" name="a_'+a[0]+'" value="c" '+(selected[a[0]]==='c'?'checked':'')+'> Contains</label></div><div class="allergen-choice"><label><input type="radio" name="a_'+a[0]+'" value="m" '+(selected[a[0]]==='m'?'checked':'')+'> May contain</label></div><div class="allergen-choice"><label><input type="radio" name="a_'+a[0]+'" value="n" '+(selected[a[0]]!=='c'&&selected[a[0]]!=='m'?'checked':'')+'> Not listed</label></div></div></div>').join('');
openModal('<button class="close" onclick="closeModal()">Close</button><h3>'+(p?'Edit pizza':'Add pizza')+'</h3><p class="muted">Record the allergens from the current recipe and ingredient specifications.</p><div class="allergen-field"><label>Pizza name</label><input id="allergenPizzaName" value="'+esc(p?p.name:'')+'" placeholder="e.g. Margherita"></div><div class="allergen-field"><label>Check / review date</label><input class="allergen-date" type="date" id="allergenPizzaDate" value="'+esc(p?p.date:(typeof today==='function'?today():new Date().toISOString().slice(0,10)))+'"></div>'+fields+'<label class="allergen-check"><input type="checkbox" id="allergenPizzaVerified" '+(p&&p.verified?'checked':'')+'> I have checked this recipe against the current ingredient information</label><div class="allergen-modal-actions"><button class="secondary" onclick="closeModal()">Cancel</button><button class="primary" onclick="saveAllergenPizza('+(index==null?'null':index)+')">Save pizza</button></div>')}
window.saveAllergenPizza=function(index){const name=(document.getElementById('allergenPizzaName').value||'').trim();if(!name){toast('Enter a pizza name');return}const allergens={};A.forEach(a=>{const r=document.querySelector('input[name="a_'+a[0]+'"]:checked');allergens[a[0]]=r?r.value:'n'});const pizzas=getPizzas();const item={id:(index==null?Date.now():pizzas[index].id),name,date:document.getElementById('allergenPizzaDate').value||'',verified:document.getElementById('allergenPizzaVerified').checked,allergens};if(index==null)pizzas.push(item);else pizzas[index]=item;setPizzas(pizzas);closeModal();render();toast(index==null?'Pizza added':'Pizza updated')}
window.editAllergenPizza=function(i){openAllergenPizzaModal(i)}
window.deleteAllergenPizza=function(i){const p=getPizzas()[i];if(!p)return;openModal('<button class="close" onclick="closeModal()">Cancel</button><h3>Delete pizza?</h3><p class="muted">Remove <b>'+esc(p.name)+'</b> from the allergen register?</p><button class="primary danger" onclick="confirmDeleteAllergenPizza('+i+')">Delete pizza</button>')}
window.confirmDeleteAllergenPizza=function(i){const p=getPizzas();p.splice(i,1);setPizzas(p);closeModal();render();toast('Pizza deleted')}
window.renderAllergenMatrix=render;
function init(){if(document.getElementById('blaskos-allergen-v4'))render()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
'''

head = s.find('<head>')
if head < 0:
    raise SystemExit('Document head not found')
insert_at = head + len('<head>')
s = s[:insert_at] + css + js + s[insert_at:]
p.write_text(s, encoding='utf-8')
print('Installed allergen matrix V4 safely.')
