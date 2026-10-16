+++
id = "thm-sc-affine-torsion-cd"
kind = "theorem"
title = "The affine torsion cohomological dimension bound"
lean = ["AlgebraicGeometry.Scheme.hasTorsionCohomologicalDimensionLE_of_isAffine"]
order = 1904
uses = ["cor-weil-pbc-geometric-fiber-finite", "def-sc-etale-torsion-cd", "def-weil-pbc-scheme-conventions", "lem-kun-cd-sep-closed-point", "lem-sc-arbitrary-curve-cd", "lem-sc-cd-affine-limit", "lem-sc-cd-ground-field", "lem-sc-one-variable-field-cd", "lem-sc-support-dimension-union", "lem-weil-pbc-cohomology-filtered-colimit", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-torsion-filtered-union", "prop-weil-pbc-strict-henselization-stalk-formula", "thm-sp-grothendieck"]
+++
Let $K$ be a field with $\operatorname{cd}_{\rm tor}(K)\leq c$.
For any affine finite-type
$K$-scheme $X$, one has

$$
\operatorname{cd}_{\rm tor}(X)\leq\dim X+c,
$$

with both bounds understood as in [def-sc-etale-torsion-cd].
