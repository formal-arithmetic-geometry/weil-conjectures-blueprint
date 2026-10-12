+++
id = "lem-tate-module-no-fixed"
kind = "lemma"
title = "No fixed vectors on the Tate module when the fixed subgroup is finite"
order = 2901
uses = ["def-tate-module-abelian-group"]
lean = ["AddCommGroup.eq_zero_of_mem_tateModule_of_forall_fixed"]
+++
Let $M$ be an abelian group, $\ell$ a prime, and $\sigma$ an automorphism of $M$
whose fixed subgroup $M^\sigma$ is finite. Then $T_\ell M$ has no $\ell$-power
torsion, $(T_\ell M)^\sigma=0$, and $(V_\ell M)^\sigma=0$ (in the notation of
[def-tate-module-abelian-group]); the same holds for $\sigma^{-1}$.
