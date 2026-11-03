+++
id = "def-weil-pbc-complete-intersection-over-field"
kind = "definition"
title = "Global and local complete intersections over a field"
lean = ["Algebra.IsGlobalCompleteIntersection", "Algebra.IsLocalCompleteIntersection"]
order = 1737
+++
Let $k$ be a field. For a commutative ring $T$ and $g\in T$ let $T_g=T[1/g]$ be the localization of $T$ at the multiplicative subset $\{1,g,g^2,\dots\}$, a $k$-algebra when $T$ is; let $\dim T$ be the Krull dimension of the topological space $\operatorname{Spec}T$ (so $\dim T=-\infty$ iff $T=0$), and $D(g)=\{\mathfrak q\in\operatorname{Spec}T:g\notin\mathfrak q\}$. (1) A commutative $k$-algebra $T$ is a *global complete intersection over $k$* if $T=0$, or if there are integers $0\le c\le n$, polynomials $f_1,\dots,f_c\in k[x_1,\dots,x_n]$ and an isomorphism of $k$-algebras $k[x_1,\dots,x_n]/(f_1,\dots,f_c)\cong T$ such that $\dim T=n-c$. (Such a $T$ is in particular a finitely generated $k$-algebra; the convention that the zero ring is a global complete intersection is part of the definition, Stacks Project, Tag 00S9.) (2) Let $S$ be a finitely generated $k$-algebra. $S$ is a *local complete intersection over $k$* if there is a set $\Sigma\subseteq S$ such that $\operatorname{Spec}S=\bigcup_{g\in\Sigma}D(g)$ and each $S_g$, $g\in\Sigma$, is a global complete intersection over $k$ in the sense of (1).
