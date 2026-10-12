+++
id = "lem-weil-pbc-integral-injective-dimension-equal"
kind = "lemma"
title = "An injective integral extension preserves Krull dimension"
lean = ["ringKrullDim_eq_of_isIntegral"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 00OK (lemma-integral-sub-dim-equal, lines 27360-27373); proof cites 00GU, 00GQ, 00OI, 00OJ"
+++
Let $R\hookrightarrow S$ be an injective homomorphism of commutative rings such that every element of $S$ is integral over $R$ `integralClosure, IsIntegral, IsIntegrallyClosedIn` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/Algebra/Basic.lean)). Then the Krull dimensions `ringKrullDim` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/KrullDimension/Basic.lean)) of $R$ and $S$ are equal: $\dim R=\dim S$.
