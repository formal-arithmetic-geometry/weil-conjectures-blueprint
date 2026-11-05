+++
kind = "proof"
of = "lemma-naturality-pasting-comparison"
order = 325
uses = ["definition-pro-etale-base-change-map", "proposition-topos-functoriality", "lemma-identity-pasting", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "lemma-naturality-pasting-comparison--1", "lemma-naturality-pasting-comparison--3"]
+++
Every assertion holds because the base change map is
assembled from units, counits and composition isomorphisms for inverse
images, and each of the operations in the lemma respects these ingredients. Naturality in $K$ is immediate, since the counit
$\varepsilon_f$ is a natural transformation.

By definition, the base change map is the adjoint transpose of a counit preceded
by the composition isomorphism for inverse images. Since the counit for a
composite adjunction is the composite of the two counits, taking
adjoint transposes proves pasting, in either order of composing the
two directions of a rectangle. Similarly, the assertion about identity squares
follows from the triangle identities, as in Lemma [lemma-identity-pasting].
Finally, the comparisons of sites of Theorem [theorem-comparison-direct-images]
identify the composition maps for inverse images and the units and counits
(Lemma [lemma-comparison-direct-images-compatibilities]),
and hence also the base change maps constructed from them.
