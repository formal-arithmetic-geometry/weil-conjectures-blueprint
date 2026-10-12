+++
id = "lem-weil-pbc-etale-cohomology-triangle-laws"
kind = "lemma"
title = "Triangle laws for fixed-base etale cohomology pullback"
uses = ["def-weil-pbc-cohomology-pullback", "def-weil-pbc-etale-cohomology", "lem-weil-pbc-inverse-image-composition"]
lean = ["AlgebraicGeometry.Etale.cohomologyTriangleMap_laws"]
source = "Stacks Project and source Lean, Cohomology Section 20.14 (01F7); inverse-image coherence from WeilConjectures.SixFunctors.BaseChange.Pasting, upperStarComp_hom_app_map_upperStarComp_inv_app_assoc"
+++
Given a scheme S, an abelian etale sheaf G on S `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)), and q≥0, with cohomology as in [def-weil-pbc-etale-cohomology], assign to every commuting triangle X --f--> Y --a--> S with b=f a the homomorphism H^q(a⁻¹G)→H^q(b⁻¹G) obtained by cohomological pullback [def-weil-pbc-cohomology-pullback] and the inverse-image composition isomorphism [lem-weil-pbc-inverse-image-composition]. The identity triangle induces the identity homomorphism. For X --f--> Y --g--> Z over S, the map of the composite triangle is the composite of the two triangle maps. The triangle map sends the restriction of x in H^q(S,G) along a to its restriction along b.
