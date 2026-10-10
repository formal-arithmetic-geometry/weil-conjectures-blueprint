+++
id = "thm-weil-pbc-qbar"
kind = "theorem"
title = "Qbar-l proper base change"
order = 1359
uses = ["def-weil-pbc-finite-stage-pair-category", "def-weil-pbc-qbar-category", "def-weil-pbc-scheme-conventions", "prop-weil-pbc-descent-functors", "thm-weil-pbc-finite-extension"]
+++
Let $f:X\to Y$ be proper, let $g:Y'\to Y$ be arbitrary, and let
$K\in\Dbc(X,\Qlb)$. The descended exchange transformation of
[prop-weil-pbc-descent-functors] is an isomorphism
$$
 Lg^*Rf_*K\xrightarrow{\sim}Rf'_*Lg'^*K
 \quad\text{in }\Dbc(Y',\Qlb).
$$
If $K$ is represented by a pair $(E,K_E)$ with $K_E\in\Dbc(X,E)$, this map
is represented after a finite overfield $M$ by the $M$-coefficient exchange
isomorphism of [thm-weil-pbc-finite-extension] applied to $T_{M/E}K_E$. The
result is independent of $E$, $M$, and the representative.
