+++
id = "def-sc-general-curve"
kind = "definition"
title = "Curves over an arbitrary field"
order = 4505
lean = ["AlgebraicGeometry.Curve.IsGeometricallyIntegralSmoothProjective"]
+++
Let $k$ be a field. A *geometrically integral smooth projective curve over
$k$* is a scheme $C$ over $k$ which is smooth and projective over $k$ and
geometrically integral over $k$. Its *genus* is
$$
g(C):=\dim_kH^1(C,\mathcal O_C),
$$
finite because coherent cohomology of a proper scheme over a field is
finite-dimensional, and invariant under base change, $g(C_{k'})=g(C)$ for
every field extension $k'/k$, by flat base change.

For an algebraically closed extension $k'/k$ the base change $C_{k'}$ is a
proper smooth curve in the sense of the algebraically closed conventions of
the smooth-curve chapter, and $g(C)=g(C_{k'})$ with the genus of that
chapter; in particular the degree and $\operatorname{Pic}^0$ conventions
apply to $C_{k'}$. The statements of the present chapter that are formulated
over an arbitrary field use this definition; the algebraically closed
statements use the smooth-curve chapter's convention.

Unresolved dependencies: def:pc-smooth-projective-curve, def:pc-geometrically-irreducible, def:pc-base-change, def:sc-curves, def:sc-genus, def:sc-pic0
