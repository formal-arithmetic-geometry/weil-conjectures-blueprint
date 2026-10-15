+++
id = "lem-weil-pbc-filtered-colimit-algebras-underlying-module"
kind = "lemma"
title = "A filtered colimit of algebras is the colimit of the underlying modules"
lean = ["CommAlgCat.filtered_colimit_algebras_underlying_module"]
+++
Let $R$ be a commutative ring, $I$ a small filtered category and $i\mapsto A_i$ a functor from $I$ to the category of commutative $R$-algebras, with transition maps $A(u):A_i\to A_j$ for $u:i\to j$, colimit $A=\varinjlim_IA_i$ in that category `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)) and coprojections $\iota_i:A_i\to A$. Regard every $A_i$ and $A$ as $R$-modules and the $R$-algebra homomorphisms $A(u)$, $\iota_i$ as $R$-linear maps. Then $(A,(\iota_i)_{i\in I})$ is a colimit of the diagram $i\mapsto A_i$ in the category of $R$-modules `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)): for every $R$-module $P$ and $R$-linear maps $f_i:A_i\to P$ with $f_j\circ A(u)=f_i$ for all $u:i\to j$ there is exactly one $R$-linear map $f:A\to P$ with $f\circ\iota_i=f_i$ for all $i$.
