+++
id = "dag-lem-pe-classical-derived-counit"
kind = "dag-lemma"
title = "Derived counit on bounded-below classical complexes"
name_showing = false
order = 129502
tags = ["sheaf-dag"]
split_from = "corollary-bounded-below-classical-complexes--2"
dag_id = "lem-pe-classical-derived-counit"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.classicalDerivedCounit"]
uses = ["dag-det-pe-classical-definition-continuity-map", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
theorem classicalDerivedCounit (X : Scheme.{u}) (Λ : Type (u + 1))
    [CommRing Λ] [TopologicalSpace Λ] [DiscreteTopology Λ]
    (hunit : ∀ L : DerivedCategory.Plus
      (Sheaf X.smallEtaleTopology (ModuleCat.{u + 1} Λ)),
      IsIso ((comparisonAdjunction (ModuleCat.{u + 1} Λ) X).derivedPlus.unit.app L)) :
    ∀ K : DerivedCategory.Plus
      (Sheaf (Scheme.ProEt.topology X) (ModuleCat.{u + 1} Λ)),
      ClassicalPlus X Λ K →
        IsIso ((comparisonAdjunction (ModuleCat.{u + 1} Λ) X).derivedPlus.counit.app K)

(SHEAF DAG node `lem-pe-classical-derived-counit`; machine-alignment layer.) Split from [corollary-bounded-below-classical-complexes--2]. DAG kind: statement. Placed through `det-pe-classical-derived-equivalence` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-abstract-derived-category`, `def-weil-pbc-bounded-derived-subcategories`, `def-weil-pbc-derived-inverse-image`, `def-weil-sheaf-of-modules-category`, `lem-coef-grothendieck-locally-presentable`, `lem-pc-derived-category-locally-small`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-proetale-sheaves-grothendieck`, `lem-trf-bounded-below-derived-adjunction`, `lem-weil-pbc-sheaf-tensor-closed`, `prop-weil-pbc-derived-inverse-image-adjunction`.
