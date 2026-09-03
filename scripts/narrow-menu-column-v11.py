from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
css='''<style id="blaskos-allergen-v11">\n#docsAllergens .allergen-table th:first-child,#docsAllergens .allergen-table td:first-child{width:115px!important;min-width:115px!important}\n#docsAllergens .allergen-table td:first-child{padding:8px 34px 7px 9px!important}\n#docsAllergens .allergen-table th:first-child{padding:8px 9px!important}\n#docsAllergens .allergen-table td:first-child b{font-size:11px!important}\n#docsAllergens .allergen-table td:first-child .allergen-status{font-size:7px!important}\n#docsAllergens .allergen-table .allergen-actions{right:4px!important;gap:2px!important}\n#docsAllergens .allergen-table .allergen-actions button{width:19px!important;height:19px!important;border-radius:6px!important}\n@media(max-width:620px){#docsAllergens .allergen-table{min-width:720px!important;width:720px!important}#docsAllergens .allergen-table th:first-child,#docsAllergens .allergen-table td:first-child{width:115px!important;min-width:115px!important}}\n</style>'''
s=s.replace('</head>',css+'\n</head>',1)
p.write_text(s,encoding='utf-8')
