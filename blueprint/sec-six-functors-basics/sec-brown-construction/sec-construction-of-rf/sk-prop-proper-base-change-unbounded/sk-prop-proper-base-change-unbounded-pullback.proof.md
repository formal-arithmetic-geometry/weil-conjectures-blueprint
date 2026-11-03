+++
kind = "proof"
of = "det-proper-base-change-unbounded-pullback"
+++
*Exactness and sums.* By [sk-prop-sfb-cartesian-coefficients], $g^*\Lambda_Y=\Lambda_{Y'}$, so the module
inverse image is the exact inverse image of sheaves; it is computed termwise, is an exact functor of
triangulated categories, and is a left adjoint (of $Rg_*$), hence preserves direct sums.

*Constructible complexes.* For finite $A$: by [sk-lem-sf-flat-model], $K\in\Dctf(Y,A)$ is a bounded complex of
flat constructible sheaves, and $g^*$ preserves flatness (stalks are unchanged), constructibility
(pull back the stratification) and boundedness, so $g^*K\in\Dctf(Y',A)$. For $\mathcal O_E$, $E$, $\Qlb$ (where
$\Dctf=\Dbc$): by [det-def-sfb-dc-restricted-functors], $g^*$ preserves bounded constructible complexes, via
the local coefficient models on strata.

*Localizing closures.* Apply [det-proper-image-localizing-principle].
