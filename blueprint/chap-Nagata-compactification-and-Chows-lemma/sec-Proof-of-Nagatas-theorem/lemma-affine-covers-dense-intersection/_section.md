+++
id = "lemma-affine-covers-dense-intersection"
kind = "lemma"
title = "Affine covers with dense intersection"
order = 1462
lean = ["AlgebraicGeometry.Scheme.finiteAffineOpenCoverDenseIInter_spec", "AlgebraicGeometry.exists_isAffineOpen_iSup_eq_top_and_genericPoints_subset_iInter", "AlgebraicGeometry.HasCompactification.of_isQuasiAffine"]
uses = ["definition-compactification-refinement"]
+++
For a scheme $X$ of finite type over a Noetherian scheme $S$, there is
a finite affine cover $X=\bigcup_{r=1}^m U_r$ whose total
intersection is dense in $X$. If $X\to S$ is separated, then each
$U_r\to S$ has a projective compactification.
