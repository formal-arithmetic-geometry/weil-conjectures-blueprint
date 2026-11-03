+++
id = "sk-lem-pbc-composition-cancellation"
kind = "lemma"
title = "Composition and cancellation"
order = 215
lean = ["AlgebraicGeometry.Etale.HasTorsionBaseChange.comp", "AlgebraicGeometry.Etale.HasTorsionBaseChange.of_comp", "AlgebraicGeometry.Etale.HasInjectiveAcyclicity.comp", "AlgebraicGeometry.Etale.HasInjectiveAcyclicity.of_comp"]
uses = ["sk-def-pbc", "sk-thm-iff", "sk-prop-pbc-degree-zero", "sk-thm-picard-perfect"]
tags = ["sketch"]
+++
Let $X\xrightarrow{u}Y\xrightarrow{v}Z$ be proper morphisms. Then
proper base change is stable under composition, and it descends along
a proper surjection:

- (i) If $\mathrm{PBC}_\Lambda(u)$ and $\mathrm{PBC}_\Lambda(v)$ hold, then
  $\mathrm{PBC}_\Lambda(vu)$ holds.
- (ii) If $u$ is surjective and $\mathrm{PBC}_\Lambda(u)$ and
  $\mathrm{PBC}_\Lambda(vu)$ hold, then $\mathrm{PBC}_\Lambda(v)$ holds.
