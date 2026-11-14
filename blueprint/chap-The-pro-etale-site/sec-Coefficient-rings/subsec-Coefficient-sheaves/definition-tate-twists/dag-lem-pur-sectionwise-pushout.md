+++
id = "dag-lem-pur-sectionwise-pushout"
kind = "dag-lemma"
title = "A sectionwise pushout square of sheaves is a pushout square"
name_showing = false
order = 184518
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-pur-sectionwise-pushout"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.sheaf_isPushout_of_sectionwise"]
+++
For an arbitrary Grothendieck topology J on a category C and a category D, consider a commuting square of D-valued sheaves. If evaluation at every object of C makes it a pushout square in D, then it is a pushout in Sheaf J D.

theorem sheaf_isPushout_of_sectionwise
    {C : Type u} [Category.{v} C] (J : GrothendieckTopology C)
    {D : Type w} [Category.{t} D]
    {A B M N : Sheaf J D} (a : A ⟶ B) (b : A ⟶ M)
    (c : B ⟶ N) (d : M ⟶ N) (h : a ≫ c = b ≫ d)
    (hs : ∀ U : Cᵒᵖ, IsPushout (a.hom.app U) (b.hom.app U)
      (c.hom.app U) (d.hom.app U)) : IsPushout a b c d

(SHEAF DAG node `lem-pur-sectionwise-pushout`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split.
