+++
id = "sk-thm-iff"
kind = "theorem"
title = "PBC and injective acyclicity"
order = 1660
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_iff_hasInjectiveAcyclicity", "AlgebraicGeometry.Etale.HasTorsionBaseChange.hasInjectiveAcyclicity"]
uses = ["sk-def-conv", "sk-def-exchange", "sk-def-ia", "sk-def-pbc", "sk-thm-acyclicity", "sk-def-pbc-conventions", "sk-prop-pbc-degree-zero"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be proper, and let $\Lambda$ be a commutative ring which is
torsion as an abelian group. The following are equivalent:

1. $\mathrm{PBC}_\Lambda(f)$ [sk-def-pbc] holds, that is, the exchange map is
   an isomorphism for every bounded below complex of sheaves of
   $\Lambda$-modules (all of whose cohomology sheaves are torsion).
2. For every sheaf $F$ of $\Lambda$-modules and every base change as in
   [sk-def-exchange], the maps induced by the derived exchange on cohomology
   sheaves

   $$
   g^{-1}R^qf_*F\longrightarrow R^qf'_*g'^{-1}F
   $$

   are isomorphisms for all $q\geq0$.
3. $\mathrm{IA}_\Lambda(f)$ [sk-def-ia] holds.
