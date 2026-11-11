+++
id = "theorem-pbc-injective-acyclicity--1"
kind = "theorem"
title = "PBC and injective acyclicity (1)"
name_showing = false
order = 349001
aliases = ["bp-r107-1"]
lean = ["AlgebraicGeometry.Etale.tfae_hasTorsionBaseChange", "AlgebraicGeometry.Etale.hasTorsionBaseChange_iff_forall_isIso_baseChangeHomologyMap"]
uses = ["definition-derived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-pbc-property--1", "definition-injective-acyclicity--1"]
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
