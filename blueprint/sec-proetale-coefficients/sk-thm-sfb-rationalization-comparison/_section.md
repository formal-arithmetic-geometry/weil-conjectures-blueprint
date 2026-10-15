+++
id = "sk-thm-sfb-rationalization-comparison"
kind = "proposition"
title = "Rationalization"
order = 743
uses = ["sk-def-sfb-derived-extension-of-scalars", "sk-def-sfb-rationalization", "sk-def-sfb-bounded-constructible", "sk-prop-sfb-qlbar-colimit-x"]
lean = ["AlgebraicGeometry.ProEtale.padicIntegersRingObjToContinuousMapRingObj", "AlgebraicGeometry.ProEtale.padicIntegersToPadicSubfield", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalars_obj", "AlgebraicGeometry.ProEtale.boundedConstructibleExtendScalars", "AlgebraicGeometry.ProEtale.boundedConstructibleExtendScalarsCompatibility", "AlgebraicGeometry.ProEtale.isLocalization_boundedConstructibleExtendScalars", "AlgebraicGeometry.ProEtale.rationalizationEquivalence", "AlgebraicGeometry.ProEtale.rationalizationQCompEquivalenceIso"]
tags = ["sketch"]
+++
Let $X$ be a scheme and $E/\mathbf Q_\ell$ finite, with coefficient rings $\cO_{E,X}$ and
$E_X$ on $X_{\mathrm{proét}}$ ([sk-prop-sfb-qlbar-colimit-x]). Passing from $\cO_E$ to $E$
means inverting $\ell$, and on derived categories this is a Verdier localization:
extension of scalars
$$
E_X\otimes_{\cO_{E,X}}-\colon D(X_{\mathrm{proét}},\cO_E)\to D(X_{\mathrm{proét}},E)
$$
identifies $D(X_{\mathrm{proét}},E)$ with the Verdier quotient of
$D(X_{\mathrm{proét}},\cO_E)$ by the complexes $K$ with $H^q(K)[1/\ell]=0$ for all $q$.

**Bounded constructible complexes.** The kernel is larger than one might first guess:
$\bigoplus_{n\ge1}\cO_{E,X}/\ell^n$ lies in it, although no single power of $\ell$ kills it.
On bounded constructible complexes ([sk-def-sfb-bounded-constructible]) this cannot
happen. There a complex killed by inverting $\ell$ is killed by a fixed power of $\ell$,
and extension of scalars induces an equivalence
$$
\Dbc(X,\cO_E)[\ell^{-1}]\xrightarrow{\ \sim\ }\Dbc(X,E),
$$
where the left side has the objects of $\Dbc(X,\cO_E)$ and Hom groups tensored with $E$
(Bhatt–Scholze, Proposition 6.8.14(2)); compare the rationalization of
[sk-def-sfb-rationalization]. The Hom part of this statement is the localized Hom formula
of the smooth-purity chapter. For essential surjectivity, the integral generators of
[sk-lem-integral-models] (4) are used: by the Hom statement, a connecting morphism between
them lifts to an integral one after multiplying by a power of $\ell$, so finite cones of
the generators also have integral models.
