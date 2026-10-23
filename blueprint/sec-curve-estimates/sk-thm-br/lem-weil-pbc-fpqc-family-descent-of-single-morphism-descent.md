+++
id = "lem-weil-pbc-fpqc-family-descent-of-single-morphism-descent"
kind = "lemma"
title = "Fpqc family descent from single-morphism descent (proved source-library tool)"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.Scheme.of_isPullback_of_ofArrows_mem_fpqcTopology"]
order = 1395
+++
Let $P$ be a property of morphisms of schemes [def-pc-scheme], Zariski local on the target, stable under arbitrary base change, and descending along surjective flat quasi-compact morphisms. Let $f:Z\to T$ and let $\{g_i:T_i\to T\}_{i\in I}$ generate a covering sieve for the fpqc topology. For each $i$ let $a_i:Z_i\to Z$ and $b_i:Z_i\to T_i$ form a cartesian square with $f,g_i$. If $P(b_i)$ for all $i$, then $P(f)$.
