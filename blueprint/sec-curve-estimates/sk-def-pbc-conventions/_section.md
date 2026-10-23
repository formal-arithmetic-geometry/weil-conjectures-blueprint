+++
id = "sk-def-pbc-conventions"
kind = "definition"
title = "Conventions for proper base change"
order = 1275
lean = ["AlgebraicGeometry.Etale.upperStar", "AlgebraicGeometry.Etale.preservesFiniteLimits_upperStar", "AlgebraicGeometry.Etale.upperStarLowerStarAdjunction", "CategoryTheory.Functor.mapDerivedCategoryPlus", "CategoryTheory.Functor.rightDerivedFunctorPlus", "AlgebraicGeometry.Scheme.isZero_rightDerived_etale_toSheaf_of_injective", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerStarRestrictScalars", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerStarForget₂"]
uses = ["sk-def-conv"]
tags = ["sketch"]
+++
For proper base change, schemes are arbitrary unless an additional
hypothesis is stated. The theorem concerns the classical part of
$D^+(T_{\mathrm{proét}},\Lambda)$, for a discrete commutative ring $\Lambda$.
The intermediate calculations (acyclicity, curves, Chow's lemma) are made on
$T_{\Et}$, with abelian sheaves or modules over its discrete constant
ring. We write $D^+(T_{\Et},\Lambda)$ for the bounded below derived
category. Inverse image on these sheaves is denoted by $u^{-1}$. For
$u:S\to T$ it is a functor $\Sh(T_{\Et})\to\Sh(S_{\Et})$, and likewise
on sheaves of modules and $D^+(T_{\Et},\Lambda)\to D^+(S_{\Et},\Lambda)$. It is
exact and agrees with $u^*$ for the constant coefficient rings under
consideration. The derived direct image is $Ru_*$. Torsion always
means torsion of the underlying abelian sheaves.

Proper base change holds for torsion coefficients of every
characteristic, so the primes $r$ used as torsion coefficients below may
equal a residue characteristic. The standing condition on $\ell$ from
the introduction is imposed again when we return to the $\ell$-adic
constructible theory.

Results for abelian sheaves apply to sheaves of modules, because the
cohomology of a sheaf of $\Lambda$-modules agrees with the cohomology
of its underlying abelian sheaf (Stacks Project, Tag 03FD). The reason is that an
injective sheaf of modules is acyclic for the section functor on
every object of the site, although it need not be injective as an
abelian sheaf. Applying this on the étale objects over the target,
we get the same compatibility for $R^qu_*$ and, by bounded below
resolutions, for $Ru_*$.
