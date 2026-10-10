+++
id = "lem-wf-conjugate-tensor-traces"
kind = "lemma"
title = "The conjugate-tensor trace identity"
order = 2761
uses = ["cor-rp-euler-product", "def-weil-pbc-qbar-category", "def-weil-pbc-scheme-conventions", "def-weil-punctual-weights", "lem-zl-log-det-identity"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.traceFunction_tensorObj_and_l2Series_mul_lSeries"]
+++
Let $X_0$ be a smooth geometrically connected affine curve over
$k_0=\mathbf F_q$ (the separated finite-type conventions of
[def-weil-pbc-scheme-conventions]), let $\mathcal F$ be a lisse
Weil sheaf in the coefficient category of
[def-weil-pbc-qbar-category], and let
$\bar{\mathcal F}$ be a Weil sheaf on $X_0$ whose local Frobenius
eigenvalues are the complex-conjugate ($\iota$-conjugate) ones: at every
closed point $x$, the image under $\iota$ of the local polynomial
$\det(1-F_xT\mid\bar{\mathcal F}_{\bar x})$ is the complex conjugate of
that of $\det(1-F_xT\mid\mathcal F_{\bar x})$. Then for every
$y\in X_0(k_m)$,

$$
\iota\operatorname{Tr}\bigl(F_y\mid
(\mathcal F\otimes\bar{\mathcal F})_{\bar y}\bigr)
=
\bigl|\iota\operatorname{Tr}(F_y\mid\mathcal F_{\bar y})\bigr|^2
\in\mathbf R_{\ge0},
$$

and consequently the $L^2$-series of the trace function,

$$
\varphi_{\mathcal F}(t):=\sum_{m\ge1}\Bigl(\sum_{y\in X_0(k_m)}
\bigl|\iota\operatorname{Tr}(F_y\mid\mathcal F_{\bar y})\bigr|^2\Bigr)t^{m-1},
$$

is the logarithmic derivative $L'/L$ of the $L$-series

$$
L(t):=L(X_0,\mathcal F\otimes\bar{\mathcal F},t)
=\prod_{x\in|X_0|}
\det\bigl(1-F_xt^{d(x)},(\mathcal F\otimes\bar{\mathcal F})_{\bar x}\bigr)^{-1},
$$

the factorization being the Euler-product form of the
Grothendieck–Lefschetz trace formula on the affine curve.
