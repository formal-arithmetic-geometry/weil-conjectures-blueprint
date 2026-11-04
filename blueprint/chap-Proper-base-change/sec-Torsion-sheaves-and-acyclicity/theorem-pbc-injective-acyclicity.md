+++
id = "theorem-pbc-injective-acyclicity"
kind = "theorem"
title = "PBC and injective acyclicity"
order = 348
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_iff_hasInjectiveAcyclicity"]
uses = ["definition-torsion-pbc-property", "definition-injective-acyclicity"]
+++
Let $f:X\to Y$ be proper. The following are equivalent:

- (i) $\mathrm{PBC}_\Lambda(f)$ holds.
- (ii) For every sheaf $F$ of $\Lambda$-modules and every base change
  (4.1), the maps
  induced by (4.3) on cohomology sheaves
  $$
  g^*R^qf_*F\longrightarrow R^qf'_*g'^*F
  $$
  are isomorphisms for all $q\geq0$.
- (iii) $\mathrm{IA}_\Lambda(f)$ holds.
