+++
id = "sk-p-frob"
kind = "proposition"
title = "Frobenius local terms on smooth curves"
order = 2355
uses = ["sk-d-curve-pieces", "sk-d-integral", "sk-d-local-term", "sk-d-proper-pushforward", "sk-d-trace", "sk-d-weil", "sk-i-additivity", "sk-i-curve-zero", "sk-p-local", "sk-p-proper", "sk-thm-sf-package"]
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations.localTerm_traceClass_eq_trace"]
tags = ["sketch"]
+++
Let $s$ be the spectrum of a field and let $X$ be quasi-compact, compactifiable
and smooth of relative dimension one over $s$. Let $(K,\varphi)$ be a Weil
complex on $X$ with the model Frobenius of a scheme $X_0$ over a finite field
$\mathbf F_q$, with $K\in D^b_{ctf}(X,A)$ and $\varphi:\Phi_1^*K\to K$ an
arbitrary (not necessarily invertible) Frobenius coefficient morphism. Fix
$m\ge1$, a point $\bar x:s\to X$ over $s$ fixed by $\Phi_m$ with perfect
(dualizable) stalk $K_{\bar x}$, and a clopen subscheme $B$ of the fixed scheme
$\Fix(1,\Phi_m)$ whose underlying set is $\{\bar x\}$; assume $\Fix(1,\Phi_m)$ is
proper over $s$. Then the local term at $\bar x$ is

$$
\LT_B(\varphi_m)=
\hyperref[sk-d-trace]{\tr_A}(F_{x,m}\mid K_{\bar x}).
$$

No local constancy of $K$ at $\bar x$ is assumed.
