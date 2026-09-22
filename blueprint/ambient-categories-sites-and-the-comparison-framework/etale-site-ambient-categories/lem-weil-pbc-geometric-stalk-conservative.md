+++
id = "lem-weil-pbc-geometric-stalk-conservative"
kind = "lemma"
title = "Conservativity of geometric stalks"
order = 2007
lean = ["AlgebraicGeometry.Etale.isIso_iff_isIso_stalkMap"]
uses = ["def-weil-pbc-geometric-stalks", "def-weil-pbc-etale-sheaves"]
+++
A morphism of etale sheaves of abelian groups is an isomorphism if and only
if it is an isomorphism at every geometric stalk
[def-weil-pbc-geometric-stalks].

## Proof

The kernel and cokernel have zero geometric stalks by exactness of the stalk
functors of [prop-weil-pbc-geometric-stalks-exact]. If a sheaf has zero
stalks, every local section vanishes on an etale neighbourhood of each point,
and quasi-compact refinement on an etale object makes it zero on a cover,
hence zero by the sheaf axiom of [def-weil-pbc-etale-sheaves]; so kernel and
cokernel vanish.
