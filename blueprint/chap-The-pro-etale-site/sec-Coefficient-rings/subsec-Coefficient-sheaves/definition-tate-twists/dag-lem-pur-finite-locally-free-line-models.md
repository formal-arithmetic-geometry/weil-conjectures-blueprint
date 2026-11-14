+++
id = "dag-lem-pur-finite-locally-free-line-models"
kind = "dag-lemma"
title = "Finite local models for a locally free coefficient line"
name_showing = false
order = 184517
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-pur-finite-locally-free-line-models"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.finiteLocallyFreeLine_models"]
+++
A rank-one locally free module over a finite constant commutative coefficient ring on any scheme is locally constant and constructible, with finite geometric stalks. The zero ring and empty scheme are allowed.

theorem finiteLocallyFreeLine_models (S : Scheme.{u}) (A : Type u)
    [CommRing A] [Finite A]
    (L : proEtaleRingModules S (proEtaleConstantRing S A))
    (hL : L.IsFiniteLocallyFreeOfRank 1) :
    IsLocallyConstantProEtaleModuleSheaf S A L ∧
      IsConstructibleProEtaleModuleSheaf S A L ∧
      ∀ (Ω : Type u) [Field Ω] [IsAlgClosed Ω] (s : Spec (.of Ω) ⟶ S),
        Finite (proEtaleGeometricModuleStalk s (proEtaleConstantRing S A) L)

(SHEAF DAG node `lem-pur-finite-locally-free-line-models`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-amb-finite-locally-free-module`, `def-weil-pbc-proetale-operations`, `def-weil-proetale-constructible-sheaf`, `def-weil-proetale-inverse-image`, `sk-def-pbc-conventions`.
