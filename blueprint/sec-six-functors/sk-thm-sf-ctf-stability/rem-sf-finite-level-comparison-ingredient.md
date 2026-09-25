+++
id = "rem-sf-finite-level-comparison-ingredient"
kind = "remark"
title = "The local-model proof and normalized DVR reconstruction"
order = 2333
uses = ["cor-coef-finite-verdier", "cor-sf-finite-level-comparison-two-cases", "def-coef-normalized-dvr-tower", "def-weil-pbc-bounded-constructible-tower", "lem-coef-finite-direct-image", "lem-coef-finite-exceptional", "lem-coef-integral-hom-reduction", "lem-coef-normalized-dvr-effectivity", "lem-sf-finite-level-comparison", "prop-coef-integral-exceptional-adjoint", "thm-sf-uniform-models-constant-tower", "thm-sf-uniform-models-lisse-tower"]
+++
The proof of [lem-sf-finite-level-comparison] uses the uniform
local models of [def-weil-pbc-bounded-constructible-tower].
The two sufficient criteria
[thm-sf-uniform-models-constant-tower], [thm-sf-uniform-models-lisse-tower]
retain all of their lisse and amplitude hypotheses, and
[cor-sf-finite-level-comparison-two-cases] applies under those
complete hypotheses. These results provide additional local-model
information; they are not necessary hypotheses for DVR reconstruction.

The separate theorem [lem-coef-normalized-dvr-effectivity]
reconstructs every coherent normalized DVR tower of
[def-coef-normalized-dvr-tower], without a common stratification
or common lisse model. With finite-level constructibility and a
uniform amplitude bound it yields an object of the integral category.
The direct-image and duality towers have their normalization maps from
[lem-coef-finite-direct-image], [cor-coef-finite-verdier]; the
exceptional tower has them from [lem-coef-finite-exceptional].
General internal-Hom reduction and the integral exceptional adjunction
are independently established in
[lem-coef-integral-hom-reduction], [prop-coef-integral-exceptional-adjoint].
For an arbitrary tower whose normalization has not been checked,
merely taking its derived limit still supplies no identification with
the proposed finite reductions.
