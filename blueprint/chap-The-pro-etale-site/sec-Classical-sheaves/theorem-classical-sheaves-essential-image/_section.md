+++
id = "theorem-classical-sheaves-essential-image"
kind = "theorem"
title = "Classical sheaves as the essential image"
order = 115
lean = ["AlgebraicGeometry.proEtaleClassicalSheaves", "AlgebraicGeometry.ProEtale.proEtaleClassicalSheavesModules", "AlgebraicGeometry.ProEtale.isIso_comparisonAdjunction_unit", "AlgebraicGeometry.ProEtale.full_comparisonUpperStar", "AlgebraicGeometry.ProEtale.faithful_comparisonUpperStar"]
uses = ["definition-small-pro-etale-site", "definition-classical-pro-etale-sheaves", "proposition-comparison-morphism-inverse-image"]
+++
The functor $\nu_X^*$ is fully faithful. Its essential image is exactly
the classical sheaves of Definition [definition-classical-pro-etale-sheaves].
For modules it is an exact equivalence between
$\operatorname{Mod}(X_{\acute{e}t},\Lambda)$ and the full subcategory of classical
$\Lambda_X$-module sheaves on $X_{\mathrm{pro}\acute{e}t}$.
