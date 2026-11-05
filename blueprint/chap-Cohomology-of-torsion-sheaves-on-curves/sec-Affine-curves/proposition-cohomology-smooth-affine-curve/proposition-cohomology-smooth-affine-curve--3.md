+++
id = "proposition-cohomology-smooth-affine-curve--3"
kind = "proposition"
title = "Order of the first cohomology group"
name_showing = false
order = 1579003
aliases = ["bp-r493-3"]
lean = ["AlgebraicGeometry.IsConnectedCurve.natCard_sheafH_one_constantZMod_mul"]
uses = ["definition-compactification-refinement", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image"]
+++
Let $U$ be a smooth affine connected curve over an algebraically closed
field $k$, and let $U\hookrightarrow\overline C$ be a smooth proper
connected compactification of genus $g$. Write $D$ for the set of closed
points of $\overline C$ outside $U$, and let $n\geq1$ be invertible in $k$.
Then $H^1(U,\mathbf Z/n)$ is finite and

$$
\#H^1(U,\mathbf Z/n)\,n=n^{\#D+2g}.
$$

Since $D$ is nonempty, its order is $n^{2g+\#D-1}$. This is the
cardinality statement used by Lean; no isomorphism with a free
$\mathbf Z/n$-module is asserted here.
