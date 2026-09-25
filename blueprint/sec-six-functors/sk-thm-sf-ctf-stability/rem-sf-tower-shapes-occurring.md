+++
id = "rem-sf-tower-shapes-occurring"
kind = "remark"
title = "Normalized DVR systems and additional local models"
order = 2346
uses = ["cor-sf-direct-image-ctf-proetale", "cor-sf-finite-level-comparison-two-cases", "def-coef-normalized-dvr-tower", "def-weil-derived-complete-integral-detailed", "def-weil-derived-direct-image", "lem-coef-finite-direct-image", "lem-coef-integral-compact-support", "lem-coef-integral-residue-tor", "lem-coef-normalized-dvr-effectivity", "prop-coef-integral-exceptional-adjoint", "thm-sf-uniform-models-constant-tower", "thm-sf-uniform-models-lisse-tower"]
+++
For an integral object of [def-weil-derived-complete-integral-detailed],
the reductions $K_n=K\otimes^L_{\mathcal O_E}A_{E,n}$ form a
coherent normalized tower, and
[lem-coef-integral-residue-tor] proves a common finite Tor
interval from the residue reduction. Conversely, a separately
supplied system satisfying
[def-coef-normalized-dvr-tower] reconstructs with exactly those
reductions by [lem-coef-normalized-dvr-effectivity].
This effectivity theorem needs no common stratification or lisse
local model. Membership in the integral constructible category
then follows from finite-level constructibility and a uniform bound.

For the direct-image tower in [def-weil-derived-direct-image],
normalization is [lem-coef-finite-direct-image], and the
finite direct-image bound of
[cor-sf-direct-image-ctf-proetale] is uniform in the coefficient
level. Thus normalized DVR effectivity supplies the canonical
finite-reduction comparison without additional local models.
The compact-support and exceptional versions are
[lem-coef-integral-compact-support], [prop-coef-integral-exceptional-adjoint].

The stronger local-model assertions
[thm-sf-uniform-models-constant-tower], [thm-sf-uniform-models-lisse-tower]
continue to require their displayed lisse hypotheses; the corollary
[cor-sf-finite-level-comparison-two-cases] describes those
special cases. A tower with no verified normalization or quotient
cocycle is not covered by the general effectivity theorem, and merely
forming its derived limit does not identify its purported reductions.
