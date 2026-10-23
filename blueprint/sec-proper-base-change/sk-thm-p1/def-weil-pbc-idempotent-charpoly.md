+++
id = "def-weil-pbc-idempotent-charpoly"
kind = "definition"
title = "Determinant polynomial of an idempotent summand"
lean = ["Matrix.idempotentCharpoly"]
order = 1651
+++
Let $A$ be a commutative ring and $T,P$ square matrices over $A$ indexed by a finite set $J$. Define $D(T,P)=\det(1-C(P)+(X\cdot1-C(T))C(P))\in A[X]$, where $C$ applies the constant-polynomial map $A\to A[X]$ entrywise; $X\cdot1-C(T)$ is the characteristic matrix of $T$, whose determinant is the characteristic polynomial of $T$. The formula is defined for arbitrary $T,P$, without idempotence or commutation hypotheses.
