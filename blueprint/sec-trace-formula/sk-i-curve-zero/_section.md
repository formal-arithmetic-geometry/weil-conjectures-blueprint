+++
id = "sk-i-curve-zero"
kind = "proposition"
title = "Zero-stalk vanishing on a smooth curve"
order = 2645
uses = ["sk-d-corr", "sk-d-curve-pieces", "sk-d-local-term", "sk-d-trace-class", "sk-p-pairing", "sk-thm-sf-package"]
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations.localTerm_traceClass_eq_zero_of_isZero"]
tags = ["sketch"]
+++
Let $s$ be the spectrum of a field and let $X$ be quasi-compact, compactifiable
and smooth of relative dimension one over $s$. Let $(K,\varphi)$ be a Weil
complex on $X$ with the model Frobenius of a scheme $X_0$ over a finite field
$\mathbf F_q$, with $K\in D^b_{ctf}(X,A)$ and $\varphi:\Phi_1^*K\to K$ an
arbitrary (not necessarily invertible) Frobenius coefficient morphism. Fix
$m\ge1$, a point $\bar x:s\to X$ over $s$ fixed by $\Phi_m$, and a clopen
subscheme $B$ of the fixed scheme $\Fix(1,\Phi_m)$ whose underlying set is
$\{\bar x\}$; assume $\Fix(1,\Phi_m)$ is proper over $s$. If $K_{\bar x}=0$,
then the local term $\LT_B(\varphi_m)$ is zero.
