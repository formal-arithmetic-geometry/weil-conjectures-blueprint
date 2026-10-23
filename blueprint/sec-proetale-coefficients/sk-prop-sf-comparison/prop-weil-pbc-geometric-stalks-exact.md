+++
id = "prop-weil-pbc-geometric-stalks-exact"
kind = "theorem"
title = "Exactness of geometric stalks"
lean = ["AlgebraicGeometry.Scheme.preservesFiniteLimits_geometricStalkFunctor", "AlgebraicGeometry.Scheme.preservesFiniteColimits_geometricStalkFunctor", "AlgebraicGeometry.Scheme.shortExact_map_geometricStalkFunctor"]
order = 1009
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-geometric-stalks"]
tags = ["latex:proposition"]
+++
For every geometric point $\bar t$ of $T$, the stalk functor $F\mapsto
F_{\bar t}$ of [def-weil-pbc-geometric-stalks]

$$
 \Ab(T_{\Et})\longrightarrow\Ab,\qquad F\longmapsto F_{\bar t}
$$

is exact (filtered colimits are exact and a stalk is a filtered colimit of
sections over pointed etale neighbourhoods).
