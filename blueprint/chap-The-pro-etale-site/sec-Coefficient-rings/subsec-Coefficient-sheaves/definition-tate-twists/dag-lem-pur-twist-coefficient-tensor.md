+++
id = "dag-lem-pur-twist-coefficient-tensor"
kind = "dag-lemma"
title = "Finite integral coefficient extension commutes with sheafwise completion"
name_showing = false
order = 184524
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-pur-twist-coefficient-tensor"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.purTwistCoefficientTensorMap", "AlgebraicGeometry.Scheme.purTwistCoefficientTensor"]
uses = ["dag-def-pur-twist-coefficient-rings"]
+++
Let S be an arbitrary scheme, l a prime and E a finite extension of Q_l. For the four concrete coefficient sheaves and canonical maps [dag-def-pur-twist-coefficient-rings], define the canonical ring homomorphism B(U)⊗_{A(U)}R(U)→T(U) by b⊗a↦d(b)c(a) for each site object U. The scalar-square equality makes the formula balanced. This specified map is bijective. The tensor uses the two specified maps from the discrete Z_l constant sheaf. This is a coefficient calculation and assumes no invertibility of l on S and makes no assertion about Tate twists, arbitrary module tensors, local freeness or derived completeness.

theorem purTwistCoefficientTensor (S : Scheme.{t}) (l : ℕ) [Fact l.Prime]
    (E : Type u) [Field E] [Algebra ℚ_$[l]$ E] [FiniteDimensional ℚ_$[l]$ E]
    (U : S.ProEtᵒᵖ) :
    letI := ((purTwistConstantIntegersMap S l E).hom.app U).hom.toAlgebra
    letI := ((purTwistZlCompletionMapOfUniverses.{t, u} S l).hom.app U).hom.toAlgebra
    Function.Bijective (purTwistCoefficientTensorMap S l E U)

(SHEAF DAG node `lem-pur-twist-coefficient-tensor`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `lem-weil-l-adic-extension-integers-dvr`.
