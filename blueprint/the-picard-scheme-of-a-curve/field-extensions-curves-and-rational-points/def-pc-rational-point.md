+++
id = "def-pc-rational-point"
kind = "definition"
title = "Rational points"
order = 4220
lean = ["AlgebraicGeometry.Scheme.rationalPoint"]
uses = ["def-pc-scheme", "def-pc-base-change"]
+++
Let $k$ be a field and $X$ a scheme over $k$. A *$k$-rational point* of $X$
is a section $\sigma:\operatorname{Spec}(k)\to X$ of the structure
morphism; for a scheme $T$ over $k$ the induced section is
$\sigma_T:T\to X_T$ [def-pc-base-change].
