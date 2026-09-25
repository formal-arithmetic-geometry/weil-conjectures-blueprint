+++
id = "lem-wf-euler-product-middle-extension"
kind = "theorem"
title = "Graded Euler-product identity for a middle extension"
order = 2840
tags = ["latex:corollary"]
uses = ["d-real-cohom", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-qbar-category", "def-wf-middle-extension", "lem-rp-determinant-log", "lem-sc-cohomological-dimension", "lem-wf-point-count-linear-growth", "lemma-weil-pbc-etale-cohomology-continuity", "thm-trf-grothendieck-lefschetz-qbar"]
+++
Let $X_0$ be a smooth geometrically connected affine curve, let
$j:U_0\hookrightarrow X_0$ be a dense open immersion, and let
$\mathcal F$ be lisse on $U_0$ in the coefficient conventions of
[def-weil-pbc-qbar-category], with the middle extension
$j_*\mathcal F$ of
[def-wf-middle-extension]. As power series in $t$,

$$
\prod_{x\in|X_0|}\det\bigl(1-F_xt^{d(x)},(j_*\mathcal F)_{\bar x}\bigr)^{-1}
=
\frac{\det(1-Ft,H_c^1(X,j_*\mathcal F))}
{\det(1-Ft,H_c^2(X,j_*\mathcal F))},
$$

where the left-hand side is the $L$-series [d-real-cohom] of the constructible sheaf
$j_*\mathcal F$ on $X_0$ and the right-hand side is its graded form
in the compact-support convention of
[def-weil-ordinary-compact-cohomology].

## Proof

This is the constructible-level form of the trace-formula identity in
the coefficient category [def-weil-pbc-qbar-category]: the
coefficient of $t^m$ in $t\bigl(\log\prod_{x}\det(1-F_xt^{d(x)}, (j_*\mathcal F)_{\bar x})^{-1}\bigr)'$ is

$$
\sum_{d\mid m}d\sum_{\substack{x\in|X_0|\\d(x)=d}}
\operatorname{Tr}\bigl(F_x^{m/d}\mid(j_*\mathcal F)_{\bar x}\bigr)
=\sum_{y\in X_0(k_m)}\operatorname{Tr}(F_{y,m}\mid(j_*\mathcal F)_{\bar y}),
$$

by the regrouping of closed points over the $k_m$-points (with the
local Frobenius $F_{y,m}$ of the geometric points; the same counting
step as in [lem-wf-point-count-linear-growth]), and the coefficient
of $t^m$ in $t\bigl(\log(\det(1-Ft,H_c^1)/\det(1-Ft,H_c^2))\bigr)'$
is $\sum_i(-1)^i\operatorname{Tr}(F^m\mid H_c^i(X,j_*\mathcal F))$ by
the determinant–logarithm identity
[lem-rp-determinant-log]; the two coefficient sequences agree by
the Grothendieck–Lefschetz trace formula
[thm-trf-grothendieck-lefschetz-qbar] applied to the constructible
sheaf over every $k_m$. Two details: the degree-zero factor is
$1$, because $H_c^0(X,j_*\mathcal F)=0$ (a compactly supported
global section of $j_*\mathcal F$ vanishes in a neighborhood of every
boundary point, hence restricts to zero on the complement of its finite
support in the connected open curve, and by lissity it is zero); and the
cohomology with compact support (the convention of
[def-weil-ordinary-compact-cohomology]) is concentrated in degrees
$0,1,2$ by the cohomological-dimension bound of
[lem-sc-cohomological-dimension](b) for the affine curve
at the finite-torsion levels, with the adic passage of
[lemma-weil-pbc-etale-cohomology-continuity], so the graded form has
exactly the two displayed factors (and $H_c^i=0$ for $i\notin\{0,1,2\}$
enters the log-derivative comparison as zero). Both series have
constant term $1$, so they coincide.
