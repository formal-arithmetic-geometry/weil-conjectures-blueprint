+++
id = "def-weil-pbc-pointed-etale-neighbourhoods-detailed"
kind = "definition"
title = "Pointed etale neighborhoods"
order = 2047
lean = ["AlgebraicGeometry.Etale.PointedNeighbourhoodCat"]
uses = ["def-weil-pbc-scheme-conventions", "def-weil-pbc-etale-site"]
+++
For a geometric point [def-weil-pbc-scheme-conventions] $\bar
s:\operatorname{Spec}\Omega\to S$, let $\mathcal N_{\bar s}$ be the category
whose objects are pairs $(V,\bar v)$ with $V\to S$ etale
[def-weil-pbc-scheme-conventions] and $\bar v\to V$ above $\bar s$. A
morphism preserves the chosen geometric points. Stalk colimits are indexed by
$\mathcal N_{\bar s}^{\mathrm{op}}$.
