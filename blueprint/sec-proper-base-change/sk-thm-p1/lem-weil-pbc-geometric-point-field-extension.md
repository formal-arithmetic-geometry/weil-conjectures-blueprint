+++
id = "lem-weil-pbc-geometric-point-field-extension"
kind = "lemma"
title = "Extension of separably closed geometric point fields"
uses = ["def-pc-scheme", "def-pc-separably-closed", "def-weil-pbc-geometric-stalks"]
lean = ["AlgebraicGeometry.Scheme.isIso_pointSmallEtalePrecomp_sheafFiber"]
+++
Let S be a scheme [def-pc-scheme], k and l separably closed fields [def-pc-separably-closed], s:Spec k -> S a point `AlgebraicGeometry.Scheme.SpecToEquivOfField, IsAlgClosed` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/ResidueField.lean)), and a:Spec l -> Spec k any morphism. For an abelian etale sheaf F `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)), precomposition of pointed etale lifts U by a induces a canonical map F_s -> F_(a s) of geometric stalks [def-weil-pbc-geometric-stalks]. This map is an isomorphism, natural in F. There is no algebraicity assumption on l/k.
