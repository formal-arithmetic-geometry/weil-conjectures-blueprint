+++
id = "sbc-lem-degree-zero-flat-base-change"
kind = "lemma"
title = "Degree-zero flat base change"
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeMap_app_of_flat"]
order = 2168
uses = ["def-sbc-normal-dominant-galois", "def-weil-pbc-direct-image", "sbc-def-base-change-square"]
+++
Consider a base-change square
where $f$ is flat and locally of finite presentation with
geometrically reduced
fibres (in particular, $f$ may be smooth). Then

$$
f^{-1}g_*\mathcal F=h_*e^{-1}\mathcal F
$$

for any sheaf $\mathcal F$ on $T_{\Et}$.
