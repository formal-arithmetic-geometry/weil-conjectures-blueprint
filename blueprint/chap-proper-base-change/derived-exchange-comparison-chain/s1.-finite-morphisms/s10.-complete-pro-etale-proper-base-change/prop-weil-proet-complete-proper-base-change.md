+++
id = "prop-weil-proet-complete-proper-base-change"
kind = "theorem"
title = "Complete pro-etale proper base change"
order = 898
tags = ["latex:proposition"]
uses = ["def-weil-pbc-complete-coefficient-datum", "def-weil-pbc-completed-base-change-map", "lemma-weil-pbc-completed-exchange-coherence", "lemma-weil-pbc-completed-frobenius-equivariance", "lemma-weil-pbc-r-lim-levelwise-isomorphism", "prop-weil-pbc-proet-finite-level-transport"]
+++
Let $f:X\to Y$ be proper and let $\square$ be any base change. Suppose
$K\in D(X_{\mathrm{proet}},\Lambda)$ is derived $I$-complete, each $K_n$ is
equipped with a displayed witness
$\epsilon_X^{-1}L_n\simeq K_n$ for some
$L_n\in D_c^+(X_{\mathrm{et}},\Lambda/I^n)$, and every $\Lambda/I^n$ is
perfect. Then

$$
Lg^*_{\mathrm{comp}}Rf_*K\xrightarrow{\sim}
Rf'_*L(g')^*_{\mathrm{comp}}K.
$$

The isomorphism is natural and satisfies identity and pasting coherence. If
the square and the reductions carry a Frobenius-equivariant square and Weil
tower datum, this is an isomorphism of the completed Weil objects
$(S,\Theta_S)$ and $(T,\Theta_T)$.

## Proof

Every finite-level middle arrow in Definition
[def-weil-pbc-completed-base-change-map] is an isomorphism by S8. The
derived limit preserves this compatible levelwise isomorphism. The outer
arrows in the defining composite are reconstruction, perfect projection
formula, and direct-image/limit isomorphisms. Hence the completed map is an
isomorphism. Coherence is the preceding lemma. This proves the mathematical
content located at Tag `09C9` without using that theorem as a leaf.
The completed Frobenius-equivariance lemma gives the last assertion with the
genuine pullback type $\Phi_{Y'}S\to T$.
