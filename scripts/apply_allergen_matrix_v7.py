from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

css = r'''<style id="blaskos-allergen-design-v7">
/* V7 — closer to the supplied allergen-matrix reference design */
#docsAllergens{padding-bottom:28px}
#docsAllergens .allergen-table-wrap{overflow-x:auto;border:1px solid #d9e4df;border-radius:18px;background:#fff;box-shadow:0 8px 24px rgba(20,88,78,.06)}
#docsAllergens .allergen-table{border-collapse:separate;border-spacing:0;min-width:1040px;width:100%;table-layout:fixed}
#docsAllergens .allergen-table th,#docsAllergens .allergen-table td{box-sizing:border-box;border-right:1px solid #e3ebe8;border-bottom:1px solid #e3ebe8;text-align:center;vertical-align:middle;padding:0}
#docsAllergens .allergen-table th{height:92px;background:#eef6f3;color:#14584e;font-size:0;font-weight:800;line-height:1.1}
#docsAllergens .allergen-table th:first-child{width:215px;min-width:215px;text-align:left;padding:0 15px;background:#e8f2ef;position:sticky;left:0;z-index:5}
#docsAllergens .allergen-table th:first-child::before{content:'Pizza';display:block;font-family:Georgia,serif;font-size:15px;color:#14584e;margin-bottom:4px}
#docsAllergens .allergen-table th:first-child::after{content:'Allergen record';display:block;font-family:Inter,system-ui,sans-serif;font-size:9px;color:#6c817b;font-weight:700;letter-spacing:.5px}
#docsAllergens .allergen-table th:not(:first-child):not(:last-child){width:60px;min-width:60px;padding:7px 3px}
#docsAllergens .allergen-table th:not(:first-child):not(:last-child)::before{display:grid;place-items:center;margin:0 auto 5px;width:30px;height:30px;border-radius:9px;background:#14584e;color:#fff;font-family:Inter,system-ui,sans-serif;font-size:10px;font-weight:900}
#docsAllergens .allergen-table th:nth-child(2)::before{content:'Ce'}
#docsAllergens .allergen-table th:nth-child(3)::before{content:'Gl'}
#docsAllergens .allergen-table th:nth-child(4)::before{content:'Cr'}
#docsAllergens .allergen-table th:nth-child(5)::before{content:'Eg'}
#docsAllergens .allergen-table th:nth-child(6)::before{content:'Fi'}
#docsAllergens .allergen-table th:nth-child(7)::before{content:'Lu'}
#docsAllergens .allergen-table th:nth-child(8)::before{content:'Mi'}
#docsAllergens .allergen-table th:nth-child(9)::before{content:'Mo'}
#docsAllergens .allergen-table th:nth-child(10)::before{content:'Mu'}
#docsAllergens .allergen-table th:nth-child(11)::before{content:'Pe'}
#docsAllergens .allergen-table th:nth-child(12)::before{content:'Se'}
#docsAllergens .allergen-table th:nth-child(13)::before{content:'So'}
#docsAllergens .allergen-table th:nth-child(14)::before{content:'Su'}
#docsAllergens .allergen-table th:nth-child(15)::before{content:'Nu'}
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
#docsAllergens .allergen-table th:nth-child(n+2):nth-child(-n+15)::after{display:block;font-family:Inter,system-ui,sans-serif;font-size:7px;font-weight:750;color:#637a74;white-space:nowrap}
#docsAllergens .allergen-table th:last-child{width:1px;min-width:1px;padding:0;border:0;background:#fff;font-size:0}
#docsAllergens .allergen-table td{height:62px;background:#fff}
#docsAllergens .allergen-table td:first-child{width:215px;min-width:215px;text-align:left;padding:8px 38px 8px 15px;position:sticky;left:0;z-index:4;background:#fff}
#docsAllergens .allergen-table td:first-child b{display:block;font-family:Inter,system-ui,sans-serif;font-size:12px;line-height:1.2;color:#183f39;font-weight:850;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#docsAllergens .allergen-table td:first-child .allergen-status{display:inline-flex;align-items:center;margin-top:5px;padding:0;background:transparent;color:#70827d;font-size:8px;font-weight:700;line-height:1}
#docsAllergens .allergen-table td:first-child .allergen-status::before{content:'✓';display:grid;place-items:center;width:16px;height:16px;margin-right:5px;border-radius:50%;background:#14584e;color:#fff;font-size:9px;font-weight:900}
#docsAllergens .allergen-table td:first-child .allergen-status.unverified{color:#876914}
#docsAllergens .allergen-table td:first-child .allergen-status.unverified::before{content:'!';background:#ffeab0;color:#876914}
#docsAllergens .allergen-cell{font-size:0!important;color:transparent!important;background:#fff!important}
#docsAllergens .allergen-cell::before{content:'—';display:inline-grid;place-items:center;width:30px;height:30px;border-radius:8px;background:#edf2f0;color:#899a95;font-family:Inter,system-ui,sans-serif;font-size:11px;font-weight:900}
#docsAllergens .allergen-cell.c::before{content:'C';background:#f3c9c5;color:#a04e48}
#docsAllergens .allergen-cell.m::before{content:'M';background:#ffe8ac;color:#876914}
#docsAllergens .allergen-table .allergen-actions{position:absolute;right:5px;top:20px;display:flex;gap:3px;margin:0;opacity:.32}
#docsAllergens .allergen-table .allergen-actions button{width:21px;height:21px;padding:0;border-radius:7px;background:#fff;border:1px solid #d7e1dd;font-size:0}
#docsAllergens .allergen-table .allergen-actions button:first-child::before{content:'✎';font-size:9px;color:#14584e}
#docsAllergens .allergen-table .allergen-actions button:last-child::before{content:'×';font-size:12px;color:#a14b45}
#docsAllergens .allergen-table tr:last-child td{border-bottom:0}

/* Explanation section under the matrix */
#docsAllergens .allergen-explanations{margin-top:18px;padding:18px 18px 16px;border:1px solid #d9e4df;border-radius:18px;background:#f7faf9}
#docsAllergens .allergen-explanations-head{display:flex;align-items:flex-end;justify-content:space-between;gap:12px;margin-bottom:13px}
#docsAllergens .allergen-explanations h3{margin:0;font-family:Georgia,serif;font-size:21px;line-height:1.1;color:#14584e}
#docsAllergens .allergen-explanations-head p{margin:0;color:#71817d;font-size:10px;line-height:1.35;text-align:right}
#docsAllergens .allergen-explanation-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
#docsAllergens .allergen-explanation{display:flex;align-items:flex-start;gap:9px;padding:10px 11px;border:1px solid #e0e8e5;border-radius:12px;background:#fff}
#docsAllergens .allergen-explanation-code{flex:0 0 29px;height:29px;border-radius:8px;background:#14584e;color:#fff;display:grid;place-items:center;font-size:9px;font-weight:900}
#docsAllergens .allergen-explanation strong{display:block;color:#234941;font-size:10px;line-height:1.2;margin-bottom:2px}
#docsAllergens .allergen-explanation span{display:block;color:#71817d;font-size:9px;line-height:1.35}
#docsAllergens .allergen-explanations .allergen-explanation-note{margin:11px 0 0;padding-top:10px;border-top:1px solid #e1e9e6;color:#71817d;font-size:9px;line-height:1.4}

@media(max-width:620px){
 #docsAllergens .allergen-table{min-width:1000px}
 #docsAllergens .allergen-table th:first-child,#docsAllergens .allergen-table td:first-child{width:175px;min-width:175px}
 #docsAllergens .allergen-table th:not(:first-child):not(:last-child){width:56px;min-width:56px}
 #docsAllergens .allergen-table td{height:58px}
 #docsAllergens .allergen-table td:first-child{width:175px;min-width:175px;padding-left:12px}
 #docsAllergens .allergen-explanation-grid{grid-template-columns:1fr}
 #docsAllergens .allergen-explanations-head{display:block}
 #docsAllergens .allergen-explanations-head p{text-align:left;margin-top:5px}
}
</style>
'''

explanation_js = r'''<script id="blaskos-allergen-design-v7-js">
(function(){
  const items=[
    ['Ce','Celery','Celery and products made from celery.'],
    ['Gl','Cereals containing gluten','Wheat, rye, barley, oats and related gluten-containing cereals.'],
    ['Cr','Crustaceans','Prawns, crabs, lobsters and other crustaceans.'],
    ['Eg','Eggs','Eggs and products made using eggs.'],
    ['Fi','Fish','Fish and products made from fish.'],
    ['Lu','Lupin','Lupin and products made from lupin.'],
    ['Mi','Milk','Milk and dairy products, including lactose.'],
    ['Mo','Molluscs','Mussels, squid, oysters and other molluscs.'],
    ['Mu','Mustard','Mustard and products made using mustard.'],
    ['Pe','Peanuts','Peanuts and products made from peanuts.'],
    ['Se','Sesame','Sesame seeds and products made using sesame.'],
    ['So','Soya','Soya and products made using soya.'],
    ['Su','Sulphites','Sulphur dioxide/sulphites above the regulated threshold.'],
    ['Nu','Tree nuts','Almonds, hazelnuts, walnuts, cashews, pecans, Brazil nuts, pistachios and macadamias.']
  ];
  function addExplanations(){
    const panel=document.getElementById('docsAllergens');
    const wrap=panel&&panel.querySelector('#allergenTableWrap');
    if(!wrap || panel.querySelector('.allergen-explanations')) return;
    const box=document.createElement('section');
    box.className='allergen-explanations';
    box.innerHTML='<div class="allergen-explanations-head"><div><div class="eyebrow">Allergen guide</div><h3>What the allergen codes mean</h3></div><p>Use the recipe and supplier specification to verify each pizza.</p></div><div class="allergen-explanation-grid">'+items.map(x=>'<div class="allergen-explanation"><div class="allergen-explanation-code">'+x[0]+'</div><div><strong>'+x[1]+'</strong><span>'+x[2]+'</span></div></div>').join('')+'</div><p class="allergen-explanations-note"><b>Important:</b> This guide explains the 14 regulated allergen groups used in the matrix. Always check the current ingredient label/specification and your recipe before marking a pizza as verified.</p>';
    wrap.insertAdjacentElement('afterend',box);
  }
  function run(){addExplanations()}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();
  window.addEventListener('load',run);
})();
</script>
'''

# Remove any previous V7 block, then add the new one directly after the real <head> tag.
s = re.sub(r'<style id="blaskos-allergen-design-v7">.*?</style>\s*', '', s, flags=re.S)
s = re.sub(r'<script id="blaskos-allergen-design-v7-js">.*?</script>\s*', '', s, flags=re.S)
head = s.find('<head>')
if head < 0:
    raise SystemExit('Could not find real <head> tag')
insert_at = head + len('<head>')
s = s[:insert_at] + '\n' + css + explanation_js + s[insert_at:]
p.write_text(s, encoding='utf-8')
print('Applied allergen matrix V7')
