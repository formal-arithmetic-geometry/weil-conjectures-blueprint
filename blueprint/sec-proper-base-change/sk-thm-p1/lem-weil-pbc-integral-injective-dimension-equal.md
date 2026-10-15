+++
id = "lem-weil-pbc-integral-injective-dimension-equal"
kind = "lemma"
title = "An injective integral extension preserves Krull dimension"
lean = ["ringKrullDim_eq_of_isIntegral"]
+++
Let $R\hookrightarrow S$ be an injective homomorphism of commutative rings such that every element of $S$ is integral over $R$ `integralClosure, IsIntegral, IsIntegrallyClosedIn` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/Algebra/Basic.lean)). Then the Krull dimensions `ringKrullDim` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/KrullDimension/Basic.lean)) of $R$ and $S$ are equal: $\dim R=\dim S$.
