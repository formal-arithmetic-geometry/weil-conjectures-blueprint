+++
kind = "proof"
of = "proposition-exceptional-inverse-image-smooth-morphism--8"
order = 561015
uses = ["proposition-composition-base-change-rf-shriek"]
+++
Apply the adjunction $Rf'_!\dashv f'^!$ to both sides. The proof of
`CategoryTheory.Adjunction.projectionTensorMap_mateEquiv` compares these
transposes after precomposing with the projection and compact-support base
change isomorphisms. Counit naturality and the defining counit identity for
the mate reduce the equality to compatibility of the projection map with
base change. In the étale setting that compatibility is
`AlgebraicGeometry.Etale.projectionMap_rightDerivedLowerShriekBaseChangeMap`.

The same specialization of the general identity is used in
`AlgebraicGeometry.Etale.isIso_map_leftDerivedUpperStar_map_rightDerivedUpperShriekTensorMap`,
which transports invertibility of tensor maps across base change in the
proof of the étale case. The identity therefore precedes the smooth tensor
formula and does not require either base change map to be an isomorphism.
