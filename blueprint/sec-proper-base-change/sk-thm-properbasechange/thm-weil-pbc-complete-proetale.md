+++
id = "thm-weil-pbc-complete-proetale"
kind = "theorem"
title = "Complete pro-etale proper base change"
order = 1389
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-completed-base-change-map", "def-weil-pbc-completed-pullback", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-levelwise-isomorphism-cones", "lemma-weil-pbc-completed-exchange-coherence", "lemma-weil-pbc-completed-map-reduction", "prop-weil-pbc-direct-image-limits", "thm-weil-pbc-finite-level-proetale"]
+++
Let $A$ and $I$ satisfy the adic coefficient datum, let $f:X\to Y$ be
proper, and let $g:Y'\to Y$ be arbitrary. Suppose $K\in D(X_{\Proet},A)$ is
derived $I$-complete and, for every $n$, $K_n$ is equipped with an
etale-origin witness [def-weil-pbc-etale-origin-witness]
$$
 L_n\in\Dplus(X_{\Et},P_n),
 \qquad \nu_X^*L_n\xrightarrow{\sim}K_n,
$$
compatible with transition maps. Then
$$
 \Ex^{\mathrm{comp}}_{\square,K}:
 Lg^*_{\mathrm{comp}}Rf_*K
 \xrightarrow{\sim}Rf'_*Lg'^*_{\mathrm{comp}}K
$$
is an isomorphism.
