import {readFile,readdir,stat} from 'node:fs/promises';
import {resolve,join,extname} from 'node:path';
const root=resolve('dist'),base='/';
const walk=async(dir)=>(await Promise.all((await readdir(dir,{withFileTypes:true})).map(e=>e.isDirectory()?walk(join(dir,e.name)):join(dir,e.name)))).flat();
const files=(await walk(root)).filter(p=>extname(p)==='.html');
if(!files.length)throw Error('Build the website first.');
let checked=0;const errors=[];
for(const file of files){
 const html=await readFile(file,'utf8'),url=new URL(base+file.slice(root.length+1).replace(/index\.html$/,''),'https://masjidee.github.io');
 for(const match of html.matchAll(/\b(?:href|src)\s*=\s*["']([^"']+)["']/g)){
  const value=match[1].replaceAll('&amp;','&');if(file.endsWith('/404.html')&&value==='https://masjidee.github.io/404/')continue;if(/^(?:mailto:|tel:|data:|javascript:|#)/.test(value))continue;
  const target=new URL(value,url);if(target.origin!==url.origin)continue;
  if(!target.pathname.startsWith(base)){errors.push(`${file}: outside project base: ${value}`);continue;}
  let path;try{path=resolve(root,decodeURIComponent(target.pathname.slice(base.length)));}catch{errors.push(`${file}: invalid URL ${value}`);continue;}
  if(path!==root&&!path.startsWith(root+'/')){errors.push(`${file}: escaping path ${value}`);continue;}
  const info=await stat(path).catch(()=>null);if(info?.isDirectory())path=join(path,'index.html');
  if(!(await stat(path).catch(()=>null))?.isFile())errors.push(`${file}: missing ${value}`);
  checked++;
 }
}
if(errors.length){console.error(errors.join('\n'));process.exitCode=1;}else console.log(`Checked ${checked} local links/assets across ${files.length} HTML pages.`);
