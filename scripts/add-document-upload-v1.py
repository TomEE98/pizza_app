from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='blaskos-document-library-v1'
if marker in s:
    raise SystemExit('Document library already installed; aborting.')

css=r'''<style id="blaskos-document-library-v1">
.document-list{display:grid;gap:10px;margin-top:12px}
.document-card{display:grid;grid-template-columns:42px minmax(0,1fr);gap:11px;padding:13px;border:1px solid var(--line);border-radius:17px;background:#fff}
.document-icon{width:42px;height:42px;border-radius:13px;background:var(--mint);color:var(--green);display:grid;place-items:center;font-size:20px;font-weight:900}
.document-main{min-width:0}.document-title{font-weight:900;font-size:15px;line-height:1.25;color:var(--ink);word-break:break-word}
.document-meta{font-size:10px;color:var(--muted);margin-top:4px;line-height:1.35;word-break:break-word}
.document-file{display:inline-block;margin-top:6px;padding:5px 8px;border-radius:8px;background:#f1f6f4;color:#48645f;font-size:10px;font-weight:800;max-width:100%;word-break:break-word}
.document-file.missing{background:#fff5e3;color:#866b20}.document-notes{font-size:11px;color:var(--muted);margin-top:6px;line-height:1.4;white-space:pre-wrap}
.document-actions{grid-column:1/-1;display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-top:2px}.document-actions button{width:100%;padding:9px 5px;font-size:10px}
@media(max-width:390px){.document-actions{grid-template-columns:repeat(2,1fr)}.document-card{padding:11px}}
</style>'''

js=r'''<script id="blaskos-document-library-v1">
(function(){
'use strict';
const DOC_DB='blaskosDocumentFilesV1';
let docDBPromise=null;
function openDocDB(){
  if(docDBPromise)return docDBPromise;
  docDBPromise=new Promise((resolve,reject)=>{
    if(!('indexedDB' in window)){reject(new Error('IndexedDB unavailable'));return}
    const req=indexedDB.open(DOC_DB,1);
    req.onupgradeneeded=()=>{const d=req.result;if(!d.objectStoreNames.contains('documents'))d.createObjectStore('documents',{keyPath:'id'})};
    req.onsuccess=()=>resolve(req.result);req.onerror=()=>reject(req.error||new Error('Document storage unavailable'));
  });
  return docDBPromise;
}
function putDocFile(id,file){return openDocDB().then(d=>new Promise((resolve,reject)=>{const tx=d.transaction('documents','readwrite');tx.objectStore('documents').put({id,file});tx.oncomplete=resolve;tx.onerror=()=>reject(tx.error||new Error('File save failed'))}))}
function getDocFile(id){return openDocDB().then(d=>new Promise((resolve,reject)=>{const tx=d.transaction('documents','readonly'),r=tx.objectStore('documents').get(id);r.onsuccess=()=>resolve(r.result?.file||null);r.onerror=()=>reject(r.error||new Error('File read failed'))}))}
function deleteDocFile(id){return openDocDB().then(d=>new Promise((resolve,reject)=>{const tx=d.transaction('documents','readwrite');tx.objectStore('documents').delete(id);tx.oncomplete=resolve;tx.onerror=()=>reject(tx.error||new Error('File delete failed'))}))}
function esc(v){return String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function docsArray(){
  if(!Array.isArray(db.docs))db.docs=[];
  let changed=false;
  db.docs=db.docs.map((d,i)=>{
    if(typeof d==='string'){changed=true;return{id:'legacy-'+Date.now()+'-'+i,title:d,fileName:'',mimeType:'',size:0,category:'Other',date:today(),notes:'',createdAt:new Date().toISOString(),hasFile:false}}
    return {...d,id:d.id||('doc-'+Date.now()+'-'+i),title:d.title||d.name||'Untitled document',fileName:d.fileName||'',mimeType:d.mimeType||'',size:Number(d.size)||0,category:d.category||'Other',date:d.date||today(),notes:d.notes||'',createdAt:d.createdAt||new Date().toISOString(),hasFile:d.hasFile!==false};
  });
  if(changed)localStorage.setItem(KEY,JSON.stringify(db));
  return db.docs;
}
function sizeD(n){n=Number(n)||0;if(n<1024)return n+' B';if(n<1048576)return (n/1024).toFixed(0)+' KB';return (n/1048576).toFixed(1)+' MB'}
function iconD(m){if(/^image\//.test(m||''))return '▧';if(m==='application/pdf')return '▤';return '▱'}
async function renderDocsNew(){
  const el=document.getElementById('docList');if(!el)return;
  const docs=docsArray();
  if(!docs.length){el.innerHTML='<div class="docs-empty">No documents saved yet.<br>Tap “Add document” to upload your first compliance document.</div>';return}
  el.innerHTML='<div class="document-list">'+docs.map((d,i)=>'<div class="document-card" data-doc-id="'+esc(d.id)+'"><div class="document-icon">'+iconD(d.mimeType)+'</div><div class="document-main"><div class="document-title">'+esc(d.title)+'</div><div class="document-meta">'+esc(d.category)+' · '+esc(fmtDate(d.date))+(d.fileName?' · '+esc(d.fileName):'')+'</div>'+(d.fileName?'<div class="document-file">'+iconD(d.mimeType)+' '+esc(sizeD(d.size))+'</div>':'<div class="document-file missing">No file uploaded — title only</div>')+(d.notes?'<div class="document-notes">'+esc(d.notes)+'</div>':'')+'</div><div class="document-actions"><button class="secondary" onclick="blaskoViewDocument('+i+')">View</button><button class="secondary" onclick="blaskoDownloadDocument('+i+')">Download</button><button class="secondary" onclick="blaskoEditDocument('+i+')">Edit</button><button class="secondary danger" onclick="blaskoDeleteDocument('+i+')">Delete</button></div></div>').join('')+'</div>';
}
function addDocumentNew(){openModal('<h3>Add document</h3><p class="muted">Upload the actual file so it is stored with the document record. PDFs, photos and common office documents are supported.</p><label>Document title</label><input id="mDocTitle" placeholder="e.g. Public liability insurance certificate"><label>Category</label><select id="mDocCategory"><option>Insurance</option><option>Food safety</option><option>Risk assessment</option><option>Training</option><option>Supplier / traceability</option><option>Equipment</option><option>Premises</option><option>Other</option></select><label>Document date</label><input id="mDocDate" type="date" value="'+today()+'"><label>File</label><input id="mDocFile" type="file" accept=".pdf,.jpg,.jpeg,.png,.webp,.doc,.docx,.xls,.xlsx,.csv,.txt,application/pdf,image/*"><label>Notes</label><textarea id="mDocNotes" placeholder="Optional notes, expiry date, reference, etc."></textarea><button class="primary" onclick="blaskoSaveDocument()">Upload & save document</button>')}
async function saveDocumentNew(){
  const title=(document.getElementById('mDocTitle')?.value||'').trim(),file=document.getElementById('mDocFile')?.files?.[0];
  if(!title){toast('Enter a document title');return} if(!file){toast('Choose the document file to upload');return}
  try{const id='doc-'+Date.now()+'-'+Math.random().toString(36).slice(2,8);await putDocFile(id,file);docsArray().push({id,title,fileName:file.name,mimeType:file.type||'application/octet-stream',size:file.size||0,category:document.getElementById('mDocCategory').value,date:document.getElementById('mDocDate').value||today(),notes:(document.getElementById('mDocNotes').value||'').trim(),createdAt:new Date().toISOString(),hasFile:true});localStorage.setItem(KEY,JSON.stringify(db));closeModal();renderDocsNew();toast('Document uploaded and saved')}catch(e){console.error(e);toast('Could not save the document. Please try again.')}
}
function editDocumentNew(i){const d=docsArray()[i];if(!d)return;openModal('<h3>Edit document</h3><label>Document title</label><input id="mDocTitle" value="'+esc(d.title)+'"><label>Category</label><select id="mDocCategory">'+['Insurance','Food safety','Risk assessment','Training','Supplier / traceability','Equipment','Premises','Other'].map(x=>'<option '+(x===d.category?'selected':'')+'>'+x+'</option>').join('')+'</select><label>Document date</label><input id="mDocDate" type="date" value="'+esc(d.date||today())+'"><label>Replace file <span class="muted">(optional)</span></label><input id="mDocFile" type="file" accept=".pdf,.jpg,.jpeg,.png,.webp,.doc,.docx,.xls,.xlsx,.csv,.txt,application/pdf,image/*"><label>Notes</label><textarea id="mDocNotes">'+esc(d.notes)+'</textarea><button class="primary" onclick="blaskoUpdateDocument('+i+')">Save changes</button>')}
async function updateDocumentNew(i){
  const d=docsArray()[i];if(!d)return;const title=(document.getElementById('mDocTitle')?.value||'').trim();if(!title){toast('Enter a document title');return}
  const file=document.getElementById('mDocFile')?.files?.[0];
  try{if(file){await putDocFile(d.id,file);Object.assign(d,{fileName:file.name,mimeType:file.type||'application/octet-stream',size:file.size||0,hasFile:true})}Object.assign(d,{title,category:document.getElementById('mDocCategory').value,date:document.getElementById('mDocDate').value||d.date||today(),notes:(document.getElementById('mDocNotes').value||'').trim()});localStorage.setItem(KEY,JSON.stringify(db));closeModal();renderDocsNew();toast('Document updated')}catch(e){console.error(e);toast('Could not update the document')}
}
async function viewDocumentNew(i){const d=docsArray()[i];if(!d)return;try{const f=await getDocFile(d.id);if(!f){toast('No uploaded file is stored for this document');return}const url=URL.createObjectURL(f);const w=window.open(url,'_blank');if(!w){toast('Allow pop-ups to view the document');URL.revokeObjectURL(url);return}setTimeout(()=>URL.revokeObjectURL(url),60000)}catch(e){console.error(e);toast('Could not open the document')}}
async function downloadDocumentNew(i){const d=docsArray()[i];if(!d)return;try{const f=await getDocFile(d.id);if(!f){toast('No uploaded file is stored for this document');return}const url=URL.createObjectURL(f),a=document.createElement('a');a.href=url;a.download=d.fileName||d.title;document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),2000)}catch(e){console.error(e);toast('Could not download the document')}}
async function deleteDocumentNew(i){const d=docsArray()[i];if(!d)return;if(!confirm('Delete “'+d.title+'” and its uploaded file? This cannot be undone.'))return;try{await deleteDocFile(d.id)}catch(e){console.warn(e)}db.docs.splice(i,1);localStorage.setItem(KEY,JSON.stringify(db));renderDocsNew();toast('Document deleted')}
window.renderDocs=renderDocsNew;window.addDocument=addDocumentNew;window.saveDoc=saveDocumentNew;window.renameDoc=editDocumentNew;window.blaskoSaveDocument=saveDocumentNew;window.blaskoViewDocument=viewDocumentNew;window.blaskoDownloadDocument=downloadDocumentNew;window.blaskoEditDocument=editDocumentNew;window.blaskoUpdateDocument=updateDocumentNew;window.blaskoDeleteDocument=deleteDocumentNew;
const oldSetDocsTab=window.setDocsTab;window.setDocsTab=function(tab){if(typeof oldSetDocsTab==='function')oldSetDocsTab(tab);if(tab==='documents')setTimeout(renderDocsNew,0)};
const oldRenderAll=window.renderAll;window.renderAll=function(){if(typeof oldRenderAll==='function')oldRenderAll();setTimeout(renderDocsNew,0)};
function boot(){docsArray();renderDocsNew()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();window.addEventListener('load',boot);
})();
</script>'''

pos=s.rfind('</body>')
if pos<0: raise SystemExit('Final </body> not found; aborting.')
s=s[:pos]+css+'\n'+js+'\n'+s[pos:]
p.write_text(s,encoding='utf-8')
print('Added functional document upload/download/view/edit/delete library.')
