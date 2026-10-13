+++
id = "sk-def-cohfamily"
kind = "definition"
title = "The smooth-proper cohomological family"
order = 3199
lean = ["TraceDatum", "TraceDatum.P"]
tags = ["sketch"]
+++
Let $X_0/k_0$ be smooth, proper and geometrically connected of pure dimension
$d\ge0$, put $X=X_0\times_{k_0}k$, fix $\ell\ne p$ and write $\Ql=\mathbf Q_\ell$. Let $F$ be the geometric Frobenius acting on the ordinary
cohomology $H^{i}(X,\Ql)$, and put

$$
V_{i,\ell}=H^{i}(X,\Ql),\qquad
F_{i,\ell}=F\mid_{V_{i,\ell}},\qquad
P_{i,\ell}(T)=\det\bigl(1-TF_{i,\ell}\mid V_{i,\ell}\bigr).
$$

The tuple $(V_{i,\ell},F_{i,\ell},P_{i,\ell})_{0\le i\le2d}$ is the
*smooth-proper cohomological family*. An *eigenvalue* of $F$ on
$V_{i,\ell}$ always means an eigenvalue in $\Qlb$ of $F\otimes\Qlb$ on
$V_{i,\ell}\otimes_{\Ql}\Qlb$, i.e. a root in $\Qlb$ of the characteristic
polynomial of $F_{i,\ell}$; this is what a fixed isomorphism
$\iota:\Qlb\xrightarrow{\sim}\mathbf C$ is applied to.

Notation: $P_i\in\Z[T]$ denotes the integral Frobenius factor produced later
by [sk-thm-intfactors], and $P_i^{(\ell)}$ its coefficientwise extension
$\Z[T]\to\Ql[T]$; nothing in this definition depends on $P_i$, and until
[sk-thm-intfactors] only the $\ell$-adic factors $P_{i,\ell}$ are used.
