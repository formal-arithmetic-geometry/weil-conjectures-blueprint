+++
id = "lemma-gluing-after-admissible-blow-ups--1"
kind = "lemma"
title = "Common modification and density"
name_showing = false
order = 1455001
aliases = ["bp-r454-1"]
lean = ["AlgebraicGeometry.nonempty_commonModification", "AlgebraicGeometry.CommonModification.dense_range_j"]
uses = ["definition-admissible-blow-up"]
+++
Let $S$ be qcqs, let $s_i:T_i\to S$ ($i=1,2$) be separated and of
finite type, and let $j_i:U\to T_i$ be quasi-compact open immersions
such that $s_1j_1=s_2j_2$.
There are $U$-admissible blow-ups $b_i:T_i'\to T_i$, a separated
morphism $t:T\to S$ of finite type, and open immersions
$u_i:U\to T_i'$ and $k_i:T_i'\to T$ such that

$$
b_i u_i=j_i,\qquad t k_i=s_i b_i,\qquad
k_1u_1=k_2u_2,\qquad k_1(T_1')\cup k_2(T_2')=T.
$$

For any such common modification, if both $T_i$ are Noetherian and
$j_i(U)$ is dense in $T_i$, then the common open immersion
$j=k_1u_1=k_2u_2:U\to T$ has dense image.
