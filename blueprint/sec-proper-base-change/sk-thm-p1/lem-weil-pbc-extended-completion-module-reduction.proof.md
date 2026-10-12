+++
kind = "proof"
of = "lem-weil-pbc-extended-completion-module-reduction"
+++
Give S its R-module structure via φ and put J = I S. The identities J^k = map φ (I^k) identify S/J^k with S/(I^k S), and hence the J-adic ring completion with the I-adic R-module completion of S. The given coordinate condition determines ψ uniquely and makes its action the canonical action of the completed base. Expanding generators of the extended ideal gives K^k S-completion = I^k S-completion after restriction of scalars. (`AdicCompletion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean))).

By completion of modules for a finitely generated ideal (05GG), evaluation onto S/IS is surjective and its kernel is I times the module completion. The preceding scalar comparison identifies this kernel with K times the completed algebra, so the quotient module is S/IS. (`AdicCompletion.isAdicComplete` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Completeness.lean))).

By 05GG for R, the first evaluation identifies R-completion/K with R/I. The component condition on ψ identifies the action on the quotient from the preceding step with the given quotientMap action on S/IS. Transport the finite generating family of S/IS across these scalar and module isomorphisms. (`AdicCompletion.isAdicComplete_self` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/LocalRing.lean)), `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean))).
