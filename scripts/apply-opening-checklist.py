# trigger opening checklist v2
from pathlib import Path
p=Path('index.html'); s=p.read_text(encoding='utf-8')
if 'blaskos-opening-checklist-v1' in s: raise SystemExit('already applied')
block=r'''<style id="blaskos-opening-checklist-v1">
#recordFields .opening-check-card{padding:0;overflow:hidden}
#recordFields .opening-check-head{padding:18px 16px;background:var(--mint);border-bottom:1px solid var(--line)}
#recordFields .opening-check-head h3{margin:0;color:var(--green);font-family:Inter,system-ui,sans-serif;font-size:21px;font-weight:900;line-height:1.15}
#recordFields .opening-check-head p{margin:5px 0 0;color:var(--muted);font-size:11px;line-height:1.35}
#recordFields .opening-check-list{padding:0}
#recordFields .opening-check-item{display:flex;align-items:flex-start;gap:12px;padding:15px 14px;border-bottom:1px solid var(--line);background:#fff;cursor:pointer;user-select:none}
#recordFields .opening-check-item:last-child{border-bottom:0}
#recordFields .opening-check-item input{position:absolute;opacity:0;pointer-events:none}
#recordFields .opening-check-box{width:25px;height:25px;min-width:25px;border:2px solid #cbd8d3;border-radius:8px;display:grid;place-items:center;color:transparent;background:#fff;margin-top:1px;font-weight:900;font-size:15px;line-height:1;transition:.12s ease}
#recordFields .opening-check-item:has(input:checked) .opening-check-box{background:var(--green);border-color:var(--green);color:#fff}
#recordFields .opening-check-copy{flex:1;min-width:0}
#recordFields .opening-check-copy b{display:block;font-size:14px;line-height:1.3;color:var(--ink);font-weight:800}
#recordFields .opening-check-copy small{display:block;margin-top:4px;color:var(--muted);font-size:11px;line-height:1.35}
#recordFields .opening-check-item:has(input:checked) .opening-check-copy b{color:#285b52}
#recordFields .opening-check-summary{margin:12px 0 0;padding:11px 13px;border-radius:13px;background:#f3f7f5;color:#526862;font-size:11px;font-weight:800}
#recordFields .opening-check-summary strong{color:var(--green)}
#recordFields .opening-check-failure{margin-top:14px;padding:13px;border:1px solid #ead9d3;border-radius:14px;background:#fff8f5}
#recordFields .opening-check-failure b{display:block;color:#8e4f46;font-size:12px;margin-bottom:5px}
#recordFields .opening-check-sign{margin-top:15px}
@media(max-width:390px){#recordFields .opening-check-item{padding:14px 12px}#recordFields .opening-check-copy b{font-size:13px}}
</style>
<script id="blaskos-opening-checklist-v1">
(function(){
 const TYPE='Opening checklist';
 const checks=[
 ['open1','Fit to work — no illness or symptoms','Confirm the person carrying out food handling is fit to work.'],
 ['open2','Potable water, soap and disposable towels available','Confirm the hand-washing and water supply is available and ready.'],
 ['open3','Food-contact surfaces, equipment and ovens clean and working','Check preparation surfaces, equipment and pizza ovens are clean and ready.'],
 ['open4','Food in date, covered and protected','Check dates, protection, storage and condition of food and ingredients.'],
 ['open5','Menu and allergen information current','Confirm the current menu, recipes and allergen information are available.'],
 ['open6','Probe thermometer clean, working and disinfectant wipes available','Confirm the probe is clean, functioning and ready for food checks.'],
 ['open7','Gas safety checks completed — cylinders, hoses, connections, ventilation and appliances visually safe; no smell of gas','Visually check the gas setup before use. Do not operate equipment if unsafe or if gas is suspected.'],
 ['open8','Service area safe and ready for customers','Check the gazebo/service area, access and customer-facing area are safe and ready.']
 ];
 function count(){return checks.filter(c=>document.getElementById(c[0])?.checked).length}
 function summary(){const e=document.getElementById('openingChecklistSummary');if(!e)return;const n=count();e.innerHTML='<strong>'+n+' / '+checks.length+'</strong> checks completed'+(n===checks.length?' · Ready to sign':' · Complete all checks before signing')}
 function render(){const f=document.getElementById('recordFields');if(!f)return;const rows=checks.map(c=>`<label class="opening-check-item"><input id="${c[0]}" type="checkbox"><span class="opening-check-box">✓</span><span class="opening-check-copy"><b>${c[1]}</b><small>${c[2]}</small></span></label>`).join('');f.innerHTML=`<div class="card opening-check-card"><div class="opening-check-head"><h3>Opening checks</h3><p>Complete this checklist before opening. It records the individual checks as part of your food-safety record.</p></div><div class="opening-check-list">${rows}</div></div><div id="openingChecklistSummary" class="opening-check-summary">0 / ${checks.length} checks completed · Complete all checks before signing</div><div class="opening-check-failure"><b>Something not right?</b><span class="small muted">Leave the affected check unticked and record what you did in corrective action / notes. The saved record will show the individual check status.</span></div><label style="margin-top:14px">Corrective action / notes</label><textarea id="openingAction" placeholder="Record any issue, action taken, food isolated/disposed of, equipment taken out of use, or other notes..."></textarea><div class="opening-check-sign"><label>Completed by</label><input id="openingBy" placeholder="Name"></div>`;f.querySelectorAll('.opening-check-item input').forEach(x=>x.addEventListener('change',summary));summary()}
 const oldRender=window.renderRecordFields;
 window.renderRecordFields=function(type){if(type===TYPE){document.getElementById('addTitle').textContent='Opening checks';render();return}return oldRender(type)};
 const oldSave=window.saveRecord;
 window.saveRecord=function(){const type=document.querySelector('.add-tab.active')?.dataset.type||'';if(type!==TYPE)return oldSave();const date=document.getElementById('entryDate').value||today();const time=document.getElementById('entryTime').value||new Date().toLocaleTimeString('en-GB',{hour:'2-digit',minute:'2-digit'});const signer=(document.getElementById('openingBy')?.value||'').trim();if(!signer){toast('Enter the name of the person completing the opening checks');return}const status={};checks.forEach(c=>status[c[0]]=!!document.getElementById(c[0])?.checked);const completed=count();const action=(document.getElementById('openingAction')?.value||'').trim();if(completed<checks.length&&!action){toast('Add a corrective action or note for the unticked checks');return}db.records.unshift({id:Date.now(),type:TYPE,date,time,data:{checklistVersion:'Opening checklist v1',checklist:status,checklistItems:checks.map(c=>({id:c[0],label:c[1],checked:!!status[c[0]]})),completedChecks:completed,totalChecks:checks.length,outcome:completed===checks.length?'All checks completed':'Attention required',action,notes:action,signer,completedBy:signer}});persist();toast('Opening checks saved');go('records')};
 function boot(){if(document.querySelector('.add-tab.active')?.dataset.type===TYPE)render()}
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();window.addEventListener('load',boot);
})();
</script>
'''
pos=s.rfind('</body>')
if pos<0: raise SystemExit('closing body not found')
p.write_text(s[:pos]+block+s[pos:],encoding='utf-8')