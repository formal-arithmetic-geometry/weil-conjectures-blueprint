+++
id = "sk-thm-sfb-rationalization-comparison"
kind = "theorem"
title = "$E$-coefficients as $\\mathcal O_E$-coefficients with $\\ell$ inverted"
order = 1590
uses = ["sk-def-sfb-condensed-ring", "sk-def-sfb-pullback-from-point", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-derived-extension-of-scalars", "sk-def-sfb-rationalization", "sk-def-sfb-bounded-constructible", "sk-def-sfb-constructible", "sk-def-sfb-ring-object", "sk-prop-sfb-module-category"]
lean = ["AlgebraicGeometry.ProEtale.padicIntegersRingObjToContinuousMapRingObj", "AlgebraicGeometry.ProEtale.padicIntegersToPadicSubfield", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalars_obj", "AlgebraicGeometry.ProEtale.boundedConstructibleExtendScalars", "AlgebraicGeometry.ProEtale.boundedConstructibleExtendScalarsCompatibility", "AlgebraicGeometry.ProEtale.isLocalization_boundedConstructibleExtendScalars", "AlgebraicGeometry.ProEtale.rationalizationEquivalence", "AlgebraicGeometry.ProEtale.rationalizationQCompEquivalenceIso"]
tags = ["sketch"]
+++
Let $\ell$ be a prime, $E\subseteq\Qlb$ a finite extension of $\mathbf Q_\ell$ with ring of
integers $\cO_E$, and $X$ a scheme. Let $\cO_{E,X}=p_X^*\underline{\cO}_E$ and
$E_X=p_X^*\underline E$ be the pulled-back coefficient rings
[sk-def-sfb-pulled-back-coefficients], where $E$ carries the norm restricted from $\Qlb$. Let
$$
\varphi=p_X^*(\underline{\cO}_E\hookrightarrow\underline E)\colon\cO_{E,X}\to E_X
$$
be the pullback along $p_X$ [sk-def-sfb-pullback-from-point] of the inclusion of
condensed rings [sk-def-sfb-condensed-ring].

1. The derived extension of scalars [sk-def-sfb-derived-extension-of-scalars]
   $$
   E\otimes^{\mathrm L}_{\cO_E}-:=L(\operatorname{Ext}_\varphi)\colon D(\Mod_{\cO_{E,X}})\to D(\Mod_{E_X})
   $$
   sends bounded constructible complexes to bounded constructible complexes
   [sk-def-sfb-bounded-constructible]. It therefore restricts to a functor
   $E\otimes^{\mathrm L}_{\cO_E}-\colon D_{\mathrm{cons}}(X_{\mathrm{proét}},\cO_E)\to D_{\mathrm{cons}}(X_{\mathrm{proét}},E)$.
2. Let $X$ be topologically Noetherian. Then the restricted functor is a localization at
   the morphisms of $D_{\mathrm{cons}}(X_{\mathrm{proét}},\cO_E)$ whose mapping cone is
   killed by a power of $\ell$. Hence, with the rationalization of
   [sk-def-sfb-rationalization] at the powers of $\ell$, there is an equivalence
   $$
   D_{\mathrm{cons}}(X_{\mathrm{proét}},\cO_E)[\ell^{-1}]\simeq D_{\mathrm{cons}}(X_{\mathrm{proét}},E),
   $$
   under which the localization functor corresponds to $E\otimes^{\mathrm L}_{\cO_E}-$.

The statement concerns bounded constructible complexes only. On the full derived
categories, $E\otimes^{\mathrm L}_{\cO_E}-$ is not a localization at the morphisms with
$\ell$-power-torsion cone in general. Neither of $D_{\mathrm{cons}}(X_{\mathrm{proét}},E)$
and $D_{\mathrm{cons}}(X_{\mathrm{proét}},\cO_E)[\ell^{-1}]$ is taken as the definition of
the other. Finiteness of $E$ is what makes inverting $\ell$ the right statement: every
nonzero element of the discrete valuation ring $\cO_E$ divides a power of $\ell$.
