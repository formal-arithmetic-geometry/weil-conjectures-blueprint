+++
id = "sk-i-curve-zero"
kind = "corollary"
title = "Frobenius local vanishing"
order = 3796
uses = ["sk-d-corr", "sk-d-curve-pieces", "sk-d-local-term", "sk-d-trace-class", "sk-p-pairing", "sk-thm-sf-package", "sk-lem-tf-curve-supported-pairing", "sk-lem-tf-curve-restriction-zero", "sk-lem-tf-fixed-points"]
tags = ["sketch"]
+++
In the situation of [sk-lem-tf-curve-supported-pairing], for any finite commutative
$\ell$-primary ring $A$, $K\in\Dctf(X,A)$ and $v:(\Phi_X^m)^*K\to K$, one has

$$
 K_{\bar y}=0\quad\Longrightarrow\quad
 \operatorname{LT}_y(v)=0.
$$

*Complement.* Let $s$ be the spectrum of a field and let $X$ be quasi-compact, compactifiable
and smooth of relative dimension one over $s$. Let $(K,\varphi)$ be a Weil
complex on $X$ with the model Frobenius of a scheme $X_0$ over a finite field
$\mathbf F_q$, with $K\in D^b_{ctf}(X,A)$ and $\varphi:\Phi_1^*K\to K$ an
arbitrary (not necessarily invertible) Frobenius coefficient morphism. Fix
$m\ge1$, a point $\bar x:s\to X$ over $s$ fixed by $\Phi_m$, and a clopen
subscheme $B$ of the fixed scheme $\Fix(1,\Phi_m)$ whose underlying set is
$\{\bar x\}$; assume $\Fix(1,\Phi_m)$ is proper over $s$. If $K_{\bar x}=0$,
then the local term $\LT_B(\varphi_m)$ is zero.
