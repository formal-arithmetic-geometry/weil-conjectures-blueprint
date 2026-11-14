+++
id = "dag-lem-pur-twist-integral-local-models"
kind = "dag-lemma"
title = "Scalar-extension local models of the integral root line"
name_showing = false
order = 184526
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-pur-twist-integral-local-models"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.purTwistIntegralLocalModels"]
uses = ["dag-def-pur-twist-coefficient-rings", "dag-def-pur-twist-sheaves"]
+++
For the concrete Tate sheaves [dag-def-pur-twist-sheaves], assume the completed Z_l root module has rank one. The integral tensor has a pro-etale unit trivialization. At every positive finite level its completed scalar reduction is the prescribed finite tensor, which has a unit trivialization and is nonzero if the base is nonempty. Local constancy, constructibility and finite stalks follow separately from the generic proved finite-line theorem. No derived assertion is included.

theorem purTwistIntegralLocalModels
    (S : Scheme.{u}) (l : ℕ) [Fact l.Prime]
    (E : Type u) [Field E] [Algebra ℚ_$[l]$ E] [FiniteDimensional ℚ_$[l]$ E]
    [∀ x : S, Invertible (l : S.residueField x)]
    (hL : (purTwistZlModule S l).IsFiniteLocallyFreeOfRank 1) :
    (∃ (I : Type (u + 1)) (U : I → S.ProEt)
      (f : ∀ i, U i ⟶ ProEt.mk (𝟙 S)),
      Presieve.ofArrows U f ∈ (ProEt.precoverage S).coverings _ ∧
      ∀ i, Nonempty ((purTwistIntegralModule S l E).over (U i) ≅
        (SheafOfModules.unit
          (WeilConjectures.completedIntegralCoefficientSheafUnrestricted l E S)).over (U i))) ∧
    ∀ n : ℕ,
      Nonempty (SheafOfModules.changeOfRingsOfUniverses.{u, u + 1, u + 1, u + 1}
        (WeilConjectures.completedIntegralCommRingProjectionUnrestricted l E S n)
          (purTwistIntegralModule S l E) ≅ purTwistFiniteOne S l E n) ∧
      (∃ (I : Type (u + 1)) (U : I → S.ProEt)
        (f : ∀ i, U i ⟶ ProEt.mk (𝟙 S)),
        Presieve.ofArrows U f ∈ (ProEt.precoverage S).coverings _ ∧
        ∀ i, Nonempty ((purTwistFiniteOne S l E n).over (U i) ≅
          (SheafOfModules.unit (WeilConjectures.integralCoefficientSheaf l E S n)).over (U i))) ∧
      (Nonempty S → ¬IsZero (purTwistFiniteOne S l E n))

(SHEAF DAG node `lem-pur-twist-integral-local-models`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-amb-finite-locally-free-module`, `lem-weil-l-adic-extension-integers-dvr`.
