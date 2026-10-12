+++
id = "lemma-weil-pbc-level-map-derived-limit"
kind = "lemma"
title = "The rectangle passes to the derived inverse limit"
order = 1376
uses = ["def-weil-pbc-adic-derived-inverse-limit", "lemma-weil-pbc-level-map-operator-naturality", "lemma-weil-pbc-level-map-rectangle", "lemma-weil-pbc-level-map-tower-compatibility"]
+++
Write $A_\infty=R\varprojlim A_n$ and likewise for the other three towers,
and write $H,V,H',V'$ for the limits of $h,v,h',v'$. Then

$$
V'H=H'V:A_\infty\longrightarrow D_\infty.
$$

For every $n$, both maps have the same $n$th component

$$
\operatorname{pr}_{D,n}V'H
=v'_nh_n\operatorname{pr}_{A,n}
=h'_nv_n\operatorname{pr}_{A,n}
=\operatorname{pr}_{D,n}H'V.
$$

The equality is natural for compatible tower endomorphisms.
