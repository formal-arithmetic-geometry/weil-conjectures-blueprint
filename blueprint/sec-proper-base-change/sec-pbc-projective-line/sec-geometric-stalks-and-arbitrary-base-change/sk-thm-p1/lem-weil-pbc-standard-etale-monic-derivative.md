+++
id = "lem-weil-pbc-standard-etale-monic-derivative"
kind = "lemma"
title = "The standard etale algebra of a monic polynomial localized at its derivative"
uses = ["def-weil-etale-morphism"]
lean = ["Polynomial.Monic.standardEtalePair", "StandardEtalePair.Ring", "Algebra.Etale", "StandardEtalePair.homEquiv"]
order = 2025
tags = ["mathlib", "stacks-00UB"]
+++
Let $S$ be a commutative ring, $Q\in S[T ]$ a monic polynomial with derivative $Q'$, and $S'=S[T ][Y ]/(Q,\,YQ'-1)$ (that is, $S[T ]_{Q'}/(Q)$), with $x\in S'$ the class of $T$. Then (1) $\operatorname{Spec}S'\to\operatorname{Spec}S$ is etale [def-weil-etale-morphism]; (2) for every $S$-algebra $L$ and every $b\in L$ with $Q(b)=0$ and $Q'(b)$ a unit of $L$ there is exactly one $S$-algebra map $S'\to L$ sending $x$ to $b$.
