+++
id = "cor-rp-euler-product"
kind = "theorem"
title = "Euler product of the $L$-function of a lisse sheaf"
order = 3007
tags = ["latex:corollary"]
uses = ["d-real-cohom", "def-weil-punctual-weights", "def-wf-weil-category", "lem-a1-affine-hc0", "thm-trf-grothendieck-lefschetz-qbar", "thm-trf-l-function-euler-product"]
+++
Let $U_0$ be a smooth geometrically connected affine curve, let
$U=U_0\times_{k_0}k$, and let $\mathcal G_0$ be a lisse
Weil sheaf on $U_0$. Then, as
power series in $t$ (the Euler series of [d-real-cohom]),

$$
\prod_{x\in|U_0|}\det\bigl(1-F_xt^{d(x)},\mathcal G_{0,\bar x}\bigr)^{-1}
=
\frac{\det(1-Ft,H_c^1(U,\mathcal G))}
{\det(1-Ft,H_c^2(U,\mathcal G))},
$$

where $|U_0|$ is the set of closed points, $d(x)$ the degree of
$x$, and the right-hand side is the graded form of the
Grothendieck–Lefschetz trace formula
[thm-trf-grothendieck-lefschetz-qbar] (summed
with the signs $(-1)^{i+1}$).
