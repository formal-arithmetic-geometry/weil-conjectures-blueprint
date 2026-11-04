+++
id = "definition-growth-squared-traces"
kind = "definition"
title = "Growth of squared traces"
order = 1191
lean = ["AlgebraicGeometry.WeilComplex.traceEnergy", "AlgebraicGeometry.WeilComplex.l2Weight", "AlgebraicGeometry.WeilSheaf.traceEnergy", "AlgebraicGeometry.WeilSheaf.l2Weight"]
+++
Let $K$ be a constructible Weil complex on an affine curve $X_0$. For
$n\ge1$ and $x\in X_0(k_n)$, let $\operatorname{Frob}_{x,n}$ be the
Frobenius acting on the stalk $K_{\bar x}$
(Theorem [theorem-grothendieck-lefschetz-trace-formula]), and set

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
