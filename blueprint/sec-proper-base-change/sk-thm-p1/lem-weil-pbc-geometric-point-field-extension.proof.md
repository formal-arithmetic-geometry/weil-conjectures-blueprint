+++
kind = "proof"
of = "lem-weil-pbc-geometric-point-field-extension"
+++
For an etale neighbourhood U, precomposition gives a natural map on pointed lifts. Its injectivity follows by cancellation of the faithfully flat, surjective field-spectrum map. For surjectivity base change U along s, lift the identity of Spec k through the underlying point of the given Spec l lift, using etale lifting over a separably closed field. This section of the etale projection is an open immersion. The Spec l lift factors through its open image, since it has the same unique underlying point. Composing the factorization with the projection proves that it is a, so the section gives the required pointed lift over k. Each component of the natural transformation is thus bijective; the associated isomorphism of points induces an isomorphism on sheaf fibres. This proof is written and checked in Lean from Mathlib and the source library.
