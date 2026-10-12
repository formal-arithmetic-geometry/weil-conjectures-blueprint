+++
id = "lem-wf-euler-product-middle-extension"
kind = "theorem"
title = "Graded Euler-product identity for a middle extension"
order = 2994
tags = ["latex:corollary"]
uses = ["d-real-cohom", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-qbar-category", "def-wf-middle-extension", "thm-trf-grothendieck-lefschetz-qbar", "thm-trf-l-function-euler-product"]
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
