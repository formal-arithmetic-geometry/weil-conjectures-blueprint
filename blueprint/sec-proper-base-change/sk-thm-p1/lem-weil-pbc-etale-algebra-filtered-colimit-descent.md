+++
id = "lem-weil-pbc-etale-algebra-filtered-colimit-descent"
kind = "lemma"
title = "Etale algebras over a filtered colimit of rings descend to a finite stage"
lean = ["AlgebraicGeometry.exists_etale_algebra_of_filteredColimit"]
order = 1827
+++
Let $I$ be a small filtered category and $i\mapsto A_i$ a functor from $I$ to commutative rings with colimit $A=\varinjlim_IA_i$ and coprojections $\iota_i:A_i\to A$. Let $A\to B$ be a ring map such that $\operatorname{Spec}B\to\operatorname{Spec}A$ is etale. Then there are an index $i\in I$, a ring map $A_i\to B_i$ with $\operatorname{Spec}B_i\to\operatorname{Spec}A_i$ etale, and an isomorphism of $A$-algebras $B\cong A\otimes_{A_i}B_i$ (tensor product formed via $\iota_i$).
