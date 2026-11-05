+++
kind = "proof"
of = "lemma-kunneth-one-identity-factor--1"
order = 717002
uses = ["lemma-base-change-along-product-projection"]
+++
Write $p_Y:Y\times_k T\to Y$ and $p_T:Y\times_k T\to T$ for the
projections, and $q_X:X\times_k T\to X$ and $q_T:X\times_k T\to T$ for
those on the source. The square formed by $h$, $q_X$, $p_Y$ and $f$ is
cartesian, as expressed by
`AlgebraicGeometry.Etale.isPullback_mapOverBaseRight_fst`.

Apply the tensor base change theorem
`AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap` to $Q$ and $M$ and to
this square together with the product square defining $Y\times_k T$.
Its constant tensor-factor case is the base change statement of
[lemma-base-change-along-product-projection]. It gives an isomorphism

$$
p_T^*Q\otimes_A^{\mathbf L}p_Y^*Rf_*M
\longrightarrow
Rh_*\bigl(h^*p_T^*Q\otimes_A^{\mathbf L}q_X^*M\bigr).
$$

Use the symmetry of the derived tensor product on the source. On the
target use $h^*p_T^*Q\simeq q_T^*Q$ and the symmetry once more. These
isomorphisms turn the displayed map into
`AlgebraicGeometry.Etale.externalProductRightDerivedLowerStarMap`, with
source $Rf_*M\boxtimes Q$ and target $Rh_*(M\boxtimes Q)$.
Thus `AlgebraicGeometry.Etale.isIso_externalProductRightDerivedLowerStarMap`
shows that this comparison is invertible, and packaging it as an
isomorphism proves the assertion. The tensor base change theorem applies
to arbitrary complexes, so this construction does not use the assumed
constructibility or finite Tor amplitude of $M$ and $Q$.
