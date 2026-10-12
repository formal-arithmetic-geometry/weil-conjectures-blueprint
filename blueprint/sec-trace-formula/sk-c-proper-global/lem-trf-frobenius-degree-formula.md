+++
id = "lem-trf-frobenius-degree-formula"
kind = "lemma"
title = "Degree formula for the local Frobenius"
order = 2649
uses = ["def-trf-frobenius-operators", "def-trf-iterated-weil-map", "lem-trf-iterated-weil-cocycle", "lem-trf-local-frobenius-conjugacy", "prop-trf-scheme-galois-comparison", "prop-trf-trace-formal-laws"]
+++
Let $x\in|X_0|$ be a closed point with degree
$d_x=[\kappa(x):\Fq]$, let $m$ be divisible by $d_x$, let
$x_m\in X_0(\mathbf F_{q^{d_x}})$ be a point above $x$, and put
$F_x=F_{x_m,d_x}$, the *one-circuit local Frobenius* (well
defined up to conjugation by
[lem-trf-local-frobenius-conjugacy]). Then for every
$y\in X_0(\mathbf F_{q^m})$ above $x$,

$$
\operatorname{tr}_A\bigl(F_{y,m}\mid K_{\bar y}\bigr)
=
\operatorname{tr}_A\bigl(F_x^{\,m/d_x}\mid K_{\bar x}\bigr)
$$

in $A$.
