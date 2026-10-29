+++
id = "def-sc-genus"
kind = "definition"
title = "The genus of a curve"
lean = ["AlgebraicGeometry.Scheme.Hom.genus", "AlgebraicGeometry.Scheme.genus_eq_arithmeticGenus", "AlgebraicGeometry.Scheme.finiteDimensional_H_relativeDifferentials"]
order = 615
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

For a smooth separated connected curve $C$ that is not proper, one uses
instead the genus $g(\overline C)$ of a chosen compactification
$\overline C$ of $C$, i.e. of a proper smooth connected curve containing
$C$ as an open subscheme with finite complement.
