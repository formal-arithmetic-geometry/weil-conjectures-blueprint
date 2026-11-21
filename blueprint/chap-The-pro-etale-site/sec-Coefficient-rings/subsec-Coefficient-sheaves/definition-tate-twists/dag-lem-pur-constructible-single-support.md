+++
id = "dag-lem-pur-constructible-single-support"
kind = "dag-lemma"
title = "Constructible singles have finite cohomological support in degree zero"
name_showing = false
order = 184516
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-pur-constructible-single-support"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.constructible_single_support"]
+++
For a scheme Y, a finite commutative ring A, a constructible A-module sheaf F `def-weil-proetale-constructible-sheaf`, and a derived object K isomorphic to F$[0]$, every homology sheaf of K is constructible and its cohomological support `def-weil-cohomological-support` is finite and contained in {0}. If F is nonzero, this support is {0}. Empty schemes and zero coefficient rings are allowed.

theorem constructible_single_support (Y : Scheme.{u}) (A : Type u) [CommRing A] [Finite A]
    (F : proEtaleRingModules Y (proEtaleConstantRing Y A))
    (hF : IsConstructibleProEtaleModuleSheaf Y A F)
    (K : proEtaleDerivedCategory Y A)
    (e : K ≅ (DerivedCategory.singleFunctor _ 0).obj F) :
    Set.Finite (proEtaleCohomologicalSupport K) ∧
    (∀ i : ℤ, IsConstructibleProEtaleModuleSheaf Y A
      ((DerivedCategory.homologyFunctor _ i).obj
        K)) ∧
    proEtaleCohomologicalSupport K ⊆ {0} ∧
    (¬ IsZero F →
      proEtaleCohomologicalSupport K = {0})

(SHEAF DAG node `lem-pur-constructible-single-support`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-cohomological-support`, `def-weil-pbc-proetale-operations`, `def-weil-proetale-constructible-sheaf`, `def-weil-proetale-inverse-image`.
