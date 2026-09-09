from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
index = ROOT / 'index.html'
cloud_file = ROOT / 'scripts' / 'cloud-integration.js'
s = index.read_text(encoding='utf-8')
cloud_source = cloud_file.read_text(encoding='utf-8')

client = '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>'
config = '<script src="/supabase-config.js"></script>'

if 'cdn.jsdelivr.net/npm/@supabase/supabase-js@2' not in s:
    head = s.find('</head>')
    if head < 0:
        raise SystemExit('No real </head> found')
    s = s[:head] + client + '\n' + config + '\n' + s[head:]

if 'id="blaskos-cloud-auth"' not in s:
    pos = s.rfind('</body>')
    if pos < 0:
        raise SystemExit('No final </body> found')
    block = '<script id="blaskos-cloud-auth">\n' + cloud_source + '\n</script>\n'
    s = s[:pos] + block + s[pos:]

index.write_text(s, encoding='utf-8')
print('Cloud auth/storage integration applied')
