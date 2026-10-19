+++
id = "sk-def-trace"
kind = "definition"
title = "The trace function, and the classical Fourier transform"
order = 3032
lean = ["AlgebraicGeometry.WeilSheaf.traceFunction"]
uses = ["sk-def-char", "sk-def-fourier-set"]
tags = ["sketch"]
+++
For a Weil complex $K$ on a separated finite-type $k_0$-scheme and an
$\mathbf F_{q^n}$-point $x$,

$$
t_K(x)=\Tr\bigl(F_x^{(n)}\mid K_{\bar x}\bigr)
=\sum_j(-1)^j\Tr\bigl(F_x^{(n)}\mid\mathcal H^j(K)_{\bar x}\bigr),
$$

with the local Frobenius operators of def:weil-local-frobenius-trace.
The classical Fourier transform of a function $f$ on $\mathbf F_{q^n}$ is
$\widehat f(y)=\sum_xf(x)\psi_n(xy)$.
