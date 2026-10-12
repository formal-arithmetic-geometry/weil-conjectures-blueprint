+++
id = "lem-weil-pbc-global-sections-stalk-comparison"
kind = "lemma"
title = "Global-sections pullback and one geometric stalk"
uses = ["def-weil-pbc-finite-section-pullback", "def-weil-pbc-geometric-stalks"]
lean = ["AlgebraicGeometry.Etale.exists_globalSections_stalk_comparison"]
source = "literature/blueprint/master/blueprint/sec-proper-base-change/sk-thm-p1/lem-weil-pbc-zero-dimensional-field-extension.md, Degree-zero proof, inverse-image stalk and germ compatibility; Stacks Tag 03Q1 (3)."
+++
For any morphism g:Y→X of schemes and geometric point y:Spec Ω→Y with Ω algebraically closed `AlgebraicGeometry.Scheme.SpecToEquivOfField, IsAlgClosed` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/ResidueField.lean)), and any abelian étale sheaf F on X `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)), there is an isomorphism c:(g⁻¹F)_y≅F_(y g) [def-weil-pbc-geometric-stalks]. The composite of the canonical global-sections pullback [def-weil-pbc-finite-section-pullback], evaluation at the identity étale object of Y, its germ at y, and c equals evaluation at the identity étale object of X followed by the germ at y g. Evaluation uses Sheaf.ΓNatIsoSheafSections and the explicit terminal proof MorphismProperty.Over.mkIdTerminal.
