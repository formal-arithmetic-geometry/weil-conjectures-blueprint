+++
id = "lem-weil-pbc-kahler-differentials-mod-power-ideal"
kind = "lemma"
title = "Kähler differentials modulo a power of an ideal"
lean = ["kahlerDifferential_mod_power_ideal"]
+++
Let $R\to S$ be a homomorphism of commutative rings, $I\subseteq S$ an ideal, $n\ge1$ an integer, and $S'=S/I^{n+1}$, an $R$-algebra via $R\to S\to S'$. Let $\Omega_{S/R}\to\Omega_{S'/R}$, $\mathrm ds\mapsto\mathrm d\bar s$, be the map induced by the quotient map $S\to S'$ ($\Omega$ and $\mathrm d$ as in `KaehlerDifferential` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Kaehler/Basic.lean)); $\bar s$ the class of $s$). Then the induced $S/I^n$-linear map $$\Omega_{S/R}\otimes_SS/I^n\longrightarrow\Omega_{S'/R}\otimes_{S'}S/I^n,\qquad \mathrm ds\otimes\bar t\mapsto\mathrm d\bar s\otimes\bar t,$$ is an isomorphism.
