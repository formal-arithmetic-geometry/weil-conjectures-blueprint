+++
id = "lem-weil-pbc-etale-algebra-filtered-colimit-descent"
kind = "lemma"
title = "Etale algebras over a filtered colimit of rings descend to a finite stage"
lean = ["AlgebraicGeometry.exists_etale_algebra_of_filteredColimit"]
source = "literature/stacks-project/algebra.tex, Lemma Tag 00U2 (lemma-etale), item (9), and its proof ('Follows from (8) [an etale ring map is the base change of an etale $R_0\\to S_0$ with $R_0$ of finite type over $\\mathbf Z$] since $R_0\\to A$ will factor through $A_i$ for some $i$ by Lemma Tag 00QO (lemma-characterize-finite-presentation)'); cited in more-algebra.tex, proof of Lemma Tag 0A02 (lemma-henselization)"
+++
Let $I$ be a small filtered category and $i\mapsto A_i$ a functor from $I$ to commutative rings with colimit $A=\varinjlim_IA_i$ `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)) and coprojections $\iota_i:A_i\to A$. Let $A\to B$ be a ring map such that $\operatorname{Spec}B\to\operatorname{Spec}A$ is etale `AlgebraicGeometry.Etale` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Etale.lean)). Then there are an index $i\in I$, a ring map $A_i\to B_i$ with $\operatorname{Spec}B_i\to\operatorname{Spec}A_i$ etale, and an isomorphism of $A$-algebras $B\cong A\otimes_{A_i}B_i$ (tensor product formed via $\iota_i$).
