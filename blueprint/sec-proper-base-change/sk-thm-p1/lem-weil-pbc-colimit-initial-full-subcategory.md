+++
id = "lem-weil-pbc-colimit-initial-full-subcategory"
kind = "lemma"
title = "Colimits over a weakly initial full subcategory of a cofiltered category, and over equivalent index categories"
uses = ["def-weil-pbc-category-colimit"]
lean = ["CategoryTheory.Functor.initial_of_exists_of_isCofiltered_of_fullyFaithful", "CategoryTheory.IsCofiltered.of_exists_of_isCofiltered_of_fullyFaithful", "CategoryTheory.Functor.final_op_of_initial", "CategoryTheory.Functor.Final.hasColimit_comp_iff", "CategoryTheory.Functor.Final.colimitIso", "CategoryTheory.Limits.HasColimit.isoOfEquivalence"]
order = 1697
tags = ["mathlib", "stacks-0BUC"]
+++
Let $\mathcal C$ be a category [def-weil-pbc-category-colimit]. (1) Let $\mathcal I$ be a cofiltered category and $\mathcal J\subset\mathcal I$ a full subcategory such that every object $i$ of $\mathcal I$ receives a morphism $j\to i$ from some object $j$ of $\mathcal J$. Then $\mathcal J$ is cofiltered, and for every functor $D:\mathcal I^{\mathrm{op}}\to\mathcal C$ the colimit of $D$ exists if and only if the colimit of its restriction $D|_{\mathcal J^{\mathrm{op}}}$ exists, and then the canonical map $\varinjlim_{\mathcal J^{\mathrm{op}}}D|_{\mathcal J^{\mathrm{op}}}\to\varinjlim_{\mathcal I^{\mathrm{op}}}D$ (induced by the coprojections $\iota_j$, $j\in\mathcal J$) is an isomorphism. (2) Let $e:\mathcal K\to\mathcal L$ be an equivalence of categories and $G:\mathcal L\to\mathcal C$, $F:\mathcal K\to\mathcal C$ functors with a natural isomorphism $w:G\circ e\cong F$. If $\varinjlim F$ and $\varinjlim G$ exist, there is an isomorphism $\varinjlim F\cong\varinjlim G$ whose composite with the coprojection $\iota_k$ of $F$ is $\iota_{e(k)}\circ w_k^{-1}$.
