+++
id = "lem-pc-projective-space-twist-cohomology"
kind = "lemma"
title = "Monomial cohomology of twists on projective space"
order = 648
uses = ["def-pc-projective-space-twist", "pqf-lem-affine-vanishing", "lem-pc-cech-computes", "lem-pc-twist-cocycle", "pqf-def-cohomology"]
lean = ["AlgebraicGeometry.ProjectiveSpace.nonempty_H_twist_linearEquiv_monomialCechComplex_homology", "AlgebraicGeometry.ProjectiveSpace.nonempty_H_zero_twist_linearEquiv", "AlgebraicGeometry.ProjectiveSpace.subsingleton_H_zero_twist_of_neg", "AlgebraicGeometry.ProjectiveSpace.subsingleton_H_twist_of_ne_of_commRing", "AlgebraicGeometry.ProjectiveSpace.nonempty_H_twist_top_linearEquiv_finsupp", "AlgebraicGeometry.ProjectiveSpace.twistHTopBasis", "AlgebraicGeometry.ProjectiveSpace.subsingleton_H_twist_top_of_commRing", "AlgebraicGeometry.ProjectiveSpace.nonempty_H_twist_top_linearEquiv_self", "AlgebraicGeometry.ProjectiveSpace.subsingleton_H_twist_of_pos_of_commRing", "AlgebraicGeometry.ProjectiveSpace.finite_H_twist", "AlgebraicGeometry.ProjectiveSpace.nonempty_H_zero_twist_linearEquiv_of_card_eq_one"]
+++
Let $A$ be a commutative ring, $n\ge1$, and $d\in\mathbf Z$.
For the twisting modules
on $P=\mathbf P^n_A$, one has

$$
H^q(P,\mathcal O_P(d))\cong
\begin{cases}
\displaystyle\bigoplus_{\substack{e_i\ge0\\\sum e_i=d}} A\,x^e,&q=0,\\
\displaystyle\bigoplus_{\substack{e_i<0\\\sum e_i=d}} A\,x^e,&q=n,\\
0,&q\notin\{0,n\}.
\end{cases}
$$

Here $x^e=\prod_ix_i^{e_i}$, and the class of $x^e$ in degree $n$ is
that of the Cech $n$-cochain $x^e$ on $U_0\cap\cdots\cap U_n$.
In particular, for $n\ge1$, all these modules are finite free, and:

1. **(i)** $H^0(P,\mathcal O_P(d))$ is the degree-$d$ part
$A[x_0,\ldots,x_n]_d=S^d_A(V)$, the $d$-th symmetric power of the
free module $V=A^{n+1}$ with basis $x_0,\ldots,x_n$; it is zero
for $d<0$;
1. **(ii)** $H^n(P,\mathcal O_P(d))=0$ for $d\ge-n$, and
$H^n(P,\mathcal O_P(-n-1))$ is free of rank one with basis the class
of $x_0^{-1}x_1^{-1}\cdots x_n^{-1}$;
1. **(iii)** the groups in positive degree vanish for $d\ge0$;
in particular $H^0(P,\mathcal O_P)=A$ and
$H^q(P,\mathcal O_P)=0$ for $q\neq0$.

For $n=0$, every twist is free of rank one on
$\mathbf P^0_A=\operatorname{Spec}(A)$ and has no higher cohomology.
