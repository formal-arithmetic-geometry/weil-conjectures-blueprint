+++
id = "sk-lem-pbc-composition-cancellation"
kind = "lemma"
title = "Composition and cancellation"
order = 1943
lean = ["AlgebraicGeometry.Etale.HasTorsionBaseChange.comp", "AlgebraicGeometry.Etale.HasTorsionBaseChange.of_comp", "AlgebraicGeometry.Etale.HasInjectiveAcyclicity.comp", "AlgebraicGeometry.Etale.HasInjectiveAcyclicity.of_comp"]
uses = ["sk-def-pbc", "sk-thm-iff", "sk-prop-pbc-degree-zero", "sk-thm-picard-perfect"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative ring which is torsion as an abelian group (for
instance $\Lambda=\mathbf Z/n$), and let $X\xrightarrow{u}Y\xrightarrow{v}Z$ be
proper morphisms.

1. If $\mathrm{PBC}_\Lambda(u)$ and $\mathrm{PBC}_\Lambda(v)$ hold, then
   $\mathrm{PBC}_\Lambda(vu)$ holds.
2. If $u$ is surjective and $\mathrm{PBC}_\Lambda(u)$ and
   $\mathrm{PBC}_\Lambda(vu)$ hold, then $\mathrm{PBC}_\Lambda(v)$ holds.
