+++
id = "cor-rp-euler-product"
kind = "theorem"
title = "Euler product of the $L$-function of a lisse sheaf"
order = 4183
tags = ["latex:corollary"]
uses = ["def-weil-punctual-weights", "def-wf-weil-category", "lem-a1-affine-hc0", "lem-rp-determinant-log", "thm-trf-grothendieck-lefschetz-qbar"]
+++
Let $U_0$ be a smooth geometrically connected affine curve, let
$U=U_0\times_{k_0}k$, and let $\mathcal G_0$ be a lisse
Weil sheaf on $U_0$. Then, as
power series in $t$,

$$
\prod_{x\in|U_0|}\det\bigl(1-F_xt^{d(x)},\mathcal G_{0,\bar x}\bigr)^{-1}
=
\frac{\det(1-Ft,H_c^1(U,\mathcal G))}
{\det(1-Ft,H_c^2(U,\mathcal G))},
$$

where $|U_0|$ is the set of closed points, $d(x)$ the degree of
$x$, and the right-hand side is the graded form of the
Grothendieck–Lefschetz trace formula
[thm-trf-grothendieck-lefschetz-qbar] of the trace-formula chapter (summed
with the signs $(-1)^{i+1}$).

## Proof

Let $Z(t)$ denote the left-hand side and
$P(t):=\prod_{i=0}^{2}\det\bigl(1-Ft,H_c^i(U,\mathcal G)\bigr)^{(-1)^{i+1}}$
the right-hand side in graded form (the factor $i=0$ is $1$ by
[lem-a1-affine-hc0]). The coefficient of $t^m$ in
$t(\log Z)'(t)$ is

$$
\sum_{d\mid m}d\sum_{\substack{x\in|U_0|\\ d(x)=d}}
\operatorname{Tr}\bigl(F_x^{m/d}\mid\mathcal G_{0,\bar x}\bigr),
$$

the classical regrouping of the closed points above the
$\mathbf F_{q^m}$-points: the closed points of degree $d\mid m$
contribute $d$ rational points, and the point count over
$\mathbf F_{q^m}$ together with the identity
$F_{y,m}=F_x^{m/d}$ for the local geometric Frobenius of
[def-weil-punctual-weights] gives

$$
\sum_{d\mid m}d\sum_{\substack{x\in|U_0|\\ d(x)=d}}
\operatorname{Tr}\bigl(F_x^{m/d}\mid\mathcal G_{0,\bar x}\bigr)
=
\sum_{y\in U_0(\mathbf F_{q^m})}
\operatorname{Tr}\bigl(F_{y,m}\mid\mathcal G_{0,\bar y}\bigr).
$$

The coefficient of $t^m$ in $t(\log P)'(t)$ is, by the
determinant–logarithm identity of
[lem-rp-determinant-log],

$$
\sum_i(-1)^{i}\operatorname{Tr}\bigl(F^m\mid H_c^i(U,\mathcal G)\bigr).
$$

By the Grothendieck–Lefschetz trace formula
[thm-trf-grothendieck-lefschetz-qbar], applied to
$\mathcal G_0$ over every field $\mathbf F_{q^m}$ (i.e. to the
sheaf and its finite base changes, with the iterates $F^m$ of the
global Frobenius and the local operators $F_{y,m}$), these two
coefficients agree for every $m\ge1$; hence the two power series
have the same logarithmic derivative, and both have constant term
$1$, so they coincide.
