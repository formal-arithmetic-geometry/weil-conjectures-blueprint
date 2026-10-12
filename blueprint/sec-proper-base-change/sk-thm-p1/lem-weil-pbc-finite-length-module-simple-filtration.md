+++
id = "lem-weil-pbc-finite-length-module-simple-filtration"
kind = "lemma"
title = "A finite-length module has a filtration with simple quotients"
lean = ["Module.exists_simple_filtration_of_length_lt_top"]
source = "literature/stacks-project/algebra.tex, Algebra, Definition Tag 02LY (definition-length, line 12350), Definition Tag 00J1 (definition-simple-module, line 12508) and Lemma Tag 00J3 (lemma-simple-pieces, line 12546, part (2) and the first sentence of its proof): a maximal chain in a finite-length module has simple successive quotients"
+++
Let $R$ be a commutative ring and $M$ an $R$-module of finite length, i.e. $\mathrm{length}_R(M)<\infty$ `Module.length` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Length.lean)). Then there are an integer $r\ge0$ and $R$-submodules $0=M_0\subsetneq M_1\subsetneq\cdots\subsetneq M_r=M$ such that each quotient $M_i/M_{i-1}$ ($1\le i\le r$) is simple `IsSimpleModule` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/SimpleModule/Basic.lean)): it is nonzero and has no $R$-submodule other than $0$ and itself.
