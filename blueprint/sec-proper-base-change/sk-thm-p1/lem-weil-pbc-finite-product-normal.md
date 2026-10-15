+++
id = "lem-weil-pbc-finite-product-normal"
kind = "lemma"
title = "A finite product of normal rings is normal"
lean = ["Pi.isNormalRing_of_finite"]
+++
Let $R_1,\dots,R_n$ be commutative normal rings `IsIntegrallyClosed, IsDomain, Localization.AtPrime` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/IntegrallyClosed.lean)). Then their finite product $R=\prod_iR_i$ is a normal ring: for every prime ideal $\mathfrak p\subset R$, the localization $R_{\mathfrak p}$ is a normal domain.
