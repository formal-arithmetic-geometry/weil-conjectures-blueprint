+++
id = "lem-weil-pbc-finite-over-complete-ring"
kind = "lemma"
title = "A Hausdorff module over a complete ring that is finite modulo the ideal is finite"
lean = ["Module.finite_and_span_eq_top_of_adicComplete"]
+++
Let $A$ be a commutative ring, $I\subseteq A$ an ideal and $M$ an $A$-module. Assume (1) $A$ is $I$-adically complete `IsAdicComplete` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean)); (2) $\bigcap_{n\ge1}I^nM=0$; (3) $M/IM$ is a finitely generated $A/I$-module. Then $M$ is a finitely generated $A$-module `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)); more precisely, any $x_1,\dots,x_r\in M$ whose images generate $M/IM$ over $A/I$ generate $M$ over $A$.
