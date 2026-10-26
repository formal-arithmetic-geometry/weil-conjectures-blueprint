+++
id = "lem-fet-locally-trivial"
kind = "theorem"
title = "Finite etale covers are trivial after an etale base change"
lean = ["AlgebraicGeometry.Scheme.FiniteEtale.exists_etale_isPullback_sigma"]
order = 1360
uses = ["def-galois-categories", "def-weil-pbc-scheme-conventions"]
+++
Let $P\to Y$ be finite etale and $y\in Y$. Then there are an etale
morphism $U\to Y$ whose image contains $y$ and a finite set $S$ with
$P\times_YU\cong\coprod_{s\in S}U$ over $U$. In particular the
morphisms $U\to Y$ so obtained for all $y\in Y$ form an etale covering
of $Y$ over whose members $P$ becomes a finite disjoint union of copies
of the base.
