+++
id = "lem-weil-pbc-etale-cover-geometric-point-lift"
kind = "lemma"
title = "A geometric point lifts to some member of a jointly surjective etale family"
order = 1078
uses = ["def-pc-scheme", "def-weil-etale-morphism", "def-weil-geometric-point"]
lean = ["AlgebraicGeometry.Scheme.exists_fac_of_etale_of_isSepClosed"]
tags = ["mathlib", "stacks-03PR"]
+++
Let $T$ be a scheme [def-pc-scheme], let $(t_i:T_i\to T)_{i\in I}$ be a family of etale morphisms [def-weil-etale-morphism] which is jointly surjective (every point of $T$ lies in the image of some $t_i$), and let $\bar t:\operatorname{Spec}\Omega\to T$ be a geometric point of $T$ [def-weil-geometric-point] lying over $t\in T$. Then there are $i\in I$ and a geometric point $\bar s:\operatorname{Spec}\Omega\to T_i$ (with the same field $\Omega$) such that $t_i\circ\bar s=\bar t$. More precisely, for every $i$ and every $s\in T_i$ with $t_i(s)=t$ there is such an $\bar s$ lying over $s$.
