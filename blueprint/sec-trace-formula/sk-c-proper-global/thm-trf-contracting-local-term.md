+++
id = "thm-trf-contracting-local-term"
kind = "theorem"
title = "Local term of a contracting correspondence; Varshavsky 2.1"
order = 2509
uses = ["def-trf-categorical-trace", "def-trf-frobenius-operators", "def-trf-iterated-weil-map", "def-trf-local-term", "lem-trf-contracting-trace-stalk", "lem-trf-frobenius-degree-formula", "lem-trf-frobenius-differential-vanishing", "lem-trf-local-term-locality", "thm-trf-fixed-point-evaluation-finite"]
+++
Let $X_0$ be separated of finite type over $\mathbf F_q$, put
$X=X_0\times_{\mathbf F_q}k$, let $(K,\varphi)$ be a strict Weil
complex, and let $u_m:L\Phi^m{}^*K\to K$ be the scheme-Frobenius map
of [def-trf-iterated-weil-map]. For the graph correspondence
$c=(\operatorname{id}_X,\Phi^m)$ and a point
$y\in X_0(\mathbf F_{q^m})$, the local term of
[def-trf-local-term] is

$$
\operatorname{LT}_y(u_m)
=
\operatorname{tr}_A\bigl(F_{y,m}\mid K_{\bar y}\bigr).
$$

## Proof

Step 1 (reduction to the stalk). By [lem-trf-local-term-locality],
$\operatorname{LT}_y(u_m)$ depends only on the stalk $K_{\bar y}$
and on the stalk map $u_{m,\bar y}$, which by
[def-trf-frobenius-operators] is the local geometric Frobenius
operator $F_{y,m}$ on $K_{\bar y}$.

Step 2 (the contraction). The graph correspondence
$(\operatorname{id}_X,\Phi^m)$ is contracting at the fixed point $y$
in the sense of Varshavsky, loc. cit., 2.1: its second leg is the
$m$-th Frobenius, whose differential vanishes by
[lem-trf-frobenius-differential-vanishing]. By
[lem-trf-contracting-trace-stalk], the trace map restricted to
$y$ is the stalk evaluation: the composite evaluates
$u_{m,\bar y}$ against the identity, which is exactly the categorical
trace $\operatorname{tr}_A(F_{y,m}\mid K_{\bar y})$ of
[def-trf-categorical-trace].

Step 3 (the categorical trace is the local trace). By the stalk-trace
computation of [thm-trf-fixed-point-evaluation-finite], the
categorical trace of $F_{y,m}$ on the perfect stalk $K_{\bar y}$ is
$\operatorname{tr}_A(F_{y,m}\mid K_{\bar y})$, the degree-dependence
being [lem-trf-frobenius-degree-formula]. Combining Steps 1–3
gives the asserted equality.
