+++
id = "proposition-proper-base-change-etale-site--2"
kind = "lemma"
title = "Change of coefficients for the PBC property"
name_showing = false
order = 398003
lean = ["AlgebraicGeometry.Etale.HasTorsionBaseChange.quotient", "AlgebraicGeometry.Etale.hasTorsionBaseChange_of_forall_prime"]
uses = ["definition-torsion-pbc-property"]
+++
Let $\Lambda$ be a commutative ring and let $f:X\to Y$ be a morphism of
schemes.

- (i) If $\mathrm{PBC}_\Lambda(f)$ holds, then
  $\mathrm{PBC}_{\Lambda/N\Lambda}(f)$ holds for every integer $N\geq0$.
- (ii) Suppose that $f$ is quasi-compact and quasi-separated. If
  $\mathrm{PBC}_{\Lambda/p\Lambda}(f)$ holds for every prime $p$, then
  $\mathrm{PBC}_\Lambda(f)$ holds.
