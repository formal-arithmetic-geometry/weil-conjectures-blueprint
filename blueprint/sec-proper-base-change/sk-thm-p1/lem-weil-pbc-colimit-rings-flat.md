+++
id = "lem-weil-pbc-colimit-rings-flat"
kind = "lemma"
title = "Flatness over a filtered colimit of rings"
lean = ["RingHom.flat_of_flat_comp_colimit_ι"]
source = "literature/stacks-project/algebra.tex, Lemma Tag 05UU (lemma-colimit-rings-flat, line 8857), part (1) with $M=S$ (stated for a directed set; the proof uses only that $\\otimes$ commutes with colimits and that filtered colimits of modules are exact, Lemma Tag 00DB lemma-directed-colimit-exact; a filtered index category reduces to a directed set by Categories Lemma Tag 0032 categories-lemma-directed-category-system); cited in more-algebra.tex, proof of Lemma Tag 0AGV (line 3142)"
+++
Let $\mathcal I$ be a small filtered category (for instance a directed set) and $i\mapsto R_i$ a functor from $\mathcal I$ to commutative rings with colimit $R=\varinjlim_iR_i$ `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)) and coprojections $\iota_i:R_i\to R$. Let $\psi:R\to S$ be a ring map of commutative rings such that for every object $i$ the composite $\psi\circ\iota_i:R_i\to S$ is flat `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)). Then $\psi$ is flat.
