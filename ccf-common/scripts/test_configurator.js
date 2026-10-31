// Dependency-free controller regressions using a minimal DOM and mock local API.
// This runs the real app.js; it does not replace browser layout/accessibility QA.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const path = require('node:path');
const root = path.resolve(__dirname, '..', '..');
const html = fs.readFileSync(path.join(root, 'ccf-common/assets/configurator/index.html'), 'utf8');
const script = fs.readFileSync(path.join(root, 'ccf-common/assets/configurator/app.js'), 'utf8');
const styles = fs.readFileSync(path.join(root, 'ccf-common/assets/configurator/styles.css'), 'utf8');
const copy = (v) => JSON.parse(JSON.stringify(v));
const defaults = {version:1,preferences:{independent_review:'off',extended_search:'auto',enhanced_document_parsing:'auto',figure_variants:'off',detailed_reports:'off',alternative_routes:'off',maintenance_evolution:'off',reference_style_search:'on',research_branching:'off',research_policy_evolution:'off',results_pending_draft:'off'},ui:{language:'zh-CN',theme:'system'}};

class Element {
  constructor(tag) { this.tagName=tag.toLowerCase();this.children=[];this.attributes={};this.dataset={};this.listeners={};this.parentNode=null;this.disabled=false;this.hidden=false;this.className='';this.value='';this._text='';this.classList={toggle:(name,on)=>{const list=new Set(this.className.split(/\s+/).filter(Boolean));if(on===undefined)on=!list.has(name);if(on)list.add(name);else list.delete(name);this.className=[...list].join(' ');}}; }
  setAttribute(key,value) { this.attributes[key]=String(value);if(key==='id')this.id=value;if(key==='class')this.className=value;if(key==='hidden')this.hidden=true;if(key==='value')this.value=value;if(key.startsWith('data-'))this.dataset[key.slice(5).replace(/-([a-z])/g,(_,c)=>c.toUpperCase())]=value; }
  getAttribute(key) { return this.attributes[key]; }
  append(...nodes) { for(let node of nodes){if(typeof node==='string'){const text=new Element('#text');text._text=node;node=text;}if(node.tagName==='#fragment'){this.append(...node.children);continue;}node.parentNode=this;this.children.push(node);} }
  replaceChildren(...nodes) { this.children=[];this._text='';this.append(...nodes); }
  get textContent() { return this._text+this.children.map(n=>n.textContent).join(''); }
  set textContent(value) { this.children=[];this._text=String(value); }
  matches(selector) {
    const pseudo=selector.match(/:(first|last)-child$/);if(pseudo){selector=selector.replace(/:(first|last)-child$/,'');const siblings=this.parentNode?.children.filter(n=>n.tagName!=='#text')||[];if(this!==siblings[pseudo[1]==='first'?0:siblings.length-1])return false;}
    if(selector.startsWith('#'))return this.id===selector.slice(1);
    if(selector.startsWith('.'))return this.className.split(/\s+/).includes(selector.slice(1));
    if(selector.startsWith('['))return Object.hasOwn(this.attributes,selector.slice(1,-1));
    return this.tagName===selector.toLowerCase();
  }
  descendants() { return this.children.flatMap(node=>[node,...node.descendants()]); }
  querySelectorAll(selector) { const parts=selector.split(/\s+/);return this.descendants().filter(node=>{if(!node.matches(parts.at(-1)))return false;let parent=node.parentNode;for(let i=parts.length-2;i>=0;i--){while(parent&&!parent.matches(parts[i]))parent=parent.parentNode;if(!parent)return false;parent=parent.parentNode;}return true;}); }
  querySelector(selector) { return this.querySelectorAll(selector)[0]||null; }
  addEventListener(type,fn) { (this.listeners[type]||=[]).push(fn); }
  async emit(type) { if(this.disabled)return;for(const fn of this.listeners[type]||[])await fn({target:this,preventDefault(){}}); }
  click() { return this.emit('click'); }
  remove() { if(this.parentNode)this.parentNode.children=this.parentNode.children.filter(node=>node!==this); }
  focus() { this.focused=true; }
  scrollIntoView() {}
}

function documentFromHtml() {
  const doc=new Element('#document');const stack=[doc];const voids=new Set(['meta','link','input','br']);
  for(const token of html.match(/<[^>]*>|[^<]+/g)){
    if(token.startsWith('<!'))continue;
    if(token.startsWith('</')){stack.pop();continue;}
    if(token.startsWith('<')){const match=token.match(/^<([^\s/>]+)/);if(!match)continue;const node=new Element(match[1]);for(const attr of token.matchAll(/([\w-]+)(?:="([^"]*)")?/g)){if(attr.index<match[0].length)continue;node.setAttribute(attr[1],attr[2]??'');}stack.at(-1).append(node);if(!voids.has(node.tagName)&&!token.endsWith('/>'))stack.push(node);}
    else{const text=new Element('#text');text._text=token;stack.at(-1).append(text);}
  }
  doc.documentElement=doc.querySelector('html');doc.body=doc.querySelector('body');
  doc.createElement=(tag)=>new Element(tag);doc.createElementNS=(_,tag)=>new Element(tag);doc.createTextNode=(text)=>{const n=new Element('#text');n._text=text;return n;};doc.createDocumentFragment=()=>new Element('#fragment');
  return doc;
}

function fixture(online=true, initialFail=false) {
  const document=documentFromHtml();const files={user:null,project:null};const revisions={user:'missing',project:'missing'};let serial=0;let fail=initialFail;const calls=[];
  const merged=(base,override)=>({version:1,preferences:{...base.preferences,...override?.preferences},ui:{...base.ui,...override?.ui}});
  const snapshot=(scope)=>{const inherited=scope==='user'?copy(defaults):merged(defaults,files.user);return {version:1,scope,availableScopes:['user','project'],stored:copy(files[scope]),effective:merged(inherited,files[scope]),inherited,origins:{},revision:revisions[scope],defaults:copy(defaults)};};
  const fetch=async(url,options)=>{calls.push({url,options});if(fail)throw Error('Offline');assert.equal(options.headers['X-CCFA-Token'],'test-session');if(options.method==='POST'){const body=JSON.parse(options.body);if(body.revision!==revisions[body.scope])return {ok:false,status:409,json:async()=>({code:'revision_conflict'})};files[body.scope]=copy(body.config);revisions[body.scope]=`rev-${++serial}`;return {ok:true,json:async()=>snapshot(body.scope)};}const scope=new URL(url,'http://127.0.0.1').searchParams.get('scope');return {ok:true,json:async()=>snapshot(scope)};};
  const urlClass=URL;urlClass.createObjectURL=()=> 'blob:test';urlClass.revokeObjectURL=()=>{};
  const eventListeners={};const media={matches:false,addEventListener(){}};const window={matchMedia:()=>media,addEventListener:(type,fn)=>eventListeners[type]=fn,scrollTo(){},confirm:()=>true};
  const context=vm.createContext({document,window,location:{hash:online?'#token=test-session':'',hostname:online?'127.0.0.1':'',protocol:online?'http:':'file:'},URL:urlClass,URLSearchParams,Blob,TextDecoder,setTimeout:()=>1,clearTimeout(){},fetch,console});
  vm.runInContext(script,context);
  return {context,document,files,calls,revisions,eval:(code)=>vm.runInContext(code,context),setFail:(value)=>fail=value,mutate:(scope,config)=>{files[scope]=copy(config);revisions[scope]=`rev-${++serial}`;}};
}

const flush=()=>new Promise(resolve=>setImmediate(resolve));
function modeControl(f,key){
  const control=f.document.querySelectorAll('.mode-select').find(node=>node.dataset.modeKey===key);
  assert.ok(control,`Missing mode control for ${key}`);
  return control;
}
async function chooseMode(f,key,mode){
  const control=modeControl(f,key);control.value=mode;await control.emit('change');
  assert.equal(modeControl(f,key).value,mode,`${key} must show its explicit or inherited choice`);
}
async function choosePreset(f,name){
  const button=f.document.querySelectorAll('[data-preset]').find(node=>node.dataset.preset===name);
  assert.ok(button,`Missing preset ${name}`);await button.click();
}
async function run(){
  const f=fixture();await flush();
  const expectedKeys=Object.keys(defaults.preferences);
  assert.equal(expectedKeys.length,11);
  assert.deepEqual(JSON.parse(f.eval('JSON.stringify(KEYS)')),expectedKeys);
  assert.deepEqual(JSON.parse(f.eval('JSON.stringify(DEFAULTS)')),defaults);
  assert.equal(f.document.querySelectorAll('.feature').length,expectedKeys.length);
  assert.equal(f.document.querySelectorAll('.control-group').length,4);
  assert.equal(f.document.querySelectorAll('.mode-select').length,expectedKeys.length);
  for(const key of expectedKeys){
    const control=modeControl(f,key);
    assert.deepEqual(control.querySelectorAll('option').map(node=>node.value),key==='results_pending_draft'?['inherit','off','on']:['inherit','off','auto','on']);
    assert.equal(control.value,'inherit','Initial defaults remain inherited, not pinned');
    assert.ok(control.getAttribute('aria-label'),'A combined control still has an accessible label');
  }
  for(const oldClass of ['.celestial-toggle','.auto-button','.inherit-button'])assert.equal(f.document.querySelectorAll(oldClass).length,0,'Replaced controls must not remain as duplicate UI');
  assert.equal(f.document.querySelectorAll('.summary-meter span').length,expectedKeys.length);
  assert.equal(f.document.querySelector('.art-index').textContent,'01 — 11');
  assert.equal(f.eval('current().loaded'),true);
  assert.equal(f.document.querySelector('#save').disabled,false,'Missing config can explicitly save inherited defaults');
  await f.document.querySelector('#save').click();
  assert.deepEqual(f.files.user,{version:1});
  assert.equal(f.document.querySelector('#save').disabled,true);
  assert.equal(f.eval('current().saved'),true);
  const requestCount=f.calls.length;
  await chooseMode(f,'independent_review','on');
  assert.equal(f.eval('current().draft.preferences.independent_review'),'on');
  assert.equal(f.calls.length,requestCount,'Draft changes must not call the backend');
  const lang=f.document.querySelector('#language');lang.value='en';await lang.emit('change');
  assert.equal(f.document.documentElement.lang,'en');
  assert.equal(f.document.querySelector('#save span:first-child').textContent,'Save preferences');
  const theme=f.document.querySelector('#theme');theme.value='dark';await theme.emit('change');
  assert.equal(f.document.documentElement.dataset.theme,'dark');
  await f.document.querySelector('#save').click();
  assert.deepEqual(f.files.user,{version:1,preferences:{independent_review:'on'},ui:{language:'en',theme:'dark'}});
  await f.document.querySelectorAll('[data-scope]')[1].click();
  assert.equal(f.eval('scope'),'project');
  assert.equal(f.eval('effective().preferences.independent_review'),'on');
  assert.deepEqual(JSON.parse(f.eval('JSON.stringify(current().draft)')),{version:1});
  await chooseMode(f,'figure_variants','on');
  assert.equal(f.eval('current().draft.preferences.figure_variants'),'on');
  await f.document.querySelectorAll('[data-scope]')[0].click();
  await f.document.querySelectorAll('[data-scope]')[1].click();
  assert.equal(f.eval('current().draft.preferences.figure_variants'),'on','Scope changes preserve drafts');
  await f.document.querySelector('#save').click();
  assert.deepEqual(f.files.project,{version:1,preferences:{figure_variants:'on'}},'Project save remains sparse');
  await chooseMode(f,'figure_variants','inherit');
  assert.equal(f.eval('effective().preferences.figure_variants'),'off');
  await f.document.querySelector('#save').click();
  assert.deepEqual(f.files.project,{version:1});

  await chooseMode(f,'detailed_reports','on');
  const originalRevision=f.eval('current().revision');
  f.mutate('project',{version:1,preferences:{extended_search:'on'}});
  await f.document.querySelectorAll('[data-scope]')[0].click();
  await f.document.querySelectorAll('[data-scope]')[1].click();
  assert.equal(f.eval('current().revision'),originalRevision,'Dirty draft retains original revision');
  assert.equal(f.eval('current().conflict'),true);
  assert.equal(f.document.querySelector('#save').disabled,true);
  assert.equal(f.eval('current().draft.preferences.detailed_reports'),'on');
  assert.equal(f.files.project.preferences.extended_search,'on','External changes stay intact');
  assert.equal(f.document.querySelector('#error').hidden,false);
  await f.document.querySelector('#reload').click();
  assert.equal(f.eval('current().conflict'),false);
  assert.equal(f.eval('current().draft.preferences.extended_search'),'on');

  let finishRead;const file={size:80,arrayBuffer:()=>new Promise(resolve=>finishRead=resolve)};f.context.testFile=file;
  const importPromise=f.eval('importConfig(testFile)');
  assert.equal(f.eval('busy'),true);
  assert.equal(f.document.querySelectorAll('[data-scope]')[0].disabled,true);
  await f.document.querySelectorAll('[data-scope]')[0].click();
  await f.document.querySelector('#save').click();
  assert.equal(f.eval('scope'),'project');
  finishRead(new TextEncoder().encode('{"version":1,"ui":{"language":"zh-TW","theme":"light"}}').buffer);await importPromise;
  assert.equal(f.eval('busy'),false);
  assert.equal(f.document.documentElement.lang,'zh-TW');
  assert.equal(f.eval('current().draft.ui.language'),'zh-TW');
  assert.equal(f.files.project.preferences.extended_search,'on','Import only edits draft');
  for(const content of ['{"version":1,"version":1}','{"version":1,"ui":{"theme":"dark","th\\u0065me":"light"}}','{"version":1,"bad":true}','{"version":1,"preferences":{"independent_review":"yes"}}','bad json']){
    const before=f.eval('JSON.stringify(current().draft)');f.context.badFile={size:content.length,arrayBuffer:async()=>new TextEncoder().encode(content).buffer};await f.eval('importConfig(badFile)');assert.equal(f.eval('JSON.stringify(current().draft)'),before);assert.equal(f.document.querySelector('#error').hidden,false);
  }
  f.eval(`for(const lang of LANGUAGES){if(JSON.stringify(Object.keys(COPY[lang]).sort())!==JSON.stringify(Object.keys(COPY.en).sort()))throw Error('Language keys differ: '+lang);for(const key of KEYS){if(!COPY[lang].features[key].title||!COPY[lang].features[key].desc||!COPY[lang].features[key].trigger||!COPY[lang].features[key].token||!COPY[lang].features[key].time)throw Error('Feature translation missing');}}`);

  for(const [code,status,expected] of [['storage_error',409,'errorStorage'],['storage_error',500,'errorStorage'],['revision_conflict',409,'errorConflict'],['malformed_stored_config',400,'errorStored'],['scope_unavailable',400,'errorScope'],['invalid_config',409,'errorInvalid'],['unknown',409,'errorConflict']]){
    assert.equal(f.eval(`serverError(${JSON.stringify(code)},${status})`),expected,'Explicit error codes take precedence over HTTP status');
  }
  const draftBeforeLock=f.eval('JSON.stringify(current().draft)');const originalFetch=f.context.fetch;
  f.context.fetch=async()=>({ok:false,status:409,json:async()=>({code:'storage_error'})});
  await f.document.querySelector('#save').click();
  assert.equal(f.eval('currentError.key'),'errorStorage','A file lock is not a revision conflict');
  assert.equal(f.eval('current().conflict'),false);
  assert.equal(f.eval('JSON.stringify(current().draft)'),draftBeforeLock,'A locked file preserves the draft');
  assert.equal(f.eval('dirty()'),true);
  assert.equal(f.document.querySelector('#error-text').textContent,f.eval('t("errorStorage")'));
  assert.equal(f.document.querySelector('#save').disabled,false,'A storage error can be retried without discarding the draft');
  f.context.fetch=originalFetch;

  const projectDraft=f.eval('JSON.stringify(current().draft)');f.setFail(true);await f.document.querySelectorAll('[data-scope]')[0].click();
  assert.equal(f.eval('scope'),'project','A failed scope change returns to the loaded scope');
  assert.equal(f.eval('JSON.stringify(current().draft)'),projectDraft,'A failed scope change keeps the current draft');
  f.setFail(false);

  const failed=fixture(true,true);await flush();
  assert.equal(failed.eval('current().loaded'),false);
  assert.equal(failed.document.querySelector('#save').disabled,true);
  assert.equal(failed.document.querySelector('#mode-notice').textContent,failed.eval('t("loadFailed")'));
  failed.setFail(false);await failed.document.querySelector('#reload').click();assert.equal(failed.eval('current().loaded'),true);

  const stat=fixture(false);assert.equal(stat.eval('connected'),false);assert.equal(stat.document.querySelector('#save span:first-child').textContent,stat.eval('t("saveStatic")'));
  await chooseMode(stat,'independent_review','on');await stat.document.querySelector('#save').click();assert.equal(stat.eval('current().exported'),true);assert.equal(stat.eval('dirty()'),true);assert.equal(stat.calls.length,0,'Static mode never calls a backend');
  assert.equal(stat.document.querySelector('#save-status').textContent,stat.eval('t("exported")'));
  assert.match(stat.document.querySelector('#file-help').textContent,/preferences\.json/);

  const extras=fixture();await flush();
  for(const key of ['alternative_routes','maintenance_evolution'])assert.equal(extras.eval(`effective().preferences.${key}`),'off','New enhancements are off in existing configs');
  for(const [index,name,expected] of [[0,'lean','off'],[1,'balanced','off'],[2,'deep','auto']]){
    await choosePreset(extras,name);
    assert.deepEqual(JSON.parse(extras.eval('JSON.stringify(Object.keys(current().draft.preferences))')),expectedKeys,'Every preset covers the complete setting set');
    assert.equal(extras.eval('current().draft.preferences.reference_style_search'),['off','on','on'][index]);
    assert.equal(extras.eval('current().draft.preferences.research_branching'),index===2?'auto':'off');
    assert.equal(extras.eval('current().draft.preferences.research_policy_evolution'),'off','Presets never silently enable policy evolution');
    for(const key of ['alternative_routes','maintenance_evolution'])assert.equal(extras.eval(`current().draft.preferences.${key}`),expected);
  }
  assert.equal(extras.document.querySelectorAll('.summary-meter span').filter(node=>node.className==='is-auto').length,4);
  await extras.document.querySelector('#reset').click();
  await chooseMode(extras,'alternative_routes','on');
  await chooseMode(extras,'maintenance_evolution','auto');
  assert.equal(extras.document.querySelector('#on-count').textContent,'2');
  await extras.document.querySelector('#save').click();
  assert.deepEqual(extras.files.user,{version:1,preferences:{alternative_routes:'on',maintenance_evolution:'auto'}});
  await extras.document.querySelectorAll('[data-scope]')[1].click();
  assert.equal(extras.eval('effective().preferences.alternative_routes'),'on');
  await chooseMode(extras,'alternative_routes','off');
  await extras.document.querySelector('#save').click();
  assert.deepEqual(extras.files.project,{version:1,preferences:{alternative_routes:'off'}});
  await chooseMode(extras,'alternative_routes','inherit');
  assert.equal(extras.eval('effective().preferences.alternative_routes'),'on');
  await extras.document.querySelector('#save').click();
  assert.deepEqual(extras.files.project,{version:1},'New settings restore sparse inheritance');
  extras.context.legacyFile={size:60,arrayBuffer:async()=>new TextEncoder().encode('{"version":1,"preferences":{"figure_variants":"on"}}').buffer};
  await extras.eval('importConfig(legacyFile)');
  assert.equal(extras.eval('current().draft.preferences.alternative_routes'),undefined,'Legacy imports keep new entries omitted');
  assert.equal(extras.eval('effective().preferences.alternative_routes'),'on','Legacy imports inherit instead of pinning new defaults');
  const research=fixture();await flush();
  const researchKeys=['reference_style_search','research_branching','research_policy_evolution'];
  assert.equal(research.eval('effective().preferences.reference_style_search'),'on');
  for(const key of researchKeys.slice(1))assert.equal(research.eval(`effective().preferences.${key}`),'off');
  for(const language of ['zh-CN','zh-TW','en']){
    const picker=research.document.querySelector('#language');picker.value=language;await picker.emit('change');
    for(const key of researchKeys){
      const card=research.document.querySelectorAll('.feature').find(node=>node.dataset.key===key);
      const expected=JSON.parse(research.eval(`JSON.stringify(COPY[${JSON.stringify(language)}].features.${key})`));
      assert.equal(card.querySelector('h3').textContent,expected.title);
      assert.equal(card.querySelector('.feature-description').textContent,expected.desc);
      assert.ok(card.querySelector('.trigger-description').textContent.includes(expected.trigger));
      assert.equal(card.querySelector('.cost-token').textContent,expected.token);
      assert.equal(card.querySelector('.cost-time').textContent,expected.time);
    }
  }
  await research.document.querySelector('#reset').click();
  await chooseMode(research,'reference_style_search','off');
  await chooseMode(research,'research_branching','auto');
  await chooseMode(research,'research_policy_evolution','on');
  await research.document.querySelector('#save').click();
  assert.deepEqual(research.files.user,{version:1,preferences:{reference_style_search:'off',research_branching:'auto',research_policy_evolution:'on'}});
  await research.document.querySelectorAll('[data-scope]')[1].click();
  await chooseMode(research,'reference_style_search','on');
  await chooseMode(research,'research_policy_evolution','auto');
  await research.document.querySelector('#save').click();
  assert.deepEqual(research.files.project,{version:1,preferences:{reference_style_search:'on',research_policy_evolution:'auto'}});
  assert.equal(research.eval('effective().preferences.research_branching'),'auto');
  for(const key of ['reference_style_search','research_policy_evolution'])await chooseMode(research,key,'inherit');
  await research.document.querySelector('#save').click();
  assert.deepEqual(research.files.project,{version:1});
  research.context.legacyResearch={size:60,arrayBuffer:async()=>new TextEncoder().encode('{"version":1,"preferences":{"figure_variants":"on"}}').buffer};
  await research.eval('importConfig(legacyResearch)');
  for(const key of researchKeys){
    assert.equal(research.eval(`current().draft.preferences.${key}`),undefined,'Old configs do not pin new settings');
    assert.equal(research.eval(`effective().preferences.${key}`),research.files.user.preferences[key]);
  }
  const beforeInvalid=research.eval('JSON.stringify(current().draft)');
  for(const key of researchKeys){
    const content=JSON.stringify({version:1,preferences:{[key]:'always'}});
    research.context.invalidResearch={size:content.length,arrayBuffer:async()=>new TextEncoder().encode(content).buffer};
    await research.eval('importConfig(invalidResearch)');
    assert.equal(research.eval('JSON.stringify(current().draft)'),beforeInvalid);
  }
  assert.ok(research.calls.every(call=>new URL(call.url,'http://127.0.0.1').pathname==='/api/preferences'),'Saving research options never launches research or calls another service');

  const combined=fixture();await flush();
  await chooseMode(combined,'detailed_reports','on');
  for(const mode of ['on','auto','off']){
    await chooseMode(combined,'independent_review',mode);
    assert.equal(combined.eval('effective().preferences.independent_review'),mode);
    assert.equal(combined.eval('current().draft.preferences.detailed_reports'),'on','A combined control only edits its own setting');
  }
  await chooseMode(combined,'independent_review','inherit');
  assert.equal(combined.eval('current().draft.preferences.independent_review'),undefined,'Inheritance removes the override');
  assert.equal(combined.eval('effective().preferences.independent_review'),'off');
  assert.deepEqual(JSON.parse(combined.eval('JSON.stringify(current().draft.preferences)')),{detailed_reports:'on'});
  await combined.document.querySelector('#save').click();
  assert.deepEqual(combined.files.user,{version:1,preferences:{detailed_reports:'on'}});

  const profiles=fixture();await flush();
  const presetNames=['lean','balanced','deep','writing','submission','ideation','figures','autoresearch'];
  assert.deepEqual(JSON.parse(profiles.eval('JSON.stringify(Object.keys(PRESETS))')).sort(),[...presetNames].sort());
  assert.equal(profiles.document.querySelectorAll('[data-preset]').length,presetNames.length);
  assert.equal(new Set(JSON.parse(profiles.eval('JSON.stringify(Object.values(PRESETS).map(value=>JSON.stringify(value)))'))).size,presetNames.length,'Every preset must make a distinct choice');
  const profileCalls=profiles.calls.length;
  for(const language of ['zh-CN','zh-TW','en']){
    const picker=profiles.document.querySelector('#language');picker.value=language;await picker.emit('change');
    for(const name of presetNames){
      await choosePreset(profiles,name);
      const settings=JSON.parse(profiles.eval('JSON.stringify(current().draft.preferences)'));
      assert.deepEqual(Object.keys(settings),expectedKeys,'A preset covers every setting');
      assert.ok(Object.values(settings).every(value=>['off','auto','on'].includes(value)));
      assert.equal(settings.research_policy_evolution,'off','General presets never enable research policy evolution');
      assert.equal(settings.results_pending_draft,'off','Presets never enable results-pending drafting');
      assert.equal(profiles.eval('current().draft.ui.language'),language,'Applying a preset preserves UI language');
      assert.equal(profiles.files.user,null,'Preset selection must not save implicitly');
      const button=profiles.document.querySelectorAll('[data-preset]').find(node=>node.dataset.preset===name);
      assert.equal(button.getAttribute('aria-pressed'),'true');
      assert.ok(button.textContent.trim(),'Each preset is named in the selected language');
      for(const key of expectedKeys){
        const control=modeControl(profiles,key);
        assert.equal(control.value,settings[key]);
        assert.ok(control.querySelectorAll('option').every(node=>node.textContent.trim()),'All available modes are translated');
      }
    }
  }
  assert.equal(profiles.calls.length,profileCalls,'All preset and language interactions edit drafts only');
  for(const [name,key] of [['writing','reference_style_search'],['submission','independent_review'],['ideation','alternative_routes'],['figures','figure_variants'],['autoresearch','research_branching']]){
    await choosePreset(profiles,name);
    assert.notEqual(profiles.eval(`effective().preferences.${key}`),'off',`${name} must enable its defining enhancement`);
  }

  const cautious=fixture();await flush();
  const cautionCard=cautious.document.querySelector('.feature-caution');
  assert.ok(cautionCard,'Results-pending drafting has its own caution treatment');
  assert.equal(cautious.document.querySelectorAll('.feature-caution').length,1);
  assert.equal(cautionCard.dataset.key,'results_pending_draft');
  assert.equal(cautionCard.parentNode.parentNode.dataset.group,'reading');
  assert.equal(cautious.eval('effective().preferences.results_pending_draft'),'off');
  assert.equal(modeControl(cautious,'results_pending_draft').getAttribute('aria-describedby'),cautionCard.querySelector('.caution-note').id);
  for(const language of ['zh-CN','zh-TW','en']){
    const picker=cautious.document.querySelector('#language');picker.value=language;await picker.emit('change');
    const expected=JSON.parse(cautious.eval(`JSON.stringify(COPY[${JSON.stringify(language)}])`));
    assert.equal(cautionCard.querySelector('.caution-badge').textContent,expected.cautionLabel);
    assert.equal(cautionCard.querySelector('.caution-note').textContent,expected.cautionRisk);
    assert.equal(cautionCard.querySelector('h3').textContent,expected.features.results_pending_draft.title);
    assert.equal(cautionCard.querySelector('.cost-token').textContent,expected.features.results_pending_draft.token);
    assert.equal(cautionCard.querySelector('.cost-time').textContent,expected.features.results_pending_draft.time);
    assert.equal(modeControl(cautious,'results_pending_draft').querySelectorAll('option').find(node=>node.value==='on').textContent,expected.cautionOn);
  }
  for(const selector of [':root', ':root[data-theme="dark"]']){
    const block=styles.slice(styles.indexOf(selector+' {')).split('}')[0];
    const color=block.match(/--caution:\s*#([a-f0-9]{6});/i);
    assert.ok(color,'Both themes define a caution color');
    const [red,green,blue]=color[1].match(/../g).map(value=>parseInt(value,16));
    assert.ok(red>green+30&&red>blue+30,'Caution treatment stays red in both themes');
  }
  await cautious.document.querySelector('#reset').click();
  await chooseMode(cautious,'results_pending_draft','on');
  assert.equal(cautionCard.dataset.mode,'on');
  await cautious.document.querySelector('#save').click();
  assert.deepEqual(cautious.files.user,{version:1,preferences:{results_pending_draft:'on'}});
  await cautious.document.querySelectorAll('[data-scope]')[1].click();
  assert.equal(cautious.eval('effective().preferences.results_pending_draft'),'on');
  assert.equal(modeControl(cautious,'results_pending_draft').value,'inherit');
  await chooseMode(cautious,'results_pending_draft','off');
  await cautious.document.querySelector('#save').click();
  assert.deepEqual(cautious.files.project,{version:1,preferences:{results_pending_draft:'off'}});
  await chooseMode(cautious,'results_pending_draft','inherit');
  await cautious.document.querySelector('#save').click();
  assert.deepEqual(cautious.files.project,{version:1});
  assert.equal(cautious.eval('effective().preferences.results_pending_draft'),'on');
  const beforeInvalidCaution=cautious.eval('JSON.stringify(current().draft)');
  for(const value of ['auto',true,'always']){
    const content=JSON.stringify({version:1,preferences:{results_pending_draft:value}});
    cautious.context.invalidCaution={size:content.length,arrayBuffer:async()=>new TextEncoder().encode(content).buffer};
    await cautious.eval('importConfig(invalidCaution)');
    assert.equal(cautious.eval('JSON.stringify(current().draft)'),beforeInvalidCaution);
    assert.equal(cautious.eval('currentError.key'),'errorValue');
  }
  cautious.context.legacyCaution={size:13,arrayBuffer:async()=>new TextEncoder().encode('{"version":1}').buffer};
  await cautious.eval('importConfig(legacyCaution)');
  assert.equal(cautious.eval('current().draft.preferences?.results_pending_draft'),undefined);
  assert.equal(cautious.eval('effective().preferences.results_pending_draft'),'on','Legacy imports retain sparse inheritance');
  for(const name of presetNames){
    await chooseMode(cautious,'results_pending_draft','on');
    await choosePreset(cautious,name);
    assert.equal(cautious.eval('current().draft.preferences.results_pending_draft'),'off','Every preset explicitly turns cautious drafting off');
  }
  assert.ok(cautious.calls.every(call=>new URL(call.url,'http://127.0.0.1').pathname==='/api/preferences'),'The new switch only saves preferences; no experiments or writing calls launch from the UI');

  const postConflict=fixture();await flush();
  await chooseMode(postConflict,'independent_review','on');
  const originalDraft=postConflict.eval('JSON.stringify(current().draft)');
  const oldRevision=postConflict.eval('current().revision');
  const externalConfig={version:1,preferences:{figure_variants:'on'}};
  postConflict.mutate('user',externalConfig);
  await postConflict.document.querySelector('#save').click();
  assert.equal(postConflict.eval('currentError.key'),'errorConflict');
  assert.equal(postConflict.eval('current().conflict'),true,'A conflict found by POST must also set the persistent UI state');
  assert.equal(postConflict.document.querySelector('#save').disabled,true,'Do not offer repeated stale writes');
  assert.equal(postConflict.document.querySelector('#save-status').textContent,postConflict.eval('t("conflictState")'));
  assert.equal(postConflict.eval('JSON.stringify(current().draft)'),originalDraft);
  assert.equal(postConflict.eval('current().revision'),oldRevision);
  assert.deepEqual(postConflict.files.user,externalConfig,'The newer stored configuration is preserved');
  await postConflict.document.querySelector('#dismiss-error').click();
  assert.equal(postConflict.document.querySelector('#save').disabled,true,'Dismissing a message is not conflict resolution');
  await postConflict.document.querySelector('#reload').click();
  assert.equal(postConflict.eval('current().conflict'),false);
  assert.deepEqual(JSON.parse(postConflict.eval('JSON.stringify(current().draft)')),externalConfig);
  console.log('PASS: actual app controller renders 11 combined controls in 4 groups; missing-file save; 3-language parity; theme; draft-only edits; sparse persistence; scope draft retention; inheritance reset; external-change revision conflict; storage-lock error and retry; async import locking; bad/duplicate JSON; failed load/retry; static export and no backend requests; 8 complete presets; new-setting persistence and inheritance; legacy version-1 imports; red cautious results-pending drafting with explicit off/on, no Auto, and presets off.');
}
run().catch(error=>{console.error(error);process.exitCode=1;});
