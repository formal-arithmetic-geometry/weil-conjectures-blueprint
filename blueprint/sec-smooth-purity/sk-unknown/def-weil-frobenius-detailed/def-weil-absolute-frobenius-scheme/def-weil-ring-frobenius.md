+++
id = "def-weil-ring-frobenius"
kind = "definition"
title = "Frobenius endomorphism of a ring of characteristic p and its iterates"
refines = "def-weil-absolute-frobenius-scheme"
lean = ["frobenius, iterateFrobenius"]
tags = ["sheaf-dag", "mathlib", "stacks-0CC6"]
+++
Let $p$ be a prime number and $A$ a commutative ring in which $p\cdot1=0$. The *Frobenius endomorphism* of $A$ is the map $F_A:A\to A$, $a\mapsto a^p$; it is a ring homomorphism ($F_A(1)=1$, $F_A(ab)=F_A(a)F_A(b)$, and $(a+b)^p=a^p+b^p$ because the binomial coefficients $\binom pi$, $0<i<p$, are divisible by $p$). For $n\geq0$ its $n$-fold iterate is the ring endomorphism $F_A^n:a\mapsto a^{p^n}$. Every ring homomorphism $\varphi:A\to B$ between such rings satisfies $\varphi\circ F_A=F_B\circ\varphi$.
