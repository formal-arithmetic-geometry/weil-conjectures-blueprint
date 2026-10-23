+++
id = "lem-weil-pbc-finite-product-integral-closure"
kind = "lemma"
title = "Integral closure commutes with finite products"
lean = ["integralClosure_finite_pi"]
order = 1790
+++
Let $R_i\to S_i$ be homomorphisms of commutative rings for $i=1,\dots,n$, let $R=\prod_iR_i$ and $S=\prod_iS_i$, and let $S_i'\subseteq S_i$ be the subring of elements integral over $R_i$. Then the subring of $S$ consisting of elements integral over $R$ is exactly $\prod_iS_i'$. If every $R_i\to S_i$ is injective, so that $R\subseteq S$, then $R$ is integrally closed in $S$ if and only if each $R_i$ is integrally closed in $S_i$.
