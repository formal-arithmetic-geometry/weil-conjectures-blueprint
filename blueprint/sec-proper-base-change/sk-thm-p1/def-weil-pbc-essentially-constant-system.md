+++
id = "def-weil-pbc-essentially-constant-system"
kind = "definition"
title = "Essentially constant inverse system of abelian groups (Stacks 05PU (2))"
lean = ["CategoryTheory.Functor.IsEssentiallyConstant", "CategoryTheory.Functor.IsEssentiallyConstantWithValue"]
order = 1613
+++
Let $(B_i)_{i\ge1}$ be an inverse system of abelian groups, with composite transition homomorphisms $B_k\to B_i$ for $k\ge i$. The system is *essentially constant with value $X$* if there are an abelian group $X$ with homomorphisms $\pi_i:X\to B_i$ compatible with the transition maps ($B_{i+1}\to B_i$ composed with $\pi_{i+1}$ is $\pi_i$), an index $i_0\ge1$ and a homomorphism $r:B_{i_0}\to X$ such that (a) $r\circ\pi_{i_0}=\mathrm{id}_X$, and (b) for every $j\ge1$ there is $k\ge\max(i_0,j)$ such that the transition map $B_k\to B_j$ equals the composite $\pi_j\circ r\circ(B_k\to B_{i_0})$. It is *essentially constant* if it is essentially constant with some value $X$.
