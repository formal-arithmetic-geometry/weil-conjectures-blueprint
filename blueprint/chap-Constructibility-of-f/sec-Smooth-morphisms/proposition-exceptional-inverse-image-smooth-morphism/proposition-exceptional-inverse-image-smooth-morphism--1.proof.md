+++
kind = "proof"
of = "proposition-exceptional-inverse-image-smooth-morphism--1"
order = 561010
uses = ["lemma-affine-space-etale-localization", "proposition-composition-base-change-rf-shriek", "proposition-exceptional-inverse-image-smooth-morphism--8"]
+++
The two assumptions are the étale and affine-space cases supplied by
[lemma-affine-space-etale-localization]. In Lean they are expressed by
`AlgebraicGeometry.Etale.EtaleSmoothDuality` and
`AlgebraicGeometry.Etale.AffineSpaceSmoothDuality`.

First compose $e$ with $p_d$. Since $\omega_e\simeq A_U$, the composition
isomorphism identifies $\omega_{p_de}$ with $e^*\omega_{p_d}$, which has the
required rank-one shape. The canonical tensor maps compose, using
`AlgebraicGeometry.Etale.isIso_dualizingComplexTensorMap_comp_of_forall`;
the rank-one shape makes $\omega_{p_d}$ tensor-invertible. Compose next with
the open immersion $v$. Its dualizing complex is the tensor unit, so the
shape is unchanged and the tensor maps remain isomorphisms. These are the
two compositions in `AlgebraicGeometry.Etale.satisfiesSmoothDuality_chart`.
The compatibility in [proposition-exceptional-inverse-image-smooth-morphism--8]
is used in the proof of the étale case.
