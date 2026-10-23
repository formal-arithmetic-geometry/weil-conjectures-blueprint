+++
id = "lem-wf-euler-product-middle-extension"
kind = "theorem"
title = "Graded Euler-product identity for a middle extension"
lean = ["AlgebraicGeometry.WeilSheaf.coeff_prod_inv_localPolynomial_stalk_directImage"]
order = 3901
tags = ["latex:corollary"]
uses = ["d-real-cohom", "def-weil-ordinary-compact-cohomology", "def-wf-middle-extension", "lem-wf-boundary-stalk-invariants", "prop-wf-weil-sheaf-representation-equivalence", "det-def-sfb-bounded-constructible", "sk-lem-coefficient-heart", "det-thm-tf-uniform-formula-weil", "thm-trf-l-function-euler-product"]
+++
Let $X_0$ be a smooth geometrically connected affine curve, let
$j:U_0\hookrightarrow X_0$ be a dense open immersion, and let
$\mathcal F$ be a lisse Weil sheaf on $U_0$, i.e. a lisse
$\overline{\mathbf Q}_{\ell,U}$-module ([sk-lem-coefficient-heart]) with a Weil structure,
with the middle extension
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
