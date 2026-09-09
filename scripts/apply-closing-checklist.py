from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'blaskos-closing-checklist-v2' in s:
    raise SystemExit('already applied')
block=r'''<style id="blaskos-closing-checklist-v2">
#recordFields .closing-check-card{padding:0;overflow:hidden}
#recordFields .closing-check-head{padding:18px 16px;background:var(--mint);border-bottom:1px solid var(--line)}
#recordFields .closing-check-head h3{margin:0;color:var(--green);font-family:Inter,system-ui,sans-serif;font-size:21px;font-weight:900;line-height:1.15}
#recordFields .closing-check-head p{margin:5px 0 0;color:var(--muted);font-size:11px;line-height:1.35}
#recordFields .closing-check-list{padding:0}
#recordFields .closing-check-item{display:flex;align-items:flex-start;gap:12px;padding:15px 14px;border-bottom:1px solid var(--line);background:#fff;cursor:pointer;user-select:none}
#recordFields .closing-check-item:last-child{border-bottom:0}
#recordFields .closing-check-item input{position:absolute;opacity:0;pointer-events:none}
#recordFields .closing-check-box{width:25px;height:25px;min-width:25px;border:2px solid #cbd8d3;border-radius:8px;display:grid;place-items:center;color:transparent;background:#fff;margin-top:1px;font-weight:900;font-size:15px;line-height:1;transition:.12s ease}
#recordFields .closing-check-item:has(input:checked) .closing-check-box{background:var(--green);border-color:var(--green);color:#fff}
#recordFields .closing-check-copy{flex:1;min-width:0}
#recordFields .closing-check-copy b{display:block;font-size:14px;line-height:1.3;color:var(--ink);font-weight:800}
#recordFields .closing-check-copy small{display:block;margin-top:4px;color:var(--muted);font-size:11px;line-height:1.35}
#recordFields .closing-check-item:has(input:checked) .closing-check-copy b{color:#285b52}
#recordFields .closing-check-summary{margin:12px 0 0;padding:11px 13px;border-radius:13px;background:#f3f7f5;color:#526862;font-size:11px;font-weight:800}
#recordFields .closing-check-summary strong{color:var(--green)}
#recordFields .closing-check-failure{margin-top:14px;padding:13px;border:1px solid #ead9d3;border-radius:14px;background:#fff8f5}
#recordFields .closing-check-failure b{display:block;color:#8e4f46;font-size:12px;margin-bottom:5px}
#recordFields .closing-check-sign{margin-top:15px}
@media(max-width:390px){#recordFields .closing-check-item{padding:14px 12px}#recordFields .closing-check-copy b{font-size:13px}}
</style>
<script id="blaskos-closing-checklist-v2">
(function(){
 const TYPE='Closing checklist';
 const checks=[
  ['close1','All surfaces cleaned and sanitised','Clean and sanitise food-contact surfaces and other relevant work areas before closing.'],
  ['close2','Waste bagged and removed to bin store','Bag waste securely and remove it to the designated bin store.'],
  ['close3','Fridges closed and at correct temperature','Confirm fridge doors are closed and food is being kept at the required temperature.'],
  ['close4','Cooking equipment switched off','Switch off cooking equipment safely and leave the area in a safe condition.'],
  ['close5','Premises secured (doors and windows locked)','Check the premises are secure and doors/windows are locked before leaving.']
 ];
 function count(){return checks.filter(c=>document.getElementById(c[0])?.checked).length}
 function summary(){const e=document.getElementById('closingChecklistSummary');if(!e)return;const n=count();e.innerHTML='<strong>'+n+' / '+checks.length+'</strong> checks completed'+(n===checks.length?' · Ready to sign':' · Complete all checks before signing')}
 function render(){const f=document.getElementById('recordFields');if(!f)return;const rows=checks.map(c=>`<label class="closing-check-item"><input id="${c[0]}" type="checkbox"><span class="closing-check-box">✓</span><span class="closing-check-copy"><b>${c[1]}</b><small>${c[2]}</small></span></label>`).join('');f.innerHTML=`<div class="card closing-check-card"><div class="closing-check-head"><h3>Closing checks</h3><p>Complete this checklist before leaving. It records the individual closing checks as part of your food-safety record.</p></div><div class="closing-check-list">${rows}</div></div><div id="closingChecklistSummary" class="closing-check-summary">0 / ${checks.length} checks completed · Complete all checks before signing</div><div class="closing-check-failure"><b>Something not right?</b><span class="small muted">Leave the affected check unticked and record what you did in corrective action / notes. The saved record will show the individual check status.</span></div><label style="margin-top:14px">Corrective action / notes</label><textarea id="closingAction" placeholder="Record any issue, action taken, food isolated/disposed of, equipment taken out of use, or other notes..."></textarea><div class="closing-check-sign"><label>Completed by</label><input id="closingBy" placeholder="Name"></div>`;f.querySelectorAll('.closing-check-item input').forEach(x=>x.addEventListener('change',summary));summary()}
 const oldRender=window.renderRecordFields;
 window.renderRecordFields=function(type){if(type===TYPE){document.getElementById('addTitle').textContent='Closing checks';render();return}return oldRender(type)};
 const oldSave=window.saveRecord;
 window.saveRecord=function(){const type=document.querySelector('.add-tab.active')?.dataset.type||'';if(type!==TYPE)return oldSave();const date=document.getElementById('entryDate').value||today();const time=document.getElementById('entryTime').value||new Date().toLocaleTimeString('en-GB',{hour:'2-digit',minute:'2-digit'});const signer=(document.getElementById('closingBy')?.value||'').trim();if(!signer){toast('Enter the name of the person completing the closing checks');return}const status={};checks.forEach(c=>status[c[0]]=!!document.getElementById(c[0])?.checked);const completed=count();const action=(document.getElementById('closingAction')?.value||'').trim();if(completed<checks.length&&!action){toast('Add a corrective action or note for the unticked checks');return}db.records.unshift({id:Date.now(),type:TYPE,date,time,data:{checklistVersion:'Closing checklist v2',checklist:status,checklistItems:checks.map(c=>({id:c[0],label:c[1],checked:!!status[c[0]]})),completedChecks:completed,totalChecks:checks.length,outcome:completed===checks.length?'All checks completed':'Attention required',action,notes:action,signer,completedBy:signer}});persist();toast('Closing checks saved');go('records')};
 function boot(){if(document.querySelector('.add-tab.active')?.dataset.type===TYPE)render()}
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();window.addEventListener('load',boot);
})();
</script>
'''
pos=s.rfind('</body>')
if pos<0:
    raise SystemExit('closing body not found')
p.write_text(s[:pos]+block+s[pos:],encoding='utf-8')
print('Closing checklist applied')
