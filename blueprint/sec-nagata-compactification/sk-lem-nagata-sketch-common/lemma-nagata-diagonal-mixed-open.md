+++
id = "lemma-nagata-diagonal-mixed-open"
kind = "lemma"
title = "The diagonal on a mixed open"
order = 235
lean = ["AlgebraicGeometry.diagonalRestrictChartArrowIso"]
+++
Let $X$ be an $S$-scheme and let $U,V\subseteq X$ be open subschemes. The
restriction of $\Delta_{X/S}$ over the open $U\times_SV\subseteq X\times_SX$
is canonically isomorphic, as an arrow, to the map

$$
U\cap V\longrightarrow U\times_SV.
$$

The analogous assertion holds over $V\times_SU$.

## Proof

Both schemes represent triples consisting of a point of $U$, a point of
$V$, and an equality of their images in $X$. The canonical isomorphism is
obtained from the universal property of the pullback.
