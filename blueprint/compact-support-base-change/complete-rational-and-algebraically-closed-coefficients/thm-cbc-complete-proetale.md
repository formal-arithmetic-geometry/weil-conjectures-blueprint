+++
id = "thm-cbc-complete-proetale"
kind = "theorem"
title = "Complete pro-etale compact-support base change"
order = 6625
lean = ["AlgebraicGeometry.Proetale.completedCompactSupportExchange_isIso"]
uses = ["def-compact-support-direct-image", "def-cbc-completed-exchange-map", "def-cbc-compact-support-square", "def-cbc-exchange-map", "lem-cbc-proetale-extension-zero", "lem-cbc-completed-extension-zero-comparison"]
+++
Let $(A,I)$ be an adic coefficient datum, let $\square$ be a
compact-support base-change square ([def-cbc-compact-support-square]) with $f$
separated of finite type and $g:Y'\to Y$ arbitrary, and let
$K\in D(X_{\Proet},A)$ be derived $I$-complete whose reductions $K_n$ carry
compatible etale-origin witnesses. Then
$$
 \Ex^{\mathrm{comp}}_!(K):
 Lg^*_{\mathrm{comp}}Rf_!K
 \xrightarrow{\ \sim\ }Rf'_!Lg'^*_{\mathrm{comp}}K
$$
of [def-cbc-completed-exchange-map] is an isomorphism, natural in $K$ and
coherent for identities and pasted squares.

## Proof

Choose a compactification $c=(j,p)$ of $f$ and its base change $c'$; the
composite defining [def-cbc-completed-exchange-map] consists of two
isomorphisms: the completed proper base change applied to the proper $p$ (the
hypotheses hold: $j_!K$ is derived $I$-complete by the exactness of
[lem-cbc-proetale-extension-zero], and its reductions $j_!K_n$ carry the
witnesses $j_!L_n$ if the witnesses of $K$ are $L_n$), and the completed
extension-by-zero comparison
[lem-cbc-completed-extension-zero-comparison]. Hence
$\Ex^{\mathrm{comp}}_!(K)$ is an isomorphism, and it is independent of the
compactification and natural by the corresponding properties of the two
factors (the coherence of [def-cbc-exchange-map] and of the completed proper
exchange map, with the compatibility of the comparisons of the compact-support
direct image with the completed maps).

Unresolved dependencies: def:weil-pbc-adic-coefficient-datum, def:weil-pbc-etale-origin-witness, def:weil-pbc-scheme-conventions, thm:weil-pbc-complete-proetale
