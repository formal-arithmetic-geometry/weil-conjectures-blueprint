+++
id = "lem-a1-middle-extension-endpoints"
kind = "lemma"
title = "Degree zero and degree two"
order = 3074
uses = ["def-weil-frobenius-module-weights", "def-weil-ordinary-compact-cohomology", "def-weil-punctual-weights", "def-wf-fundamental-representation", "def-wf-middle-extension", "lem-a1-affine-hc0", "lem-a1-affine-hc2", "lem-a1-geometric-coinvariants-pure", "lem-wf-tate-twist-frobenius", "lem-zl-affine-curve-range", "prop-a1-curve-boundary-sequence"]
lean = ["AlgebraicGeometry.subsingleton_compactlySupportedCohomology_directImage", "AlgebraicGeometry.subsingleton_compactlySupportedCohomology_directImage_zero", "AlgebraicGeometry.nonempty_equiv_compactlySupportedCohomology_directImage_two", "AlgebraicGeometry.isPureOfWeightOver_compactlySupportedCohomology_directImage_two"]
+++
Let $j:U_0\hookrightarrow C_0$ be a dense open immersion, with $C_0$ a
smooth geometrically connected affine curve over $k_0=\mathbf F_q$, and
let $\mathcal F$ be a lisse Weil sheaf on $U_0$ with generic geometric
representation $V$ ([def-wf-fundamental-representation]). For the
middle extension $j_*\mathcal F$ of [def-wf-middle-extension], in the
compactly supported cohomology of [def-weil-ordinary-compact-cohomology],

$$
H_c^0(C,j_*\mathcal F)=0,\qquad
H_c^2(C,j_*\mathcal F)\simeq V_{\pi_1(U)}(-1)
$$

Frobenius-equivariantly, and $H_c^r(C,j_*\mathcal F)=0$ for
$r\notin\{0,1,2\}$. If $\mathcal F$ is punctually $\iota$-pure of weight
$w$, then $H_c^2(C,j_*\mathcal F)$ is $\iota$-pure of weight $w+2$
(possibly zero).
