from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

old = "document.getElementById('stockCount').textContent=db.ingredients.length;"
new = "const stockCount=document.getElementById('stockCount');if(stockCount)stockCount.textContent=db.ingredients.length;"
if old not in s:
    raise SystemExit('Expected stockCount render code was not found; aborting.')
s = s.replace(old, new, 1)

old = "function persist(){localStorage.setItem(KEY,JSON.stringify(db));renderAll()}"
new = "function persist(){localStorage.setItem(KEY,JSON.stringify(db));try{renderAll()}catch(e){console.error('Render error after save',e)}}"
if old not in s:
    raise SystemExit('Expected persist function was not found; aborting.')
s = s.replace(old, new, 1)

p.write_text(s, encoding='utf-8')
print('Fixed live render error and made saves resilient to render errors.')
