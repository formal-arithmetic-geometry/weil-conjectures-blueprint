+++
id = "prop-weil-pbc-projective-line-detailed"
kind = "theorem"
title = "Projective-line proper base change"
order = 1168
lean = ["AlgebraicGeometry.Etale.isBaseChangeIso_projectiveLine"]
uses = ["lem-weil-pbc-exchange-geometric-stalk", "prop-weil-pbc-separably-closed-extension", "def-weil-pbc-property"]
+++
For every scheme $S$, the projection $\mathbf P^1_S\to S$ satisfies
$\mathrm{PBC}$ in the sense of [def-weil-pbc-property].

## Proof

Let $I$ be injective in $\mathbf F_r$-module sheaves on $\mathbf P^1_S$ and
make an arbitrary base change. On every geometric stalk,
[lem-weil-pbc-exchange-geometric-stalk] identifies the exchange map with
pullback between proper curves over separably closed fields;
[prop-weil-pbc-separably-closed-extension] makes it an isomorphism. Since
$R^qp_*I=0$ for $q>0$, the target stalks $R^qp'_*g'^{-1}I$ vanish for $q>0$,
and conservativity of geometric stalks gives $\mathrm{IA}_r$ for the
projection; the equivalence between $\mathrm{PBC}$ and $\mathrm{IA}$ gives
$\mathrm{PBC}$.

Unresolved dependencies: lem:weil-pbc-geometric-stalk-conservative, def:weil-pbc-injective-acyclicity, prop:weil-pbc-property-iff-acyclicity
