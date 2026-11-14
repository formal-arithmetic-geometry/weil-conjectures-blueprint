+++
id = "dag-lem-pur-tensor-pushout-action"
kind = "dag-lemma"
title = "A sectionwise scalar pushout acts uniquely on a balanced tensor sheaf"
name_showing = false
order = 184521
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-pur-tensor-pushout-action"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.tensorPushoutAction_existsUnique"]
+++
Let C be a category with a Grothendieck topology J and sheafification of abelian presheaves, with the locally bijective criterion. Let A,B,R,T be sheaves of commutative rings, a:A→R, b:A→B, c:R→T and d:B→T, and M an R-module sheaf `def-weil-sheaf-of-modules-category`. Suppose for every object U there is a ring equivalence e_U:B(U)⊗_{A(U)}R(U)≃T(U) taking s⊗r to d(s)c(r). Let N be extension along b of M restricted along a [dag-def-pur-sheaf-tensor-product]. There is a unique family of T(U)-module structures on N(U) compatible with restriction, whose d(B)-action is the original B-action and whose c(r)-action on the sheafification image of s⊗x is the image of s⊗(r x). Neither finite freeness nor a nonzero ring hypothesis is required.

theorem tensorPushoutAction_existsUnique (e : ∀ U : Cᵒᵖ,
    letI := (b.hom.app U).hom.toAlgebra
    letI := (a.hom.app U).hom.toAlgebra
    B.obj.obj U ⊗[A.obj.obj U] R.obj.obj U ≃+* T.obj.obj U)
    (he : ∀ (U : Cᵒᵖ) (s : B.obj.obj U) (r : R.obj.obj U),
      letI := (b.hom.app U).hom.toAlgebra
      letI := (a.hom.app U).hom.toAlgebra
      e U (s ⊗ₜ[A.obj.obj U] r) = d.hom.app U s * c.hom.app U r) :
    let M' := (SheafOfModules.restrictScalars
      ((sheafCompose J (forget₂ CommRingCat RingCat)).map a)).obj M
    let N := SheafOfModules.changeOfRingsOfUniverses b M'
    let P := SheafOfModules.changeOfRingsPresheafOfUniverses b M'
    let φ := (PresheafOfModules.toPresheaf _).map
      ((PresheafOfModules.sheafificationAdjunction
        (𝟙 ((sheafCompose J (forget₂ CommRingCat RingCat)).obj B).obj)).unit.app P)
    ∃! K : ∀ U : Cᵒᵖ, Module (T.obj.obj U) (N.val.obj U),
      (∀ ⦃U V : Cᵒᵖ⦄ (f : U ⟶ V) (z : T.obj.obj U) (x : N.val.obj U),
        N.val.map f (@SMul.smul _ _ (K U).toSMul z x) =
          @SMul.smul _ _ (K V).toSMul (T.obj.map f z) (N.val.map f x)) ∧
      (∀ (U : Cᵒᵖ) (s : B.obj.obj U) (x : N.val.obj U),
        @SMul.smul _ _ (K U).toSMul (d.hom.app U s) x = s • x) ∧
      ∀ (U : Cᵒᵖ) (r : R.obj.obj U) (s : B.obj.obj U) (x : M.val.obj U),
        @SMul.smul _ _ (K U).toSMul (c.hom.app U r)
          (φ.app U (s ⊗ₜ[A.obj.obj U, (b.hom.app U).hom] x)) =
        φ.app U (s ⊗ₜ[A.obj.obj U, (b.hom.app U).hom] (r • x))

(SHEAF DAG node `lem-pur-tensor-pushout-action`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`.
