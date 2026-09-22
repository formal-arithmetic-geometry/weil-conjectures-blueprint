+++
id = "def-pc-genus"
kind = "definition"
title = "The genus of a curve"
order = 4255
lean = ["AlgebraicGeometry.Curve.genus"]
uses = ["def-pc-smooth-projective-curve", "def-pc-geometrically-irreducible", "lem-pc-genus-well-defined"]
+++
Let $k$ be a field and let $X$ be a smooth projective curve
[def-pc-smooth-projective-curve] over $k$ which is geometrically
irreducible [def-pc-geometrically-irreducible]. The *genus* of $X$ is
$$
g(X):=\dim_kH^1(X,\mathcal{O}_X)\in\Z_{\geq0}
$$
(Stacks Project, Picard Schemes of Curves, Definition 44.6.3, [Tag
0B9W](https://stacks.math.columbia.edu/tag/0B9W)). That the dimension is
finite is [lem-pc-genus-well-defined]; that it agrees with the genus of the
curve-calculation chapter is [lem-pc-genus-agrees-sc]; that it is invariant
under extension of the ground field is [lem-pc-genus-base-change], as
[rem-ptr-pc-genus-15] records.

Unresolved dependencies: def:sc-genus
