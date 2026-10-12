+++
id = "def-weil-pbc-idempotent-charpoly"
kind = "definition"
title = "Determinant polynomial of an idempotent summand"
lean = ["Matrix.idempotentCharpoly"]
source = "literature/stacks-project/more-algebra.tex, Tag 09XI, lemma-characterize-henselian-pair, proof of (3) implies (1), splitting and characteristic-polynomial paragraphs; matrix formula and omitted details written out by G2"
+++
Let $A$ be a commutative ring and $T,P$ square matrices indexed by a finite set $J$. Define $D(T,P)=\det(1-C(P)+(X1-C(T))C(P))\in A[X]$, where $C$ applies the constant-polynomial map entrywise. The characteristic matrix $X1-C(T)$ is the one defining the free characteristic polynomial `Matrix.charpoly` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/Matrix/Charpoly/Basic.lean)). The formula is defined for arbitrary $T,P$, without idempotence or commutation hypotheses.
