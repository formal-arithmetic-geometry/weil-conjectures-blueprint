+++
id = "thm-cbc-complete-proetale"
kind = "theorem"
title = "Complete pro-etale compact-support base change"
order = 1936
uses = ["def-cbc-compact-support-square", "def-cbc-completed-exchange-map", "def-cbc-exchange-map", "def-compact-support-direct-image-detailed", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-scheme-conventions", "lem-cbc-completed-extension-zero-comparison", "lem-cbc-proetale-extension-zero", "thm-weil-pbc-complete-proetale"]
+++
Let $(A,I)$ satisfy [def-weil-pbc-adic-coefficient-datum], let
$\square$ be a
compact-support
base-change square with $f$ separated of finite type and
$g:Y'\to Y$ arbitrary, and let $K\in D(X_{\Proet},A)$ be derived
$I$-complete whose reductions $K_n$ carry compatible
etale-origin witnesses.
Then

$$
\Ex^{\mathrm{comp}}_!(K):
Lg^*_{\mathrm{comp}}Rf_!K
\xrightarrow{\ \sim\ }Rf'_!Lg'^*_{\mathrm{comp}}K
$$

of [def-cbc-completed-exchange-map] is an isomorphism, natural
in $K$ and coherent for identities and pasted squares.
