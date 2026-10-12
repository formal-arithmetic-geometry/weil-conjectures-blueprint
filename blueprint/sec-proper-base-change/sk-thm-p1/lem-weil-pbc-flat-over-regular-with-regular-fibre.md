+++
id = "lem-weil-pbc-flat-over-regular-with-regular-fibre"
kind = "lemma"
title = "Flat local maps with regular source and fibre have regular target"
lean = ["IsRegularLocalRing.of_flat_of_regular_closedFiber"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 031E (lemma-flat-over-regular-with-regular-fibre); its proof uses Lemma Tag 00ON (dimension-base-fibre-equals-total)"
+++
Let $R\to S$ be a local homomorphism of Noetherian local rings `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)). Assume that $R$ is regular `IsRegularLocalRing, IsRegularRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/RegularLocalRing/Defs.lean)), that the closed fibre $S/\mathfrak m_RS$ is regular, and that $R\to S$ is flat `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)). Then $S$ is regular.
