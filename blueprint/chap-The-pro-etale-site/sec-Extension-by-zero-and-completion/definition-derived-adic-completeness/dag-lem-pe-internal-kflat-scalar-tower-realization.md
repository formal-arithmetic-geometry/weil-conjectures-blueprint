+++
id = "dag-lem-pe-internal-kflat-scalar-tower-realization"
kind = "dag-lemma"
title = "Native internal K-flat scalar tower realization"
name_showing = false
order = 208503
tags = ["sheaf-dag"]
split_from = "definition-derived-adic-completeness--1"
dag_id = "lem-pe-internal-kflat-scalar-tower-realization"
dag_kind = "lemma"
dag_status = "proved"
serial = false
dag_lean = ["CategoryTheory.Mod.KFlatScalarTower.reduction", "CategoryTheory.Mod.KFlatScalarTower.restriction", "CategoryTheory.Mod.KFlatScalarTower.restrictionComp", "CategoryTheory.Mod.KFlatScalarTower.association", "CategoryTheory.Mod.KFlatScalarTower.step", "CategoryTheory.Mod.KFlatScalarTower.tensorLevel", "CategoryTheory.Mod.KFlatScalarTower.tensorStep", "CategoryTheory.Mod.KFlatScalarTower.tensorUnit", "CategoryTheory.Mod.KFlatScalarTower.realization", "CategoryTheory.Mod.KFlatScalarTower.natural_computation", "CategoryTheory.Mod.KFlatScalarTower.derived_realization"]
+++
Let C be a closed symmetric monoidal Grothendieck abelian category with additive tensor and functorial flat resolutions. Let R and S_n be commutative monoid objects, q_n:R→S_n and r_n:S_{n+1}→S_n monoid morphisms with q_{n+1}r_n=q_n. Let B_n be R-modules with isomorphisms eB_n:B_n≅Res(q_n)(S_n), unit maps ι_n:R→B_n and transitions τ_n:B_{n+1}→B_n such that ι_n eB_n=q_n and τ_n eB_n=eB_{n+1}r_n on underlying C-morphisms. Use the native extension-restriction adjunctions of `sk-def-sfb-change-of-scalars` and their total derived adjunctions `sk-def-sfb-derived-extension-of-scalars`. For every native K-flat cochain complex P and isomorphism eP:QP≅K, there are isomorphisms e_n:Q(P⊗_R B_n)≅Res(q_n)L Ext(q_n)(K). They identify the termwise maps 1⊗τ_n with the restricted transition formed from the derived r_n-unit and left-adjoint-uniqueness associator, and identify the termwise right-unitor/tensor-ι_n maps with eP followed by the derived q_n-unit. No flatness of q_n or of the terms of P is assumed. All tensor products, K-flatness and derived functors are the native internal-module constructions.

(SHEAF DAG node `lem-pe-internal-kflat-scalar-tower-realization`; machine-alignment layer.) Split from [definition-derived-adic-completeness--1]. DAG kind: lemma. Placed through `sk-def-pe-derived-completion` (ancestor-1). DAG status: proved. Statement dependencies not drawn: `def-pc-flat-sheaf-modules`, `def-pc-kflat-complex`, `def-pc-module-kflat-complex`, `def-sfb-derived-extend-levelwise-adjunction`, `def-sfb-derived-tensor-modules`, `def-sfb-modobj-extension`, `def-sfb-modobj-internal-hom`, `def-sfb-modobj-relative-tensor`, `def-sfb-modobj-symmetric-tensor`, `lem-pc-derived-category-locally-small`, `lem-sfb-extend-scalars-kflat`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-modobj-abelian`, `lem-sfb-modobj-flat-resolutions`, `lem-sfb-modobj-forget-creates`, `lem-sfb-modobj-grothendieck`, `lem-sfb-modobj-symmetric-bimodules`, `lem-weil-pbc-module-functorial-flat-resolution`, `lem-weil-pbc-module-relative-tensor-adjoint`, `pur713-def-relative-tensor`, `sk-def-sfb-change-of-scalars`, `sk-def-sfb-derived-extension-of-scalars`, `sk-def-sfb-derived-tensor-hom`, `sk-def-sfb-finite-derived-functors`, `sk-def-sfb-module-derived-pushpull`.
