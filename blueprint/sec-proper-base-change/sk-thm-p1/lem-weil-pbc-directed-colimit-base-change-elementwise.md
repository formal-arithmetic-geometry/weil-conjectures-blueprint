+++
id = "lem-weil-pbc-directed-colimit-base-change-elementwise"
kind = "lemma"
title = "Base change along a directed colimit of rings: elements and zero elements come from a stage"
lean = ["TensorProduct.directedColimitBaseChangeElementwise"]
+++
Let $I$ be a directed set, $(A_i,\alpha_{i'i}:A_i\to A_{i'})_{i\le i'}$ a directed system of commutative rings with colimit $A=\varinjlim_iA_i$ in the category of commutative rings `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)) and coprojections $\alpha_i:A_i\to A$. Let $0\in I$ and $M_0$ an $A_0$-module. For $i\ge0$ regard $A_i$ as an $A_0$-algebra via $\alpha_{i0}$ and $A$ via $\alpha_0$, and put $M_i=A_i\otimes_{A_0}M_0$, $M=A\otimes_{A_0}M_0$, with the maps $\mu_{i'i}=\alpha_{i'i}\otimes\mathrm{id}:M_i\to M_{i'}$ ($0\le i\le i'$) and $\mu_i=\alpha_i\otimes\mathrm{id}:M_i\to M$. Then (1) every element of $M$ is $\mu_i(t)$ for some $i\ge0$ and some $t\in M_i$; (2) if $t\in M_i$ satisfies $\mu_i(t)=0$, then $\mu_{i'i}(t)=0$ for some $i'\ge i$. (Equivalently, $M$ with the maps $\mu_i$ is the colimit of the directed system $(M_i,\mu_{i'i})_{i\ge0}$ of $A_0$-modules.)
