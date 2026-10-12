+++
kind = "proof"
of = "lem-weil-pbc-flat-algebra-faithfully-flat-descent"
+++
For an injective A-linear map u : N → P, flatness of C over A makes C ⊗[A] u injective. The flatness criterion reduces flatness of B over A to injectivity of B ⊗[A] u. (`Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean))).

The natural tensor-cancellation equivalences C ⊗[B] (B ⊗[A] N) ≃ C ⊗[A] N and the corresponding equivalence for P intertwine C ⊗[B] (B ⊗[A] u) with C ⊗[A] u. Hence the former is injective. (`TensorProduct.AlgebraTensorModule.cancelBaseChange` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/TensorProduct/Tower.lean))).

Faithful flatness of C over B reflects injectivity after tensoring, so B ⊗[A] u is injective. Since u was arbitrary, B is flat over A. The existing Lean theorem proves exactly this argument without sorry. (`Module.FaithfullyFlat, RingHom.FaithfullyFlat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/FaithfullyFlat/Basic.lean)), `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean))).
