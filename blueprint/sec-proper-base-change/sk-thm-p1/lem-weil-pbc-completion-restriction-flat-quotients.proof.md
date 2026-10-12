+++
kind = "proof"
of = "lem-weil-pbc-completion-restriction-flat-quotients"
+++
Write C = completion_I(A), iota : A -> C, J = I C, g = f.comp iota. For every n, evaluation C -> A/I^n is surjective, has kernel I^n C = J^n by finite generation, and sends iota(a) to a mod I^n. The first isomorphism theorem gives e : C/J^n ~= A/I^n with this formula. (`AdicCompletion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean)), `AdicCompletion.pow_smul_top_eq_ker_eval` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Completeness.lean))).

Put K = (I^n).map g. By map of products and composition, (J^n).map f = K, so f induces qf : C/J^n -> S/K. Flatness of g and flat base change give flatness of A/I^n -> S/K; in Lean use quotIdealMapEquivQuotTensor and Module.Flat.baseChange. (`Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)), `Module.Flat.baseChange` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Stability.lean))).

The representative formula for e shows qf.comp e.symm is the canonical A/I^n -> S/K map. Flatness is invariant under precomposition with a bijective ring map (Mathlib RingHom.Flat.comp_iff_of_bijective_right), so qf is flat. (`Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean))).

The identity J^n S = K, as C-submodules of S, identifies the module quotient S/(J^n S) with the ring quotient S/K. The representative formula shows this additive equivalence is C/J^n-linear. Transport flatness along it. When n = 0 these are zero quotients, and the same construction applies. (`Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean))).
