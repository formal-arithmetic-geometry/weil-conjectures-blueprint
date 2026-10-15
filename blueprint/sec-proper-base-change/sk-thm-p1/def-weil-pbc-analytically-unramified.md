+++
id = "def-weil-pbc-analytically-unramified"
kind = "definition"
title = "Analytically unramified local rings and primes"
lean = ["IsAnalyticallyUnramified"]
+++
Let $(A,\mathfrak m)$ be a Noetherian local ring `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)). The ring $A$ is analytically unramified when its $\mathfrak m$-adic completion $\widehat A=\varprojlim_n A/\mathfrak m^n$ `AdicCompletion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean)) is reduced, meaning it has no nonzero nilpotent element. A prime ideal $\mathfrak p\subseteq A$ is analytically unramified when the local ring $A/\mathfrak p$, with maximal ideal $\mathfrak m/\mathfrak p$, is analytically unramified.
