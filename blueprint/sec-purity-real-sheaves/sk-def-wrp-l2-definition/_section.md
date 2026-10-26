+++
id = "sk-def-wrp-l2-definition"
kind = "definition"
title = "Growth of squared traces"
order = 3892
uses = ["sk-d-real-weil"]
tags = ["sketch"]
+++
For a constructible Weil complex $K$ on an affine curve $X_0$, set

$$
 t_{K,n}(x)=\sum_i(-1)^i\operatorname{Tr}
       (F_x^{(n)}\mid\mathcal H^i(K)_{\bar x}),\qquad
 S_n(K)=\sum_{x\in X_0(k_n)}|\iota t_{K,n}(x)|^2.
$$

Its *$L^2$ growth parameter* is

$$
 \nu(K)=\limsup_{n\to\infty}\frac{\log_q S_n(K)}n-1,
 \qquad \log_q0=-\infty.
$$

Equivalently, $\nu(K)$ is the supremum of the real numbers $a$ for
which $\limsup_n S_n(K)/q^{n(a+1)}>0$, where the supremum of the empty
set is $-\infty$. A cohomological shift multiplies the trace function
by a sign and leaves $\nu(K)$ unchanged; thus $\nu$ measures the growth
of traces and, unlike the weights of complexes in [sk-d-real-weights],
does not see shifts.

*Complement.* In the detail nodes $\nu(K)$ is written $\|K\|$ and the series
$\sum_nS_n(K)t^{n-1}$ is the $L^2$-series ([def-wf-l2-norm],
[def-wf-l2-series]).
