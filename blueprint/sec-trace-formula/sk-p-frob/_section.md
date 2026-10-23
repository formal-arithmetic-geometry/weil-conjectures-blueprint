+++
id = "sk-p-frob"
kind = "proposition"
title = "The Frobenius local term on a curve"
order = 3529
uses = ["sk-d-curve-pieces", "sk-d-integral", "sk-d-local-term", "sk-d-proper-pushforward", "sk-d-trace", "sk-d-weil", "sk-i-additivity", "sk-i-curve-zero", "sk-p-local", "sk-p-proper", "sk-thm-sf-package", "sk-d-trace-class", "sk-p-pairing", "sk-lem-tf-fixed-points"]
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations.localTerm_traceClass_eq_trace"]
tags = ["sketch"]
+++
Recall the $k$-linear Frobenius $\Phi_X$ of [sk-d-weil], the local terms
$\operatorname{LT}_y$ of [sk-d-trace-class] and the trace $\operatorname{tr}_A$ of [sk-d-trace].
Let $X_0$ be a smooth curve over $k_0$, let
$X=X_0\times_{k_0}k$, let $K\in\Dctf(X,A)$ and let
$v:(\Phi_X^m)^*K\to K$ be any morphism in $\Dctf(X,A)$. For
$y\in X_0(\mathbf F_{q^m})$ one has

$$
 \operatorname{LT}_y(v)
   =\operatorname{tr}_A(v_{\bar y}\mid K_{\bar y}).
$$

*Complement.* Let $s$ be the spectrum of a field and let $X$ be quasi-compact, compactifiable
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
