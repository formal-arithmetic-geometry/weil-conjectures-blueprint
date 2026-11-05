+++
kind = "proof"
of = "proposition-weights-under-usual-operations--12"
order = 1070013
uses = ["proposition-weights-under-usual-operations--10", "proposition-weights-under-usual-operations--2"]
+++
Apply `AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.map` to the
exact functor $j^*$. Its preservation of punctual purity is
[proposition-weights-under-usual-operations--10]; the cokernel
isomorphisms identify the graded pieces with pullbacks of the original
pure pieces. The named Lean theorem has an immersion hypothesis,
although this proof works for any morphism of $k_0$-schemes locally of
finite type, as the proof of [proposition-weights-under-usual-operations--11]
also shows. There is no declaration named
`AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.upperStar`
in the inspected source.
