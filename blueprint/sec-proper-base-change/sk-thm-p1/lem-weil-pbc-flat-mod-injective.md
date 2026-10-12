+++
id = "lem-weil-pbc-flat-mod-injective"
kind = "lemma"
title = "Injectivity modulo the maximal ideal into a flat module (Noetherian local)"
lean = ["flat_mod_injective"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 00ME (lemma-mod-injective, line 23424), proof lines 23436-23477 (Krull intersection theorem, Lemma lemma-intersect-powers-ideal-module-zero; flatness via Tor, Lemma lemma-characterize-flat). Tag verified in tags/tags: 00ME,algebra-lemma-mod-injective"
+++
Let $\varphi:(R,\mathfrak m)\to(S,\mathfrak m_S)$ be a local homomorphism of local rings (commutative rings with exactly one maximal ideal; $\varphi(\mathfrak m)\subseteq\mathfrak m_S$) with $S$ Noetherian `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)). Let $M$ be an $R$-module which is flat `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)), let $N$ be a finite $S$-module `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)), regarded as an $R$-module via $\varphi$, and let $u:N\to M$ be an $R$-linear map. If the induced map $\bar u:N/\mathfrak mN\to M/\mathfrak mM$ is injective, then $u$ is injective and the $R$-module $M/u(N)$ is flat.
