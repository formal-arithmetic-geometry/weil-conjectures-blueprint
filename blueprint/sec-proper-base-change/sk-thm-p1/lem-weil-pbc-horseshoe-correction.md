+++
id = "lem-weil-pbc-horseshoe-correction"
kind = "lemma"
title = "The horseshoe defect correction preserves both row squares and the augmentation"
uses = ["def-sp-abelian"]
lean = ["CategoryTheory.InjectiveResolution.corrected_middle_map"]
source = "literature/stacks-project/derived.tex, Tag 015I, final correction of the middle map"
+++
theorem corrected_middle_map
    {C : Type u} [Category.{v} C] [Abelian C]
    {X Y Z X' Y' Z' : CochainComplex C ℕ} {U U' : C}
    (α : X ⟶ Y) (β : Y ⟶ Z) (α' : X' ⟶ Y') (β' : Y' ⟶ Z')
    (φA : X ⟶ X') (φC : Z ⟶ Z') (χ q : Y ⟶ Y')
    (ε : (CochainComplex.single₀ C).obj U ⟶ Y)
    (ε' : (CochainComplex.single₀ C).obj U' ⟶ Y')
    (b : (CochainComplex.single₀ C).obj U ⟶ (CochainComplex.single₀ C).obj U')
    (hχα : α ≫ χ = φA ≫ α') (hχβ : χ ≫ β' = β ≫ φC)
    (hqa : α ≫ q = 0) (hqb : q ≫ β' = 0)
    (hε : ε ≫ χ - ε ≫ q = b ≫ ε') :
    ∃ φB : Y ⟶ Y', ε ≫ φB = b ≫ ε' ∧
      α ≫ φB = φA ≫ α' ∧ φB ≫ β' = β ≫ φC := by
  refine ⟨χ - q, ?_, ?_, ?_⟩
  · simpa only [Preadditive.comp_sub] using hε
  · rw [Preadditive.comp_sub, hχα, hqa, sub_zero]
  · rw [Preadditive.sub_comp, hχβ, hqb, sub_zero]
