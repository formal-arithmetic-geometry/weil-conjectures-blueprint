+++
id = "sk-def-sfb-derived-categories"
kind = "definition"
title = "Derived categories and derived functors"
order = 1620
uses = ["def-weil-abstract-derived-category", "def-weil-pbc-proetale-site"]
lean = ["DerivedCategory", "CategoryTheory.Abelian.hasKInjectiveResolutions_of_isGrothendieckAbelian", "CategoryTheory.Functor.rightDerivedFunctor", "CategoryTheory.Functor.rightDerivedFunctorIsoMapDerivedCategory", "CategoryTheory.Functor.PreservesKFlatQuasiIso", "CategoryTheory.Functor.leftDerivedFunctor", "CategoryTheory.Functor.leftDerivedFunctorIsoMapDerivedCategory"]
tags = ["sketch"]
+++
All derived categories are unbounded. For an abelian category $\mathcal C$, $D(\mathcal C)$
is the localization of the category of cochain complexes in $\mathcal C$ at the
quasi-isomorphisms [def-weil-abstract-derived-category]. Its bounded below part
$D^+(\mathcal C)\subseteq D(\mathcal C)$ is the full subcategory of complexes whose
cohomology vanishes in all sufficiently negative degrees. Derived functors are total
derived functors on the unbounded categories, computed on resolutions:

- **Right derived functors.** Let $\mathcal C$ have K-injective resolutions, i.e. every
  complex admits a quasi-isomorphism to a K-injective complex. Then every additive
  functor $F\colon\mathcal C\to\mathcal D$ to an abelian category has a total right
  derived functor $RF\colon D(\mathcal C)\to D(\mathcal D)$, computed by applying $F$
  termwise to a K-injective resolution. Every Grothendieck abelian category has
  K-injective resolutions.
- **Left derived functors.** Let $\mathcal C$ be a monoidal abelian category with the
  following properties: its tensor product is additive in each variable; it has
  countable coproducts and exact $\mathbf Z$-indexed colimits, which tensoring with a
  fixed object on either side preserves; and it has functorial flat resolutions. Let
  $F\colon\mathcal C\to\mathcal D$ be additive and send quasi-isomorphisms between
  K-flat complexes to quasi-isomorphisms. Then $F$ has a total left derived functor
  $LF\colon D(\mathcal C)\to D(\mathcal D)$, computed by applying $F$ termwise to a
  K-flat resolution. Pullback, tensor product and extension of scalars are derived
  this way.
- **Exact functors.** If $F$ is exact, then $RF\cong D(F)$ and $LF\cong D(F)$, where
  $D(F)$ applies $F$ termwise.
- **Derived adjunctions.** Let $f\colon\mathcal C\rightleftarrows\mathcal D\colon g$ be
  an adjunction $f\dashv g$ of additive functors, with $f$ as in the second item and
  $\mathcal D$ with K-injective resolutions. Then $Lf\dashv Rg$.

The derived categories of this section are the following.

| Category | Definition |
|---|---|
| $D(X_{\mathrm{proét}},\mathcal A)$ | $D(\Sh(X_{\mathrm{proét}},\mathcal A))$, finite coefficients (layer A). Here $\mathcal A$ is a closed symmetric monoidal Grothendieck abelian category and $\Sh(X_{\mathrm{proét}},\mathcal A)$ carries the tensor product of [sk-def-sfb-sheaf-tensor]. |
| $D(\Mod_{\Lambda_X})$ | $D(\Mod(\Sh(X_{\mathrm{proét}},\Ab),\Lambda_X))$, non-finite coefficients (layer B), for the ring object $\Lambda_X$ of [sk-def-sfb-pulled-back-coefficients] and its module objects [sk-def-sfb-module-objects]. For $\Lambda=\underline{\cO}_E$ resp. $\underline E$ this is $D(X_{\mathrm{proét}},\cO_E)$ resp. $D(X_{\mathrm{proét}},E)$. |
| $D_{\mathrm{cons}}(X_{\mathrm{proét}},\mathcal R)$ | the bounded complexes with constructible cohomology in $D(\Mod_{\mathcal R})$, see [sk-def-sfb-bounded-constructible]. |
