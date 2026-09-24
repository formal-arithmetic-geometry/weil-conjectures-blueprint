+++
id = "lemma-weil-pbc-geometric-stalk-conservative"
kind = "lemma"
title = "Conservativity of geometric stalks"
order = 1550
lean = ["AlgebraicGeometry.Scheme.isIso_of_isIso_sheafFiber_map"]
+++
A morphism of etale abelian sheaves is an isomorphism if and only if it is an
isomorphism at every geometric stalk.

## Proof

The kernel and cokernel have zero geometric stalks. If a sheaf has zero
stalks, every local section vanishes on an etale neighbourhood of each point;
quasi-compact refinement on an etale object makes it locally zero on a cover,
hence zero by the sheaf axiom. Thus kernel and cokernel vanish.
