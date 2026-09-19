+++
id = "lemma-weil-pbc-epsilon-inverse-image-exact"
kind = "lemma"
title = "Exactness of comparison inverse image"
order = 794
uses = ["lemma-weil-pbc-epsilon-geometric-morphism"]
+++
For every commutative ring $A$, the functor
$\epsilon_X^{-1}:\operatorname{Sh}_A(X_{\mathrm{et}})\to \operatorname{Sh}_A(X_{\mathrm{proet}})$ is exact.

## Proof

It preserves kernels by the finite-limit assertion in
Lemma [lemma-weil-pbc-epsilon-geometric-morphism]. It preserves
cokernels because it is a left adjoint. Applying these two facts to a short
exact sequence

$$
0\longrightarrow F'\longrightarrow F\longrightarrow F''\longrightarrow0
$$

shows that its inverse-image sequence is exact at all three terms.
