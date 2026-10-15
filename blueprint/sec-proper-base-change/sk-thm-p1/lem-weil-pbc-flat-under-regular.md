+++
id = "lem-weil-pbc-flat-under-regular"
kind = "lemma"
title = "Regularity descends along flat local homomorphisms"
lean = ["IsRegularLocalRing.of_ringHom_flat"]
+++
Let $(R,\mathfrak m_R)$ and $(S,\mathfrak m_S)$ be Noetherian `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)) local rings and $\varphi:R\to S$ a local homomorphism ($\varphi(\mathfrak m_R)\subseteq\mathfrak m_S$). If $\varphi$ is flat `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)) and $S$ is a regular local ring `IsRegularLocalRing, IsRegularRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/RegularLocalRing/Defs.lean)), then $R$ is a regular local ring.
