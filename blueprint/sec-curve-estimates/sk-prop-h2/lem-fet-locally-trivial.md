+++
id = "lem-fet-locally-trivial"
kind = "theorem"
title = "Finite etale covers are trivial after an etale base change"
lean = ["AlgebraicGeometry.Scheme.FiniteEtale.exists_etale_isPullback_sigma"]
order = 973
uses = ["def-galois-categories", "def-weil-pbc-scheme-conventions"]
+++
Let $P\to Y$ be finite etale. Then there is a surjective etale
$Y'\to Y$ and a finite set $S$ with
$P\times_YY'\cong Y'\times S$ over $Y'$.
