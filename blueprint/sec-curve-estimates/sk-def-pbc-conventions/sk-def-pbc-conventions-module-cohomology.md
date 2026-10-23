+++
id = "det-pbc-conventions-module-cohomology"
kind = "lemma"
title = "Module cohomology is abelian cohomology"
lean = ["AlgebraicGeometry.Scheme.isZero_rightDerived_etale_toSheaf_of_injective", "AlgebraicGeometry.Etale.rightAcyclic_lowerStar_restrictScalars_obj", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerStarRestrictScalars", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerStarForget₂", "AlgebraicGeometry.Etale.forget₂HomologyRightDerivedFunctorPlusIso"]
order = 1300
uses = ["def-weil-pbc-etale-sheaves", "lemma-weil-pbc-leray-acyclicity"]
+++
Let $\Lambda$ be a commutative ring, let $T$ be a scheme and write
$\mathrm{For}:\Mod(T_{\Et},\Lambda)\to\Ab(T_{\Et})$ for the functor forgetting
the $\Lambda$-module structure.

1. If $I$ is an injective object of $\Mod(T_{\Et},\Lambda)$, then for every
   étale $U\to T$ one has $H^q(U_{\Et},\mathrm{For}\,I)=0$ for $q>0$.
2. For every sheaf $F$ of $\Lambda$-modules and every étale $U\to T$, the
   derived functors of $\Gamma(U,-)$ computed in $\Mod(T_{\Et},\Lambda)$ and
   in $\Ab(T_{\Et})$ agree: $\mathrm{For}\,H^q_{\Lambda}(U,F)\cong
   H^q(U,\mathrm{For}\,F)$ canonically.
3. For a morphism $u:S\to T$ and $F\in\Mod(S_{\Et},\Lambda)$ there are
   canonical isomorphisms $\mathrm{For}\,R^qu_*F\cong R^qu_*\mathrm{For}\,F$,
   and for $K\in D^+(S_{\Et},\Lambda)$ a canonical isomorphism
   $\mathrm{For}\,Ru_*K\cong Ru_*\mathrm{For}\,K$ in $D^+(T_{\Et},\mathbf Z)$.

The forgetful functor need not preserve injectives; only the acyclicity of
(1) is used.
