+++
id = "def-weil-compactifications-refinements"
kind = "definition"
title = "Compactifications and refinements"
order = 421
lean = ["AlgebraicGeometry.Compactification", "AlgebraicGeometry.Compactification.Refinement", "AlgebraicGeometry.Compactification.category"]
uses = ["def-weil-scheme-morphism-properties"]
+++
Let $f:X\to Y$ be a morphism of schemes (typically $X$ and $Y$ are
finite-type [def-weil-scheme-morphism-properties] schemes over a base $S$ and
$f$ is a separated finite-type $S$-morphism). A *compactification*
$c=(j,\bar f)$ of $f$ is a factorization

$$
 X\xrightarrow{j}\overline X\xrightarrow{\bar f}Y
$$

with $j$ an open immersion, $\bar f$ proper, and $\bar f\circ j=f$. A
*refinement* $u:c_1\to c_2$ is a $Y$-morphism

$$
 u:\overline X_1\longrightarrow\overline X_2
$$

such that $u\circ j_1=j_2$; it is automatically proper, since $\overline X_1$
is proper and $\overline X_2$ is separated over $Y$. Compactifications and
refinements, with composition of the underlying morphisms, form a category
$\operatorname{Comp}(f)$.
