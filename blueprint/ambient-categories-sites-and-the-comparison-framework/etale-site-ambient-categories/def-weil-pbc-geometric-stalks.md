+++
id = "def-weil-pbc-geometric-stalks"
kind = "definition"
title = "Geometric stalks"
order = 2005
lean = ["AlgebraicGeometry.Etale.PointedNeighbourhood", "AlgebraicGeometry.Etale.stalk"]
uses = ["def-weil-pbc-scheme-conventions", "def-weil-pbc-etale-site"]
+++
Let $\bar t:\operatorname{Spec}\Omega\to T$ be a geometric point
[def-weil-pbc-scheme-conventions]. A *pointed etale neighbourhood* of $\bar
t$ is a pair $(U,\bar u)$ with $U\to T$ an object of the small etale site
[def-weil-pbc-etale-site] and $\bar u:\operatorname{Spec}\Omega\to U$ a lift
of $\bar t$. For a sheaf $F$ on $T_{\Et}$, define its *stalk at $\bar t$* by

$$
 F_{\bar t}=\varinjlim_{(U,\bar u)}F(U),
$$

where the colimit runs over pointed etale neighbourhoods with the opposite
index category.
