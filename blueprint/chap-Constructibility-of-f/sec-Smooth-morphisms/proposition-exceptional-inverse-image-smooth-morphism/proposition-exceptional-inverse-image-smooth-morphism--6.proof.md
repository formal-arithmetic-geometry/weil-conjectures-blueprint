+++
kind = "proof"
of = "proposition-exceptional-inverse-image-smooth-morphism--6"
order = 561013
uses = ["lemma-affine-space-etale-localization", "proposition-adjunction-projective-line", "proposition-composition-base-change-rf-shriek"]
+++
The étale case follows from base change compatibility of the unit of the
étale adjunction (`AlgebraicGeometry.Etale.etaleBaseChange`). The affine-line
case comes from the projective-line adjunction, and iteration gives the
affine-space case of [lemma-affine-space-etale-localization].

On an affine chart, paste the squares for the étale map, the affine-space
projection and the open immersion into $S$. Compatibility of exceptional
base change with composition shows that the map for the chart is an
isomorphism. Pull these charts back to $X'$ and use conservativity of the
open cover to conclude globally. Quasi-separatedness makes the affine-open
inclusions quasi-compact, as required for the pasting argument. If the
exponent of $A$ is only assumed invertible on $X$, first factor through its
invertibility locus in $S$ and then compose with that open immersion.
These steps are expressed by
`AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekBaseChangeMap_of_etale_of_affineLine`.
