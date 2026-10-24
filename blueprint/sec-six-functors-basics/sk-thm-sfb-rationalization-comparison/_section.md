+++
id = "sk-thm-sfb-rationalization-comparison"
kind = "proposition"
title = "Rationalization"
order = 2193
uses = ["sk-prop-sfb-module-derived-factorization", "sk-prop-sf-open-closed-triangle", "sk-prop-sfb-qlbar-colimit-x", "sk-lem-integral-models"]
lean = ["AlgebraicGeometry.ProEtale.padicIntegersRingObjToContinuousMapRingObj", "AlgebraicGeometry.ProEtale.padicIntegersToPadicSubfield", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalars_obj", "AlgebraicGeometry.ProEtale.boundedConstructibleExtendScalars", "AlgebraicGeometry.ProEtale.boundedConstructibleExtendScalarsCompatibility", "AlgebraicGeometry.ProEtale.isLocalization_boundedConstructibleExtendScalars", "AlgebraicGeometry.ProEtale.rationalizationEquivalence", "AlgebraicGeometry.ProEtale.rationalizationQCompEquivalenceIso", "CategoryTheory.Rationalization.tensorHomEquiv"]
tags = ["sketch"]
+++
Let $X$ be a scheme and $E/\mathbf Q_\ell$ finite, with coefficient rings $\cO_{E,X}$ and
$E_X$ on $X_{\mathrm{proét}}$ ([sk-prop-sfb-qlbar-colimit-x]) and the inclusion
$\varphi\colon\cO_{E,X}\to E_X$. Passing from $\cO_E$ to $E$ means inverting $\ell$.
The derived extension of scalars
$E\otimes^{\mathrm L}_{\cO_E}-=L(\operatorname{Ext}_\varphi)$
([det-def-sfb-derived-extension-of-scalars]) sends bounded constructible complexes
([det-def-sfb-bounded-constructible]) to bounded constructible complexes. Let the
underlying topological space of $X$ be Noetherian. Then the restricted functor
$E\otimes^{\mathrm L}_{\cO_E}-\colon\Dbc(X,\cO_E)\to\Dbc(X,E)$ is a localization at the
morphisms whose mapping cone is killed by some power of $\ell$, and it induces an
equivalence
$$
\Dbc(X,\cO_E)[\ell^{-1}]\xrightarrow{\ \sim\ }\Dbc(X,E)
$$
from the rationalization of [det-def-sfb-rationalization] at the powers of $\ell$. The left
side has the objects of $\Dbc(X,\cO_E)$ and Hom groups tensored with $E$
(Bhatt–Scholze, Proposition 6.8.14(2)). The Hom part of this statement is the localized Hom
formula of the smooth-purity chapter. For essential surjectivity, the integral generators of
[sk-lem-integral-models] (4) are used: by the Hom statement, a connecting morphism between
them lifts to an integral one after multiplying by a power of $\ell$, so finite cones of
the generators also have integral models.
