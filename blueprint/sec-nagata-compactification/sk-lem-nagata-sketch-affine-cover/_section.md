+++
id = "sk-lem-nagata-sketch-affine-cover"
kind = "lemma"
title = "Enough compactifiable affine opens"
order = 18
uses = ["sk-lem-nagata-sketch-closure"]
lean = ["AlgebraicGeometry.Scheme.finiteAffineOpenCoverDenseIInter_spec", "AlgebraicGeometry.HasCompactification.of_isQuasiAffine"]
tags = ["sketch"]
+++
For a finite-type scheme $X$ over a Noetherian scheme $S$ there is a finite
affine cover $X=\bigcup_{r=1}^mU_r$ whose total intersection is dense in $X$.
If $X\to S$ is separated, each $U_r\to S$ has a projective compactification.
