+++
id = "lemma-composition-cancellation"
kind = "lemma"
title = "Composition and cancellation"
order = 389
lean = ["AlgebraicGeometry.Etale.HasTorsionBaseChange.comp", "AlgebraicGeometry.Etale.HasTorsionBaseChange.of_comp"]
uses = ["definition-torsion-pbc-property"]
+++
Let $X\xrightarrow{u}Y\xrightarrow{v}Z$ be proper morphisms. Then
proper base change is stable under composition, and it descends along
a proper surjection:

- (i) If $\mathrm{PBC}_\Lambda(u)$ and $\mathrm{PBC}_\Lambda(v)$ hold, then
  $\mathrm{PBC}_\Lambda(vu)$ holds.
- (ii) If $u$ is surjective and $\mathrm{PBC}_\Lambda(u)$ and
  $\mathrm{PBC}_\Lambda(vu)$ hold, then $\mathrm{PBC}_\Lambda(v)$ holds.
