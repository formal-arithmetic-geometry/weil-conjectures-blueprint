+++
kind = "proof"
of = "lemma-class-diagonal-projective-line--1"
order = 550002
uses = ["lemma-cycle-class-cartier-divisor", "lemma-cohomology-projective-line-trace"]
+++
An endomorphism of $\Lambda_P$ is determined by its pullback along the
section at infinity $\iota:Z\hookrightarrow P$. Indeed, on a geometric
fibre the Tate twist is trivial, and the projective-line decomposition
shows that every endomorphism of the constant complex comes from the
base point. Its pullbacks to any point and to infinity therefore agree.
Equality can then be checked on geometric stalks. This is
`AlgebraicGeometry.Etale.eq_of_leftDerivedUpperStar_lineInfinityι_map_eq`.

Pull the first composite back along $\iota$. By compatibility of the
trace with base change, it becomes the trace on $\mathbf P^1_Z$ of the
restriction of $\gamma$. The inverse image of the diagonal is the
section at infinity of $\mathbf P^1_Z$. Near $(\infty,\infty)$ the
diagonal has equation $z-t$, which restricts to the coordinate cutting
out that section. Restriction of the supported Kummer boundary thus
gives the boundary class of infinity. After forgetting supports,
`AlgebraicGeometry.Etale.cartierKummerCycleClass_diagonal_baseChange`
identifies this class with $h$. The trace sends its adjoint to $1$,
since it is the projection onto the $h$-summand of the decomposition.
The first composite is therefore the identity after pullback along
$\iota$, hence is the identity on $P$.

Finally, the exchange of factors fixes the diagonal. Compatibility of
the supported Cartier class with pullback, followed by forgetting
supports, gives $\sigma^*\gamma=\gamma$
(`AlgebraicGeometry.Etale.cartierKummerCycleClass_diagonalSwap`).
Substitution reduces the second equality to the first.
