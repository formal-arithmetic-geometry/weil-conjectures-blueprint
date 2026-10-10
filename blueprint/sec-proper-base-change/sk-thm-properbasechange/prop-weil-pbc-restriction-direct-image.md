+++
id = "prop-weil-pbc-restriction-direct-image"
kind = "theorem"
title = "Restriction of the direct image to bounded constructibles"
order = 1302
uses = ["def-weil-pbc-constructible-direct-image-finiteness", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-operations", "lem-sp-finite-filtration-induction", "thm-constructible-serre", "thm-sp-truncation-e2"]
tags = ["latex:proposition"]
+++
Let $\Lambda=P_n$ be as in
[def-weil-pbc-constructible-direct-image-finiteness], let $u:S\to T$ be a
morphism of schemes, and suppose $\mathrm{FIN}(u,\Lambda;c)$. Then the
ambient functor $Ru_*$ restricts to an exact triangulated functor
$$
 Ru_*:\Dbc(S_{\Proet},\Lambda)\longrightarrow\Dbc(T_{\Proet},\Lambda),
$$
and if $K\in\Dbc(S_{\Proet},\Lambda)$ has cohomology in $[a,b]$, then
$Ru_*K$ has cohomology in $[a,b+c]$.
