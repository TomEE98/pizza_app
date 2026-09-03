from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='</head>'
if marker not in s:
    raise SystemExit('No real </head> found')

css=r'''<style id="blaskos-allergen-v10">
/* V10: clean matrix headers, clean pizza rows, single add-pizza CTA */
#docsAllergens .allergen-table-wrap{overflow-x:auto!important;border:1px solid #d8e4df!important;border-radius:18px!important;background:#fff!important;box-shadow:0 8px 24px rgba(20,88,78,.06)!important}
#docsAllergens .allergen-table{min-width:820px!important;width:100%!important;table-layout:fixed!important;border-collapse:separate!important;border-spacing:0!important}
#docsAllergens .allergen-table th,#docsAllergens .allergen-table td{box-sizing:border-box!important;text-align:center!important;vertical-align:middle!important}
/* Header: show ONLY the short allergen code. The full names live below the matrix. */
#docsAllergens .allergen-table th{height:64px!important;padding:8px 2px!important;font-size:0!important;line-height:1!important;color:transparent!important;white-space:normal!important}
#docsAllergens .allergen-table th:first-child{width:190px!important;min-width:190px!important;text-align:left!important;padding:10px 12px!important;background:#eef6f3!important}
#docsAllergens .allergen-table th:first-child::before{content:'Menu item'!important;display:block!important;font-family:Georgia,serif!important;font-size:13px!important;line-height:1.1!important;color:#14584e!important;margin:0!important}
#docsAllergens .allergen-table th:first-child::after{content:'Pizza'!important;display:block!important;font-family:Inter,system-ui,sans-serif!important;font-size:8px!important;color:#71817d!important;font-weight:700!important;margin-top:3px!important;letter-spacing:.3px!important}
#docsAllergens .allergen-table th:not(:first-child):not(:last-child){width:45px!important;min-width:45px!important;padding:7px 2px!important}
#docsAllergens .allergen-table th:not(:first-child):not(:last-child)::before{display:grid!important;place-items:center!important;width:27px!important;height:27px!important;margin:0 auto!important;border-radius:8px!important;background:#14584e!important;color:#fff!important;font-family:Inter,system-ui,sans-serif!important;font-size:9px!important;font-weight:900!important;line-height:1!important}
#docsAllergens .allergen-table th:not(:first-child):not(:last-child)::after{display:none!important;content:none!important}
#docsAllergens .allergen-table th:nth-child(2)::before{content:'Ce'!important}
#docsAllergens .allergen-table th:nth-child(3)::before{content:'Gl'!important}
#docsAllergens .allergen-table th:nth-child(4)::before{content:'Cr'!important}
#docsAllergens .allergen-table th:nth-child(5)::before{content:'Eg'!important}
#docsAllergens .allergen-table th:nth-child(6)::before{content:'Fi'!important}
#docsAllergens .allergen-table th:nth-child(7)::before{content:'Lu'!important}
#docsAllergens .allergen-table th:nth-child(8)::before{content:'Mi'!important}
#docsAllergens .allergen-table th:nth-child(9)::before{content:'Mo'!important}
#docsAllergens .allergen-table th:nth-child(10)::before{content:'Mu'!important}
#docsAllergens .allergen-table th:nth-child(11)::before{content:'Pe'!important}
#docsAllergens .allergen-table th:nth-child(12)::before{content:'Se'!important}
#docsAllergens .allergen-table th:nth-child(13)::before{content:'So'!important}
#docsAllergens .allergen-table th:nth-child(14)::before{content:'Su'!important}
#docsAllergens .allergen-table th:nth-child(15)::before{content:'Nu'!important}
#docsAllergens .allergen-table th:last-child{width:1px!important;min-width:1px!important;padding:0!important;border:0!important}
/* Pizza rows: name + verification status, with compact actions tucked to the right. */
#docsAllergens .allergen-table td{height:68px!important;background:#fff!important}
#docsAllergens .allergen-table td:first-child{width:190px!important;min-width:190px!important;text-align:left!important;padding:9px 58px 8px 12px!important;position:relative!important;background:#fff!important}
#docsAllergens .allergen-table td:first-child b{display:block!important;font-family:Inter,system-ui,sans-serif!important;font-size:13px!important;line-height:1.15!important;color:#183f39!important;font-weight:850!important;white-space:nowrap!important;overflow:hidden!important;text-overflow:ellipsis!important}
#docsAllergens .allergen-table td:first-child .allergen-status{display:inline-flex!important;align-items:center!important;margin-top:7px!important;padding:0!important;background:transparent!important;color:#70827d!important;font-size:8px!important;font-weight:700!important;line-height:1!important}
#docsAllergens .allergen-table td:first-child .allergen-status::before{content:'✓'!important;display:grid!important;place-items:center!important;width:17px!important;height:17px!important;margin-right:5px!important;border-radius:50%!important;background:#14584e!important;color:#fff!important;font-size:9px!important;font-weight:900!important}
#docsAllergens .allergen-table .allergen-actions{position:absolute!important;right:8px!important;top:10px!important;display:flex!important;gap:3px!important;margin:0!important;opacity:.7!important}
#docsAllergens .allergen-table .allergen-actions button{width:24px!important;height:24px!important;padding:0!important;border-radius:8px!important;background:#fff!important;border:1px solid #d7e1dd!important;font-size:0!important}
#docsAllergens .allergen-table .allergen-actions button:first-child::before{content:'✎'!important;font-size:10px!important;color:#14584e!important}
#docsAllergens .allergen-table .allergen-actions button:last-child::before{content:'×'!important;font-size:14px!important;color:#a14b45!important}
#docsAllergens .allergen-cell{font-size:0!important;color:transparent!important;background:#fff!important}
#docsAllergens .allergen-cell::before{content:'—'!important;display:inline-grid!important;place-items:center!important;width:28px!important;height:28px!important;border-radius:8px!important;background:#edf2f0!important;color:#899a95!important;font-family:Inter,system-ui,sans-serif!important;font-size:10px!important;font-weight:900!important}
#docsAllergens .allergen-cell.c::before{content:'C'!important;background:#f3c9c5!important;color:#a04e48!important}
#docsAllergens .allergen-cell.m::before{content:'M'!important;background:#ffe8ac!important;color:#876914!important}
@media(max-width:620px){
 #docsAllergens .allergen-table{min-width:820px!important;width:820px!important}
 #docsAllergens .allergen-table th:first-child,#docsAllergens .allergen-table td:first-child{width:175px!important;min-width:175px!important}
 #docsAllergens .allergen-table th:not(:first-child):not(:last-child){width:45px!important;min-width:45px!important}
 #docsAllergens .allergen-table td:first-child{width:175px!important;min-width:175px!important}
}
</style>'''

js=r'''<script id="blaskos-allergen-v10-js">
(function(){
  function removeDuplicateAddPizza(){
    const panel=document.getElementById('docsAllergens');
    if(!panel) return;
    const buttons=[...panel.querySelectorAll('button')].filter(b=>/add\s+(new\s+)?pizza/i.test((b.textContent||'').trim()));
    buttons.slice(1).forEach(btn=>{
      let node=btn.parentElement;
      while(node && node!==panel){
        const buttonsInside=node.querySelectorAll('button');
        if(buttonsInside.length===1){node.remove();break;}
        node=node.parentElement;
      }
    });
  }
  function run(){removeDuplicateAddPizza();}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();
  window.addEventListener('load',run);
})();
</script>'''

s=s.replace(marker,css+js+'\n'+marker,1)
p.write_text(s,encoding='utf-8')
print('Applied V10')
'''
