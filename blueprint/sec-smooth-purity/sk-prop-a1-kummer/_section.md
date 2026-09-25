+++
id = "sk-prop-a1-kummer"
kind = "section"
title = "The affine line and $\\mathbf G_m$ with $\\Lambda(1)$-coefficients"
order = 1900
uses = ["sk-def-av-pic", "sk-def-curve", "sk-def-purity-conv", "sk-prop-cd", "sk-prop-kummer-exact", "sk-thm-smooth-base-change"]
+++
*Proposition (sketch).*

In the conventions of [sk-def-purity-conv], write
$p:\Aaf^1_Y\to Y$ for the projection, $j:\mathbf G_{m,Y}\hookrightarrow \Aaf^1_Y$ for the open complement of the zero section, and $\pi=pj$.
For every separated finite-type $Y$:

- **(a)** *Acyclicity of the affine line.*
$Rp_*\Lambda\simeq\Lambda_Y$; equivalently $R^mp_*\Lambda=0$ for $m>0$.
- **(b)** *The Kummer generator.* $R^0\pi_*\Lambda(1)\simeq\Lambda_Y(1)$,
with $p^*$ an isomorphism onto it, and $R^1\pi_*\Lambda(1)\simeq\Lambda_Y$
is free of rank one on the Kummer class $\kappa(t)$.
- **(c)** *Vanishing above degree one.* $R^m\pi_*\Lambda(1)=0$ for $m\ge2$.

All three are compatible with base change on $Y$, as is $\kappa(t)$.
Equivalently, (a)–(c) are the corresponding statements for
$\Aaf^1$ and $\mathbf G_m$ over a geometric point.
Compare Milne, *Lectures on Étale Cohomology*, §16; SGA 4, IX.

## Proof

*Reduction to a geometric fibre.* $p$ and $\pi$ are smooth, so by
smooth base change ([sk-thm-smooth-base-change]; §[sec-smooth-base-change]
does not use the present section, so the reference is not circular) the
formation of $Rp_*\Lambda$ and $R\pi_*\Lambda(1)$ commutes with arbitrary
base change on $Y$. All three clauses may therefore be checked on stalks,
i.e. for $Y=\Spec k$ with $k$ separably closed, and after enlarging $k$ we
may take it algebraically closed. Then $\Aaf^1_k$ and $\mathbf G_{m,k}$ are
affine curves in the sense of [sk-def-curve]. The twist $\Lambda(1)$ is
pulled back from $Y$, so by the projection formula the twisted and untwisted
statements determine one another.

*Coefficients.* With $N$ as in [sk-def-purity-conv], $\ell^NA=0$ and
$A\cong(\Z/\ell^N\Z)^{ef}$ is free over $\Z/\ell^N\Z$, where $e=e(E/\mathbf Q_\ell)$
and $f$ is the residue degree. Since $\Lambda(1)=\mu_{\ell^N}\otimes_{\Z/\ell^N\Z}A$
and $-\otimes_{\Z/\ell^N\Z}A$ is exact, it suffices to compute with
$\mu_{\ell^N}$ and tensor up.

*Clause (c).* $\ell$ is prime to $\operatorname{char}k$ and both curves
are affine, so [sk-prop-cd] gives $H^q(-,\mu_{\ell^N})=0$ for $q\ge2$.
This is (c), and it reduces (a) and (b) to degrees $0$ and $1$.

*Degrees $0$ and $1$.* By [sk-prop-kummer-exact] with $n=\ell^N$
invertible, the Kummer sequence gives

$$
0\to H^0(C,\mu_{\ell^N})\to\Gamma(C,\mathbb G_m)
\xrightarrow{\ \ell^N\ }\Gamma(C,\mathbb G_m)\to H^1(C,\mu_{\ell^N})\to\Pic(C).
$$

For $C=\Aaf^1_k$: $\Gamma(C,\mathbb G_m)=k^\times$ and $\Pic(C)=0$, since
$k[T]$ is a principal ideal domain. As $k$ is algebraically closed,
$k^\times$ is divisible, so the $\ell^N$-power map is surjective and
$H^1(\Aaf^1_k,\mu_{\ell^N})=0$. With (c) this gives $R^mp_*\Lambda=0$ for
$m>0$, and $R^0p_*\Lambda=\Lambda_Y$ because the geometric fibres $\Aaf^1_k$ are
connected; this is (a).
For $C=\mathbf G_{m,k}$: $\Gamma(C,\mathbb G_m)=k^\times\times t^{\Z}$, the
units of $k[T,T^{-1}]$, and $\Pic(C)=0$. Divisibility of $k^\times$ leaves
$\Gamma(C,\mathbb G_m)/\ell^N\cong t^{\Z}/\ell^Nt^{\Z}\cong\Z/\ell^N\Z$, so
$H^1(\mathbf G_{m,k},\mu_{\ell^N})$ is free of rank one on the class of $t$,
which is $\kappa(t)$ by [sk-def-purity-conv]; and
$H^0(\mathbf G_{m,k},\mu_{\ell^N})=\mu_{\ell^N}(k)$ is free of rank one, with
restriction from $\Aaf^1_k$ an isomorphism onto it. Tensoring with $A$
gives (b).

Uses: [sk-def-curve], [sk-def-purity-conv], [sk-prop-cd], [sk-prop-kummer-exact], [sk-thm-smooth-base-change]
