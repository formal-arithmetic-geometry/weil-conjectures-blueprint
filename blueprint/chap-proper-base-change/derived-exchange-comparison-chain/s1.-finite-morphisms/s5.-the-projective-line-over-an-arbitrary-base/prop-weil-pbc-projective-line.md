+++
id = "prop-weil-pbc-projective-line"
kind = "theorem"
title = "Projective-line proper base change"
order = 1686
tags = ["latex:proposition"]
uses = ["lemma-weil-pbc-geometric-stalk-conservative", "lemma-weil-pbc-p1-exchange-geometric-stalk", "lemma-weil-pbc-property-iff-acyclicity", "prop-weil-pbc-proper-curve-sepclosed-invariance"]
+++
For every scheme $S$, the projection $\mathbf P^1_S\to S$ satisfies
$\mathsf{PBC}$.

## Proof

At every geometric $\bar t\to T$, the exchange map is the field-extension
map of the preceding lemma. The two residue fields are separably closed and
the fibre is a proper curve, so proper-curve invariance makes this map an
isomorphism. Geometric stalk conservativity gives an isomorphism of every
$R^q$ sheaf. Specializing to inverse images of injective
$\mathbf F_\ell$-module sheaves gives $\mathsf{IA}$ after every base change;
the S0 equivalence gives $\mathsf{PBC}$.
