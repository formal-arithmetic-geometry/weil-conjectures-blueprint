+++
id = "thm-weil-pbc-finite-level-proetale"
kind = "theorem"
title = "Finite-level pro-etale proper base change"
lean = ["AlgebraicGeometry.ProEtale.isIso_derivedBaseChangeMap_app_of_isProper"]
order = 2017
uses = ["def-weil-pbc-ambient-ringed-exchange", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-transport-identifies-exchange", "thm-weil-pbc-bounded-below", "thm-weil-pbc-site-comparison"]
+++
Let $\Lambda$ be finite, let $f$ be proper, and let
$K\in\Dplus(X_{\Proet},\Lambda)$ carry an etale-origin witness
[def-weil-pbc-etale-origin-witness] $(L,\alpha)$. Then the pro-etale exchange
map

$$
 g^{-1}Rf_*K\xrightarrow{\sim}Rf'_*g'^{-1}K
$$

is an isomorphism. It is independent of replacing the witness by an
isomorphic witness.
