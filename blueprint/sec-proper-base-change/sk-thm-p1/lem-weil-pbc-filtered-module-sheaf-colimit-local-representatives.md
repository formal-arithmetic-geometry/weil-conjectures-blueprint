+++
id = "lem-weil-pbc-filtered-module-sheaf-colimit-local-representatives"
kind = "lemma"
title = "Local stage representatives for filtered colimits of module-valued sheaves"
lean = ["CategoryTheory.filtered_module_sheaf_colimit_local_representatives"]
order = 1767
+++
Let $\mathcal C$ be a category with a Grothendieck topology $J$, $\Lambda$ a commutative ring, $I$ a small filtered category and $i\mapsto G_i$ a functor from $I$ to sheaves of $\Lambda$-modules on $(\mathcal C,J)$, with colimit cocone $(G,(c_i:G_i\to G)_{i\in I})$ in the category of sheaves of $\Lambda$-modules. For every object $U$ of $\mathcal C$ and every section $t\in G(U)$ there is a covering sieve $S$ on $U$ such that for every $f:V\to U$ in $S$ there are $i\in I$ and $s\in G_i(V)$ with $c_i(s)=f^*t$. No finite-cover hypothesis, compatibility of the local sections, or uniform choice of $i$ is asserted. (The sizes of $\mathcal C$, of $\Lambda$ and of $I$ are independent; the section modules live in the larger of the sizes of $\Lambda$ and $I$.)
