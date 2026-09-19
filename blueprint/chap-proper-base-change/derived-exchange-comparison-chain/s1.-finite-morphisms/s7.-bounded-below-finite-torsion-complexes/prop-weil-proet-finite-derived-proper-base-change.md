+++
id = "prop-weil-proet-finite-derived-proper-base-change"
kind = "theorem"
title = "Bounded-below finite derived proper base change"
order = 758
tags = ["latex:proposition"]
uses = ["lemma-weil-pbc-hypercohomology-convergence", "lemma-weil-pbc-hypercohomology-map", "prop-weil-proet-finite-proper-base-change"]
+++
For a proper Cartesian square and $K\in D^+(X_{\mathrm{et}})$ with torsion
cohomology, the exchange map

$$
g^{-1}Rf_*K\xrightarrow{\sim}Rf'_*g'^{-1}K
$$

is an isomorphism.

## Proof

S6 makes every $E_2$ component of the spectral-sequence morphism an
isomorphism. Induction on the page gives isomorphisms on $E_r$ and
$E_\infty$. In each total degree the finite filtrations have isomorphic
associated graded pieces, so induction on the filtration length gives an
isomorphism of abutments. A morphism in the derived category is an
isomorphism when every cohomology sheaf map is an isomorphism. This expands
Tag `0DDE`, including its exact-couple comparison.
