+++
id = "sk-thm-trace-formula"
kind = "proposition"
title = "Finite-coefficient Lefschetz trace formula"
order = 2720
uses = ["sk-c-proper-global", "sk-d-lines", "sk-d-operator", "sk-d-relative-frob", "sk-d-six", "sk-d-trace", "sk-d-weil", "sk-d-weil-push", "sk-i-global-additivity", "sk-i-relative-frob", "sk-i-topology", "sk-p-frob", "sk-p-local", "sk-p-trace", "sk-thm-sf-package"]
lean = ["AlgebraicGeometry.ProEtale.trace_globalOperator_eq_sum_trace_stalkFrobenius"]
tags = ["sketch"]
+++
Let $\Omega$ be an algebraically closed field, $s=\operatorname{Spec}\Omega$, and
let $X_0$ be a separated scheme of finite type over a finite field $\mathbf F_q$
with $X=X_0\times_{\mathbf F_q}\Omega$ compactifiable over $s$. For every Weil
datum $(K,\varphi)$ on $X$ (model Frobenius, $K\in D^b_{ctf}(X,A)$, $\varphi$
invertible) and every $m\ge1$, the fixed points $\bar x:s\to X$ of $\Phi_m$
over $s$ are the points of $X_0(\mathbf F_{q^m})$, and, with compact cohomology
and ordinary traces,

$$
\boxed{\tr_A(F_{c,m}\mid R\Gamma_c(X,K))
=\sum_{x\in X_0(\mathbf F_{q^m})}\tr_A(F_{x,m}\mid K_{\bar x}).}
$$
