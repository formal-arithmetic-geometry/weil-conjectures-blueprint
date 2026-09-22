+++
id = "lem-sc-affine-open-proper"
kind = "lemma"
title = "Open subschemes of a proper curve"
order = 3631
lean = ["AlgebraicGeometry.Curve.isAffine_of_isOpenImmersion_of_compl_nonempty"]
uses = ["def-sc-effective-cartier-divisor", "def-sc-divisor", "lem-sc-point-cartier", "lem-sc-deg-principal-zero", "lem-sc-positive-degree-ample", "lem-sc-ample-complement-affine"]
+++
Let $k$ be algebraically closed, let $\overline C$ be a proper smooth curve
over $k$, and let $j:U\hookrightarrow\overline C$ be an open immersion with
$\overline C\setminus U\neq\emptyset$. Then $U$ is affine.

## Proof

The complement $S:=\overline C\setminus U$ is a nonempty closed subset of
dimension at most zero, hence a finite nonempty set of closed points, and
$U=\overline C\setminus S$. By [lem-sc-point-cartier] each $P\in S$ is an
effective Cartier divisor, so $D:=\sum_{P\in S}[P]$ is an effective Cartier
divisor with support $S$ [def-sc-effective-cartier-divisor]; its degree is
$\deg D=|S|\geq1$ [def-sc-divisor], and $\deg\mathcal O(D)=\deg D>0$ by the
well-definedness of the degree on $\operatorname{Pic}$
[lem-sc-deg-principal-zero], so $\mathcal O(D)$ is ample by
[lem-sc-positive-degree-ample]. By [lem-sc-ample-complement-affine],
$U=\overline C\setminus D$ is affine.

Unresolved dependencies: def:sc-curves, lem:sc-dim0-finite
