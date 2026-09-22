+++
id = "def-kun-dimension"
kind = "definition"
title = "Dimension"
order = 6014
lean = ["AlgebraicGeometry.Scheme.krullDim", "AlgebraicGeometry.Scheme.dimAt"]
uses = ["def-kun-support"]
+++
The *Krull dimension* $\dim X$ of a scheme is the supremum of the integers
$r$ such that there is a strict chain $Z_0\subsetneq\cdots\subsetneq Z_r$ of
nonempty irreducible closed subsets of $|X|$. For $x\in X$, the *dimension
at $x$* is
$$
\dim_xX=\min\{\dim U:x\in U\subseteq X\text{ open}\}.
$$

For a scheme $X$ of finite type over a field $K$ the finiteness
$\dim X<\infty$ is [lem-kun-dimension-finite-type], and the computation of
the dimension at a point $x\in X$ in terms of the transcendence degree of
[def-kun-support] is [lem-kun-dimension-formula].

Unresolved dependencies: def:weil-pbc-scheme-conventions
