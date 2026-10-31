+++
id = "sk-def-pbc-conventions"
kind = "definition"
title = "Conventions for proper base change"
order = 172
lean = ["AlgebraicGeometry.Etale.upperStar", "AlgebraicGeometry.Etale.preservesFiniteLimits_upperStar", "AlgebraicGeometry.Etale.upperStarLowerStarAdjunction", "CategoryTheory.Functor.mapDerivedCategoryPlus", "CategoryTheory.Functor.rightDerivedFunctorPlus", "AlgebraicGeometry.Scheme.isZero_rightDerived_etale_toSheaf_of_injective", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerStarRestrictScalars", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerStarForget₂"]
uses = ["sk-def-conv"]
tags = ["sketch", "latex:convention"]
+++
For proper base change, schemes are arbitrary unless an additional
hypothesis is stated. The theorem concerns the classical part of
$D^+(T_{\mathrm{pro}\acute{e}t},\Lambda)$, for a discrete commutative ring $\Lambda$.
The intermediate calculations (acyclicity, curves, Chow's lemma) are made on
$T_{\acute{e}t}$, with abelian sheaves or modules over its discrete constant
ring. We write $D^+(T_{\acute{e}t},\Lambda)$ for the bounded below derived
category. Inverse image of étale sheaves along $u:S\to T$ is written
$u^*:\Sh(T_{\acute{e}t})\to\Sh(S_{\acute{e}t})$, as for module sheaves; it is exact,
and so is its extension to $D^+(T_{\acute{e}t},\Lambda)\to D^+(S_{\acute{e}t},\Lambda)$. The derived direct image is $Ru_*$. Torsion always
means torsion of the underlying abelian sheaves.

Proper base change holds for torsion coefficients of every
characteristic. Until Section [sec-pbc-condensed], $\ell$ therefore denotes
an arbitrary prime, which may equal a residue characteristic; from
Section [sec-pbc-condensed] on, the standing condition on $\ell$ applies
again.
