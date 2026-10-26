+++
id = "def-pc-genus"
kind = "definition"
title = "The genus of a curve"
lean = ["AlgebraicGeometry.Scheme.arithmeticGenus", "AlgebraicGeometry.Scheme.genus_eq_arithmeticGenus"]
order = 627
uses = ["def-pc-geometrically-irreducible", "def-pc-smooth-projective-curve", "def-sc-genus"]
+++
Let $k$ be a field and let $X$ be a proper scheme over $k$, typically a
smooth projective curve over
$k$ which is geometrically
irreducible. The *genus* (arithmetic genus) of $X$ is

$$
g(X):=\dim_kH^1(X,\mathcal{O}_X)\in\Z_{\geq0}
$$
