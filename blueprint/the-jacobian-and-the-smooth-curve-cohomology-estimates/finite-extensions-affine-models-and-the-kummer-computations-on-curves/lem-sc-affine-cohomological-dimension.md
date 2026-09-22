+++
id = "lem-sc-affine-cohomological-dimension"
kind = "lemma"
title = "Cohomological dimension of a smooth affine curve"
order = 4535
lean = ["AlgebraicGeometry.Curve.cohomology_eq_zero_of_isAffine_of_one_lt"]
uses = ["lem-sc-cohomological-dimension", "lem-sc-generic-cohomology-comparison", "lem-sc-affine-generic-second"]
+++
For a smooth affine curve $C$ over an algebraically closed field and any
torsion étale sheaf $F$, one has $H^q(C,F)=0$ for $q>1$.

## Proof

The degrees $q>2$ vanish by [lem-sc-cohomological-dimension]. In degree two,
work componentwise and apply [lem-sc-generic-cohomology-comparison] with
$M=\eta^*F$; the resulting group $H^2(C,\eta_*M)$ vanishes by
[lem-sc-affine-generic-second].

Unresolved dependencies: def:sc-curves, def:weil-pbc-etale-sheaves, def:weil-pbc-etale-cohomology
