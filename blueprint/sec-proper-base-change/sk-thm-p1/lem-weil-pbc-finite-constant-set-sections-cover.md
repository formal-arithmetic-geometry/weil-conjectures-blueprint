+++
id = "lem-weil-pbc-finite-constant-set-sections-cover"
kind = "lemma"
title = "Finite families of constant set-sheaf sections lift on a common cover"
lean = ["CategoryTheory.GrothendieckTopology.exists_mem_forall_exists_toSheafify_const_app_eq", "CategoryTheory.GrothendieckTopology.toSheafify_const_app_injective"]
order = 1750
+++
Let $J$ be a Grothendieck topology on a category $\mathcal C$ and let $\mathcal A$ be a concrete category admitting sheafification for $J$ in which a morphism of presheaves becomes an isomorphism after sheafification exactly when it is locally injective and locally surjective (for instance sets or modules over a ring). Let $N$ be an object of $\mathcal A$, let $\underline N$ be the sheafification of the constant presheaf with value $N$, and write $\eta_V:N\to\underline N(V)$ for the component at $V$ of the sheafification map.
(1) Let $U$ be an object of $\mathcal C$, $I$ a finite set and $z_i\in\underline N(U)$ for $i\in I$. There is a covering sieve $R$ of $U$ such that for every arrow $g:V\to U$ in $R$ and every $i\in I$ there is $n\in N$ with $\eta_V(n)=z_i|_V$.
(2) If $U$ is an object of $\mathcal C$ which is not covered by the empty sieve, then $\eta_U:N\to\underline N(U)$ is injective.
No finiteness of $N$ is required.
