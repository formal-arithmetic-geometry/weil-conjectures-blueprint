+++
id = "sk-def-sp-tate-twist"
kind = "definition"
title = "Tate twists"
order = 1548
uses = ["sk-prop-sfb-qlbar-colimit-x", "sk-def-sfb-pulled-back-coefficients"]
tags = ["sketch"]
+++
Let $X$ be a scheme on which $\ell$ is invertible. Let $\mu_{\ell^n,X}$ be the sheaf of
$\ell^n$th roots of unity on $X_{\mathrm{proét}}$; since $\ell$ is invertible on $X$, it is
locally isomorphic to $(\mathbf Z/\ell^n\mathbf Z)_X$. For a finite ring $A$ with $\ell^rA=0$
put
$$
A_X(1)=\mu_{\ell^r,X}\otimes_{\mathbf Z/\ell^r\mathbf Z}A_X,
$$
which by the Kummer maps does not depend on $r$. Put
$$
\cO_{E,X}(1)=\varprojlim_n(\cO_E/\ell^n)_X(1),
$$
and obtain $E_X(1)$ and $\QbarX(1)$ by inverting $\ell$ and passing to the colimit over $E$
(compare [sk-prop-sfb-qlbar-colimit-x]). Each $\Lambda_X(1)$ is locally free of rank one.
For $d\ge0$, $\Lambda_X(d)$ is the $d$-fold tensor power, $\Lambda_X(-d)$ its dual, and
$$
K(d)=K\otimes^{\mathbf L}_{\Lambda_X}\Lambda_X(d)
$$
for $K\in D(X_{\mathrm{proét}},\Lambda)$.
