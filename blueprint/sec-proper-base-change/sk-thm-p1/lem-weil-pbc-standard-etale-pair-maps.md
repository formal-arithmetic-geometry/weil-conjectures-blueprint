+++
id = "lem-weil-pbc-standard-etale-pair-maps"
kind = "lemma"
title = "Maps out of a standard etale algebra are roots f(b)=0 with h(b) a unit"
lean = ["StandardEtalePair.homEquiv"]
order = 2026
tags = ["mathlib", "stacks-00UB"]
+++
For a commutative ring $S$, a monic $f\in S[t ]$ and $h\in S[t ]$ such that $f'p_1+fp_2=h^n$ in $S[t ]$ for some $p_1,p_2\in S[t ]$ and $n\ge0$ (equivalently: $f'$ is invertible in $S[t ]_h/(f)$), write $C(f,h)=S[t ][Y ]/(f,\,Yh-1)$ ($=S[t ]_h/(f)$, the *standard etale algebra* of the pair $(f,h)$, Stacks Definition Tag 00UB) and $x\in C(f,h)$ for the class of $t$. Then for every $S$-algebra $L$: (1) for every $b\in L$ with $f(b)=0$ and $h(b)$ a unit of $L$ there is exactly one $S$-algebra map $\chi:C(f,h)\to L$ with $\chi(x)=b$; (2) every $S$-algebra map $\chi:C(f,h)\to L$ satisfies $f(\chi(x))=0$ and $h(\chi(x))\in L^\times$, and is determined by $\chi(x)$.
