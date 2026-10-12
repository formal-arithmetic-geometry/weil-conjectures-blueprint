+++
id = "def-sc-genus"
kind = "definition"
title = "The genus of a curve"
lean = ["AlgebraicGeometry.Scheme.Hom.genus"]
order = 429
uses = ["def-sc-curves"]
+++
Let $C$ be a proper smooth connected curve over
a field $k$. The *genus* of $C$ is

$$
g(C):=\dim_kH^0(C,\Omega^1_{C/k}),
$$

the $k$-dimension of the space of global sections of the sheaf of
relative differentials. Equivalently, by Serre duality,
$g(C)=\dim_kH^1(C,\mathcal O_C)$.

For a smooth separated, not necessarily proper, connected curve $C$ the
genus of $C$ is the genus of a compactification $\overline C$ of $C$, i.e.
of a proper smooth connected curve containing $C$ as an open subscheme
with finite complement.
