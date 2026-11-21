+++
id = "dag-lem-pur-twist-root-local-models"
kind = "dag-lemma"
title = "Finite and compatible completed local bases of the root tower"
name_showing = false
order = 184527
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-pur-twist-root-local-models"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.purTwistRootLocalModels"]
uses = ["dag-def-pur-roots-of-unity-sheaf", "dag-def-pur-twist-coefficient-rings", "dag-def-pur-twist-sheaves"]
+++
For any scheme on which l is invertible, the concrete finite root modules [dag-def-pur-twist-sheaves] admit etale unit trivializations and have finite geometric stalks. The completed root module admits a pro-etale unit trivialization, and its ordinary finite scalar reductions are the prescribed finite root modules. There is no coefficient field or derived-completeness assertion.

theorem purTwistRootLocalModels (S : Scheme.{u}) (l : ℕ) [Fact l.Prime]
    [∀ x : S, Invertible (l : S.residueField x)] :
    (∀ n : ℕ,
      (∃ (I : Type (u + 1)) (U : I → S.ProEt)
        (f : ∀ i : I, U i ⟶ ProEt.mk (𝟙 S)),
        Presieve.ofArrows U f ∈ (ProEt.precoverage S).coverings _ ∧
        (∀ i : I, Etale (U i).hom) ∧
        ∀ i : I, Nonempty ((purTwistRootsModule S l n).over (U i) ≅
          (SheafOfModules.unit (purTwistRing S (purTwistFiniteRing S l n))).over (U i))) ∧
      (∀ (Ω : Type u) [Field Ω] [IsAlgClosed Ω] (s : Spec (.of Ω) ⟶ S),
        Finite ((proEtaleGeometricStalk (C := AddCommGrpCat.{u + 1}) s
          (proEtaleRootsOfUnitySheaf S (l ^ (n + 1)))) : Type (u + 1)))) ∧
    ((∃ (I : Type (u + 1)) (U : I → S.ProEt)
        (f : ∀ i : I, U i ⟶ ProEt.mk (𝟙 S)),
        Presieve.ofArrows U f ∈ (ProEt.precoverage S).coverings _ ∧
        ∀ i : I, Nonempty ((purTwistZlModule S l).over (U i) ≅
          (SheafOfModules.unit (purTwistRing S (purTwistZlCompletion S l))).over (U i))) ∧
      ∀ n : ℕ, Nonempty
        (SheafOfModules.changeOfRingsOfUniverses.{u, u + 1, u + 1, u + 1}
          (purTwistZlProjection S l n)
          (purTwistZlModule S l) ≅ purTwistRootsModule S l n))

(SHEAF DAG node `lem-pur-twist-root-local-models`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split.
