+++
id = "lem-weil-pbc-noether-normalization-over-domain"
kind = "lemma"
title = "Noether normalization over a domain, up to inverting one nonzero element"
lean = ["Algebra.FiniteType.exists_finite_subalgebra_away"]
order = 1899
+++
Let $R$ be an integral domain and $R\to S$ an injective ring map of finite type. For an $R$-algebra $T$ and $f\in R$ write $T_f$ for the ring of fractions $t/f^n$ ($t\in T$, $n\ge0$; $t/f^n=t'/f^m$ iff $f^u(tf^m-t'f^n)=0$ in $T$ for some $u\ge0$). Then there are an integer $d\ge0$, elements $y_1,\ldots,y_d\in S$ and an $R$-subalgebra $S'\subseteq S$ such that: (1) the $R$-algebra map $R[Y_1,\ldots,Y_d]\to S$, $Y_i\mapsto y_i$, from the polynomial ring is injective and its image $R[y_1,\ldots,y_d]$ is contained in $S'$; (2) $S'$ is a finitely generated $R[y_1,\ldots,y_d]$-module; (3) there is a nonzero $f\in R$ such that the map $S'_f\to S_f$, $s/f^n\mapsto s/f^n$, induced by the inclusion is bijective.
