+++
id = "sk-thm-iff"
kind = "theorem"
title = "PBC and injective acyclicity"
order = 191
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_iff_hasInjectiveAcyclicity", "AlgebraicGeometry.Etale.HasTorsionBaseChange.hasInjectiveAcyclicity"]
uses = ["sk-def-conv", "sk-def-exchange", "sk-def-ia", "sk-def-pbc", "sk-thm-acyclicity", "sk-def-pbc-conventions", "sk-prop-pbc-degree-zero"]
tags = ["sketch"]
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
