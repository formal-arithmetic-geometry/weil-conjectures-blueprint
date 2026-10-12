+++
id = "sk-def-sfb-dc-restricted-functors"
kind = "definition"
title = "$Lf^*$, $Rf_*$, $j_!$, $\\otimes^{\\mathrm L}$, $\\RHom$ on $D_{\\mathrm{cons}}$: restrictions"
order = 1773
uses = ["sk-def-sfb-dc-setting", "sk-def-sfb-derived-tensor-hom", "sk-thm-sfb-rationalization-comparison", "sk-thm-sfb-qlbar-two-colimit"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_leftDerivedUpperStar_obj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperStar", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperStarComp", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightDerivedLowerStar_obj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerStar", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperStarLowerStarAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_openImmersionLowerShriek_obj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleOpenImmersionLowerShriek", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleOpenImmersionLowerShriekUpperStarAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_derivedTensor_obj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_derivedHom_obj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleTensor", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleHom", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleTensorHomAdjunction"]
tags = ["sketch"]
+++
Work in the setting of [sk-def-sfb-dc-setting], and let $\Lambda$ be a commutative condensed
ring. Consider the following functors on the ambient derived categories of module objects:

- the derived pullback $Lf^*\colon D(\Mod_{\Lambda_Y})\to D(\Mod_{\Lambda_X})$ and the derived
  pushforward $Rf_*\colon D(\Mod_{\Lambda_X})\to D(\Mod_{\Lambda_Y})$ of a morphism
  $f\colon X\to Y$ ([sk-def-sfb-module-derived-pushpull]);
- the extension by zero $j_!=D(j_!)\colon D(\Mod_{\Lambda_U})\to D(\Mod_{\Lambda_X})$ along an
  open immersion $j\colon U\to X$, applied levelwise to complexes
  ([sk-def-sfb-module-lower-shriek], [sk-prop-sfb-module-derived-factorization]);
- the derived tensor product $-\otimes^{\mathrm L}_{\Lambda_X}-$ and the derived internal hom
  $\RHom_{\Lambda_X}(-,-)$ on $D(\Mod_{\Lambda_X})$ ([sk-def-sfb-derived-tensor-hom]).

Each of them carries bounded constructible complexes ([sk-def-sfb-bounded-constructible]) to
bounded constructible complexes in the following cases. For $Lf^*$ and $j_!$ this holds for every
$\Lambda$. For $Rf_*$, $\otimes^{\mathrm L}$ and $\RHom$ it holds for the $\ell$-adic rings
$\Lambda=\underline{\cO}_E$, $\underline E$ ($E/\mathbf Q_\ell$ finite;
[sk-def-sfb-condensed-ring]) and $\Lambda=\underline{\Qlb}$ ([sk-def-sfb-qlbar-condensed]); these
are Deligne's finiteness theorems. It fails for a general $\Lambda$.

When the preservation property holds, the functor on $D_{\mathrm{cons}}$ is defined as the
**restriction** of the ambient functor: it is the unique functor whose composite with the fully
faithful inclusion $D_{\mathrm{cons}}\subseteq D(\Mod)$ equals the composite of the inclusion with
the ambient functor. This gives

$$
\begin{gathered}
Lf^*\colon D_{\mathrm{cons}}(Y,\Lambda)\to D_{\mathrm{cons}}(X,\Lambda),\qquad
Rf_*\colon D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(Y,\Lambda),\qquad
j_!\colon D_{\mathrm{cons}}(U,\Lambda)\to D_{\mathrm{cons}}(X,\Lambda),\\
-\otimes^{\mathrm L}-\colon D_{\mathrm{cons}}(X,\Lambda)\times D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(X,\Lambda),\qquad
\RHom(-,-)\colon D_{\mathrm{cons}}(X,\Lambda)^{\mathrm{op}}\times D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(X,\Lambda).
\end{gathered}
$$

By construction they commute with the inclusions. Nothing is derived afresh. The following
structure is also restricted along the fully faithful inclusions:

- the adjunctions $Lf^*\dashv Rf_*$, $j_!\dashv Lj^*$, and $K\otimes^{\mathrm L}-\dashv\RHom(K,-)$ for
  $K\in D_{\mathrm{cons}}(X,\Lambda)$;
- the composition isomorphism $L(g\circ f)^*\cong Lf^*\circ Lg^*$ for $f\colon X\to Y$,
  $g\colon Y\to Z$.
