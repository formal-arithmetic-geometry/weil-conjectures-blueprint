+++
id = "sbc-thm-algebraically-closed-invariance"
kind = "theorem"
title = "Invariance under extension of algebraically closed fields"
lean = ["AlgebraicGeometry.bijective_cohomologyMap_constantZMod_of_smoothOfRelativeDimension", "AlgebraicGeometry.bijective_cohomologyMap_constantZMod", "AlgebraicGeometry.IsConnectedCurve.constant_cohomology_baseChange_compatible"]
order = 2050
uses = ["def-weil-pbc-etale-cohomology", "def-weil-pbc-scheme-conventions", "thm-sc-constant-invariance", "thm-sc-proper-cohomology"]
+++
Let $k\subseteq k'$ be algebraically closed, let $C$ be a
smooth separated curve
over $k$, and let $d\geq1$ be prime to $\operatorname{char}k$. For
every $q\geq0$ the pullback map

$$
H^q(C_{\Et},\mathbf Z/d\mathbf Z)
\xrightarrow{\ \sim\ }H^q((C_{k'})_{\Et},\mathbf Z/d\mathbf Z)
$$

is an isomorphism. Moreover, for $C$ proper and connected the computation
of [thm-sc-proper-cohomology] is compatible with this extension of the base
field: the isomorphisms recorded there over $k$ and over $k'$ are matched by
these pullback maps, not merely abstractly isomorphic.
