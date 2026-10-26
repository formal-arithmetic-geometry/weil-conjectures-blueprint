+++
id = "lem-weil-pbc-dense-open-component-modifications"
kind = "lemma"
title = "Dense-open gluing of modifications of distinct components"
uses = ["def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.exists_dense_open_isIso_component_modifications"]
order = 1691
+++
Let $X$ be a reduced scheme. Let $C_i$ ($i\in\operatorname{Fin}(n)$) be integral schemes with closed immersions $\iota_i:C_i\to X$ whose images enumerate the irreducible components of $X$ without repetitions. For schemes $Y_i$ and morphisms $\nu_i:Y_i\to C_i$ [def-weil-pbc-scheme-conventions], assume each $\nu_i$ is an isomorphism over some dense open of $C_i$. Then the coproduct morphism $\coprod_iY_i\to X$, with component maps $\iota_i\circ\nu_i$, is an isomorphism over a dense open of $X$. No finiteness, smoothness or dimension assumption on $\nu_i$ or $Y_i$ is required.
