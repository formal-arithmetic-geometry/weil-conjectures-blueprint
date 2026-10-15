+++
id = "lem-weil-pbc-filtered-module-sheaf-colimit-local-representatives"
kind = "lemma"
title = "Local stage representatives for filtered colimits of module-valued sheaves"
lean = ["CategoryTheory.filtered_module_sheaf_colimit_local_representatives"]
+++
Let C be a category with Grothendieck topology J, Λ a commutative ring, I a small filtered category `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)), and G : I → Sh(C, Mod_Λ) a diagram of module-valued sheaves `SheafOfModules` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Category/ModuleCat/Sheaf.lean)). Let c be a colimit cocone of G. For every object U and section t of c.pt at U, there exists a covering sieve S on U such that for every f : V → U in S there exist i ∈ I and s ∈ G_i(V) with c_i(s) = t restricted along f. No finite-cover hypothesis, compatibility of the sections, or uniform choice of i is asserted. The object, morphism, coefficient and diagram universes are independent; the section-module universe is max of the coefficient and diagram universes.
