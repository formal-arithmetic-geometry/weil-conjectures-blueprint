+++
id = "def-sc-zariski-cohomology"
kind = "definition"
title = "Zariski sheaf cohomology"
lean = ["AlgebraicGeometry.Scheme.zariskiH"]
order = 2688
uses = ["def-sc-zariski-site", "def-sp-kinjective-bridge"]
+++
For an abelian sheaf $F$ on the
small Zariski site of $X$,
let $H^q(X_{\rm Zar},F)$ be the $q$-th right derived
functor of $F\mapsto F(X)$. Equivalently take the
cohomology of the section complex of an injective resolution,
using the ordinary resolution convention of
[def-sp-kinjective-bridge].
