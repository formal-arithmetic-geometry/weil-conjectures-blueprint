+++
kind = "proof"
of = "proposition-exceptional-inverse-image-smooth-morphism--7"
order = 561014
uses = ["proposition-exceptional-inverse-image-smooth-morphism--6"]
+++
Evaluate the functor isomorphism of
[proposition-exceptional-inverse-image-smooth-morphism--6] at the tensor
unit, and use the unit comparison for inverse image.

For the diagonal square, Lean obtains this functor isomorphism from
`AlgebraicGeometry.Etale.nonempty_iso_leftDerivedUpperStar_comp_rightDerivedUpperShriek`.
It first identifies $\omega_{p_1}$ with $p_1^!f^*A_S$ using
`AlgebraicGeometry.Etale.nonempty_iso_leftDerivedUpperStar_unit`, then uses
the inverse of the base change isomorphism at $A_S$. This is
`AlgebraicGeometry.Etale.nonempty_iso_dualizingComplex_pullbackFst`.
