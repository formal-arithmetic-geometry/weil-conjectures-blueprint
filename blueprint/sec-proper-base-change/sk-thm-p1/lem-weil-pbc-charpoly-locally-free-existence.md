+++
id = "lem-weil-pbc-charpoly-locally-free-existence"
kind = "lemma"
title = "Existence and uniqueness of the characteristic polynomial on a finite locally free module of constant rank"
lean = ["Algebra.charpoly_locallyFree_exists_unique"]
order = 1690
+++
Let $A$ be a commutative ring, $n\ge0$ an integer, $M$ an $A$-module and $\varphi:M\to M$ an $A$-linear map. Assume there are $f_1,\dots,f_r\in A$ generating the unit ideal such that for each $i$ the $A_{f_i}$-module $M_{f_i}$ is free of rank $n$. Then there is exactly one polynomial $\chi\in A[T]$ with the following property: for every ring map $A\to A'$ such that $M\otimes_AA'$ is a free $A'$-module of rank $n$, the image of $\chi$ in $A'[T]$ is the characteristic polynomial $\det(T\cdot1-\varphi_{A'})$ of $\varphi_{A'}=\varphi\otimes1$ on $M\otimes_AA'$ (computed in any basis). Moreover $\chi=T^n+c_{n-1}T^{n-1}+\dots+c_0$ with $c_k\in A$ (in particular $\chi$ is monic). In particular, if $M$ itself is free of rank $n$, then $\chi$ is the usual characteristic polynomial of $\varphi$.
