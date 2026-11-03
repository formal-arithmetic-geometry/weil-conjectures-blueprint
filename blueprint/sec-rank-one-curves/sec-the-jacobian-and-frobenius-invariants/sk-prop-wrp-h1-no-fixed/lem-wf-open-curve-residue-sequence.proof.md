+++
kind  = "proof"
of    = "lem-wf-open-curve-residue-sequence"
+++
The geometric boundary $D$ is a finite disjoint union of closed points of
the smooth curve $C$. Each point is an effective Cartier divisor by
[lem-sc-point-cartier]; hence $i$ is a regular closed immersion of
pure codimension one. For every $n$, purity in
[thm-pur-regular-immersion-purity] gives

$$
Ri^!A_{n,C}\xrightarrow{\sim}A_{n,D}(-1)[-2].
\tag{5.2}
$$

The finite-reduction compatibility in
[prop-pur-regular-immersion-purity-compatibilities] makes (5.2)
compatible with $n$. Apply the support-localization triangle
[lem-pur-support-localization-triangle] at level $n$:

$$
R\Gamma(D,Ri^!A_{n,C})\longrightarrow R\Gamma(C,A_n)
\longrightarrow R\Gamma(U,A_n)\xrightarrow{+1}.
\tag{5.3}
$$

The shift in (5.2) gives $H_D^1(C,A_n)=0$ and
$H_D^2(C,A_n)=H^0(D,A_n(-1))$. The degree-one part of the long exact
sequence of (5.3) is (5.1). Naturality of purity and localization gives
Frobenius equivariance and compatibility under reduction.

Frobenius permutes the finite set $D(\overline{\mathbf F}_q)$. Choose
$m$ divisible by all cycle lengths. Then $\Phi_Q=\Phi_q^m$ fixes every
point. By the normalization in
[def-weil-frobenius-coefficient-twists], it acts on
$A_n(-1)$ by $Q\bmod\ell^n$. Hence it acts on the inverse limit as
the scalar $Q$ on the finite free $\mathbf Z_\ell$-module
$\mathbf Z_\ell(-1)^{D(\overline{\mathbf F}_q)}$. Since $Q-1\ne0$ and
this module is torsion-free, its fixed element is zero.
