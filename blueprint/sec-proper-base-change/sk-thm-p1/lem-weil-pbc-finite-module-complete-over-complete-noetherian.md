+++
id = "lem-weil-pbc-finite-module-complete-over-complete-noetherian"
kind = "lemma"
title = "A finite module over a Noetherian ring complete along an ideal is complete"
lean = ["finite_module_complete_over_complete_noetherian"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma 00MA (lemma-completion-tensor) (3): N^ = N (x)_R R^, applied with R -> R^ bijective; equivalently Lemma 031B (lemma-when-finite-module-complete-over-complete-ring) with the Krull intersection theorem (Lemma 00IP, lemma-intersect-powers-ideal-module-zero) for J in the Jacobson radical (Lemma 05GI)"
+++
Let $R$ be a Noetherian ring `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)) and $J\subseteq R$ an ideal such that $R$ is $J$-adically complete `IsAdicComplete` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean)). Let $N$ be a finitely generated $R$-module `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)). Then $N$ is $J$-adically complete: the canonical $R$-linear map $N\to\varprojlim_nN/J^nN$, $x\mapsto(x\bmod J^nN)_n$, into the module of compatible sequences is bijective.
