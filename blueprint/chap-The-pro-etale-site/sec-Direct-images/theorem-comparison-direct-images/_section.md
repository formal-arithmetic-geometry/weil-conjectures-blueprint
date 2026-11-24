+++
id = "theorem-comparison-direct-images"
kind = "theorem"
title = "Comparison of direct images"
order = 133
lean = ["AlgebraicGeometry.ProEtale.rightDerivedLowerStarComparisonPlusBaseChange", "AlgebraicGeometry.ProEtale.rightDerivedLowerStarComparisonPlusIso", "AlgebraicGeometry.ProEtale.isIso_rightDerivedLowerStarComparisonPlusBaseChange"]
uses = ["definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image"]
+++
If $g$ is quasi-compact and quasi-separated, the canonical natural
transformation

$$
\href{@proposition-comparison-morphism-inverse-image}{\nu_Y^*}Rg_{\acute{e}t,*}K\longrightarrow
\href{@proposition-topos-functoriality}{Rg_{\mathrm{pro}\acute{e}t,*}}\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*K}
\tag{2.9}
$$

is an isomorphism for $K\in D^+(X_{\acute{e}t},\Lambda)$.
