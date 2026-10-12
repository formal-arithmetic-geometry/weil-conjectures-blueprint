+++
id = "cor-zl-hasse-weil-general-bound"
kind = "theorem"
title = "Hasse–Weil bound in every dimension"
order = 3220
tags = ["latex:corollary"]
uses = ["cor-trf-point-counting", "cor-zl-hasse-bound", "def-weil-algebraically-closed-coefficients", "def-weil-betti-numbers", "def-weil-finite-field-fiber", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-reciprocal-roots", "def-weil-point-counts-zeta", "def-weil-smooth-proper-cohomological-family", "prop-endpoints", "prop-weight-purity-roots"]
+++
Fix the finite-field datum
$(p,a,q,k_0,k)$, where $q=p^a$, and a prime $\ell\neq p$; write
$\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$,
fix an isomorphism $\iota:\Qlb\xrightarrow{\sim}\mathbf C$, and interpret
the $\Qlb$-objects in the
algebraically closed
coefficient category. Let $X_0/k_0$ be
smooth, proper, geometrically
connected of pure dimension $d\in\mathbf Z_{\geq1}$, put
$X=X_0\times_{k_0}k$, let $F$ be the
global geometric Frobenius
in the geometric-Frobenius convention, and
let $(V_{i,\ell},F_{i,\ell},P_{i,\ell})_{0\leq i\leq2d}$ be the
smooth-proper
cohomological family extended to $\Qlb$, with
reciprocal roots taken in the
ordinary/reciprocal-root convention. Let
$b_i=\deg P_i=\dim_{\Qlb}H^i(X,\Qlb)$ be the
Betti numbers, and let
$N_n:=\#X_0(\mathbf F_{q^n})$ in the
point-count convention. Then, for every
integer $n\geq1$,

$$
\boxed{
\bigl|N_n-(q^{dn}+1)\bigr|\;\le\;\sum_{i=1}^{2d-1}b_i\,q^{in/2}}.
$$

In particular, for $n=1$,
$|N_1-q^d|\leq1+\sum_{i=1}^{2d-1}b_iq^{i/2}$, and for a curve ($d=1$,
$b_1=2g$) the bound reads $|N_n-(q^n+1)|\leq2g\,q^{n/2}$.

The endpoint term $1$ coming from $H^0$ cannot be dropped: for
$X_0=\mathbf P^1_{k_0}$ one has $d=1$, $b_1=0$ and $N_1=q+1$, so
$|N_1-q^d|=1>0=\sum_{i=1}^{2d-1}b_iq^{i/2}$. For $d=0$ the scheme
$X_0$ is $\operatorname{Spec}k_0$ and $N_n=1=q^{dn}$; the endpoints
$i=0$ and $i=2d$ coincide, which is why $d\geq1$ is assumed above.
