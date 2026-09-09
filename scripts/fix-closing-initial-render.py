from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = 'id="blaskos-closing-initial-render-fix"'
if marker in s:
    print('Fix already present')
    raise SystemExit(0)
patch = r'''
<script id="blaskos-closing-initial-render-fix">
(function(){
  'use strict';
  function refreshClosingFields(){
    try{
      const add=document.getElementById('add');
      const active=document.querySelector('.add-tab.active');
      const type=active?.dataset.type||'';
      if(add?.classList.contains('active') && type==='Closing checklist' && typeof window.renderRecordFields==='function') window.renderRecordFields(type);
    }catch(e){console.error('Closing checklist refresh error',e)}
  }
  const originalGo=window.go;
  if(typeof originalGo==='function') window.go=function(id){const result=originalGo.apply(this,arguments);if(id==='add'){refreshClosingFields();setTimeout(refreshClosingFields,0);setTimeout(refreshClosingFields,60)}return result};
  const originalQuickToday=window.quickToday;
  if(typeof originalQuickToday==='function') window.quickToday=function(type){if(type==='Closing checklist'&&typeof window.setRecordType==='function'){window.go('add');window.setRecordType(type);refreshClosingFields();return}return originalQuickToday.apply(this,arguments)};
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',()=>setTimeout(refreshClosingFields,0)); else setTimeout(refreshClosingFields,0);
  window.addEventListener('load',()=>setTimeout(refreshClosingFields,0));
})();
</script>
'''
pos=s.rfind('</body>')
if pos==-1: raise SystemExit('Final </body> not found')
p.write_text(s[:pos]+patch+s[pos:],encoding='utf-8')
print('Closing initial render fix inserted')
