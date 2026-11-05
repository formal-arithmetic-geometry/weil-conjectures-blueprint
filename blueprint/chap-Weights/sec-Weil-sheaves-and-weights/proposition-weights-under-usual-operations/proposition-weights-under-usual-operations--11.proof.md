+++
kind = "proof"
of = "proposition-weights-under-usual-operations--11"
order = 1070012
uses = ["proposition-weights-under-usual-operations--10", "proposition-weights-under-usual-operations--2"]
+++
Choose an upper bound $w$ for a mixed filtration of $\mathcal F$.
The functor $f^*$ is exact and preserves punctual purity by
[proposition-weights-under-usual-operations--10]. Apply
`AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.map`: the image
filtration has pure quotients of the same weights, using the
isomorphisms between pullbacks of cokernels and cokernels of pullbacks.
The same $w$ witnesses mixedness of $f^*\mathcal F$.
