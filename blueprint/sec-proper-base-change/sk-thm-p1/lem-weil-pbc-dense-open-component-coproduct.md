+++
id = "lem-weil-pbc-dense-open-component-coproduct"
kind = "lemma"
title = "Component coproduct over prescribed dense opens"
uses = ["def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.exists_dense_open_component_coproduct"]
source = "literature/stacks-project/morphisms.tex, Tag 0BAJ, reduction to a dense disjoint union of components; expanded component-open proof in lem-weil-pbc-dense-open-component-modifications, steps 1-3 (Stacks web text checked)"
+++
Let X be a reduced scheme `AlgebraicGeometry.IsReduced` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Properties.lean)), and let ι_i:C_i→X, indexed by Fin(n), be closed immersions `AlgebraicGeometry.IsClosedImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/ClosedImmersion.lean)) from integral schemes `AlgebraicGeometry.IsIntegral` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Properties.lean)) whose images enumerate without repetitions the irreducible components `irreducibleComponents` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Topology/Irreducible.lean)). For dense opens V_i⊆C_i, there is a dense open U⊆X such that the component coproduct morphism [def-weil-pbc-scheme-conventions] restricted to U is an isomorphism and ι_i^{-1}(U)⊆V_i for every i.
