+++
id = "def-pc-degree-line-bundle"
kind = "definition"
title = "The degree of an invertible module"
lean = ["AlgebraicGeometry.Scheme.Modules.degree"]
order = 666
uses = ["def-sc-divisor", "def-sc-pic0"]
+++
Let $k$ be a field, $X$ a proper scheme over $k$ and $\mathcal{L}$ an
invertible $\mathcal{O}_X$-module. The
*degree* of $\mathcal{L}$ is

$$
\deg(\mathcal{L}):=\chi(X,\mathcal{L})-\chi(X,\mathcal{O}_X)\in\Z
$$

For an
effective Cartier divisor $D$ on $X$ the degree of $D$ is
$\deg(D):=\deg(\mathcal{O}_X(D))$.
