+++
id = "lem-pc-projective-space-serre-pairing"
kind = "lemma"
title = "Top cohomology of twists on projective space as a dual"
lean = ["AlgebraicGeometry.ProjectiveSpace.cechComplexFunctor_map_twistMulHom_monomialCechToCechFun", "AlgebraicGeometry.ProjectiveSpace.twistMulPairing", "AlgebraicGeometry.ProjectiveSpace.twistHTopLinearEquivDual", "AlgebraicGeometry.ProjectiveSpace.twistHTopLinearEquivDual_apply", "AlgebraicGeometry.ProjectiveSpace.twistSerrePairing", "AlgebraicGeometry.ProjectiveSpace.isPerfPair_twistSerrePairing", "AlgebraicGeometry.ProjectiveSpace.twistSerrePairing_basis", "AlgebraicGeometry.ProjectiveSpace.monomialCechPairing", "AlgebraicGeometry.ProjectiveSpace.monomialCechComplexHomologyTopLinearEquivDual_apply", "AlgebraicGeometry.ProjectiveSpace.twistMulHom"]
order = 625
uses = ["def-pc-projective-space-twist", "lem-pc-cech-computes", "lem-pc-projective-space-twist-cohomology", "lem-pc-twist-tensor", "pqf-def-cohomology"]
+++
Let $A$ be a commutative ring, $n\ge1$, $P=\mathbf P^n_A$ with the
standard opens $U_i=D_+(x_i)$ and twists $\mathcal O_P(d)$ of
[def-pc-projective-space-twist], and let $V=A^{n+1}$ be the free
module with basis $x_0,\ldots,x_n$. For $a,b\in\mathbf Z$, multiplying
a Cech cochain $(c_J)_J$ of $\mathcal O_P(b)$ on the standard cover by
a global section $s$ of $\mathcal O_P(a)$, componentwise
$c_J\mapsto s|_{U_J}c_J$ through the isomorphism
$\mathcal O_P(a)\otimes\mathcal O_P(b)\cong\mathcal O_P(a+b)$ of
[lem-pc-twist-tensor], induces an $A$-bilinear pairing

$$
H^0(P,\mathcal O_P(a))\times H^n(P,\mathcal O_P(b))\longrightarrow
H^n(P,\mathcal O_P(a+b)).
$$

For $d\ge0$ the pairing

$$
H^0(P,\mathcal O_P(d))\times H^n(P,\mathcal O_P(-d-n-1))\longrightarrow
H^n(P,\mathcal O_P(-n-1))=A\cdot\bigl[x_0^{-1}\cdots x_n^{-1}\bigr]\cong A
$$

is perfect: in the monomial bases of
[lem-pc-projective-space-twist-cohomology], $x^f$ pairs to $1$ with
$x^{-f-\mathbf 1}$, where $\mathbf 1=(1,\ldots,1)$, and to $0$ with every
other basis element. Consequently, for every $m\le-n-1$,

$$
H^n(P,\mathcal O_P(m))\cong
\operatorname{Hom}_A\bigl(S^{-m-n-1}_A(V),A\bigr)=S^{-m-n-1}(V)^{\vee}
$$

canonically, while $H^n(P,\mathcal O_P(m))=0$ for $m\ge-n$. For $A=k$ a
field this is the description
$H^n(\mathbf P^n_k,\mathcal O(m))=S^{-m-n-1}(k^{n+1})^{\vee}$.
