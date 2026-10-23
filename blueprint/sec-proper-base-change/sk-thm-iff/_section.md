+++
id = "sk-thm-iff"
kind = "theorem"
title = "PBC and injective acyclicity"
order = 1558
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_iff_hasInjectiveAcyclicity", "AlgebraicGeometry.Etale.HasTorsionBaseChange.hasInjectiveAcyclicity", "AlgebraicGeometry.Etale.HasTorsionBaseChange.quotient", "AlgebraicGeometry.Etale.hasTorsionBaseChange_of_hasInjectiveAcyclicity", "AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_isTorsionSheaf"]
uses = ["sk-def-conv", "sk-def-exchange", "sk-def-ia", "sk-def-pbc", "sk-thm-acyclicity", "sk-def-pbc-conventions", "sk-prop-pbc-degree-zero"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be proper. The following are equivalent:

1. $\mathrm{PBC}(f)$ [sk-def-pbc] holds for bounded below complexes with
   torsion cohomology sheaves.
2. For every torsion abelian sheaf $F$ and every base change as in
   [sk-def-exchange], the maps of abelian sheaves on $Y'_{\Et}$ induced by the
   derived exchange on cohomology sheaves

   $$
   g^{-1}R^qf_*F\longrightarrow R^qf'_*g'^{-1}F
   $$

   are isomorphisms for all $q\geq0$.
3. $\mathrm{IA}_r(f)$ [sk-def-ia] holds for every prime $r$.

For a commutative ring $\Lambda$ annihilated by a positive integer, the
corresponding fixed-coefficient statement is
$\mathrm{PBC}_\Lambda(f)\Longleftrightarrow\mathrm{IA}_\Lambda(f)$.
