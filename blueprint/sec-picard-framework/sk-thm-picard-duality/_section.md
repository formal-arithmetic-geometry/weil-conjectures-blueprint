+++
id = "sk-thm-picard-duality"
kind = "theorem"
title = "Serre duality"
order = 712
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sk-def-curve"]
lean = ["AlgebraicGeometry.Scheme.serreDuality"]
tags = ["sketch"]
+++
Let $X$ be a smooth proper curve over $k$, of pure dimension
$n\le1$, and $\cF$ a finite locally free $\cO_X$-module. With
$\omega_X=\Omega^n_{X/k}$ the canonical module, let
$t_X:H^n(X,\omega_X)\to k$ be the *trace*: for $n=0$,
$X=\Spec A$ with $A$ finite étale over $k$, $\omega_X=\cO_X$ and
$t_X=\operatorname{Tr}_{A/k}$; for $n=1$ ($X$ integral with function
field $K$), the residue sequence
$0\to\omega_X\to\underline{\Omega^1_{K/k}}\to\bigoplus_{x}i_{x,*}\bigl(\Omega^1_{K/k}/\omega_{X,x}\bigr)\to0$
($x$ over the closed points; the constant sheaf in the middle is flasque) identifies
$H^1(X,\omega_X)$ with the cokernel of
$\Omega^1_{K/k}\to\bigoplus_x\Omega^1_{K/k}/\omega_{X,x}$, and
$t_X\bigl((\eta_x)_x\bigr)=\sum_x\operatorname{res}_x(\eta_x)$, where
$\operatorname{res}_x:\Omega^1_{K/k}\to k$ is Tate's $k$-linear residue
at $x$: it kills $\omega_{X,x}$, it satisfies the residue theorem
$\sum_x\operatorname{res}_x(\eta)=0$ for $\eta\in\Omega^1_{K/k}$, and it
equals $\operatorname{Tr}_{\kappa(x)/k}$ of the classical residue
(computed in $\widehat{\cO}_{X,x}\cong\kappa(x)[[t]]$) whenever
$\kappa(x)/k$ is separable, hence at every $x$ when $k$ is perfect. The residue theorem is exactly what makes
$t_X$ well defined on the cokernel. (The naive formula
$\sum_x\operatorname{Tr}_{\kappa(x)/k}\circ\operatorname{res}_x$ is not
available over imperfect $k$: at a closed point with $\kappa(x)/k$
inseparable, $\widehat{\cO}_{X,x}$ has no coefficient field containing
$k$, and $\operatorname{Tr}_{\kappa(x)/k}$ vanishes on a purely
inseparable extension; Tate's residue avoids both problems.) Then the
trace pairing

$$
H^q(X,\cF)\otimes_kH^{n-q}(X,\cF^{\vee}\otimes\omega_X)
\xrightarrow{\ \cup\ }H^n(X,\cF\otimes\cF^{\vee}\otimes\omega_X)
\xrightarrow{\ \mathrm{ev}\ }H^n(X,\omega_X)\xrightarrow{\ t_X\ }k
$$

is perfect for every $q$:

$$
H^q(X,\cF)^{\vee}\ \cong\ H^{n-q}\bigl(X,\cF^{\vee}\otimes\omega_X\bigr),
$$

and this isomorphism is natural in $\cF$: for a morphism
$\varphi:\cF\to\mathcal G$ of finite locally free modules,
$\langle\varphi_*a,b\rangle=\langle a,(\varphi^{\vee}\otimes1)_*b\rangle$,
i.e. it carries $H^q(\varphi)^{\vee}$ to
$H^{n-q}(\varphi^{\vee}\otimes1)$. In particular ($n=1$, $q=1$,
$\cF=\cO_X$), $H^1(X,\cO_X)^{\vee}\cong H^0(X,\Omega^1_{X/k})$: for a
smooth proper connected curve over algebraically closed $k$ the genus
$\dim_kH^0(C,\Omega^1_{C/k})$ of [sk-def-curve] equals
$\dim_kH^1(C,\cO_C)$, the genus of the conventions of this section.
