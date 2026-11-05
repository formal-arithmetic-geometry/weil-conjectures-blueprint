+++
id = "lemma-cohomological-range-curve"
kind = "lemma"
title = "Cohomological range on a curve"
order = 1189
lean = ["AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_of_krullDim_le_one", "AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_of_isAffine"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $C$ be a smooth curve over an algebraically closed field and let
$F$ be a constructible sheaf on $C$ with coefficients in $E$ or $\overline{\mathbf Q}_\ell$.
Then $H^i_c(C,F)=0$ for $i\notin\{0,1,2\}$.
