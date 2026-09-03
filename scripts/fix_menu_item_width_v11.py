from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='</head>'
css='''<style id="blaskos-allergen-v11">\n/* V11: make the Menu item column narrower */\n#docsAllergens .allergen-table th:first-child,#docsAllergens .allergen-table td:first-child{width:145px!important;min-width:145px!important}\n#docsAllergens .allergen-table td:first-child{padding:8px 42px 8px 10px!important}\n#docsAllergens .allergen-table td:first-child b{font-size:12px!important}\n@media(max-width:620px){#docsAllergens .allergen-table{min-width:775px!important;width:775px!important}#docsAllergens .allergen-table th:first-child,#docsAllergens .allergen-table td:first-child{width:145px!important;min-width:145px!important}}\n</style>\n'''
if marker not in s: raise SystemExit('No head marker')
s=s.replace(marker,css+marker,1)
p.write_text(s,encoding='utf-8')
