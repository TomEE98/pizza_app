from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
old="not in this records-only export.</p>')}"
new="not in this records-only export.</p>'}"
if old not in s:
    raise SystemExit('Expected inspection pack syntax marker not found')
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
