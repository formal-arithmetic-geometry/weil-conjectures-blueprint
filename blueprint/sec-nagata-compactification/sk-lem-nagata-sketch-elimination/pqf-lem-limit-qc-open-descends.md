+++
id = "pqf-lem-limit-qc-open-descends"
kind = "lemma"
title = "Quasi-compact opens of a filtered limit descend"
lean = ["AlgebraicGeometry.Scheme.exists_preimage_eq_and_isLimit_opensCone", "AlgebraicGeometry.Scheme.exists_map_preimage_eq_map_preimage_of_isLimit"]
order = 304
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $S=\varprojlim_{i\in I}S_i$ be a filtered limit of
schemes with affine transition morphisms
$f_{i'i}:S_{i'}\to S_i$, with projections $f_i:S\to S_i$, and let
$V\subset S$ be a quasi-compact open subscheme. No quasi-compactness or
quasi-separatedness of the $S_i$ is needed.

1. There are an index $i$ and a quasi-compact open
$V_i\subset S_i$ with $f_i^{-1}(V_i)=V$.
1. If $V_i\subset S_i$ and $V_{i'}\subset S_{i'}$ are
quasi-compact opens with $f_i^{-1}(V_i)=f_{i'}^{-1}(V_{i'})$,
then $f_{i''i}^{-1}(V_i)=f_{i''i'}^{-1}(V_{i'})$ for some index
$i''\ge i,i'$.
1. In the situation of (1) let $V_j\subset S_j$ be the preimage of
$V_i$ for $j\ge i$. Then the projections exhibit $V$ as the
filtered limit $\varprojlim_{j\ge i}V_j$; each $V_j$ is
quasi-compact, and the transition morphisms $V_{j'}\to V_j$ are
affine.
