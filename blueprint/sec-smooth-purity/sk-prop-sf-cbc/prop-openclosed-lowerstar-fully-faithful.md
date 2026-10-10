+++
id = "prop-openclosed-lowerstar-fully-faithful"
kind = "theorem"
title = "$i_*$ is fully faithful"
order = 1522
lean = ["AlgebraicGeometry.Etale.fullyFaithfulLowerStar", "AlgebraicGeometry.Etale.isIso_upperStarLowerStarAdjunction_counit"]
tags = ["latex:proposition"]
uses = ["def-kun-separably-closed", "lemma-openclosed-point-ulift", "lemma-openclosed-stalk-lowerstar", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $i\colon Z\to X$ be a closed immersion. Then the counit

$$
\varepsilon\colon i^*i_*\Longrightarrow\mathrm{id}_{\shv{\et Z}}
$$

is an isomorphism; equivalently, $i_*$ is fully faithful.
