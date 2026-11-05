+++
kind = "proof"
of = "proposition-compatibility-purity-base-change--1"
order = 797003
uses = ["lemma-naturality-under-base-change-etale", "proposition-exceptional-inverse-image-smooth-morphism"]
+++
The blueprint argument compares the orientations using
[lemma-naturality-under-base-change-etale](1), and compares the transposes
of the tensor maps under $Rf'_!\dashv f'^!$, as in
[proposition-exceptional-inverse-image-smooth-morphism](3).
This argument for the chosen finite-coefficient purity maps is not carried
out in the supplied mainline. Its finite-coefficient input is instead the
invertibility of exceptional base change,
`AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekBaseChangeMap_of_smoothOfRelativeDimension`;
that statement does not identify the chosen orientations.
