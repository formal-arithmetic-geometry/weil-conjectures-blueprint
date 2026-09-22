+++
id = "def-pc-dimension"
kind = "definition"
title = "Dimension"
order = 4206
lean = ["AlgebraicGeometry.Scheme.dim", "AlgebraicGeometry.Scheme.relativeDim"]
uses = ["def-pc-scheme", "def-pc-base-change"]
+++
The *dimension* $\dim X$ of a nonempty scheme $X$ is the supremum of the
Krull dimensions of the local rings of $X$, and the *relative dimension* of
a morphism $f:X\to S$ of finite type at a point $s\in S$ is $\dim X_s$ (the
dimension of the fibre); $f$ is *of relative dimension $d$* if all nonempty
fibres have dimension $d$.
