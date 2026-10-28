+++
id = "lem-weil-pbc-derivation-extends"
kind = "lemma"
title = "A derivation extends to adic completions and to localizations"
lean = ["Derivation.exists_completion_and_unique_localization"]
order = 1819
+++
Let $R$ be a commutative ring and $D:R\to R$ a derivation, i.e. an additive map with $D(ab)=aD(b)+bD(a)$ for all $a,b\in R$. (1) Let $I\subseteq R$ be an ideal, $R^\wedge=\varprojlim_{n\geq1}R/I^n$ the $I$-adic completion and $c:R\to R^\wedge$ the canonical map. Then there is a derivation $D^\wedge:R^\wedge\to R^\wedge$ with $D^\wedge\circ c=c\circ D$; it is induced by the maps $D_n:R/I^{n+1}\to R/I^n$, $a\bmod I^{n+1}\mapsto D(a)\bmod I^n$ (well defined since $D(I^{n+1})\subseteq I^n$), namely $D^\wedge((x_n)_{n\geq1})=(D_n(x_{n+1}))_{n\geq1}$. (2) Let $W\subseteq R$ be a multiplicative subset ($1\in W$, $vw\in W$ for $v,w\in W$), $W^{-1}R$ the ring of fractions $a/w$ ($a\in R$, $w\in W$; $a/w=a'/w'$ iff $u(aw'-a'w)=0$ for some $u\in W$; $a/w+b/v=(av+bw)/wv$, $(a/w)(b/v)=ab/wv$) and $\lambda:R\to W^{-1}R$, $a\mapsto a/1$, the localization map. Then there is a unique derivation $D_W:W^{-1}R\to W^{-1}R$ with $D_W\circ\lambda=\lambda\circ D$, namely $D_W(a/w)=D(a)/w-aD(w)/w^2$.
