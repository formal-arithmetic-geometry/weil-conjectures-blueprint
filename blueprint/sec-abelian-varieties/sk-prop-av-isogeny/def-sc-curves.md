+++
id = "def-sc-curves"
kind = "definition"
title = "Curves over algebraically closed fields"
lean = ["AlgebraicGeometry.IsCurve", "AlgebraicGeometry.IsConnectedCurve", "AlgebraicGeometry.SmoothConnectedCurve"]
order = 477
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $k$ be a field (in this chapter $k$ is algebraically closed). A
*curve over $k$* is a separated scheme of finite
type over $k$ of dimension at most one; it is
*smooth* if it is smooth over $k$, *proper* if it is
proper over $k$, and *affine* if it is an affine scheme.
A *connected curve* is a curve that is nonempty, connected (as a
topological space) and of dimension one.
$\mathcal C$ denotes the category of smooth separated connected curves over
$k$.

A curve may be empty, disconnected, or have zero-dimensional components;
for instance $\Spec k$ is a curve but not a connected curve. A smooth
projective geometrically integral curve over an algebraically closed field
$k$ is a connected curve in the present sense.
