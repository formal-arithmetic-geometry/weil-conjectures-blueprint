+++
id = "lem-weil-pbc-fibre-ring-noetherian"
kind = "lemma"
title = "Fibre rings of a Noetherian algebra are Noetherian"
lean = ["Ideal.isNoetherianRing_fiber"]
source = "literature/stacks-project/algebra.tex, Remark Tag 00E6 (remark-fundamental-diagram, line 3422: B (x)_A kappa(p) = (A\\p)^{-1}B/pB) with Lemma Tag 00FN (lemma-Noetherian-permanence, line 5991: quotients and localizations of Noetherian rings are Noetherian); used without mention in more-algebra.tex, proof of Lemma Tag 0AH1 ('on the other hand it is Noetherian')"
+++
Let $A\to B$ be a homomorphism of commutative rings with $B$ Noetherian `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)), and let $\mathfrak p\subset A$ be a prime ideal with residue field $\kappa(\mathfrak p)=A_{\mathfrak p}/\mathfrak pA_{\mathfrak p}$ `Localization.AtPrime, Ideal.ResidueField, Ideal.Fiber` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Localization/AtPrime/Basic.lean)). Then the fibre ring $B\otimes_A\kappa(\mathfrak p)$ is Noetherian.
