+++
id = "sk-p-proper"
kind = "theorem"
title = "Proper pushforward and Lefschetz–Verdier"
order = 562
uses = ["sk-d-corr", "sk-d-integral", "sk-d-proper-pushforward", "sk-d-trace-class", "sk-def-sf-kv-maps", "sk-p-pairing", "sk-thm-sf-comp-composition", "sk-thm-sf-kunneth-verdier", "sk-thm-sf-package"]
tags = ["sketch"]
+++
Let $f:X\to Y$ and $g:C\to C'$ be proper, and let
$c'=(c'_1,c'_2):C'\to Y\times Y$ satisfy $c'_ig=fc_i$. Set $K'=Rf_*K$, and
let $u'$ be the pushforward of $u$ to $(Y,K')$ of
Definition [sk-d-proper-pushforward]. With
the induced proper map $h:\Fix(c)\to \Fix(c')$ one has

$$
\operatorname{Tr}_{c'}(u')=h_*\operatorname{Tr}_c(u).
$$

If $X$ and $C$ are proper over $k$, this gives

$$
\operatorname{tr}_A(T_c(u)\mid R\Gamma(X,K))
=\int_{\Fix(c)}\operatorname{Tr}_c(u)
=\sum_B\operatorname{LT}_B(u),
$$

for any finite open-and-closed decomposition $\Fix(c)=\coprod B$.
