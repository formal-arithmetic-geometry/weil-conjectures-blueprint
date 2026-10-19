+++
id = "sk-lem-nagata-sketch-affine-cover"
kind = "lemma"
title = "Enough compactifiable affine opens"
order = 18
uses = ["sk-lem-nagata-sketch-closure", "sk-def-nagata-sketch-data"]
lean = ["AlgebraicGeometry.Scheme.finiteAffineOpenCoverDenseIInter_spec", "AlgebraicGeometry.HasCompactification.of_isQuasiAffine"]
tags = ["sketch"]
+++
For a quasi-compact scheme $X$ with finitely many irreducible components
(e.g. $X$ of finite type over a Noetherian scheme $S$) there is a finite
affine cover $X=\bigcup_{r=1}^mU_r$ whose total intersection is dense in $X$.
If $Y$ is quasi-affine and $Y\to S$ is locally of finite type and
quasi-compact, then $Y\to S$ has a compactification
([sk-def-nagata-sketch-data]); this applies to each $U_r\to S$ when $X$ is of
finite type over a quasi-separated $S$.
