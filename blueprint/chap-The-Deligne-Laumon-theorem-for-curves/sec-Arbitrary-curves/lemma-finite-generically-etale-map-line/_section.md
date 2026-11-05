+++
id = "lemma-finite-generically-etale-map-line"
kind = "lemma"
title = "A finite generically étale map to the line"
order = 1312
lean = ["AlgebraicGeometry.AffineSpace.exists_isOpenImmersion_isFinite_etale_morphismRestrict", "AlgebraicGeometry.WeilSheaf.isLisse_and_isPunctuallyPureOfWeight_upperStar_lowerStar_extensionByZero", "AlgebraicGeometry.WeilSheaf.nonempty_equiv_compactlySupportedCohomology_lowerStar_extensionByZero"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-weights", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $C_0$ be a smooth geometrically connected affine curve. There
are a smooth curve $C'_0$ containing $C_0$ with finite complement
and a finite generically étale map $\pi:C'_0\to\mathbf A^1_{k_0}$.
If $F$ is a pure lisse sheaf of weight $w$ on $C_0$, then the sheaf
$K=\pi_*j_!F$, where $j:C_0\hookrightarrow C'_0$, is lisse and
pure of weight $w$ outside the branch locus and the image of
$C'_0\setminus C_0$. Moreover,
$R\Gamma_c(\mathbf A^1,K)=R\Gamma_c(C,F)$ canonically.
