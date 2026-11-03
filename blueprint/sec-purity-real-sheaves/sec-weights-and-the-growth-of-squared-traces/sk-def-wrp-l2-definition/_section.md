+++
id = "sk-def-wrp-l2-definition"
kind = "definition"
title = "Growth of squared traces"
order = 705
uses = ["sk-d-real-weil", "sk-thm-tf-uniform-formula"]
tags = ["sketch"]
+++
For a constructible Weil complex $K$ on an affine curve $X_0$, a point
$x\in X_0(k_n)$, with $\operatorname{Frob}_{x,n}$ the Frobenius acting on
the stalk $K_{\bar x}$ (Theorem [sk-thm-tf-uniform-formula]), set

$$
t_{K,n}(x)=\sum_i(-1)^i\operatorname{Tr}
(\operatorname{Frob}_{x,n}\mid\mathcal H^i(K)_{\bar x}),\qquad
S_n(K)=\sum_{x\in X_0(k_n)}|\iota t_{K,n}(x)|^2.
$$

Put

$$
\nu(K)=\limsup_{n\to\infty}\frac{\log_q S_n(K)}n-1,
\qquad \log_q0=-\infty.
$$

Equivalently, $\nu(K)$ is the supremum of the real numbers $a$ for
which $\limsup_n S_n(K)/q^{n(a+1)}>0$, where the supremum of the empty
set is $-\infty$.

*Complement.* In the detail nodes $\nu(K)$ is written $\|K\|$ and the series
$\sum_nS_n(K)t^{n-1}$ is the $L^2$-series ([def-wf-l2-norm],
[def-wf-l2-series]).
