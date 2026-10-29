+++
id = "lem-sc-divisible-quotient-torsion"
kind = "lemma"
title = "Torsion in a quotient of a divisible group"
lean = ["AddSubgroup.exists_exact_torsionBy_quotient"]
order = 1523
+++
Let $G$ be an abelian group, $\Lambda\subseteq G$ a subgroup,
and $n\in\mathbf Z$. Assume multiplication by $n$ on $G$ is
surjective. Then there is a short exact sequence

$$
0\longrightarrow G[n]/\Lambda[n]
\longrightarrow (G/\Lambda)[n]
\xrightarrow{\delta}\Lambda/n\Lambda\longrightarrow0,
\qquad \delta(g+\Lambda)=ng+n\Lambda.
$$
