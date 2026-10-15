+++
id = "sk-def-nagata-sketch-data"
kind = "definition"
title = "Compactification and refinement"
order = 1
lean = ["AlgebraicGeometry.Compactification", "AlgebraicGeometry.IsSchemeTheoreticallyDominant", "AlgebraicGeometry.IsAdmissible"]
tags = ["sketch"]
+++
Let $f:X\to S$ be a morphism. A *compactification* is a factorization

$$
X\xrightarrow{j}\overline X\xrightarrow{p}S
$$

with $j$ a quasi-compact open immersion and $p$ proper. It is *dense* if
$j$ is scheme-theoretically dense: the map
$\mathcal O_{\overline X}\to j_*\mathcal O_X$ is injective.
A *refinement* of compactifications is an $S$-morphism
$h:\overline X'\to\overline X$ with $hj'=j$ and $h^{-1}(X)=X$, under the
specified identifications with $X$.
