+++
kind = "proof"
of = "proposition-exceptional-inverse-image-smooth-morphism--4"
order = 561011
uses = ["proposition-exceptional-inverse-image-smooth-morphism--1"]
+++
Factor $f$ through the open subscheme of $S$ where the exponent of $A$ is
invertible. Smoothness gives affine charts there. Apply
[proposition-exceptional-inverse-image-smooth-morphism--1] and descend the
rank-one shape along the open cover of $X$, using
`AlgebraicGeometry.Etale.IsShiftedRankOneLocalSystem.of_jointlySurjective`.
Restriction of $\omega_f$ to a chart agrees with the dualizing complex of
the composite with its open immersion. Composing back with the open
immersion into $S$ preserves this shape. This gives the first part of
`AlgebraicGeometry.Etale.exists_dualizingComplex_iso_and_tensor`.

A locally constant rank-one sheaf has its dual as tensor inverse. Shifting
preserves invertibility, as expressed by
`AlgebraicGeometry.Etale.isInvertible_shift_singleFunctor_obj_of_isLocallyConstantSheaf`.
Transport this invertibility across $\omega_f\simeq L[2d]$ to obtain
`AlgebraicGeometry.Etale.isInvertible_dualizingComplex`.
