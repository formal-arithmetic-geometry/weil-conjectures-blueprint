+++
kind = "proof"
of = "lem-weil-pbc-constant-module-sheaves-forget-colimits"
+++
For a commutative ring Λ, restriction of scalars along ℤ → Λ is left adjoint to coextension (Mathlib ModuleCat.restrictCoextendScalarsAdj). The forgetful functor from ℤ-modules to abelian groups is an equivalence (ModuleCat.forget₂AddCommGroupIsEquivalence). Their composite is definitionally the coefficient forgetful functor, so it is a left adjoint. This step is fully proved in Lean, including the coefficient universes.

Sheaf.composeAndSheafify of that coefficient functor is a left adjoint by Mathlib Sheaf.adjunction. Forgetting module coefficients preserves the sheaf condition, and sheafificationNatIso therefore identifies composeAndSheafify with sheafCompose. Transport the left adjoint across this natural isomorphism and apply `CategoryTheory.Adjunction.leftAdjoint_preservesColimits` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Adjunction/Limits.lean)). This proves preservation of all colimits of size u+1, with their canonical legs.
