+++
id = "prop-weil-pbc-roos-triangle"
kind = "theorem"
title = "Roos triangle and Milnor exact sequence"
order = 1314
uses = ["def-weil-derived-limit", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-derived-inverse-limit", "lem-weil-derived-limit-existence", "prop-weil-pbc-derived-product-representation"]
tags = ["latex:proposition"]
+++
For every $M_\bullet\in D(\operatorname{Tow}_{A}(T))$, the tower category
being that of [def-weil-pbc-adic-coefficient-datum], the transition maps
define an endomorphism $s$ of $R\!\prod_nM_n$, and the defining Roos triangle
of [def-weil-pbc-derived-inverse-limit] is the functorial distinguished
triangle

$$
 \Rlim M_\bullet\longrightarrow R\!\prod_nM_n
 \xrightarrow{1-s}R\!\prod_nM_n
 \longrightarrow(\Rlim M_\bullet)[1].
$$

If $U$ is a weakly contractible quasi-compact object of $T_{\Proet}$, then
for every $i\in\mathbf Z$ this triangle induces the functorial exact sequence

$$
 0\to\varprojlim{}^1_nH^{i-1}(U,M_n)
 \to H^i(U,\Rlim M_\bullet)
 \to\varprojlim_nH^i(U,M_n)\to0.
$$
