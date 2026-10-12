+++
id = "lem-weil-pbc-integral-extension-dimension"
kind = "lemma"
title = "An integral ring map does not raise Krull dimension"
lean = ["RingHom.integralExtensionDimension"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 00OJ (lemma-integral-dim-up, line 27348) and its proof (Lemmas Tag 00GT integral-no-inclusion and 00OI going-up-maximal-on-top); used in the proof of Lemma Tag 032D ('Since $\\dim(R)=\\dim(R_0)$ this implies that $R_0\\to R$ is injective')"
+++
Let $A\to B$ be a ring map of commutative rings such that $B$ is integral over $A$ `integralClosure, IsIntegral, IsIntegrallyClosedIn` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/Algebra/Basic.lean)) (every element of $B$ is a root of a monic polynomial with coefficients in the image of $A$). Then $\dim B\le\dim A$ (Krull dimensions `ringKrullDim` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/KrullDimension/Basic.lean)): suprema of lengths of chains of prime ideals), and every maximal ideal of $B$ lies over a maximal ideal of $A$.
