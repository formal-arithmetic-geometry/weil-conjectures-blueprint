+++
id = "lem-weil-pbc-dense-open-component-modifications"
kind = "lemma"
title = "Dense-open gluing of modifications of distinct components"
uses = ["def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.exists_dense_open_isIso_component_modifications"]
+++
Let $X$ be a reduced scheme `AlgebraicGeometry.IsReduced` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Properties.lean)). Let $C_i$ ($i\in\operatorname{Fin}(n)$) be integral schemes `AlgebraicGeometry.IsIntegral` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Properties.lean)) with closed immersions $\iota_i:C_i\to X$ `AlgebraicGeometry.IsClosedImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/ClosedImmersion.lean)) whose images enumerate the irreducible components of $X$ `irreducibleComponents` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Topology/Irreducible.lean)) without repetitions. For schemes $Y_i$ and morphisms $\nu_i:Y_i\to C_i$ [def-weil-pbc-scheme-conventions], assume each $\nu_i$ is an isomorphism over some dense open of $C_i$. Then the coproduct morphism $\coprod_iY_i\to X$, with component maps $\iota_i\circ\nu_i$, is an isomorphism over a dense open of $X$. No finiteness, smoothness or dimension assumption on $\nu_i$ or $Y_i$ is required.
