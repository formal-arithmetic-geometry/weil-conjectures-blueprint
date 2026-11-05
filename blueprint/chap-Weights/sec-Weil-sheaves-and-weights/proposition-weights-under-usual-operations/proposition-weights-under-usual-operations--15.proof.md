+++
kind = "proof"
of = "proposition-weights-under-usual-operations--15"
order = 1070016
uses = ["proposition-weights-under-usual-operations--2"]
+++
At a closed point $x$ of degree $m$, the stalk of the twist is the stalk
of $\mathcal F$ with Frobenius multiplied by $b^m$, by
`AlgebraicGeometry.WeilSheaf.nonempty_equiv_stalk_constantTwist`.
The equality $|\iota(b)|=q^{c/2}$ gives the added weight $c$ through
`FrobeniusModule.IsPureOfWeight.rescale`. For mixedness, apply the exact
constant-twist functor to a mixed filtration, using
`AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.map_add`.
The functor's cokernel isomorphisms identify each graded piece with a
twist of an original pure piece, whose weight increases by $c$.
