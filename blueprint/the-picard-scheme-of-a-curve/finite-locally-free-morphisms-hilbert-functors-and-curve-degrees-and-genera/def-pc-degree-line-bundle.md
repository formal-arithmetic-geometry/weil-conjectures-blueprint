+++
id = "def-pc-degree-line-bundle"
kind = "definition"
title = "The degree of an invertible module"
order = 4254
lean = ["AlgebraicGeometry.degreeLineBundle"]
uses = ["def-pc-euler-characteristic", "def-pc-divisor-line-bundle"]
+++
Let $k$ be a field, $X$ a proper scheme over $k$ and $\mathcal{L}$ an
invertible $\mathcal{O}_X$-module. The *degree* of $\mathcal{L}$ is
$$
\deg(\mathcal{L}):=\chi(X,\mathcal{L})-\chi(X,\mathcal{O}_X)\in\Z
$$
(Varieties, Definition 33.44.1, [Tag
0AYR](https://stacks.math.columbia.edu/tag/0AYR)). For an effective
Cartier divisor $D$ on $X$ the degree of $D$ is
$\deg(D):=\deg(\mathcal{O}_X(D))$. That this agrees with the degree of the
curve-calculation chapter is [lem-pc-degree-agrees-sc], as
[rem-ptr-pc-degree-line-bundle-14] records.

Unresolved dependencies: def:sc-pic0, def:sc-divisor, def:sc-invertible-module
