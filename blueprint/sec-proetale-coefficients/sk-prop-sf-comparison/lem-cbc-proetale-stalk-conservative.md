+++
id = "lem-cbc-proetale-stalk-conservative"
kind = "lemma"
title = "Detecting isomorphisms on the pro-etale site"
order = 1034
lean = ["CategoryTheory.Sheaf.isIso_iff_of_coversTop", "AlgebraicGeometry.ProEtale.upperStarIsoLocalizationRestriction", "AlgebraicGeometry.ProEtale.isIso_of_isIso_app_affineProEt", "AlgebraicGeometry.ProEtale.ShortComplex.exact_of_exact_sectionsFunctor", "AlgebraicGeometry.ProEtale.full_comparisonUpperStar", "AlgebraicGeometry.ProEtale.faithful_comparisonUpperStar", "AlgebraicGeometry.Scheme.isIso_of_isIso_sheafFiber_map", "AlgebraicGeometry.ProEtale.bijective_comparisonUpperStar_mapDerivedCategory_map"]
uses = ["def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "lem-weil-pbc-ind-etale-basis", "lem-weil-pbc-proetale-restriction-injectives", "lemma-weil-pbc-geometric-stalk-conservative", "thm-weil-pbc-site-comparison"]
+++
Let $\Lambda$ be a ring and let $T$ be a scheme.

1. *locality for covering families.* Let $\{g_i\colon W_i\to T\}$ be a
pro-etale covering family. A morphism $\varphi\colon F\to G$ of sheaves of
$\Lambda$-modules on $T_{\Proet}$ is an isomorphism if and only if every
inverse image $g_i^*\varphi$ is an isomorphism. Consequently a sheaf on
$T_{\Proet}$ vanishes if and only if its inverse images along all $g_i$
vanish, and a morphism of complexes of $\Lambda$-module sheaves on $T_{\Proet}$
is a quasi-isomorphism if and only if its inverse images along all $g_i$ are.
1. *detection on the affine pro-etale site.* Call an object of $T_{\Proet}$
affine pro-etale if it is a cofiltered limit of affine etale $T$-schemes. A
morphism of sheaves on $T_{\Proet}$ is an isomorphism if it induces an
isomorphism on sections over every affine pro-etale object; in particular a
sheaf vanishes if its sections over every affine pro-etale object vanish. A
short complex of sheaves on $T_{\Proet}$ is exact if its sections over every
affine pro-etale object form an exact sequence; consequently a morphism of
complexes is a quasi-isomorphism if it induces quasi-isomorphisms of sections
over every affine pro-etale object.
1. *complexes of etale origin.* Let $\nu_T\colon T_{\Proet}\to T_{\Et}$ be the
comparison morphism of [def-weil-pbc-site-comparison-morphism] and let
$\varphi\colon F'\to G'$ be a morphism of etale $\Lambda$-module sheaves. Then
$\nu_T^*\varphi$ is an isomorphism if and only if $\varphi$ is, if and only if
$\varphi$ induces an isomorphism of geometric stalks at the geometric point
$\bar s$ over every point $s\in T$, at an algebraic closure of
$\kappa(s)$. For a morphism $\varphi$ of bounded-below complexes of etale
$\Lambda$-module sheaves, $\nu_T^*\varphi$ is an isomorphism in the derived
category if and only if $\varphi$ is. This applies to the bounded constructible
objects of $\Dbc(T_{\Proet},\Lambda)$, which are of etale origin by
[def-weil-pbc-proetale-modules].
