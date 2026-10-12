+++
id = "lem-weil-pbc-completion-restriction-flat-quotients"
kind = "lemma"
title = "Flat quotients of a completion algebra whose restriction to the original ring is flat"
lean = ["AdicCompletion.flat_quotients_of_flat_restriction"]
source = "literature/stacks-project/more-algebra.tex, Lemma Tag 0C4G, second paragraph of the forward implication; Algebra Lemmas Tags 05GG and 00HI. Read at https://stacks.math.columbia.edu/tag/0C4G."
+++
Let A and S be commutative rings, I a finitely generated ideal of A, C its I-adic completion `AdicCompletion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean)), and iota : A -> C the canonical map. Let f : C -> S be a ring homomorphism such that f composed with iota is flat `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)). Put J = I C. Then for every natural number n, including zero, the C/J^n-module S/J^n S with action induced by f is flat. No Noetherianity or locality of A or S is assumed.
