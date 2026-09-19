+++
id = "lemma-weil-pbc-finite-exchange"
kind = "lemma"
title = "Finite exchange isomorphism"
order = 679
lean = ["AlgebraicGeometry.Etale.isBaseChangeIso_of_isFinite", "AlgebraicGeometry.Etale.isIso_baseChangeMap_of_isFinite"]
uses = ["def-weil-pbc-cartesian-square", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-stalk-formula"]
+++
For a finite Cartesian square, the underived exchange map is an isomorphism;
therefore all its derived exchange maps are isomorphisms.

## Proof

At a geometric point $\bar y'\to Y'$, the fibre of $f'$ is the base change of
the finite fibre of $f$ along $\kappa(\bar y)\to\kappa(\bar y')$. The stalk
formula identifies both sides with the same finite product indexed by these
points, and the exchange map is the identity on each factor. Thus it is a
stalkwise bijection and hence an isomorphism. Exactness from the preceding
lemma means injective resolutions remain direct-image acyclic, so the same
degreewise argument computes the derived map.
