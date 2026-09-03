from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

css = '''<style id="blaskos-allergen-final-fix">
/* Final allergen matrix override — inserted outside every JS/template string. */
#docsAllergens .allergen-table{table-layout:fixed!important;width:706px!important;min-width:706px!important}
#docsAllergens .allergen-table thead tr th:first-child,#docsAllergens .allergen-table tbody tr td:first-child{width:90px!important;min-width:90px!important;max-width:90px!important;box-sizing:border-box!important}
#docsAllergens .allergen-table thead tr th:nth-child(n+2):nth-child(-n+15),#docsAllergens .allergen-table tbody tr td:nth-child(n+2):nth-child(-n+15){width:44px!important;min-width:44px!important;max-width:44px!important}
#docsAllergens .allergen-table thead tr th:last-child,#docsAllergens .allergen-table tbody tr td:last-child{width:1px!important;min-width:1px!important;max-width:1px!important}
#docsAllergens .allergen-table th:first-child{padding:6px 5px!important;text-align:left!important}
#docsAllergens .allergen-table th:first-child::before{font-size:10px!important;line-height:1.1!important;white-space:normal!important}
#docsAllergens .allergen-table td:first-child{padding:5px 20px 5px 5px!important;overflow:hidden!important}
#docsAllergens .allergen-table td:first-child b{max-width:78px!important;font-size:9px!important;line-height:1.1!important}
#docsAllergens .allergen-table td:first-child .allergen-status{font-size:6px!important;line-height:1!important;margin-top:3px!important}
#docsAllergens .allergen-table .allergen-actions{right:1px!important;top:13px!important;gap:1px!important}
#docsAllergens .allergen-table .allergen-actions button{width:15px!important;min-width:15px!important;height:15px!important}
#docsAllergens .allergen-table th:nth-child(n+2):nth-child(-n+15)::before{font-size:7px!important}
#docsAllergens .allergen-cell::before{width:16px!important;height:16px!important;border-radius:5px!important;font-size:6px!important}

/* The main modal already has its own Close button. Remove any duplicate Close inside the allergen form. */
#modalContent button[data-allergen-close],#modalContent .allergen-modal-close{display:none!important}
</style>
<script id="blaskos-allergen-final-fix-js">
(function(){
  function removeDuplicateAllergenClose(){
    const root=document.getElementById('modalContent');
    if(!root)return;
    root.querySelectorAll('button').forEach(function(btn){
      const text=(btn.textContent||'').trim().toLowerCase();
      if(text==='close' || btn.hasAttribute('data-allergen-close') || btn.classList.contains('allergen-modal-close')) btn.remove();
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',removeDuplicateAllergenClose);else removeDuplicateAllergenClose();
  const root=document.getElementById('modalContent');
  if(root)new MutationObserver(removeDuplicateAllergenClose).observe(root,{childList:true,subtree:true});
})();
</script>'''

# Do not use </head>, </body> or </html>: those strings also occur inside the print-contract template.
# The last literal </script> is the real end of the app's main script because the print template uses <\\/script>.
pos = s.rfind('</script>')
if pos < 0:
    raise SystemExit('No final script tag found')
insert_at = pos + len('</script>')
s = s[:insert_at] + '\n' + css + s[insert_at:]
p.write_text(s, encoding='utf-8')
