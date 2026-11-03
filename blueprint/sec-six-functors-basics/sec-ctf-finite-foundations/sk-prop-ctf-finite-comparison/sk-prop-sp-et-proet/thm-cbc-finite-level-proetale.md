+++
id = "thm-cbc-finite-level-proetale"
kind = "theorem"
title = "Finite-level pro-etale compact-support base change"
lean = ["AlgebraicGeometry.ProEtale.isIso_rightDerivedLowerShriekOfCompactificationBaseChangeMap_app"]
order = 2888
uses = ["def-cbc-compact-support-square", "def-cbc-exchange-map", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-scheme-conventions", "lem-cbc-proetale-extension-zero-base-change", "lem-cbc-proetale-extension-zero-comparison", "lem-weil-pbc-transport-identifies-exchange", "prop-weil-pbc-comparison-direct-image", "thm-cbc-finite-torsion", "thm-weil-pbc-site-comparison"]
+++
Let $\Lambda$ be finite, let $\square$ be a
compact-support
base-change square with $f$ separated of finite type and
$g:Y'\to Y$ arbitrary, and let
$K\in D^+(X_{\Proet},\Lambda)$ carry an
etale-origin witness
$(L,\alpha)$. Then the pro-etale exchange map

$$
g^{-1}Rf_!K\xrightarrow{\ \sim\ }Rf'_!g'^{-1}K
$$

of [def-cbc-exchange-map] (with the compact-support functors
and exchange map of [def-cbc-exchange-map] transported to the
pro-etale site) is an isomorphism; it is independent of replacing
the witness by an isomorphic one.
