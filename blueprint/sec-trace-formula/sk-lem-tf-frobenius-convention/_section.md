+++
id = "sk-lem-tf-frobenius-convention"
kind = "lemma"
title = "Agreement with geometric Weil Frobenius"
order = 3755
uses = ["sk-d-weil", "sk-def-sf-weil-complexes"]
tags = ["sketch"]
+++
Let $X=X_0\times_{k_0}k$, the $k$-linear Frobenius $\Phi_X$, the graphs $c_m$, the iterates
$\psi_m$ and the operators $T_{c_m}$ be as in [sk-d-weil].
Let $\operatorname{Fr}_X$ be the semilinear geometric Frobenius
of [sk-def-sf-weil-complexes], and for a morphism
$\phi:\operatorname{Fr}_X^*K\to K$ put
$\phi^{[m]}=\phi\circ \operatorname{Fr}_X^*\phi\circ\cdots\circ(\operatorname{Fr}_X^{m-1})^*\phi$.
There are natural isomorphisms of functors
$\Dctf(X,A)\to\Dctf(X,A)$

$$
 \kappa_m:(\Phi_X^m)^*K\xrightarrow{\sim}(\operatorname{Fr}_X^m)^*K
$$

compatible with iteration. For a Weil structure
$\phi:\operatorname{Fr}_X^*K\xrightarrow{\sim}K$, put
$\psi=\phi\kappa_1$. Then

$$
 \psi_m=\phi^{[m]}\kappa_m,
 \qquad T_{c_m}(\psi_m)=\operatorname{Frob}_{X,K}^{m},
$$

where $\operatorname{Frob}_{X,K}$ is the geometric Frobenius operator
on compact cohomology defined after
[sk-def-sf-weil-complexes]. The same identity of
operators holds for an arbitrary morphism $(\operatorname{Fr}_X^m)^*K\to K$ in place
of $\phi^{[m]}$.
