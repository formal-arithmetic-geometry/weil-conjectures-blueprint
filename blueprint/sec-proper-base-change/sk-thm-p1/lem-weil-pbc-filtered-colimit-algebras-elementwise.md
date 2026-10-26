+++
id = "lem-weil-pbc-filtered-colimit-algebras-elementwise"
kind = "lemma"
title = "Elements of a filtered colimit of commutative algebras come from a stage"
uses = ["def-weil-pbc-category-colimit"]
lean = ["CategoryTheory.Limits.Concrete.isColimit_exists_rep", "CategoryTheory.Under.preservesColimitsOfShape_forget_of_isConnected", "commAlgCatEquivUnder", "CommRingCat.FilteredColimits.forget_preservesFilteredColimits"]
order = 1739
tags = ["mathlib", "stacks-00D6"]
+++
Let $R$ be a commutative ring, $I$ a filtered category and $i\mapsto A_i$ a functor from $I$ to the category of commutative $R$-algebras, with a colimit $A=\varinjlim_IA_i$ in that category [def-weil-pbc-category-colimit] and coprojections $\iota_i:A_i\to A$. Then (1) $A$ with the maps $\iota_i$ is also a colimit of the underlying diagram of commutative rings; (2) every element of $A$ is of the form $\iota_i(a)$ for some $i\in I$ and some $a\in A_i$.
