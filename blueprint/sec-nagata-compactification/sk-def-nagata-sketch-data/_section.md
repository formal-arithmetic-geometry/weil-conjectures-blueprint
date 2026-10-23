+++
id = "sk-def-nagata-sketch-data"
kind = "definition"
title = "Compactification and refinement"
order = 15
lean = ["AlgebraicGeometry.Compactification", "AlgebraicGeometry.Compactification.IsDense", "AlgebraicGeometry.IsSchemeTheoreticallyDominant", "AlgebraicGeometry.isSchemeTheoreticallyDominant_iff_app_injective", "AlgebraicGeometry.Compactification.Refinement", "AlgebraicGeometry.Compactification.Refinement.IsStrict"]
tags = ["sketch"]
+++
Let $f:X\to S$ be a morphism. A *compactification* is a factorization

$$
X\xrightarrow{j}\overline X\xrightarrow{p}S
$$

with $j$ an open immersion and $p$ proper. It is *dense* if $j$ is
scheme-theoretically dense: no nonzero quasi-coherent ideal of
$\mathcal O_{\overline X}$ lies in the kernel of
$\mathcal O_{\overline X}\to j_*\mathcal O_X$; for quasi-compact $j$ this
says that the map is injective.
A *refinement* of compactifications is an $S$-morphism
$h:\overline X'\to\overline X$ with $hj'=j$; it is *strict* if moreover
$h^{-1}(X)=X$, under the specified identifications with $X$.
