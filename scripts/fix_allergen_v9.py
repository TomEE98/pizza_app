from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

style = r'''<style id="blaskos-allergen-design-v9">
/* V9 — compact reference-style matrix: short allergen codes + cleaner pizza rows */
#docsAllergens .allergen-table-wrap{overflow-x:auto!important;border:1px solid #d8e2de!important;border-radius:14px!important;background:#fff!important;box-shadow:0 4px 14px rgba(20,88,78,.045)!important;-webkit-overflow-scrolling:touch!important}
#docsAllergens .allergen-table{width:540px!important;min-width:540px!important;table-layout:fixed!important;border-collapse:separate!important;border-spacing:0!important}
#docsAllergens .allergen-table th,#docsAllergens .allergen-table td{box-sizing:border-box!important;padding:0!important;text-align:center!important;vertical-align:middle!important;border-right:1px solid #e3e9e7!important;border-bottom:1px solid #e3e9e7!important}
#docsAllergens .allergen-table th{height:30px!important;background:#eaf3f0!important;color:#46645e!important;font-size:0!important;line-height:1!important;font-weight:800!important;white-space:nowrap!important}
#docsAllergens .allergen-table th:first-child{width:108px!important;min-width:108px!important;text-align:left!important;padding-left:9px!important;position:sticky!important;left:0!important;z-index:6!important;background:#eaf3f0!important}
#docsAllergens .allergen-table th:first-child::before{content:'Menu item'!important;display:block!important;font-family:Inter,system-ui,sans-serif!important;font-size:7px!important;color:#46645e!important;font-weight:800!important}
#docsAllergens .allergen-table th:first-child::after{display:none!important;content:none!important}
#docsAllergens .allergen-table th:nth-child(n+2):nth-child(-n+15){width:31px!important;min-width:31px!important;font-size:0!important;color:transparent!important;padding:0!important}
#docsAllergens .allergen-table th:nth-child(n+2):nth-child(-n+15)::before{display:grid!important;place-items:center!important;width:auto!important;height:auto!important;margin:0!important;background:none!important;border:0!important;border-radius:0!important;color:#46645e!important;font-family:Inter,system-ui,sans-serif!important;font-size:7px!important;line-height:1!important;font-weight:900!important}
#docsAllergens .allergen-table th:nth-child(2)::before{content:'Ce'!important}
#docsAllergens .allergen-table th:nth-child(3)::before{content:'Gl'!important}
#docsAllergens .allergen-table th:nth-child(4)::before{content:'Cr'!important}
#docsAllergens .allergen-table th:nth-child(5)::before{content:'Eg'!important}
#docsAllergens .allergen-table th:nth-child(6)::before{content:'Fi'!important}
#docsAllergens .allergen-table th:nth-child(7)::before{content:'Lu'!important}
#docsAllergens .allergen-table th:nth-child(8)::before{content:'Mi'!important}
#docsAllergens .allergen-table th:nth-child(9)::before{content:'Mo'!important}
#docsAllergens .allergen-table th:nth-child(10)::before{content:'Mu'!important}
#docsAllergens .allergen-table th:nth-child(11)::before{content:'Pe'!important}
#docsAllergens .allergen-table th:nth-child(12)::before{content:'Se'!important}
#docsAllergens .allergen-table th:nth-child(13)::before{content:'So'!important}
#docsAllergens .allergen-table th:nth-child(14)::before{content:'Su'!important}
#docsAllergens .allergen-table th:nth-child(15)::before{content:'Nu'!important}
#docsAllergens .allergen-table th:nth-child(n+2):nth-child(-n+15)::after{display:none!important;content:none!important}
#docsAllergens .allergen-table th:last-child{width:1px!important;min-width:1px!important;padding:0!important;border:0!important;background:#fff!important;font-size:0!important}
#docsAllergens .allergen-table td{height:34px!important;background:#fff!important;font-size:0!important;line-height:1!important}
#docsAllergens .allergen-table td:first-child{width:108px!important;min-width:108px!important;max-width:108px!important;text-align:left!important;padding:4px 24px 4px 8px!important;position:sticky!important;left:0!important;z-index:5!important;background:#fff!important;overflow:hidden!important}
#docsAllergens .allergen-table td:first-child b{display:block!important;margin:0!important;font-family:Inter,system-ui,sans-serif!important;font-size:7.5px!important;line-height:1.1!important;color:#24453f!important;font-weight:850!important;white-space:nowrap!important;overflow:hidden!important;text-overflow:ellipsis!important}
#docsAllergens .allergen-table td:first-child .allergen-status{display:block!important;margin:2px 0 0!important;padding:0!important;background:none!important;border:0!important;color:#82908c!important;font-family:Inter,system-ui,sans-serif!important;font-size:5.5px!important;line-height:1.05!important;font-weight:650!important;white-space:nowrap!important;overflow:hidden!important;text-overflow:ellipsis!important}
#docsAllergens .allergen-table td:first-child .allergen-status::before{display:none!important;content:none!important}
#docsAllergens .allergen-table .allergen-actions{position:absolute!important;right:2px!important;top:4px!important;display:flex!important;flex-direction:column!important;gap:1px!important;margin:0!important;opacity:.35!important}
#docsAllergens .allergen-table .allergen-actions button{width:14px!important;height:12px!important;min-width:14px!important;padding:0!important;border:0!important;border-radius:4px!important;background:transparent!important;font-size:0!important;line-height:1!important}
#docsAllergens .allergen-table .allergen-actions button:first-child::before{content:'✎'!important;font-size:6px!important;color:#14584e!important}
#docsAllergens .allergen-table .allergen-actions button:last-child::before{content:'×'!important;font-size:8px!important;color:#a14b45!important}
#docsAllergens .allergen-cell{width:31px!important;min-width:31px!important;height:34px!important;padding:0!important;font-size:0!important;color:transparent!important;background:#fff!important;position:relative!important}
#docsAllergens .allergen-cell::before{content:'—'!important;display:inline-grid!important;place-items:center!important;width:16px!important;height:16px!important;margin:0!important;border-radius:5px!important;background:#edf2f0!important;color:#91a09b!important;font-family:Inter,system-ui,sans-serif!important;font-size:6.5px!important;font-weight:900!important;line-height:1!important}
#docsAllergens .allergen-cell.c::before{content:'C'!important;background:#f3cbc7!important;color:#a24f49!important}
#docsAllergens .allergen-cell.m::before{content:'M'!important;background:#ffe8ad!important;color:#896b17!important}
#docsAllergens .allergen-explanations{margin-top:12px!important;padding:5px 0 2px!important;border:0!important;border-radius:0!important;background:transparent!important;box-shadow:none!important}
#docsAllergens .allergen-explanations-head{display:none!important}
#docsAllergens .allergen-explanation-grid{display:grid!important;grid-template-columns:1fr 1fr!important;gap:6px 20px!important}
#docsAllergens .allergen-explanation{display:flex!important;align-items:center!important;gap:6px!important;padding:0!important;border:0!important;border-radius:0!important;background:transparent!important}
#docsAllergens .allergen-explanation-code{width:15px!important;height:15px!important;flex:0 0 15px!important;border-radius:5px!important;background:#e5efec!important;color:#45645e!important;font-size:5.5px!important}
#docsAllergens .allergen-explanation strong{display:block!important;margin:0!important;color:#536b66!important;font-size:6.5px!important;line-height:1.1!important;font-weight:700!important}
#docsAllergens .allergen-explanation span{display:none!important}
#docsAllergens .allergen-explanations .allergen-explanation-note{display:none!important}
#docsAllergens .allergen-table tr:last-child td{border-bottom:0!important}
@media(max-width:390px){
 #docsAllergens .allergen-table{width:540px!important;min-width:540px!important}
 #docsAllergens .allergen-table th:first-child,#docsAllergens .allergen-table td:first-child{width:108px!important;min-width:108px!important;max-width:108px!important}
 #docsAllergens .allergen-table th:nth-child(n+2):nth-child(-n+15),#docsAllergens .allergen-table td:nth-child(n+2):nth-child(-n+15){width:31px!important;min-width:31px!important}
}
</style>'''

# Remove any previous V9 style, then place the new style immediately before the real closing head tag.
start = s.find('<style id="blaskos-allergen-design-v9">')
if start >= 0:
    end = s.find('</style>', start)
    if end >= 0:
        s = s[:start] + s[end + len('</style>'):]

head_end = s.rfind('</head>')
if head_end < 0:
    raise SystemExit('Closing head tag not found')
s = s[:head_end] + style + '\n' + s[head_end:]
p.write_text(s, encoding='utf-8')
