+++
id = "lemma-separation-closures--1"
kind = "lemma"
title = "Separation with quasi-compact complements"
order = 1453001
aliases = ["bp-r452-1"]
lean = ["AlgebraicGeometry.exists_admissibleBlowup_disjoint_closures"]
uses = ["definition-admissible-blow-up--1"]
+++
Let $T$ be qcqs and let $j:V\hookrightarrow T$ be a quasi-compact open.
Let $F_1,F_2\subseteq V$ be disjoint closed subsets such that
$V\setminus F_1$ and $V\setminus F_2$ are quasi-compact. There is a
$V$-admissible blow-up $b:T'\to T$ such that

$$
\overline{b^{-1}(j(F_1))}\cap
\overline{b^{-1}(j(F_2))}=\varnothing,
$$

where the closures are taken in $T'$. Since $V$ is spectral, the
quasi-compactness of these complements is equivalent to the
constructibility of the closed subsets $F_i$.
