from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

css = r'''<style id="blaskos-allergen-design-v6">
/* V6 — match the approved Blasko's Pizza allergen matrix mockup */
#docsAllergens{padding-bottom:18px}
#docsAllergens h2{font-family:Georgia,serif;font-size:40px;line-height:1.02;letter-spacing:-1.3px;color:#14584e;margin:6px 0 9px}
#docsAllergens>p.muted{font-size:13px;line-height:1.45;margin:0 0 16px;max-width:760px}
#docsAllergens .allergen-hero{display:flex;align-items:center;justify-content:space-between;gap:18px;background:linear-gradient(135deg,#0f5d52,#0b4b43);border-radius:20px;padding:18px 20px;min-height:105px;margin:16px 0 12px;box-shadow:0 8px 22px rgba(20,88,78,.10)}
#docsAllergens .allergen-hero h3{font-family:Georgia,serif;font-size:23px;line-height:1.1;margin:3px 0 6px;color:#fff}
#docsAllergens .allergen-hero p{font-size:12px;line-height:1.4;margin:0;color:#d9ebe7}
#docsAllergens .allergen-score{min-width:72px;padding:10px 12px;border-radius:15px;background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.17)}
#docsAllergens .allergen-score b{font-size:27px;line-height:1.05}
#docsAllergens .allergen-score span{font-size:9px;letter-spacing:1px}
#docsAllergens .allergen-note{display:flex;gap:10px;align-items:flex-start;margin:0 0 12px;padding:14px 16px;border-radius:17px;background:#fffaf0;border:1px solid #ead9a8;box-shadow:none;color:#6f633e}
#docsAllergens .allergen-note b{display:block;color:#6e5918;font-size:12px;line-height:1.25;white-space:normal}
#docsAllergens .allergen-note p{margin:4px 0 0;color:#75683f;font-size:11px;line-height:1.4}
#docsAllergens .allergen-add-card{display:flex;align-items:center;justify-content:space-between;gap:16px;margin:0 0 14px;padding:14px 16px;border-radius:18px;background:#f1f8f6;border:1px solid #c7ddd7}
#docsAllergens .allergen-add-card h3{font-family:Inter,system-ui,sans-serif;font-size:15px;line-height:1.2;margin:0 0 3px;font-weight:850;color:#173d38}
#docsAllergens .allergen-add-card p{font-size:12px;line-height:1.35;margin:0;color:#58716c}
#docsAllergens .allergen-add-card .allergen-add{width:auto;margin:0;flex:0 0 auto;padding:11px 14px;border-radius:12px;background:#14584e;color:#fff;box-shadow:0 4px 10px rgba(20,88,78,.14)}
#docsAllergens .allergen-legend{display:flex;gap:16px;align-items:center;flex-wrap:wrap;margin:12px 0 9px;color:#48645f;font-size:11px}
#docsAllergens .allergen-legend b{display:inline-grid;place-items:center;width:24px;height:24px;border-radius:7px;margin-right:5px;font-size:10px}
#docsAllergens .a-c{background:#f5cbc7;color:#9b4d47}
#docsAllergens .a-m{background:#ffeab0;color:#876914}
#docsAllergens .a-n{background:#edf2f0;color:#70817c}
#docsAllergens .allergen-table-wrap{overflow-x:auto;border:1px solid #d8e1dd;border-radius:17px;background:#fff;box-shadow:0 5px 18px rgba(20,88,78,.045);-webkit-overflow-scrolling:touch}
#docsAllergens .allergen-table{width:max-content;min-width:100%;border-collapse:separate;border-spacing:0;table-layout:fixed}
#docsAllergens .allergen-table th,#docsAllergens .allergen-table td{box-sizing:border-box;border-right:1px solid #e5ebe8;border-bottom:1px solid #e5ebe8;background:#fff;padding:0;text-align:center;vertical-align:middle}
#docsAllergens .allergen-table th{height:64px;background:#f1f7f5;color:#1d5a52;font-size:9px;font-weight:850;line-height:1.1;white-space:normal}
#docsAllergens .allergen-table th:first-child{width:190px;min-width:190px;text-align:left;padding-left:14px;position:sticky;left:0;z-index:4;background:#f1f7f5}
#docsAllergens .allergen-table th:not(:first-child):not(:last-child){width:58px;min-width:58px}
#docsAllergens .allergen-table th:last-child{width:1px;min-width:1px;padding:0;font-size:0;border:0;background:#fff}
#docsAllergens .allergen-table th:nth-child(n+2):nth-child(-n+15){font-size:0}
#docsAllergens .allergen-table th:nth-child(2)::before{content:'Ce';}
#docsAllergens .allergen-table th:nth-child(3)::before{content:'Gl';}
#docsAllergens .allergen-table th:nth-child(4)::before{content:'Cr';}
#docsAllergens .allergen-table th:nth-child(5)::before{content:'Eg';}
#docsAllergens .allergen-table th:nth-child(6)::before{content:'Fi';}
#docsAllergens .allergen-table th:nth-child(7)::before{content:'Lu';}
#docsAllergens .allergen-table th:nth-child(8)::before{content:'Mi';}
#docsAllergens .allergen-table th:nth-child(9)::before{content:'Mo';}
#docsAllergens .allergen-table th:nth-child(10)::before{content:'Mu';}
#docsAllergens .allergen-table th:nth-child(11)::before{content:'Pe';}
#docsAllergens .allergen-table th:nth-child(12)::before{content:'Se';}
#docsAllergens .allergen-table th:nth-child(13)::before{content:'So';}
#docsAllergens .allergen-table th:nth-child(14)::before{content:'Su';}
#docsAllergens .allergen-table th:nth-child(15)::before{content:'Nu';}
#docsAllergens .allergen-table th:nth-child(n+2):nth-child(-n+15)::after{display:block;margin-top:4px;font-size:8px;font-weight:600;color:#71827e;line-height:1.1}
#docsAllergens .allergen-table th:nth-child(2)::after{content:'Celery'}
#docsAllergens .allergen-table th:nth-child(3)::after{content:'Gluten'}
#docsAllergens .allergen-table th:nth-child(4)::after{content:'Crust.'}
#docsAllergens .allergen-table th:nth-child(5)::after{content:'Eggs'}
#docsAllergens .allergen-table th:nth-child(6)::after{content:'Fish'}
#docsAllergens .allergen-table th:nth-child(7)::after{content:'Lupin'}
#docsAllergens .allergen-table th:nth-child(8)::after{content:'Milk'}
#docsAllergens .allergen-table th:nth-child(9)::after{content:'Moll.'}
#docsAllergens .allergen-table th:nth-child(10)::after{content:'Must.'}
#docsAllergens .allergen-table th:nth-child(11)::after{content:'Peanuts'}
#docsAllergens .allergen-table th:nth-child(12)::after{content:'Sesame'}
#docsAllergens .allergen-table th:nth-child(13)::after{content:'Soya'}
#docsAllergens .allergen-table th:nth-child(14)::after{content:'Sulph.'}
#docsAllergens .allergen-table th:nth-child(15)::after{content:'Tree nuts'}
#docsAllergens .allergen-table td{height:48px;min-width:58px;font-size:10px}
#docsAllergens .allergen-table td:first-child{width:190px;min-width:190px;text-align:left;padding:0 34px 0 12px;position:sticky;left:0;z-index:3;background:#fff}
#docsAllergens .allergen-table td:first-child b{display:block;font-size:11px;line-height:1.2;color:#173d38;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#docsAllergens .allergen-table td:first-child .allergen-status{display:block;margin:4px 0 0;padding:0;background:none;color:#71817d;font-size:8px;font-weight:600;line-height:1.1}
#docsAllergens .allergen-table td:first-child .allergen-status::before{content:'✓';display:inline-grid;place-items:center;width:14px;height:14px;margin-right:5px;border-radius:50%;background:#14584e;color:#fff;font-size:9px;font-weight:900;vertical-align:-3px}
#docsAllergens .allergen-table td:first-child .allergen-status.unverified{color:#8a6c17}
#docsAllergens .allergen-table td:first-child .allergen-status.unverified::before{content:'!';background:#ead58f;color:#6e5918}
#docsAllergens .allergen-cell{font-size:0!important;color:transparent!important;background:#fff!important;position:relative}
#docsAllergens .allergen-cell::before{content:'—';display:inline-grid;place-items:center;width:29px;height:29px;border-radius:8px;background:#edf2f0;color:#9aa8a5;font-size:11px;font-weight:800}
#docsAllergens .allergen-cell.c::before{content:'C';background:#f5cbc7;color:#a4524b}
#docsAllergens .allergen-cell.m::before{content:'M';background:#ffeab0;color:#876914}
#docsAllergens .allergen-table .allergen-actions{position:absolute;right:5px;top:7px;display:flex;gap:2px;margin:0;opacity:.45}
#docsAllergens .allergen-table .allergen-actions button{width:20px;height:20px;padding:0;border-radius:7px;font-size:0;background:#fff;border:1px solid #d7e0dc}
#docsAllergens .allergen-table .allergen-actions button:first-child::before{content:'✎';font-size:9px;color:#14584e}
#docsAllergens .allergen-table .allergen-actions button:last-child::before{content:'×';font-size:12px;color:#a14b45}
#docsAllergens .allergen-table tr:last-child td{border-bottom:0}
#docsAllergens .allergen-guidance{margin-top:13px!important;border-radius:18px!important}
#docsAllergens .allergen-guidance h3{font-family:Georgia,serif;font-size:19px;color:#14584e}
#docsAllergens .allergen-toolbar{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0 0}
#docsAllergens .allergen-toolbar button{background:#fff;border:1px solid #d7e0dc;border-radius:11px;padding:10px 12px;color:#14584e;font-size:11px;font-weight:800}
#docsAllergens .allergen-toolbar button.danger{color:#a14b45;border-color:#e6c8c4}
@media(max-width:520px){
 #docsAllergens h2{font-size:36px}
 #docsAllergens .allergen-hero{padding:16px;min-height:98px}
 #docsAllergens .allergen-hero h3{font-size:20px}
 #docsAllergens .allergen-score{min-width:64px;padding:9px}
 #docsAllergens .allergen-add-card{align-items:flex-start}
 #docsAllergens .allergen-add-card p{max-width:180px}
 #docsAllergens .allergen-table th:first-child,#docsAllergens .allergen-table td:first-child{width:155px;min-width:155px}
 #docsAllergens .allergen-table th:not(:first-child):not(:last-child){width:54px;min-width:54px}
 #docsAllergens .allergen-table td{height:46px;min-width:54px}
 #docsAllergens .allergen-cell::before{width:27px;height:27px;border-radius:7px}
}
@media(max-width:390px){
 #docsAllergens h2{font-size:32px}
 #docsAllergens .allergen-add-card{padding:13px}
 #docsAllergens .allergen-add-card .allergen-add{padding:10px 11px;font-size:11px}
 #docsAllergens .allergen-table th:first-child,#docsAllergens .allergen-table td:first-child{width:148px;min-width:148px}
}
</style>
'''

js = r'''<script id="blaskos-allergen-design-v6-js">
(function(){
  function decorate(){
    const panel=document.getElementById('docsAllergens');
    if(!panel) return;
    const wrap=panel.querySelector('#allergenTableWrap');
    if(!wrap) return;
    const table=wrap.querySelector('.allergen-table');
    if(!table) return;
    const head=table.querySelector('thead tr');
    if(head && head.lastElementChild && head.lastElementChild.textContent.trim()==='Review'){
      head.lastElementChild.remove();
    }
    table.querySelectorAll('tbody tr').forEach(row=>{
      const cells=row.children;
      if(!cells.length) return;
      const review=cells[cells.length-1];
      const status=cells[0].querySelector('.allergen-status');
      if(status){
        const date=(review && review.textContent.trim())||'';
        status.textContent=date?'Checked '+date:'Not verified';
      }
      if(review) review.remove();
    });
  }
  function addCard(){
    const panel=document.getElementById('docsAllergens');
    const hero=panel&&panel.querySelector('.allergen-hero');
    if(hero && !panel.querySelector('.allergen-add-card')){
      const card=document.createElement('div');
      card.className='allergen-add-card';
      card.innerHTML='<div><h3>Add something new to the menu</h3><p>New pizzas stay private until their allergen record is verified.</p></div><button class="allergen-add" onclick="openAllergenPizzaModal()">＋ Add new pizza</button>';
      hero.insertAdjacentElement('afterend',card);
    }
  }
  function toolbar(){
    const panel=document.getElementById('docsAllergens');
    const wrap=panel&&panel.querySelector('#allergenTableWrap');
    if(wrap && !panel.querySelector('.allergen-toolbar')){
      const bar=document.createElement('div');
      bar.className='allergen-toolbar';
      bar.innerHTML='<button onclick="printAllergenMatrix()">▣ Print matrix</button><button onclick="exportAllergenMatrix()">⇩ Export matrix</button><button class="danger" onclick="clearAllergenMatrix()">♲ Clear matrix</button>';
      wrap.insertAdjacentElement('afterend',bar);
    }
  }
  function run(){addCard();decorate();toolbar()}
  window.printAllergenMatrix=function(){window.print()};
  window.exportAllergenMatrix=window.exportAllergenMatrix||function(){};
  window.clearAllergenMatrix=window.clearAllergenMatrix||function(){};
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();
  const root=document.getElementById('docsAllergens');
  if(root){new MutationObserver(function(){run()}).observe(root,{childList:true,subtree:true});}
  setTimeout(run,300);
  setTimeout(run,1000);
})();
</script>
'''

# Replace V5 style block and V5 script block, if present; otherwise insert V6 after the real <head>.
s, n1 = re.subn(r'<style id="blaskos-allergen-design-v5">.*?</style>\s*', css, s, count=1, flags=re.S)
s, n2 = re.subn(r'<script id="blaskos-allergen-design-v5-js">.*?</script>\s*', js, s, count=1, flags=re.S)
if n1 == 0 or n2 == 0:
    head=s.find('<head>')
    if head<0: raise SystemExit('real head not found')
    pos=head+len('<head>')
    s=s[:pos]+css+js+s[pos:]

p.write_text(s,encoding='utf-8')
print('Applied allergen matrix V6')
