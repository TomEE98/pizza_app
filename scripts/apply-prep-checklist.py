from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

marker = 'id="blaskos-prep-cleaning-v1"'
if marker in s:
    raise SystemExit('Prep checklist block already present')

css = r'''
<style id="blaskos-prep-cleaning-v1">
/* Prep + cleaning checklist — replaces Pass / Fail / N/A with one auditable checklist. */
#recordFields .prep-clean-card{padding:0;overflow:hidden}
#recordFields .prep-clean-head{padding:18px 16px;background:var(--mint);border-bottom:1px solid var(--line)}
#recordFields .prep-clean-head h3{margin:0;color:var(--green);font-family:Inter,system-ui,sans-serif;font-size:21px;font-weight:900;line-height:1.15}
#recordFields .prep-clean-head p{margin:5px 0 0;color:var(--muted);font-size:11px;line-height:1.35}
#recordFields .prep-clean-list{padding:0}
#recordFields .prep-clean-item{display:flex;align-items:flex-start;gap:12px;padding:15px 14px;border-bottom:1px solid var(--line);background:#fff;cursor:pointer;user-select:none}
#recordFields .prep-clean-item:last-child{border-bottom:0}
#recordFields .prep-clean-item input{position:absolute;opacity:0;pointer-events:none}
#recordFields .prep-clean-box{width:25px;height:25px;min-width:25px;border:2px solid #cbd8d3;border-radius:8px;display:grid;place-items:center;color:transparent;background:#fff;margin-top:1px;font-weight:900;font-size:15px;line-height:1;transition:.12s ease}
#recordFields .prep-clean-item:has(input:checked) .prep-clean-box{background:var(--green);border-color:var(--green);color:#fff}
#recordFields .prep-clean-copy{flex:1;min-width:0}
#recordFields .prep-clean-copy b{display:block;font-size:14px;line-height:1.3;color:var(--ink);font-weight:800}
#recordFields .prep-clean-copy small{display:block;margin-top:4px;color:var(--muted);font-size:11px;line-height:1.35}
#recordFields .prep-clean-item:has(input:checked) .prep-clean-copy b{color:#285b52}
#recordFields .prep-clean-summary{margin:12px 0 0;padding:11px 13px;border-radius:13px;background:#f3f7f5;color:#526862;font-size:11px;font-weight:800}
#recordFields .prep-clean-summary strong{color:var(--green)}
#recordFields .prep-clean-failure{margin-top:14px;padding:13px;border:1px solid #ead9d3;border-radius:14px;background:#fff8f5}
#recordFields .prep-clean-failure b{display:block;color:#8e4f46;font-size:12px;margin-bottom:5px}
#recordFields .prep-clean-sign{margin-top:15px}
@media(max-width:390px){#recordFields .prep-clean-item{padding:14px 12px}#recordFields .prep-clean-copy b{font-size:13px}}
</style>
'''

js = r'''
<script id="blaskos-prep-cleaning-v1">
(function(){
  const PREP_TYPE='Prep record';
  const checks=[
    ['prep1','Fit to work — no illness or symptoms','Confirm the person carrying out food handling is fit to work.'],
    ['prep2','Prep-room hot running water, soap and disposable towels stocked and ready','Hand-wash facilities are available and ready for use.'],
    ['prep3','Prep-room worktops, sink, utensils and food-contact surfaces cleaned and disinfected','Food-contact areas are clean and disinfected before preparation.'],
    ['prep4','Mixer and other food-preparation machinery clean and ready to use','Food-preparation equipment is clean, safe and ready.'],
    ['prep5','Ingredients in date, covered and protected','Check use-by/best-before dates, protection and storage condition.'],
    ['prep6','Recipes, supplier labels and allergen information current','Use the current recipe and supplier information before preparation.'],
    ['prep7','Prep-room refrigeration monitoring active — no unresolved alarms','Refrigeration is operating and there are no unresolved food-safety alarms.'],
    ['prep8','Probe thermometer clean, working and disinfectant wipes available','Probe is clean, functioning and suitable for food checks.'],
    ['prep9','Cleaning chemicals stored safely and cleaning equipment ready','Cleaning materials are available, labelled and kept away from food.']
  ];
  function checkedCount(){return checks.filter(c=>document.getElementById(c[0])?.checked).length}
  function updateSummary(){const el=document.getElementById('prepChecklistSummary');if(!el)return;const n=checkedCount();el.innerHTML='<strong>'+n+' / '+checks.length+'</strong> checks completed'+(n===checks.length?' · Ready to sign':' · Complete all checks before signing')}
  function renderPrep(){const fields=document.getElementById('recordFields');if(!fields)return;const rows=checks.map(c=>`<label class="prep-clean-item"><input id="${c[0]}" type="checkbox"><span class="prep-clean-box">✓</span><span class="prep-clean-copy"><b>${c[1]}</b><small>${c[2]}</small></span></label>`).join('');fields.innerHTML=`<div class="card prep-clean-card"><div class="prep-clean-head"><h3>Prep & cleaning checks</h3><p>This single checklist records your preparation, hygiene and cleaning checks for the service.</p></div><div class="prep-clean-list">${rows}</div></div><div id="prepChecklistSummary" class="prep-clean-summary">0 / ${checks.length} checks completed · Complete all checks before signing</div><div class="prep-clean-failure"><b>Something not right?</b><span class="small muted">Leave the affected check unticked and explain what you did below. The saved record will show exactly which checks were completed and any corrective action.</span></div><label style="margin-top:14px">Corrective action / notes</label><textarea id="prepAction" placeholder="Record any issue, action taken, food isolated/disposed of, or other notes..."></textarea><div class="prep-clean-sign"><label>Completed by</label><input id="prepBy" placeholder="Name"></div>`;fields.querySelectorAll('.prep-clean-item input').forEach(x=>x.addEventListener('change',updateSummary));updateSummary()}
  const originalRender=window.renderRecordFields;
  window.renderRecordFields=function(type){if(type===PREP_TYPE){document.getElementById('addTitle').textContent='Prep & cleaning checks';renderPrep();document.getElementById('add')?.classList.remove('temperature-entry');return}return originalRender(type)};
  const originalSave=window.saveRecord;
  window.saveRecord=function(){const type=document.querySelector('.add-tab.active')?.dataset.type||'';if(type!==PREP_TYPE)return originalSave();const date=document.getElementById('entryDate').value||today();const time=document.getElementById('entryTime').value||new Date().toLocaleTimeString('en-GB',{hour:'2-digit',minute:'2-digit'});const signer=(document.getElementById('prepBy')?.value||'').trim();if(!signer){toast('Enter the name of the person completing the checks');return}const status={};checks.forEach(c=>status[c[0]]=!!document.getElementById(c[0])?.checked);const completed=checks.filter(c=>status[c[0]]).length;if(completed<checks.length){const action=(document.getElementById('prepAction')?.value||'').trim();if(!action){toast('Add a corrective action or note for the unticked checks');return}}const r={id:Date.now(),type:PREP_TYPE,date,time,data:{checklistVersion:'Prep & cleaning checklist v1',checklist:status,checklistItems:checks.map(c=>({id:c[0],label:c[1],checked:!!status[c[0]]})),completedChecks:completed,totalChecks:checks.length,outcome:completed===checks.length?'All checks completed':'Attention required',action:(document.getElementById('prepAction')?.value||'').trim(),notes:(document.getElementById('prepAction')?.value||'').trim(),signer:signer,completedBy:signer}};db.records.unshift(r);persist();toast('Prep & cleaning checks saved');go('records')};
  const originalRenderToday=window.renderToday;
  window.renderToday=function(){const out=originalRenderToday();const rs=db.records.filter(r=>r.date===today());const prepDone=rs.some(r=>r.type==='Prep record');const clean=document.getElementById('coreClean');const prep=document.getElementById('corePrep');if(clean)clean.style.display='none';if(prep){prep.querySelector('span:last-child')?.replaceChildren(document.createTextNode('Prep & clean'));prep.classList.toggle('done',prepDone)}const orderDone=['Opening checklist','Temperature check','Prep record','Closing checklist'].filter(t=>rs.some(r=>r.type===t)).length;const count=document.getElementById('todayProgressCount');if(count)count.textContent=orderDone+' / 4';const text=document.getElementById('todayProgressText');if(text)text.textContent=(4-orderDone)+' core checks remaining';const bar=document.getElementById('todayProgressBar');if(bar)bar.style.width=((orderDone/4)*100)+'%';const pct=document.getElementById('todayProgressPercent');if(pct)pct.textContent=Math.round(orderDone/4*100)+'%';return out};
  window.completeRemainingChecks=function(){const order=[['Opening checklist',document.getElementById('coreOpening')?.classList.contains('done')],['Temperature check',document.getElementById('coreFridge')?.classList.contains('done')],['Prep record',document.getElementById('corePrep')?.classList.contains('done')],['Closing checklist',document.getElementById('coreClosing')?.classList.contains('done')]];const next=order.find(x=>!x[1]);if(next)quickToday(next[0]);else toast('All core checks are complete')};
  const originalSpeak=window.speakToday;
  window.speakToday=function(){if(typeof originalSpeak!=='function')return;const rs=db.records.filter(r=>r.date===today());const done=['Opening checklist','Temperature check','Prep record','Closing checklist'].filter(t=>rs.some(r=>r.type===t)).length;if(!('speechSynthesis' in window)){toast('Voice is not available on this device');return}const text=`Blasko's Pizza. Today is ${new Date().toLocaleDateString('en-GB',{weekday:'long',day:'numeric',month:'long'})}. You have completed ${done} of 4 core checks. ${4-done} remaining.`;speechSynthesis.cancel();speechSynthesis.speak(new SpeechSynthesisUtterance(text))};
  function boot(){document.querySelector('.add-tab[data-type="Prep record"]')?.replaceChildren(document.createTextNode('Prep & clean'));if(document.querySelector('.add-tab.active')?.dataset.type===PREP_TYPE)renderPrep()}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();window.addEventListener('load',boot);
})();
</script>
'''
pos=s.rfind('</body>')
if pos<0: raise SystemExit('Real closing body tag not found')
s=s[:pos]+css+js+'\n'+s[pos:]
p.write_text(s,encoding='utf-8')
print('Applied prep + cleaning checklist')
# trigger marker comment
# v1
