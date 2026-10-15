+++
id = "lem-weil-pbc-fibre-ring-noetherian"
kind = "lemma"
title = "Fibre rings of a Noetherian algebra are Noetherian"
lean = ["Ideal.isNoetherianRing_fiber"]
+++
Let $A\to B$ be a homomorphism of commutative rings with $B$ Noetherian `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)), and let $\mathfrak p\subset A$ be a prime ideal with residue field $\kappa(\mathfrak p)=A_{\mathfrak p}/\mathfrak pA_{\mathfrak p}$ `Localization.AtPrime, Ideal.ResidueField, Ideal.Fiber` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Localization/AtPrime/Basic.lean)). Then the fibre ring $B\otimes_A\kappa(\mathfrak p)$ is Noetherian.
