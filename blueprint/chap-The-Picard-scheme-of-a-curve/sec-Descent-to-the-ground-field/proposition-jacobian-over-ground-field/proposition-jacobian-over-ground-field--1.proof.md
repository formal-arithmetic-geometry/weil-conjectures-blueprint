+++
kind = "proof"
of = "proposition-jacobian-over-ground-field--1"
order = 1562007
uses = ["theorem-picard-scheme-jacobian-over-separably", "corollary-serre-duality-field-extension", "lemma-symmetric-ample-sheaf", "proposition-jacobian-over-ground-field--2"]
+++
A smooth geometrically connected curve is geometrically integral. Over
$k_s$, Theorem [theorem-picard-scheme-jacobian-over-separably] gives the
Jacobian $J_s$ of $C_{0,k_s}$, of dimension $g$ by
[corollary-serre-duality-field-extension]. By
[proposition-jacobian-over-ground-field--2], it represents the restriction
of $F$ to $k_s$-schemes.

The representation supplies the canonical descent datum on $J_s$.
Spreading out gives a finite separable subextension $K/k$ of $k_s/k$
and a $K$-scheme $J_K$ whose base change is $J_s$ and which represents
the restriction of $F$ to $K$-schemes. This is
`AlgebraicGeometry.exists_intermediateField_representableBy`:
the descent of the representation uses the sheaf condition for flat,
surjective, quasi-compact covers, including the base changes of
$\operatorname{Spec}k_s\to\operatorname{Spec}K$.

Projectivity of the Jacobian, as in [lemma-symmetric-ample-sheaf], gives
an immersion of $J_s$ into projective space. Descend the immersion to
$J_K$; it is closed because properness also descends. Every finite set
of points of $J_K$ therefore lies in an affine open. Effective descent
along the finite faithfully flat map $\operatorname{Spec}K\to
\operatorname{Spec}k$ gives a scheme $J_0$ and a projection
$J_K\to J_0$ invariant under the canonical descent datum.

The sheaf descent theorem
`AlgebraicGeometry.nonempty_representableBy_picardFunctorDegree_of_isPullback`
then gives a representation $r$ of $F$ by $J_0$. Properness, smoothness
of relative dimension $g$, and geometric integrality descend from
$J_s$. Finally the tensor-product law on $F$ gives the commutative
group scheme structure on $J_0$, by
`AlgebraicGeometry.exists_commGrpObj_isPicardZeroMul`.
