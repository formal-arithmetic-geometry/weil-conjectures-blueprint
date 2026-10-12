+++
kind = "proof"
of = "lem-weil-pbc-closed-immersion-localized-section-map"
+++
The basic opens have localized section rings. The universal property identifies localization of the A-linear section map with the ring map on the localized rings; this identification and its preservation of surjectivity are proved by the private helper in the Lean module. (`AlgebraicGeometry.Scheme.isOpenImmersion_SpecMap_localizationAway` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/OpenImmersion.lean))).

The affine criterion turns surjectivity of the map on basic-open sections into a closed immersion of the restriction, using morphismRestrict_appTop and the isomorphism on restricted sections. (`AlgebraicGeometry.Scheme.Hom.app_surjective, AlgebraicGeometry.IsAffineOpen.preimage, AlgebraicGeometry.HasAffineProperty.iff_of_iSup_eq_top, AlgebraicGeometry.IsClosedImmersion.hasAffineProperty` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Affine.lean), [Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Basic.lean), [Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/ClosedImmersion.lean))).
