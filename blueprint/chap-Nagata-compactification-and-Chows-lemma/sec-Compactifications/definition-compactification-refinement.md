+++
id = "definition-compactification-refinement"
kind = "definition"
title = "Compactification and refinement"
order = 1396
lean = ["AlgebraicGeometry.Compactification", "AlgebraicGeometry.Compactification.IsDense", "AlgebraicGeometry.isSchemeTheoreticallyDominant_iff_app_injective", "AlgebraicGeometry.Compactification.Refinement", "AlgebraicGeometry.Compactification.Refinement.IsStrict", "AlgebraicGeometry.Compactification.quasiCompact_openImmersion_iff"]
+++
Let $f:X\to S$ be a morphism. A compactification is a factorization

$$
X\xrightarrow{j}\overline X\xrightarrow{p}S
$$

with $j$ a quasi-compact open immersion and $p$ proper. We say that it is
*dense* if $j$ is scheme-theoretically dense, i.e., if the map
$\mathcal O_{\overline X}\to j_*\mathcal O_X$ is injective.
A refinement of compactifications is an $S$-morphism
$h:\overline X'\to\overline X$ with $hj'=j$ and
$h^{-1}(X)=X$, under the specified identifications with $X$.
