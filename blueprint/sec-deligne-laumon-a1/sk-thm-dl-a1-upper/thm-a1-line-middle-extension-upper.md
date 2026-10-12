+++
id = "thm-a1-line-middle-extension-upper"
kind = "theorem"
title = "Deligne–Laumon affine-line estimate for the middle extension"
order = 3146
uses = ["cor-a1-fourier-middle-hc1", "def-weil-frobenius-module-weights", "def-weil-ordinary-compact-cohomology", "def-weil-punctual-weights", "def-wf-constant-weil-twist", "def-wf-fundamental-representation", "def-wf-middle-extension", "lem-a1-constituent-nonexceptional-comparison", "lem-a1-exceptional-constituents", "lem-a1-extension-bounds", "lem-a1-geometric-constituent-reduction", "lem-a1-middle-extension-endpoints", "lem-a1-spectrum-exact-sequence", "lem-a1-subquotient-extension-bounds", "lem-a1-unramified-nonexceptional", "lem-a1-weight-bound-constant-extension", "p-dl-a1-exact", "prop-a1-curve-boundary-sequence", "rem-dl-a1-conventions"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.hasWeightsAtMost_compactlySupportedCohomology_directImage", "AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.subsingleton_compactlySupportedCohomology_directImage_zero", "AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.isPureOfWeightOver_compactlySupportedCohomology_directImage_two", "AlgebraicGeometry.subsingleton_compactlySupportedCohomology_directImage"]
+++
In the conventions of [rem-dl-a1-conventions], let
$j:U_0\hookrightarrow A_0=\mathbf A^1_{k_0}$ be a dense open immersion
and let $\mathcal F$ be a lisse Weil sheaf on $U_0$, punctually
$\iota$-pure of weight $w$ ([def-weil-punctual-weights]) and
unramified at infinity. Then, for the ordinary middle extension
$j_*\mathcal F$ of [def-wf-middle-extension] and the compactly
supported cohomology of [def-weil-ordinary-compact-cohomology], for
every integer $r$

$$
H_c^r(A,j_*\mathcal F)\quad\text{has weights at most }w+r
$$

in the sense of [def-weil-frobenius-module-weights]. More precisely,
$H_c^0(A,j_*\mathcal F)=0$, $H_c^2(A,j_*\mathcal F)$ is $\iota$-pure of
weight $w+2$ (possibly zero), $H_c^r(A,j_*\mathcal F)=0$ for
$r\notin\{0,1,2\}$, and $H_c^1(A,j_*\mathcal F)$ has weights at most
$w+1$.
