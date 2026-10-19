+++
id = "det-nagata-common-modification-dense"
kind = "lemma"
title = "Density of the common open in a common modification"
lean = ["AlgebraicGeometry.CommonModification.dense_range_j_of_qcqs", "AlgebraicGeometry.CommonModification.isSchemeTheoreticallyDominant_j"]
uses = ["def-nagata-common-modification"]
+++
Let $s_i\colon T_i\to S$ ($i=1,2$) be morphisms of schemes, let
$j_i\colon U\hookrightarrow T_i$ be open immersions, and let
$(\pi_i:T_i'\to T_i,\ w:T\to S,\ k_i:T_i'\to T,\ u_i:U\to T_i')$ be a common
modification of $T_1,T_2$ along $U$ ([def-nagata-common-modification]); put
$j=k_1u_1=k_2u_2:U\to T$.

1. If $T_1,T_2$ are quasi-compact and quasi-separated and $j_i(U)$ is
   topologically dense in $T_i$ for $i=1,2$, then $j(U)$ is dense in $T$.
1. If $j_1,j_2$ are quasi-compact and $j_i(U)$ is scheme-theoretically dense
   in $T_i$ for $i=1,2$, then $j(U)$ is scheme-theoretically dense in $T$.
