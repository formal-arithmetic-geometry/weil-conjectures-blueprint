+++
id = "lem-weil-pbc-associated-prime-power-quotient"
kind = "lemma"
title = "A prime minimal over an associated prime plus (x) is associated to M/x^nM for some n"
lean = ["Module.exists_mem_associatedPrimes_quotient_pow"]
order = 1794
+++
Let $(R,\mathfrak m)$ be a Noetherian local ring (a Noetherian commutative ring with exactly one maximal ideal $\mathfrak m$) and let $M$ be a finite $R$-module. An *associated prime* of an $R$-module $N$ is a prime ideal $\mathfrak p\subset R$ for which there is an element $z\in N$ with $\operatorname{Ann}_R(z):=\{a\in R: az=0\}=\mathfrak p$; $\operatorname{Ass}_R(N)$ is the set of them. Let $x\in\mathfrak m$, let $\mathfrak p\in\operatorname{Ass}_R(M)$, and let $\mathfrak q$ be a prime ideal of $R$ that is minimal over the ideal $\mathfrak p+(x)$ (that is, $\mathfrak p+(x)\subseteq\mathfrak q$ and no prime ideal $\mathfrak q'$ satisfies $\mathfrak p+(x)\subseteq\mathfrak q'\subsetneq\mathfrak q$). Then there is an integer $n\ge1$ with $\mathfrak q\in\operatorname{Ass}_R(M/x^nM)$, i.e. some $w\in M/x^nM$ has $\operatorname{Ann}_R(w)=\mathfrak q$.
