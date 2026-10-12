+++
id = "lem-weil-pbc-flat-under-regular"
kind = "lemma"
title = "Regularity descends along flat local homomorphisms"
lean = ["IsRegularLocalRing.of_ringHom_flat"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 00OF (lemma-flat-under-regular, line 27188) and its proof: a finite free resolution of the residue field kappa of R truncated at d = dim S, tensored with S (flatness), K_d tensor S finite free by Proposition Tag 00O7 (proposition-regular-finite-gl-dim) and Lemma Tag 00O5 (lemma-independent-resolution), K_d finite free by Lemma Tag 00O1 (lemma-finite-projective-descends), so kappa has finite projective dimension and R is regular by Proposition Tag 00OC (proposition-finite-gl-dim-regular, Serre)"
+++
Let $(R,\mathfrak m_R)$ and $(S,\mathfrak m_S)$ be Noetherian `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)) local rings and $\varphi:R\to S$ a local homomorphism ($\varphi(\mathfrak m_R)\subseteq\mathfrak m_S$). If $\varphi$ is flat `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)) and $S$ is a regular local ring `IsRegularLocalRing, IsRegularRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/RegularLocalRing/Defs.lean)), then $R$ is a regular local ring.
