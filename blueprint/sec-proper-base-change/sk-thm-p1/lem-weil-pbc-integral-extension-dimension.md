+++
id = "lem-weil-pbc-integral-extension-dimension"
kind = "lemma"
title = "An integral ring map does not raise Krull dimension"
lean = ["RingHom.integralExtensionDimension"]
+++
Let $A\to B$ be a ring map of commutative rings such that $B$ is integral over $A$ `integralClosure, IsIntegral, IsIntegrallyClosedIn` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/Algebra/Basic.lean)) (every element of $B$ is a root of a monic polynomial with coefficients in the image of $A$). Then $\dim B\le\dim A$ (Krull dimensions `ringKrullDim` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/KrullDimension/Basic.lean)): suprema of lengths of chains of prime ideals), and every maximal ideal of $B$ lies over a maximal ideal of $A$.
