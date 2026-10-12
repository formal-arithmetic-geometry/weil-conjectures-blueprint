+++
id = "sk-l-dl-a1-endpoints"
kind = "lemma"
title = "Degree zero and degree two"
order = 3067
uses = ["sk-d-dl-a1-setup", "sk-p-linear-filtration", "sk-thm-derived-duality", "sk-thm-sf-dual-perfect", "sk-thm-sf-global-duality"]
lean = ["AlgebraicGeometry.subsingleton_compactlySupportedCohomology_directImage", "AlgebraicGeometry.subsingleton_compactlySupportedCohomology_directImage_zero", "AlgebraicGeometry.nonempty_equiv_compactlySupportedCohomology_directImage_two", "AlgebraicGeometry.isPureOfWeightOver_compactlySupportedCohomology_directImage_two"]
tags = ["sketch"]
+++
Let $j:U_0\hookrightarrow C_0$ be dense, with $C_0$ a smooth
geometrically connected affine curve, and let $F$ be lisse.
If $V$ is its generic geometric representation, then

$$
H_c^0(C,j_*F)=0,\qquad
H_c^2(C,j_*F)\simeq V_{\pi_1(U)}(-1).
$$

There is no cohomology outside degrees $0,1,2$. If $F$ is pure of
weight $w$, the degree-two group is pure of weight $w+2$ (possibly zero).
