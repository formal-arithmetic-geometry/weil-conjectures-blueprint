+++
id = "lem-sc-finite-extension-affine-model"
kind = "lemma"
title = "An affine curve model for a finite extension"
order = 4533
lean = ["AlgebraicGeometry.Curve.exists_affineModel_of_finiteExtension"]
uses = ["def-fin-normalization-extension", "lem-fin-normalization-extension-finite"]
+++
Let $C/k$ be a smooth integral affine curve over algebraically closed $k$,
and let $L/k(C)$ be finite. The normalization
[def-fin-normalization-extension] $h:C'\to C$ in $L$ is a finite morphism
from a smooth integral affine curve with function field $L$.

## Proof

By [lem-fin-normalization-extension-finite] the integral closure $B'$ of the
affine coordinate ring $B$ in $L$ is finite over $B$. It is a normal domain.
Every element of $L$ becomes integral over $B$ after multiplication by a
nonzero element of $B$, by clearing the coefficients of its algebraic
equation; hence $\operatorname{Frac}(B')=L$. The construction of
[def-fin-normalization-extension] gives $C'=\operatorname{Spec}B'$.

Integral extensions preserve dimension, so $C'$ has dimension one. Its local
rings at closed points are regular, since a one-dimensional normal local
ring is a discrete valuation ring; at the generic point its local ring is a
field. A regular scheme of finite type over the perfect field $k$ is smooth:
this last local algebra criterion is [Stacks Project, Tag
00TV](https://stacks.math.columbia.edu/tag/00TV), applied to its essentially
finite-type local rings. This proves the assertion.

Unresolved dependencies: def:sc-curves, def:sc-function-field, def:weil-pbc-scheme-conventions, lem:sc-normal-dim1-dvr
