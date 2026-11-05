+++
kind = "proof"
of = "corollary-determinant-weights--1"
uses = ["theorem-rank-one-sheaves-have-finite", "corollary-rank-one-weights"]
+++
Let $L$ be a one-dimensional $\overline{\mathbf Q}_\ell$-space on which
$g$ acts by multiplication by $\det\rho(g)$. The determinant is a
polynomial in the matrix coefficients, so this representation is lisse
(`AlgebraicGeometry.WeilGroup.IsLisse.ofCharacter_detCharacter`). Its
rank is one even when $V=0$.

By [theorem-rank-one-sheaves-have-finite], the geometric image on $L$ is
finite. The map sending a scalar to its multiplication operator on $L$
is injective, as one sees by evaluating at $1$. Hence the determinant
character has finite image on $\pi_1(U)$.

By [corollary-rank-one-weights], $L$ is pure of weight
$\lambda_\iota(\det\rho(s))$. Its local eigenvalue at $x$ is
$\det\rho(\operatorname{Frob}_x)$, and the determinant of its action at
$s$ is $\det\rho(s)$
(`AlgebraicGeometry.WeilGroup.det_mem_localEigenvalues_ofCharacter` and
`AlgebraicGeometry.WeilGroup.det_ofCharacter_detCharacter`). This gives
the displayed identity after cancelling $r$ when $r>0$. When $r=0$,
$V=0$ and its determinant character is $1$, whose weight is zero.
