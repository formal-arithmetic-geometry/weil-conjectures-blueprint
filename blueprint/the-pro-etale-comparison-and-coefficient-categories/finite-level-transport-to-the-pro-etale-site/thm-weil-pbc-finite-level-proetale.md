+++
id = "thm-weil-pbc-finite-level-proetale"
kind = "theorem"
title = "Finite-level pro-etale proper base change"
order = 2719
lean = ["AlgebraicGeometry.Proetale.isIso_ambientExchange_of_isProper_of_etaleOrigin"]
uses = ["def-weil-pbc-etale-origin-witness", "def-weil-pbc-ambient-ringed-exchange", "thm-weil-pbc-site-comparison", "lem-weil-pbc-transport-identifies-exchange"]
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

## Proof

The bounded-below theorem of the proper-base-change chapter makes the etale
exchange map for $L$ an isomorphism; the fully faithful comparison of
[thm-weil-pbc-site-comparison] transports it to the pro-etale site, where
[lem-weil-pbc-transport-identifies-exchange] identifies the transported map
with the pro-etale exchange map for $\nu_X^*L$, which is $K$ under the
witness of [def-weil-pbc-etale-origin-witness]. Independence of the witness
follows from the functoriality of the transported map.

Unresolved dependencies: def:weil-pbc-scheme-conventions, thm:weil-pbc-bounded-below
