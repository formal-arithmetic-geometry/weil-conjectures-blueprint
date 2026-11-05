+++
kind = "proof"
of = "theorem-picard-scheme-jacobian-over-separably--3"
order = 1549008
uses = ["theorem-picard-scheme-jacobian-over-separably--1", "theorem-picard-scheme-jacobian-over-separably--2", "lemma-rigidification-along-section"]
+++
Take the degree-zero representing scheme in
[theorem-picard-scheme-jacobian-over-separably--1]. The degree-zero
Picard presheaf is a presheaf of commutative groups under tensor
product. Sheafify this group law and transfer it to the representing
scheme. This is `AlgebraicGeometry.exists_commGrpObj_isPicardZeroMul`.
The geometric properties follow from
[theorem-picard-scheme-jacobian-over-separably--2].

Choose a rational point of $C$ and apply the split Picard comparison
of [lemma-rigidification-along-section] to $\operatorname{Spec}k$.
Since $\operatorname{Pic}(k)=0$, this identifies
$\operatorname{Pic}_{C/k}(k)$ with $\operatorname{Pic}(C)$.
Compatibility with degree restricts the comparison to a bijection
$\operatorname{Pic}^0(C)\simeq\operatorname{Pic}^0_{C/k}(k)$, proved
in `AlgebraicGeometry.exists_picardZero_equiv_picardFunctorDegree_zero`.
The representation respects tensor product, so
`AlgebraicGeometry.exists_mulEquiv_of_isPicardZeroMul` turns this
bijection into the asserted group isomorphism.

The degree-zero component is open and closed and geometrically
connected, and contains the unit. Thus it is the identity component
of the Picard scheme; Lean packages the construction as a
representation of the degree-zero functor in
`AlgebraicGeometry.exists_jacobian`.
