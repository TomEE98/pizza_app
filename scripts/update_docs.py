from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

css = r'''
/* Docs library tabs + premises */
.docs-tabs{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;background:#e8e3d8;padding:5px;border-radius:18px;margin:14px 0}
.docs-tab{padding:13px 6px;border-radius:14px;background:transparent;color:#64736e;font-size:11px;font-weight:900;white-space:nowrap}
.docs-tab.active{background:#fffdf8;color:var(--green);box-shadow:0 2px 8px rgba(20,88,78,.08)}
.docs-panel{display:none}.docs-panel.active{display:block}
.docs-hero{background:var(--mint);border:1px solid var(--line);border-radius:20px;padding:17px;margin:14px 0}
.docs-hero h3{font-family:Inter,system-ui,sans-serif;font-size:20px;margin:0 0 5px}
.premise-item{padding:15px 0;border-bottom:1px solid var(--line)}.premise-item:last-child{border-bottom:0}
.premise-name{font-size:18px;font-weight:900}.premise-meta{font-size:12px;color:var(--muted);line-height:1.45;margin-top:5px}
.photo-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:12px}
.premise-photo{border:1px solid var(--line);border-radius:16px;background:white;overflow:hidden}
.premise-photo img{display:block;width:100%;aspect-ratio:1/1;object-fit:cover;background:#eef2ef}
.premise-photo-body{padding:10px}.premise-photo-date{font-size:11px;font-weight:900;color:var(--green)}.premise-photo-note{font-size:11px;color:var(--muted);margin-top:3px;line-height:1.35}
.docs-empty{padding:24px 8px;text-align:center;color:var(--muted);font-size:13px}
@media(max-width:390px){.docs-tab{font-size:10px;padding-left:3px;padding-right:3px}}
'''
if '/* Docs library tabs + premises */' not in s:
    s = s.replace('</style>', css + '</style>', 1)

old_docs = '<section id="docs" class="page"><div class="eyebrow">Compliance library</div><h2>Docs</h2><div class="card"><h3>Your compliance pack</h3><p class="muted">Keep the documents you may need for an EHO inspection together. The prototype records document names and status; file uploads can be added next.</p><div id="docList"></div><button class="primary" onclick="addDocument()">+ Add document</button></div></section>'
new_docs = '''<section id="docs" class="page">
 <div class="eyebrow">Compliance library</div><h2>Docs</h2>
 <div class="docs-tabs"><button class="docs-tab active" data-doc-tab="documents" onclick="setDocsTab('documents')">▤ &nbsp; Documents</button><button class="docs-tab" data-doc-tab="premises" onclick="setDocsTab('premises')">⌂ &nbsp; Premises photos</button><button class="docs-tab" data-doc-tab="allergens" onclick="setDocsTab('allergens')">♙ &nbsp; Allergens</button></div>
 <div id="docsDocuments" class="docs-panel active"><div class="card"><h3>Your compliance pack</h3><p class="muted">Keep the documents you may need for an EHO inspection together.</p><div id="docList"></div><button class="primary" onclick="addDocument()">+ Add document</button></div></div>
 <div id="docsPremises" class="docs-panel"><div class="docs-hero"><h3>Premises & site evidence</h3><p class="muted" style="margin:0">Save the premises you operate from and keep dated photographs as evidence of the setup and condition.</p></div><div class="card"><div class="row"><div><h3>Premises</h3><p class="muted">Add each location you use for the business.</p></div><button class="secondary" onclick="addPremise()">＋ Add premises</button></div><div id="premisesList"></div></div><div class="card"><div class="row"><div><h3>Premises photos</h3><p class="muted">Upload a photo, record the date it was taken, and optionally link it to a premises.</p></div><button class="primary" style="width:auto" onclick="addPremisePhoto()">＋ Add photo</button></div><div id="premisePhotosList"></div></div></div>
 <div id="docsAllergens" class="docs-panel"><div class="card"><div class="eyebrow">Menu safety</div><h3>Allergen matrix</h3><p class="muted">This section will contain your verified recipe and allergen matrix.</p><button class="primary" onclick="toast('Allergen matrix coming next')">Open allergen matrix</button></div></div>
</section>'''
if old_docs in s:
    s = s.replace(old_docs, new_docs, 1)

funcs = r'''function setDocsTab(tab){document.querySelectorAll('.docs-tab').forEach(b=>b.classList.toggle('active',b.dataset.docTab===tab));document.querySelectorAll('.docs-panel').forEach(p=>p.classList.remove('active'));const panel=document.getElementById('docs'+tab.charAt(0).toUpperCase()+tab.slice(1));panel?.classList.add('active');if(tab==='premises'){renderPremises();renderPremisePhotos()}else if(tab==='documents'){renderDocs()}}
function addPremise(){openModal('<h3>Add premises</h3><p class="muted">Save the details of a premises or operating location used by Blasko\'s Pizza.</p><label>Premises name</label><input id="mPremiseName" placeholder="e.g. Blasko\'s Pizza trailer"><label>Address</label><textarea id="mPremiseAddress" placeholder="Full address or site location"></textarea><label>Notes</label><textarea id="mPremiseNotes" placeholder="Site details, setup area, access, storage, etc."></textarea><button class="primary" onclick="savePremise()">Save premises</button>')}
function savePremise(){const name=(document.getElementById('mPremiseName')?.value||'').trim();if(!name){toast('Enter a premises name');return}db.premises=Array.isArray(db.premises)?db.premises:[];db.premises.push({id:Date.now()+Math.random(),name,address:(document.getElementById('mPremiseAddress')?.value||'').trim(),notes:(document.getElementById('mPremiseNotes')?.value||'').trim(),createdAt:new Date().toISOString()});closeModal();persist();setDocsTab('premises');toast('Premises saved')}
function deletePremise(id){if(!confirm('Delete these premises? Existing photos will remain but will be marked as Premises removed.'))return;db.premises=db.premises.filter(x=>String(x.id)!==String(id));persist();renderPremises();renderPremisePhotos();toast('Premises deleted')}
function renderPremises(){const el=document.getElementById('premisesList');if(!el)return;el.innerHTML=db.premises?.length?db.premises.map(p=>`<div class="premise-item"><div class="row"><div class="premise-name">${p.name}</div><button class="secondary danger" onclick="deletePremise(${p.id})">Delete</button></div>${p.address?`<div class="premise-meta">⌖ ${p.address}</div>`:''}${p.notes?`<div class="premise-meta">${p.notes}</div>`:''}</div>`).join(''):'<div class="docs-empty">No premises saved yet.<br>Tap “Add premises” to create your first location.</div>'}
const PREMISE_DB='blaskosPremisePhotosV1';
let premisePhotoDBPromise=null;
function openPremisePhotoDB(){if(premisePhotoDBPromise)return premisePhotoDBPromise;premisePhotoDBPromise=new Promise((resolve,reject)=>{if(!('indexedDB' in window)){reject(new Error('IndexedDB unavailable'));return}const req=indexedDB.open(PREMISE_DB,1);req.onupgradeneeded=()=>{const dbi=req.result;if(!dbi.objectStoreNames.contains('photos'))dbi.createObjectStore('photos',{keyPath:'id'})};req.onsuccess=()=>resolve(req.result);req.onerror=()=>reject(req.error||new Error('IndexedDB open failed'))});return premisePhotoDBPromise}
function putPremiseImage(id,image){return openPremisePhotoDB().then(dbi=>new Promise((resolve,reject)=>{const tx=dbi.transaction('photos','readwrite');tx.objectStore('photos').put({id,image});tx.oncomplete=resolve;tx.onerror=()=>reject(tx.error||new Error('Photo save failed'))}))}
function getPremiseImage(id){return openPremisePhotoDB().then(dbi=>new Promise((resolve,reject)=>{const tx=dbi.transaction('photos','readonly'),req=tx.objectStore('photos').get(id);req.onsuccess=()=>resolve(req.result?.image||'');req.onerror=()=>reject(req.error||new Error('Photo read failed'))}))}
function deletePremiseImage(id){return openPremisePhotoDB().then(dbi=>new Promise((resolve,reject)=>{const tx=dbi.transaction('photos','readwrite');tx.objectStore('photos').delete(id);tx.oncomplete=resolve;tx.onerror=()=>reject(tx.error||new Error('Photo delete failed'))}))}
function addPremisePhoto(){if(!db.premises?.length){openModal('<h3>Add premises first</h3><p class="muted">Create at least one premises before adding a site photo.</p><button class="primary" onclick="closeModal();addPremise()">＋ Add premises</button>');return}openModal(`<h3>Add premises photo</h3><label>Premises</label><select id="mPhotoPremise">${db.premises.map(p=>`<option value="${p.id}">${p.name}</option>`).join('')}</select><label>Photo date</label><input id="mPhotoDate" type="date" value="${today()}"><label>Description</label><input id="mPhotoNote" placeholder="e.g. Front of trailer / hand-wash station"><label>Image</label><input id="mPhotoFile" type="file" accept="image/*" capture="environment"><p class="small muted">Photos are stored separately from the diary data so normal phone photos do not exceed localStorage limits.</p><button class="primary" onclick="savePremisePhoto()">Save photo</button>`)}
function savePremisePhoto(){const file=document.getElementById('mPhotoFile')?.files?.[0];if(!file){toast('Choose an image first');return}const reader=new FileReader();reader.onerror=()=>toast('Could not read that image');reader.onload=()=>{const img=new Image();img.onerror=()=>toast('Could not open that image');img.onload=async()=>{try{const max=1000,scale=Math.min(1,max/Math.max(img.width,img.height)),canvas=document.createElement('canvas');canvas.width=Math.max(1,Math.round(img.width*scale));canvas.height=Math.max(1,Math.round(img.height*scale));canvas.getContext('2d').drawImage(img,0,0,canvas.width,canvas.height);const data=canvas.toDataURL('image/jpeg',.7);const id=String(Date.now())+'-'+Math.random().toString(36).slice(2,8);await putPremiseImage(id,data);db.premisePhotos=Array.isArray(db.premisePhotos)?db.premisePhotos:[];db.premisePhotos.unshift({id,premiseId:document.getElementById('mPhotoPremise').value,date:document.getElementById('mPhotoDate').value||today(),note:(document.getElementById('mPhotoNote').value||'').trim(),createdAt:new Date().toISOString()});persist();closeModal();setDocsTab('premises');toast('Premises photo saved')}catch(e){console.error(e);toast('Could not save the photo')}};img.src=reader.result};reader.readAsDataURL(file)}
async function deletePremisePhoto(id){if(!confirm('Delete this premises photo?'))return;try{await deletePremiseImage(String(id))}catch(e){console.warn(e)}db.premisePhotos=db.premisePhotos.filter(x=>String(x.id)!==String(id));persist();renderPremisePhotos();toast('Photo deleted')}
async function renderPremisePhotos(){const el=document.getElementById('premisePhotosList');if(!el)return;const photos=Array.isArray(db.premisePhotos)?db.premisePhotos:[];if(!photos.length){el.innerHTML='<div class="docs-empty">No premises photos saved yet.<br>Use “Add photo” to upload dated site evidence.</div>';return}el.innerHTML='<div class="photo-grid">'+photos.map(x=>{const p=(db.premises||[]).find(y=>String(y.id)===String(x.premiseId));return `<div class="premise-photo" data-photo-id="${x.id}"><div class="premise-photo-image" style="min-height:120px;display:flex;align-items:center;justify-content:center;background:#eef2ef;color:var(--muted);font-size:12px">Loading…</div><div class="premise-photo-body"><div class="premise-photo-date">${fmtDate(x.date)}</div><div class="premise-photo-note">${p?p.name:'Premises removed'}${x.note?' · '+x.note:''}</div><button class="secondary danger" style="width:100%;margin-top:9px" onclick="deletePremisePhoto('${x.id}')">Delete photo</button></div></div>`}).join('')+'</div>';for(const x of photos){try{const image=await getPremiseImage(String(x.id));const card=el.querySelector(`[data-photo-id="${CSS.escape(String(x.id))}"]`);if(card){const box=card.querySelector('.premise-photo-image');if(image)box.innerHTML=`<img src="${image}" alt="${x.note||'Premises photo'}" style="display:block;width:100%;aspect-ratio:1/1;object-fit:cover">`;else box.textContent='Image unavailable'}}catch(e){console.warn(e)}}}
'''
pattern = r"function setDocsTab\(tab\)\{.*?\nfunction renderDocs\(\)\{"
if not re.search(pattern, s, flags=re.S):
    raise SystemExit('Docs function block not found')
s = re.sub(pattern, funcs + 'function renderDocs(){', s, count=1, flags=re.S)

if 'premises:[]' not in s:
    old_defaults = "const defaults={records:[],bookings:[],ingredients:[],suppliers:[],fridges:[],docs:[],staff:[],settings:"
    new_defaults = "const defaults={records:[],bookings:[],ingredients:[],suppliers:[],fridges:[],docs:[],staff:[],premises:[],premisePhotos:[],settings:"
    if old_defaults not in s: raise SystemExit('defaults marker not found')
    s = s.replace(old_defaults,new_defaults,1)

if 'premisePhotos:Array.isArray(x.premisePhotos)' not in s:
    old_load = "fridges:Array.isArray(x.fridges)?x.fridges:[],docs:Array.isArray(x.docs)?x.docs:[],staff:Array.isArray(x.staff)?x.staff:[],settings:"
    new_load = "fridges:Array.isArray(x.fridges)?x.fridges:[],docs:Array.isArray(x.docs)?x.docs:[],staff:Array.isArray(x.staff)?x.staff:[],premises:Array.isArray(x.premises)?x.premises:[],premisePhotos:Array.isArray(x.premisePhotos)?x.premisePhotos:[],settings:"
    if old_load not in s: raise SystemExit('load marker not found')
    s = s.replace(old_load,new_load,1)

p.write_text(s, encoding='utf-8')
print('Docs photo storage fix prepared')
