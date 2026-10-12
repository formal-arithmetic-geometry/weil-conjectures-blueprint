+++
id = "sk-p-real-semi"
kind = "proposition"
title = "Semi-continuity of weights"
order = 2954
uses = ["sk-d-real-boundary", "sk-d-real-cohom", "sk-d-real-weights", "sk-d-real-weil", "sk-i-real-boundary", "sk-i-real-normalization", "sk-p-linear-filtration", "sk-p-real-integral", "sk-p-real-sections", "sk-thm-derived-duality", "sk-thm-trace-transport"]
lean = ["AlgebraicGeometry.BoundaryDatum.frobeniusWeight_le_of_hasWeightsAtMost", "AlgebraicGeometry.BoundaryDatum.isPunctuallyPure_of_isPunctuallyPure_restrict"]
tags = ["sketch"]
+++
For a boundary datum, if $\mathcal F$ has
weights at most $w$ on $U_0$, then $j_*\mathcal F$
has weights at most $w$ on $C_0$.
Consequently, if a lisse Weil sheaf $\mathcal G$ on
$C_0$ is punctually $\iota$-pure of weight $w$ on $U_0$, it is
punctually $\iota$-pure of weight $w$ on all of $C_0$.
