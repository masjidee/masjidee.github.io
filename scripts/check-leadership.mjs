import {readFile,readdir} from 'node:fs/promises';
import {join} from 'node:path';
import {createHash} from 'node:crypto';
import {gunzipSync} from 'node:zlib';
import assert from 'node:assert/strict';
const source='src/data/leadership.json',generator='scripts/build-leadership-assets.py',downloads='public/docs/leadership';
const hash=async path=>createHash('sha256').update(await readFile(path)).digest('hex');
const manifest=JSON.parse(await readFile(join(downloads,'assets-manifest.json'),'utf8'));
assert.equal(manifest.sourceSha256,await hash(source),'Regenerate leadership downloads after editing the shared JSON source.');
assert.equal(manifest.generatorSha256,await hash(generator),'Regenerate downloads after changing their generator.');
const content=JSON.parse(await readFile(source,'utf8'));
assert.equal(content.papers.length,2);assert.equal(content.slides.length,manifest.slides);
assert.ok(content.slides.every(s=>s.notes?.trim()),'Every slide needs presenter notes.');
const expected=['masjidee-executive-whitepaper.pdf','masjidee-detailed-whitepaper.pdf','masjidee-leadership-presentation.pdf','masjidee-leadership-presentation.pptx'];
assert.deepEqual(Object.keys(manifest.files).sort(),expected.sort());
for(const [name,info] of Object.entries(manifest.files)){
 const data=await readFile(join(downloads,name));assert.equal(await hash(join(downloads,name)),info.sha256);assert.equal(data.length,info.bytes);assert.ok(data.length>10000);
 assert.equal(data.subarray(0,name.endsWith('.pdf')?4:2).toString(),name.endsWith('.pdf')?'%PDF':'PK');
 assert.equal(await hash(join('dist/docs/leadership',name)),info.sha256,'Published asset differs from its reviewed source.');
}
const walk=async path=>(await Promise.all((await readdir(path,{withFileTypes:true})).map(e=>e.isDirectory()?walk(join(path,e.name)):join(path,e.name)))).flat();
const routes=['executive-whitepaper','detailed-whitepaper','presentation'];
for(const route of routes){const html=await readFile(`dist/docs/leadership/${route}/index.html`,'utf8');assert.match(html,/name="robots" content="noindex, nofollow, noarchive"/);assert.match(html,/data-pagefind-ignore="all"/);}
for(const path of await walk('dist')){
 if(path.endsWith('.html')&&!path.includes('/docs/leadership/'))assert.doesNotMatch(await readFile(path,'utf8'),/href=["'][^"']*\/docs\/leadership\//,'Leadership assets must not be linked from ordinary site pages.');
 if(path.includes('sitemap')&&path.endsWith('.xml'))assert.doesNotMatch(await readFile(path,'utf8'),/\/docs\/leadership\//,'Leadership pages must not appear in the sitemap.');
}
let fragments=0;
for(const name of await readdir('dist/pagefind/fragment')){
 const data=gunzipSync(await readFile(join('dist/pagefind/fragment',name))).toString();const fragment=JSON.parse(data.slice(data.indexOf('{')));
 assert.ok(!fragment.url.includes('/docs/leadership/'),'Leadership page leaked into Pagefind search.');fragments++;
}
assert.ok(fragments>0,'Ordinary documentation search must remain indexed.');
console.log(`Verified ${routes.length} direct-link pages, ${expected.length} downloads, presenter notes and provenance; excluded from navigation, sitemap and ${fragments} search fragments.`);
