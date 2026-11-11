+++
id = "lemma-functoriality-deformation"
kind = "lemma"
title = "Functoriality of the deformation"
order = 1632
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.deformationSpaceMap", "AlgebraicGeometry.Scheme.IdealSheafData.isClosedImmersion_deformationSpaceToPullback", "AlgebraicGeometry.Scheme.IdealSheafData.isIso_deformationSpaceToPullback_of_flat", "AlgebraicGeometry.ProEtale.CondensedRing.isPullback_zeroSectionSpecialFibreMap", "AlgebraicGeometry.ProEtale.CondensedRing.isProper_deformationTotalMap", "AlgebraicGeometry.ProEtale.CondensedRing.smooth_deformationTotalMap", "AlgebraicGeometry.ProEtale.CondensedRing.deformationTotalMap"]
uses = ["definition-deformation-normal-bundle"]
+++
Let $f:X'\to X$ be a morphism of separated $k$-schemes of finite type,
let $Z'\subset X'$ be a closed subscheme with ideal $I'$, and suppose
that $f^{-1}(I)\mathcal O_{X'}\subset I'$.  Then $f$ induces
$\widetilde f:\mathcal D_{Z'}X'\to\mathcal D_ZX$.
If $Z'=f^{-1}Z$ schematically, then

$$
\mathcal D_{Z'}X'\longrightarrow X'\times_X\mathcal D_ZX
$$

is a closed immersion, and it is an isomorphism if $f$ is flat.
Moreover, $\widetilde f_s^{-1}(Z)=Z'$ schematically.
In this case $\widetilde f$ is proper when $f$ is proper and smooth
when $f$ is smooth.
