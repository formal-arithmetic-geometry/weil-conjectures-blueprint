+++
id = "lem-weil-derived-direct-image-composition"
kind = "lemma"
title = "Composition of derived direct images"
order = 1950
lean = ["AlgebraicGeometry.ProEtale.rightDerivedLowerStarComp", "AlgebraicGeometry.ProEtale.rightDerivedLowerStarComp_id_left", "AlgebraicGeometry.ProEtale.rightDerivedLowerStarComp_id_right", "AlgebraicGeometry.ProEtale.rightDerivedLowerStarComp_assoc", "AlgebraicGeometry.Etale.rightDerivedLowerStarComp", "AlgebraicGeometry.ProEtale.CondensedRing.leftDerivedUpperStarComp", "AlgebraicGeometry.ProEtale.CondensedRing.leftDerivedUpperStarComp_assoc_app", "AlgebraicGeometry.ProEtale.CondensedRing.derivedUpperStarLowerStarAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerStarComp"]
uses = ["def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-sp-kinjective-bridge", "lem-sp-kinjective-computes", "lem-weil-pbc-direct-image-preserves-injectives", "def-sfb-module-upper-lower-adjunction", "det-prop-sfb-module-pullback-exact-main", "def-sfb-module-lower-star-comp"]
+++
Let $X\xrightarrow{f}Y\xrightarrow{g}Z$ be morphisms of schemes, and use the derived direct images of
[def-weil-derived-direct-image]. There is a canonical isomorphism

$$
 c_{g,f}:R(g\circ f)_*\xrightarrow{\ \sim\ }Rg_*\circ Rf_*
$$

as functors $D(X_{\mathrm{proét}},\Lambda)\to D(Z_{\mathrm{proét}},\Lambda)$ of
the derived categories of $\Lambda$-modules, for every commutative condensed
ring $\Lambda$, and on the étale site. The cases used later are:

1. at finite level $\Lambda=A_{E,n}$;
1. for $\Lambda=\mathcal O_E$;
1. for $\Lambda=E$;
1. for $\Lambda=\Qlb$;
1. on the small étale site, for any ring $A$ (more generally for sheaves with
values in a Grothendieck abelian category), as functors
$D(X_{\mathrm{et}},A)\to D(Z_{\mathrm{et}},A)$ between the ordinary
derived categories of étale sheaves of $A$-modules.

In cases (1)–(4) the isomorphism restricts to the bounded constructible
categories whenever $Rf_*$ and $Rg_*$ preserve them.

The isomorphism $c_{g,f}$ is natural in $K$, is the identity when $f$ or $g$
is an identity, and is associative: for a further morphism $h:Z\to W$ the
two isomorphisms $R(hgf)_*\cong Rh_*Rg_*Rf_*$ built from $c$ agree. In
particular it is compatible with transport of structure along automorphisms
of $X,Y,Z$ commuting with $f$ and $g$ (such as Frobenius), since the direct
image along an automorphism $\sigma$ is the inverse image along
$\sigma^{-1}$.
