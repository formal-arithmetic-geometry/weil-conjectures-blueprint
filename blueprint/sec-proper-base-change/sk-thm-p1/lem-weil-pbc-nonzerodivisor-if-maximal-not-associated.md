+++
id = "lem-weil-pbc-nonzerodivisor-if-maximal-not-associated"
kind = "lemma"
title = "If the maximal ideal is not an associated prime of a finite module, it contains a nonzerodivisor on it"
lean = ["exists_mem_maximalIdeal_smul_injective"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 00LL (lemma-ideal-nonzerodivisor, line 15471), implication (2) => (1) for $I=\\mathfrak m$ (for $I=\\mathfrak m$ the condition $\\mathfrak m\\not\\subset\\mathfrak q$ for all $\\mathfrak q\\in\\operatorname{Ass}(M)$ says $\\mathfrak m\\notin\\operatorname{Ass}(M)$, as $\\mathfrak m$ is maximal)"
+++
Let $(R,\mathfrak m)$ be a Noetherian `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)) local ring and $M$ a finite $R$-module `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)) such that $\mathfrak m$ is not an associated prime of $M$, i.e. there is no $z\in M$ with $\{a\in R: az=0\}=\mathfrak m$. Then there is an $x\in\mathfrak m$ which is a nonzerodivisor on $M$ (multiplication by $x$ on $M$ is injective).
