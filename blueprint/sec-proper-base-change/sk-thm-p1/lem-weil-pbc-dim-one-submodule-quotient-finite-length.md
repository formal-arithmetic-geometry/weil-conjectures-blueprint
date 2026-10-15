+++
id = "lem-weil-pbc-dim-one-submodule-quotient-finite-length"
kind = "lemma"
title = "Quotient of a submodule of a finite-dimensional fraction-field space has bounded length"
lean = ["Submodule.length_quotSMulTop_le_of_ringKrullDim_eq_one_of_isLocalRing"]
+++
Let $R$ be a Noetherian `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)) local integral domain of Krull dimension one `ringKrullDim` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/KrullDimension/Basic.lean)), let $K$ be its fraction field, let $r$ be a nonnegative integer, and let $M\subseteq K^{\oplus r}$ be any $R$-submodule, without a finite-generation assumption. For every nonzero $x\in R$, the $R$-module $R/xR$ has finite length `Module.length` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Length.lean)), and $M/xM$ has finite length with $\mathrm{length}_R(M/xM)\le r\,\mathrm{length}_R(R/xR)$.
