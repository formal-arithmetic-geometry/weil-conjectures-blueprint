+++
id = "det-pe-classical-sheaves-unit"
kind = "lemma"
title = "The comparison unit is an isomorphism"
lean = ["AlgebraicGeometry.ProEtale.isIso_comparisonAdjunction_unit", "AlgebraicGeometry.ProEtale.full_comparisonUpperStar", "AlgebraicGeometry.ProEtale.faithful_comparisonUpperStar"]
order = 996
uses = ["def-weil-pbc-site-comparison-morphism", "lem-weil-pbc-comparison-sections"]
+++
Let $X$ be a scheme and $\Lambda$ a ring. For every sheaf of $\Lambda$-modules
$F$ on $X_{\Et}$ the unit $\eta_F\colon F\to\nu_{X,*}\nu_X^*F$ is an
isomorphism. Consequently
$\nu_X^*\colon\Mod(X_{\Et},\Lambda)\to\Mod(X_{\Proet},\Lambda)$ is fully
faithful: for sheaves $F,F'$ of $\Lambda$-modules on $X_{\Et}$ the map
$\Hom(F,F')\to\Hom(\nu_X^*F,\nu_X^*F')$, $\varphi\mapsto\nu_X^*\varphi$, is
bijective.
