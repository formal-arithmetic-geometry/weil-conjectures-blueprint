+++
id = "sbc-thm-finite-proetale-smooth-base-change"
kind = "theorem"
title = "Finite pro-etale smooth base change"
lean = ["AlgebraicGeometry.ProEtale.isIso_derivedBaseChangeMap_app_of_smooth"]
order = 2478
uses = ["def-sbc-smooth-morphisms", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "lem-weil-pbc-comparison-pullback", "prop-weil-pbc-comparison-direct-image", "sbc-def-base-change-square", "sbc-thm-bounded-derived-smooth-base-change", "sbc-thm-smooth-base-change", "thm-weil-pbc-site-comparison"]
+++
In the square of
[sbc-thm-smooth-base-change], assume $f$ smooth, $g$ quasi-compact
and quasi-separated, and all schemes noetherian. For
$K\in\Dbc(T_{\Proet},\Lambda)$ (constructed over the
pro-etale site of
[def-weil-pbc-proetale-modules]) whose finite-level reductions
$K_n$ come from the etale site, the pro-etale exchange map

$$
Lf^*_{\Proet}Rg_{*,\Proet}K\xrightarrow{\ \sim\ }Rh_{*,\Proet}Le^*_{\Proet}K
$$

is an isomorphism, obtained by conjugating the etale exchange
isomorphism of [sbc-thm-bounded-derived-smooth-base-change] by the
site comparison equivalences.
