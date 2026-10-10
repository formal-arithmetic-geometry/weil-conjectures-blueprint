+++
id = "lemma-weil-pbc-completed-exchange-coherence"
kind = "lemma"
title = "Completed exchange coherence"
order = 1348
uses = ["def-weil-pbc-completed-base-change-map", "lem-weil-pbc-exchange-identity-pasting", "lemma-weil-pbc-completed-map-reduction", "lemma-weil-pbc-r-lim-levelwise-isomorphism"]
+++
Completed exchange of [def-weil-pbc-completed-base-change-map] is
natural in $K$, equals the identity for identity squares, and satisfies
horizontal and vertical pasting after the canonical associativity
isomorphisms.

## Proof

The finite-level reductions of [lemma-weil-pbc-completed-map-reduction]
satisfy the identity and pasting laws of the exchange identity-and-pasting
lemma levelwise, and the tower morphisms preserve these compatible
equalities, so the completed map of
[def-weil-pbc-completed-base-change-map] inherits them.

At every finite level these equations are the S0/S8 equations. They commute
with the tower transitions by naturality of coefficient reduction. Apply
$R\varprojlim$ to each equality and conjugate by the same reconstruction,
projection-formula, and direct-image/limit isomorphisms used in the definition.
The resulting equations are precisely the completed equations.
