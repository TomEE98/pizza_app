from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

old = "document.getElementById('stockCount').textContent=db.ingredients.length;"
new = "const stockCount=document.getElementById('stockCount');if(stockCount)stockCount.textContent=db.ingredients.length;"
if old in s:
    s = s.replace(old, new, 1)

old = "function persist(){localStorage.setItem(KEY,JSON.stringify(db));renderAll()}"
new = "function persist(){localStorage.setItem(KEY,JSON.stringify(db));try{renderAll()}catch(e){console.error('Render error after save',e)}}"
if old in s:
    s = s.replace(old, new, 1)

# The Today dashboard has dynamic values (date, progress, plan and core checks),
# but the HTML contains an older static snapshot. Render it synchronously at the
# end of parsing so the user never sees the stale snapshot before navigating away.
marker = 'id="blaskos-today-initial-render-fix"'
if marker not in s:
    patch = '''\n<script id="blaskos-today-initial-render-fix">\n(function(){\n  'use strict';\n  function renderTodayImmediately(){\n    try{\n      if(typeof window.renderToday==='function') window.renderToday();\n    }catch(e){\n      console.error('Today initial render error',e);\n    }\n  }\n  // Run synchronously: this script is placed immediately before the final body\n  // tag, after the main application functions have been defined.\n  renderTodayImmediately();\n  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',renderTodayImmediately,{once:true});\n  window.addEventListener('pageshow',renderTodayImmediately);\n})();\n</script>\n'''
    pos = s.rfind('</body>')
    if pos == -1:
        raise SystemExit('Final </body> not found; aborting.')
    s = s[:pos] + patch + s[pos:]

p.write_text(s, encoding='utf-8')
print('Fixed initial Today dashboard render.')
