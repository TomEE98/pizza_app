(function(){
  'use strict';
  const C=window.BLASKOS_SUPABASE_CONFIG||{};
  const APPKEY='blaskosPizzaAppV2';
  const BUCKET='blaskos-private';
  const BOOTKEY='blaskoCloudLoadedUser';
  const configured=!!(window.supabase && C.url && C.publishableKey && !/YOUR_PROJECT_ID|YOUR_SUPABASE_PUBLISHABLE_KEY/.test(C.url+' '+C.publishableKey));

  const css=`
  #blaskoAuthGate{position:fixed;inset:0;z-index:99999;background:#f8f0e3;display:flex;align-items:center;justify-content:center;padding:22px;overflow:auto}
  #blaskoAuthGate .auth-card{width:min(440px,100%);background:#fff;border:1px solid #dce7e2;border-radius:24px;box-shadow:0 18px 50px rgba(20,88,78,.14);padding:26px}
  #blaskoAuthGate .auth-mark{width:52px;height:52px;border-radius:16px;background:#14584e;color:#fff;display:grid;place-items:center;font-family:Georgia,serif;font-size:22px;margin-bottom:16px}
  #blaskoAuthGate h1{margin:0 0 8px;font-family:Georgia,serif;color:#14584e;font-size:30px}
  #blaskoAuthGate p{color:#657771;font-size:13px;line-height:1.5;margin:0 0 18px}
  #blaskoAuthGate label{display:block;color:#234941;font-size:12px;font-weight:800;margin:12px 0 6px}
  #blaskoAuthGate input{width:100%;box-sizing:border-box;border:1px solid #cfded9;border-radius:12px;padding:12px 13px;font:inherit;background:#fbfdfc}
  #blaskoAuthGate .auth-actions{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-top:16px}
  #blaskoAuthGate button{border:0;border-radius:12px;padding:12px 13px;font-weight:800;cursor:pointer}
  #blaskoAuthGate .primary{background:#14584e;color:#fff}.secondary{background:#edf4f1;color:#14584e}
  #blaskoAuthGate .auth-link{background:transparent;color:#14584e;padding:10px 0;text-align:left;font-size:12px}
  #blaskoAuthGate .auth-status{min-height:18px;margin-top:12px;color:#a04e48;font-size:12px;line-height:1.4}
  #blaskoAuthGate .auth-status.ok{color:#14584e}
  #blaskoAccount{position:fixed;right:14px;top:12px;z-index:9000;display:flex;align-items:center;gap:7px;background:rgba(255,255,255,.96);border:1px solid #d6e2de;border-radius:999px;padding:5px 7px 5px 10px;box-shadow:0 6px 20px rgba(20,88,78,.1);font-size:10px;color:#36544d}
  #blaskoAccount button{border:0;background:#edf4f1;color:#14584e;border-radius:999px;padding:6px 9px;font-size:10px;font-weight:800;cursor:pointer}
  #blaskoCloudSetup{margin-top:18px;padding:16px;border:1px solid #f0d9a7;background:#fff8e9;border-radius:16px;color:#6c5a31}
  #blaskoCloudSetup h3{margin:0 0 6px;color:#5f4b21;font-size:15px}
  #blaskoCloudSetup p{margin:0;font-size:12px;line-height:1.45}
  #blaskoCloudStatus{margin-top:10px;font-size:11px;color:#657771}
  `;
  const style=document.createElement('style'); style.id='blaskos-cloud-auth-style'; style.textContent=css; document.head.appendChild(style);

  function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
  function toastMsg(msg,ok){
    try{if(typeof window.toast==='function'){window.toast(msg);return;}}catch(e){}
    const el=document.getElementById('blaskoCloudStatus');if(el){el.textContent=msg;el.style.color=ok?'#14584e':'#a04e48';}
  }
  function appData(){try{return JSON.parse(localStorage.getItem(APPKEY)||'{}')}catch(e){return {}}}
  function setAppData(data){localStorage.setItem(APPKEY,JSON.stringify(data));}
  function cloud(){return window.supabase.createClient(C.url,C.publishableKey,{auth:{persistSession:true,autoRefreshToken:true,detectSessionInUrl:true}})}

  if(!configured){
    const box=document.createElement('div');box.id='blaskoCloudSetup';
    box.innerHTML='<h3>Cloud login not connected yet</h3><p>Add the Supabase Project URL and browser-safe Publishable key to <b>supabase-config.js</b>, then run the supplied SQL schema. No service-role or secret key belongs in this file.</p>';
    const target=document.getElementById('docsDocuments')||document.getElementById('docs');if(target)target.appendChild(box);
    return;
  }

  const sb=cloud();window.blaskosSupabase=sb;
  let session=null,ready=false,saveTimer=null,syncing=false;

  function gate(){
    let el=document.getElementById('blaskoAuthGate');if(el)return el;
    el=document.createElement('div');el.id='blaskoAuthGate';
    el.innerHTML=`<div class="auth-card"><div class="auth-mark">B</div><h1>Blasko’s Pizza</h1><p>Sign in to securely access your food-safety records and uploaded documents. Records are stored against your account, not only in this browser.</p><label for="blaskoAuthEmail">Email</label><input id="blaskoAuthEmail" type="email" autocomplete="email" placeholder="you@example.com"><label for="blaskoAuthPassword">Password</label><input id="blaskoAuthPassword" type="password" autocomplete="current-password" placeholder="At least 8 characters"><div class="auth-actions"><button class="primary" id="blaskoSignIn">Sign in</button><button class="secondary" id="blaskoSignUp">Create account</button></div><button class="auth-link" id="blaskoReset">Forgotten password?</button><div class="auth-status" id="blaskoAuthStatus"></div></div>`;
    document.body.appendChild(el);
    const status=t=>{document.getElementById('blaskoAuthStatus').textContent=t;};
    document.getElementById('blaskoSignIn').onclick=async()=>{status('Signing in…');const email=document.getElementById('blaskoAuthEmail').value.trim();const password=document.getElementById('blaskoAuthPassword').value;if(!email||!password)return status('Enter your email and password.');const r=await sb.auth.signInWithPassword({email,password});if(r.error)return status(r.error.message);status('Signed in. Loading your records…');};
    document.getElementById('blaskoSignUp').onclick=async()=>{status('Creating account…');const email=document.getElementById('blaskoAuthEmail').value.trim();const password=document.getElementById('blaskoAuthPassword').value;if(!email||password.length<8)return status('Enter an email and a password of at least 8 characters.');const r=await sb.auth.signUp({email,password});if(r.error)return status(r.error.message);status(r.data.session?'Account created. Loading…':'Account created. Check your email to verify the account, then sign in.');};
    document.getElementById('blaskoReset').onclick=async()=>{const email=document.getElementById('blaskoAuthEmail').value.trim();if(!email)return status('Enter your email first.');const r=await sb.auth.resetPasswordForEmail(email,{redirectTo:location.origin+location.pathname});status(r.error?r.error.message:'Password reset email sent.');};
    return el;
  }
  function showGate(msg){const g=gate();g.style.display='flex';if(msg)document.getElementById('blaskoAuthStatus').textContent=msg;}
  function hideGate(){const g=document.getElementById('blaskoAuthGate');if(g)g.style.display='none';}
  function accountBar(){let el=document.getElementById('blaskoAccount');if(!el){el=document.createElement('div');el.id='blaskoAccount';document.body.appendChild(el);}el.innerHTML='<span>'+esc(session?.user?.email||'Signed in')+'</span><button id="blaskoSignOut">Sign out</button>';el.querySelector('#blaskoSignOut').onclick=async()=>{await sb.auth.signOut();};}

  const FILE_TABLE='blaskos_file_records';
  function keyString(k){try{return JSON.stringify(k)}catch(e){return String(k)}}
  function safePart(s){return String(s).replace(/[^a-zA-Z0-9._-]+/g,'_').slice(0,120)}
  async function idbDatabases(){if(indexedDB.databases)return(await indexedDB.databases()).map(x=>x.name).filter(Boolean);return ['blaskosDocumentFilesV1'];}
  function openIdb(name){return new Promise((resolve,reject)=>{const r=indexedDB.open(name);r.onerror=()=>reject(r.error);r.onsuccess=()=>resolve(r.result);});}
  function readStore(db,store){return new Promise((resolve,reject)=>{let out=[];const tx=db.transaction(store,'readonly');const os=tx.objectStore(store);const req=os.openCursor();req.onerror=()=>reject(req.error);req.onsuccess=()=>{const c=req.result;if(!c)return resolve(out);out.push({key:c.key,value:c.value});c.continue();};});}
  async function encodeValue(v,ctx,path){
    if(v instanceof Blob){const ext=(v.type||'application/octet-stream').split('/')[1]?.replace(/[^a-z0-9]+/gi,'')||'bin';const storagePath=`${session.user.id}/idb/${safePart(ctx.db)}/${safePart(ctx.store)}/${safePart(ctx.keyHash)}/${path||'blob'}.${ext}`;const{error}=await sb.storage.from(BUCKET).upload(storagePath,v,{contentType:v.type||'application/octet-stream',upsert:true});if(error)throw error;return{__blaskoBlob:true,path:storagePath,type:v.type||'application/octet-stream',size:v.size,name:v.name||null,isFile:typeof File!=='undefined'&&v instanceof File};}
    if(v instanceof Date)return{__blaskoDate:v.toISOString()};
    if(v===undefined)return{__blaskoUndefined:true};
    if(Array.isArray(v)){const a=[];for(let i=0;i<v.length;i++)a.push(await encodeValue(v[i],ctx,path?path+'.'+i:String(i)));return a;}
    if(v&&typeof v==='object'){const o={};for(const k of Object.keys(v))o[k]=await encodeValue(v[k],ctx,path?path+'.'+safePart(k):safePart(k));return o;}
    return v;
  }
  async function decodeValue(v){
    if(Array.isArray(v)){const a=[];for(const x of v)a.push(await decodeValue(x));return a;}
    if(v&&typeof v==='object'){if(v.__blaskoDate)return new Date(v.__blaskoDate);if(v.__blaskoUndefined)return undefined;if(v.__blaskoBlob){const{data,error}=await sb.storage.from(BUCKET).download(v.path);if(error)throw error;return v.isFile&&v.name?new File([data],v.name,{type:v.type||data.type||'application/octet-stream',lastModified:Date.now()}):data;}const o={};for(const k of Object.keys(v))o[k]=await decodeValue(v[k]);return o;}
    return v;
  }
  async function syncIndexedDbToCloud(){
    if(!ready||!session?.user)return;
    try{const names=await idbDatabases();const seen=[];for(const name of names){let db;try{db=await openIdb(name)}catch(e){continue;}const stores=Array.from(db.objectStoreNames||[]);for(const store of stores){const rows=await readStore(db,store);for(const row of rows){const rk=keyString(row.key),kh=btoa(unescape(encodeURIComponent(rk))).replace(/[^a-zA-Z0-9]/g,'').slice(0,40)||'key';const data=await encodeValue(row.value,{db:name,store,keyHash:kh},'root');await sb.from(FILE_TABLE).upsert({user_id:session.user.id,db_name:name,store_name:store,record_key:rk,data,updated_at:new Date().toISOString()},{onConflict:'user_id,db_name,store_name,record_key'}).throwOnError();seen.push([name,store,rk]);}}db.close();}const{data:remote,error}=await sb.from(FILE_TABLE).select('db_name,store_name,record_key').eq('user_id',session.user.id);if(error)throw error;const keep=new Set(seen.map(x=>x.join('\u001f')));for(const r of(remote||[])){if(!keep.has([r.db_name,r.store_name,r.record_key].join('\u001f')))await sb.from(FILE_TABLE).delete().eq('user_id',session.user.id).eq('db_name',r.db_name).eq('store_name',r.store_name).eq('record_key',r.record_key);}}
    catch(e){console.error('Cloud file sync failed',e);toastMsg('Cloud file sync failed: '+e.message,false);}
  }
  function openIdbForRestore(name,store){return new Promise((resolve,reject)=>{const r=indexedDB.open(name);r.onerror=()=>reject(r.error);r.onupgradeneeded=()=>{const db=r.result;if(!db.objectStoreNames.contains(store))db.createObjectStore(store);};r.onsuccess=()=>{const db=r.result;if(!db.objectStoreNames.contains(store)){db.close();return reject(new Error('Missing object store '+store))}resolve(db);};});}
  function putIdb(db,store,key,value){return new Promise((resolve,reject)=>{const tx=db.transaction(store,'readwrite');tx.objectStore(store).put(value,key);tx.oncomplete=resolve;tx.onerror=()=>reject(tx.error);});}
  async function restoreCloudIndexedDb(){if(!session?.user)return;const{data:rows,error}=await sb.from(FILE_TABLE).select('db_name,store_name,record_key,data').eq('user_id',session.user.id);if(error)throw error;for(const row of(rows||[])){const db=await openIdbForRestore(row.db_name,row.store_name);const value=await decodeValue(row.data);await putIdb(db,row.store_name,JSON.parse(row.record_key),value);db.close();}}

  async function loadCloudState(){
    const uid=session.user.id;
    if(sessionStorage.getItem(BOOTKEY)===uid){ready=true;hideGate();accountBar();return;}
    const{data,error}=await sb.from('blaskos_app_state').select('data').eq('user_id',uid).maybeSingle();
    if(error){showGate('Cloud database error: '+error.message);return;}
    const local=appData();
    if(data?.data&&typeof data.data==='object')setAppData(data.data);else await sb.from('blaskos_app_state').upsert({user_id:uid,data:local,updated_at:new Date().toISOString()},{onConflict:'user_id'});
    await restoreCloudIndexedDb();
    sessionStorage.setItem(BOOTKEY,uid);
    location.reload();
  }
  async function saveCloudState(){if(!ready||!session?.user||syncing)return;syncing=true;try{const data=appData();const{error}=await sb.from('blaskos_app_state').upsert({user_id:session.user.id,data,updated_at:new Date().toISOString()},{onConflict:'user_id'});if(error)throw error;await syncIndexedDbToCloud();}catch(e){console.error('Cloud save failed',e);toastMsg('Cloud save failed: '+e.message,false);}finally{syncing=false;}}
  function queueCloudSave(){clearTimeout(saveTimer);saveTimer=setTimeout(saveCloudState,500);}

  const nativeSet=Storage.prototype.setItem;
  Storage.prototype.setItem=function(key,value){const r=nativeSet.call(this,key,value);if(this===localStorage&&key===APPKEY)queueCloudSave();return r;};
  async function handleAuth(s){session=s;if(!s){ready=false;sessionStorage.removeItem(BOOTKEY);localStorage.removeItem(APPKEY);const a=document.getElementById('blaskoAccount');if(a)a.remove();showGate('You have been signed out.');return;}showGate('Loading your secure records…');await loadCloudState();}
  sb.auth.onAuthStateChange((_event,s)=>{handleAuth(s).catch(e=>{console.error(e);showGate(e.message||'Unable to load account.');});});
  sb.auth.getSession().then(({data})=>handleAuth(data.session)).catch(e=>showGate(e.message));
  window.blaskosCloudStatus=()=>({configured,authenticated:!!session,ready,userId:session?.user?.id||null});
})();
