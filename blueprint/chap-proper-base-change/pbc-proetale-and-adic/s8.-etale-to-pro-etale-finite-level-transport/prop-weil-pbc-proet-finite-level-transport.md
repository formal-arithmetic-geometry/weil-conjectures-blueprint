+++
id = "prop-weil-pbc-proet-finite-level-transport"
kind = "theorem"
title = "Finite-level pro-etale proper base change"
order = 1923
tags = ["latex:proposition"]
uses = ["def-weil-pbc-comes-from-etale", "lemma-weil-pbc-epsilon-direct-image", "lemma-weil-pbc-epsilon-pullback", "prop-weil-proet-finite-derived-proper-base-change"]
+++
Let $A$ be a finite torsion ring and let $(L,\theta)$ witness that
$K\in D^+(X_{\mathrm{proet}},A)$ comes from the etale site, with
$L\in D_c^+(X_{\mathrm{et}},A)$. For a proper Cartesian square, the
pro-etale exchange map

$$
Lg^*Rf_*K\longrightarrow Rf'_*L(g')^*K
$$

is an isomorphism.

## Proof

Use $\theta$ to replace $K$ by $\epsilon_X^{-1}L$. Commute
$\epsilon^{-1}$ past the two pullbacks and two direct images using the
preceding lemmas. The resulting middle arrow is
$\epsilon_{Y'}^{-1}$ applied to the S7 etale exchange map and is therefore an
isomorphism. Expanding all four comparison isomorphisms shows the transported
arrow is the pro-etale unit–counit exchange map; naturality follows from the
two comparison squares.
