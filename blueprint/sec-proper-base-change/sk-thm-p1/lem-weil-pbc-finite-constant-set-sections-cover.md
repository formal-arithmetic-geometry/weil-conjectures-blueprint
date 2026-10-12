+++
id = "lem-weil-pbc-finite-constant-set-sections-cover"
kind = "lemma"
title = "Finite families of constant set-sheaf sections lift on a common cover"
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions"]
lean = ["CategoryTheory.GrothendieckTopology.exists_mem_forall_exists_toSheafify_const_app_eq"]
source = "lean/WeilConjectures/Mathlib/CategoryTheory/Sites/ConstantSheafSections.lean, GrothendieckTopology.exists_mem_forall_exists_toSheafify_const_app_eq, lines 71--83, and toSheafify_const_app_injective, lines 89--103; both proofs are already complete."
+++
Let $Y$ be a scheme [def-weil-pbc-scheme-conventions], $U$ an etale object [def-weil-pbc-etale-sheaves], and $J$ either its small etale topology or its localization at $U$. Let $S$ be any set, $T$ an object of this site, $I$ a finite set, and $z_i$ sections over $T$ of the constant set sheaf at $S$ `CategoryTheory.constantSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/ConstantSheaf.lean)). Write $\eta_W:S\to\underline S(W)$ for the sheafification unit `CategoryTheory.presheafToSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheafification.lean)). (1) There exists a covering sieve $R$ of $T$ such that, for every arrow $g:W\to T$ in $R$ and every $i\in I$, there exists $s\in S$ with $\eta_W(s)=z_i|_W$. (2) If the empty sieve does not cover $W$, the function $\eta_W$ is injective. The first assertion does not require $S$ itself finite.
