+++
id = "theorem-weight-bound-affine-line"
kind = "theorem"
title = "The weight bound on the affine line"
order = 1292
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.hasWeightsAtMost_compactlySupportedCohomology_directImage"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-weights", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open, and let
$F$ be a lisse sheaf on $U_0$, pure of weight $w$ and unramified at
infinity. Then $H_c^1(\mathbf A^1,j_*F)$ has weights at most $w+1$.
