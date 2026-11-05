+++
id = "proposition-weights-under-usual-operations"
kind = "proposition"
title = "Weights under the usual operations"
order = 1070
lean = ["AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.of_mono", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.of_epi", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.of_mono", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.of_epi", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.of_shortExact", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.tensorObj", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.dual", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.upperStar", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.upperStar", "AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.upperStar", "AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.shift", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.constantTwist", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.constantTwist", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.tateTwist", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.tateTwist"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-sp-unique-adjoint", "definition-weights"]
+++
Subobjects and quotients of a pure Weil sheaf of weight $w$ are pure of
weight $w$.  Subquotients and extensions of mixed sheaves are mixed,
and an extension of two sheaves with a common upper bound has the same
bound.  Tensor products of pure sheaves of weights $a$ and $b$ are pure
of weight $a+b$, and the dual of a pure lisse sheaf of weight $a$ is
pure of weight $-a$. A tensor product of mixed sheaves of weights at
most $a$ and at most $b$ is mixed of weights at most $a+b$. The dual of
a mixed lisse sheaf is mixed, of the negated weights; when its filtration
has lisse graded pieces, their duals are the graded pieces of the
annihilator filtration of the dual.  Inverse image preserves purity,
mixedness and their upper bounds.  If a complex $K$ has weights at most
$w$, then $K[r]$ has weights at most $w+r$.

For $b\in\overline{\mathbf Q}_\ell^\times$, let $\mathcal B_b$ be the geometrically constant
rank-one Weil sheaf on which a degree-one Frobenius acts by $b$.
Tensoring by $\mathcal B_b$ adds
$\lambda_\iota(b)=2\log_q|\iota(b)|$ to every weight.  The Tate sheaf
$\overline{\mathbf Q}_\ell(1)$ has geometric Frobenius $q^{-1}$, so twisting by $(r)$
subtracts $2r$ from every weight.
