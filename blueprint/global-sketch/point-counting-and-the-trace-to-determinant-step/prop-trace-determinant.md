+++
id = "prop-trace-determinant"
kind = "theorem"
title = "Trace-to-determinant factorization"
order = 105
tags = ["latex:proposition"]
uses = ["def-frobenius-characteristic-factors", "def-point-count-zeta", "def-smooth-proper-cohomological-family", "prop-every-iterate-trace"]
+++
For every smooth-proper datum $\mathscr X=(X_0,d,X)$ and every prime
$\ell\neq p$, the every-iterate trace identity gives

$$
Z(X_0,T)=
\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}
\quad\text{in }\Ql[[T]]\cap\Ql(T).
$$

The determinant factors use the same carriers
$V_{i,\ell}=H^i(X,\Ql)$ and geometric Frobenius operators
$F_{i,\ell}$ as the trace identity. This proposition is treated as the
single trace-to-determinant interface; the elementary formal-power-series
calculation is not declared as a separate blueprint result.
