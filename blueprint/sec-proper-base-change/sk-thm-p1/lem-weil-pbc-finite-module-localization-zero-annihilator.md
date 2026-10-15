+++
id = "lem-weil-pbc-finite-module-localization-zero-annihilator"
kind = "lemma"
title = "A finite module killed elementwise by a multiplicative set is killed by one element of it"
lean = ["Module.exists_annihilator_of_subsingleton_localizedModule"]
+++
Let $A$ be a commutative ring, $S\subseteq A$ a multiplicative subset and $M$ a finitely generated $A$-module `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)) such that $S^{-1}M=0$ `LocalizedModule` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Module/LocalizedModule/Basic.lean)), i.e. for every $m\in M$ there is $t\in S$ with $tm=0$. Then there is $s\in S$ with $sM=0$ (that is, $sm=0$ for all $m\in M$).
