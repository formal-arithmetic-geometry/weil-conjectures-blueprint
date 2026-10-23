+++
id = "lem-weil-pbc-etale-locally-standard"
kind = "lemma"
title = "Etale algebras are Zariski-locally standard etale (Stacks 00UE)"
uses = ["def-weil-etale-morphism"]
lean = ["Algebra.IsEtaleAt.exists_isStandardEtale"]
order = 1732
tags = ["mathlib", "stacks-00UE"]
+++
For a commutative ring $S$, a monic $f\in S[t ]$ and $h\in S[t ]$ such that $f'p_1+fp_2=h^n$ in $S[t ]$ for some $p_1,p_2\in S[t ]$ and $n\ge0$ (equivalently: $f'$ is invertible in $S[t ]_h/(f)$), write $C(f,h)=S[t ][Y ]/(f,\,Yh-1)$ ($=S[t ]_h/(f)$, the *standard étale algebra* of the pair $(f,h)$) and $x\in C(f,h)$ for the class of $t$. Let $S\to B$ be a ring map making $B$ a finitely presented $S$-algebra, and let $\mathfrak q\subset B$ be a prime ideal at which $B$ is étale over $S$, i.e. such that the local ring $B_{\mathfrak q}$ is formally étale over $S$ (this holds for every $\mathfrak q$ when $\operatorname{Spec}B\to\operatorname{Spec}S$ is étale [def-weil-etale-morphism]). Then there exist $g\in B\setminus\mathfrak q$, a monic $f\in S[t ]$, an $h\in S[t ]$ with $f'p_1+fp_2=h^n$ for some $p_1,p_2\in S[t ]$, $n\ge0$, and an isomorphism of $S$-algebras $B_g\cong C(f,h)$.
