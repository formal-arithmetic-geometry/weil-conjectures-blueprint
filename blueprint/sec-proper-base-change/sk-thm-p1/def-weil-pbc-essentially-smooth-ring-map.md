+++
id = "def-weil-pbc-essentially-smooth-ring-map"
kind = "definition"
title = "Essentially smooth ring maps"
lean = ["Algebra.EssentiallySmooth"]
order = 1742
uses = ["def-sbc-smooth-morphisms"]
+++
Let $R$ be a commutative ring. For a commutative $R$-algebra $P$ and a multiplicative subset $S\subseteq P$ ($1\in S$, $st\in S$ for $s,t\in S$) let $S^{-1}P$ be the ring of fractions $a/s$ ($a\in P$, $s\in S$; $a/s=a'/s'$ iff $u(as'-a's)=0$ for some $u\in S$; $a/s+a'/s'=(as'+a's)/ss'$, $(a/s)(a'/s')=aa'/ss'$), an $R$-algebra through $R\to P\to S^{-1}P$, $a\mapsto a/1$. A homomorphism of commutative rings $R\to D$ (equivalently, the $R$-algebra $D$) is *essentially smooth* if there are a smooth $R$-algebra $P$ [def-sbc-smooth-morphisms], a multiplicative subset $S\subseteq P$ and an isomorphism of $R$-algebras $D\cong S^{-1}P$.
