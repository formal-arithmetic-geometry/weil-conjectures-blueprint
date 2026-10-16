+++
id = "lem-coef-normalized-dvr-effectivity"
kind = "lemma"
title = "Effectivity of a normalized DVR tower"
lean = ["AlgebraicGeometry.Etale.NormalizedTower.isDerivedBaseChange_of_isHomotopyLimit"]
order = 2476
uses = ["def-coef-normalized-dvr-tower", "def-weil-derived-complete", "prop-weil-pbc-roos-triangle"]
+++
For a tower in [def-coef-normalized-dvr-tower], put
$M=R\varprojlim_m\operatorname{Res}_m M_m$. Then the canonical
counit comparisons give coherent isomorphisms

$$
M\otimes_R^L A_n\xrightarrow{\sim}M_n
\qquad(n\geq1).
$$

In particular $M$ is derived complete in the sense of
[def-weil-derived-complete]. No constructibility or boundedness
is required for this effectivity assertion.
