+++
id = "lem-weil-pbc-localization-of-regular-ring"
kind = "lemma"
title = "A localization of a regular ring is regular"
lean = ["RingTheory.isRegularRing_of_localization"]
order = 1865
+++
Let $R$ be a regular ring (Noetherian, with every localization at a prime ideal a regular local ring), let $M\subseteq R$ be a multiplicative subset ($1\in M$, $st\in M$ for $s,t\in M$), and let $\varphi:R\to R'$ be a homomorphism of commutative rings which is a localization of $R$ at $M$: (a) $\varphi(s)$ is a unit for every $s\in M$; (b) every element of $R'$ is $\varphi(r)\varphi(s)^{-1}$ with $r\in R$, $s\in M$; (c) $\varphi(r)=0$ implies $sr=0$ for some $s\in M$ (for instance $R'=M^{-1}R$). Then $R'$ is a regular ring.
