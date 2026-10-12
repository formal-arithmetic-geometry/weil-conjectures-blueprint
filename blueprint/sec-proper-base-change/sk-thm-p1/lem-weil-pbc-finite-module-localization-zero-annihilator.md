+++
id = "lem-weil-pbc-finite-module-localization-zero-annihilator"
kind = "lemma"
title = "A finite module killed elementwise by a multiplicative set is killed by one element of it"
lean = ["Module.exists_annihilator_of_subsingleton_localizedModule"]
source = "literature/stacks-project/exercises.tex, Exercises, Exercise 076A (exercise-localize-finite-module-zero, line 745: finite M with S^{-1}M=0 has f in S with M_f=0; the form sM=0 is the one used in the proof of Smoothing Ring Maps, Lemma 07FC, smoothing.tex line 2301: 'Hence we can find an s in S such that s annihilates Q'). Tag verified in tags/tags: 076A,exercises-exercise-localize-finite-module-zero"
+++
Let $A$ be a commutative ring, $S\subseteq A$ a multiplicative subset and $M$ a finitely generated $A$-module `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)) such that $S^{-1}M=0$ `LocalizedModule` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Module/LocalizedModule/Basic.lean)), i.e. for every $m\in M$ there is $t\in S$ with $tm=0$. Then there is $s\in S$ with $sM=0$ (that is, $sm=0$ for all $m\in M$).
