// Usage: node scripts/tex2bp_doc.mjs <web/model.js> <snapshot.json> <doc.json>
// For scripts/tex2bp_check.py.
//
// The document as the site reads it: every entry in order, a statement's
// proofs right after it, with the chain of headings it is under.
import fs from 'fs';
const M = await import(process.argv[2]);
const m = M.buildModel(JSON.parse(fs.readFileSync(process.argv[3], 'utf8')));
const out = M.documentOutline(m, 'refines');
const rows = [];
const chain = (e) => { const c = []; for (let p = e.parent; p; p = p.parent) c.unshift(p.id); return c; };
for (const e of out.entries) {
  if (e.duplicate) continue;
  const o = e.object;
  if (o.kind === 'proof') {
    rows.push({ id: o.id, kind: 'proof', heads: chain(e), of: M.boundaryEntry(o, 'of'), title: '', body: o.body || '' });
    continue;
  }
  rows.push({ id: o.id, kind: o.kind, heads: chain(e), title: o.attrs.title || '', body: o.body || '', number: e.number || null });
  for (const p of out.proofs.get(e.id) || []) rows.push({ id: p.id, kind: 'proof', heads: chain(e), of: o.id, title: '', body: p.body || '' });
}
fs.writeFileSync(process.argv[4], JSON.stringify(rows));
console.log(rows.length, 'rows');
