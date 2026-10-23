+++
id = "aux-directed-colimit-map"
kind = "lemma"
title = "Canonical section maps for directed colimits"
lean = ["CategoryTheory.Limits.colimit.post", "CategoryTheory.Limits.colimit.ι_post"]
order = 1619
+++
Let $D:J\to\mathcal C$ be a diagram admitting a colimit and let $G:\mathcal C\to\mathcal D$ be a functor such that
$G\circ D$ admits a colimit. There is a canonical morphism

$$
\operatorname{colim}_{j}G(D_j)\longrightarrow G\bigl(\operatorname{colim}_jD_j\bigr)
$$

whose composite with the $j$-th coprojection of $\operatorname{colim}_jG(D_j)$ is $G$ applied to the $j$-th
coprojection $D_j\to\operatorname{colim}_jD_j$, for every $j\in J$. In particular, for a diagram $D$ of sheaves on
a topological space $X$ and an open $U\subseteq X$, taking $G$ to be the sections over $U$ gives a canonical map
$\operatorname{colim}_jD_j(U)\to(\operatorname{colim}_jD_j)(U)$ sending the class of $s\in D_j(U)$ to the image of
$s$ under the $U$-component of the $j$-th coprojection.
