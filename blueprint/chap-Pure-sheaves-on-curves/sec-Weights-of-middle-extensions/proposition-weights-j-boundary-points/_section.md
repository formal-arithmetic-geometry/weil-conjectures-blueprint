+++
id = "proposition-weights-j-boundary-points"
kind = "proposition"
title = "Weights of $j_*$ at the boundary points"
order = 1180
lean = ["AlgebraicGeometry.BoundaryDatum.frobeniusWeight_le_of_hasWeightsAtMost", "AlgebraicGeometry.WeilSheaf.IsLisse.hasWeightsAtMost_directImage"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-weil-representation"]
+++
Let $j:U_0\hookrightarrow X_0$ be a dense open of a smooth
geometrically connected curve.  If a lisse Weil sheaf $\mathcal F$ on
$U_0$ is punctually of weights $\le a$, so is $j_*\mathcal F$ on
$X_0$.
