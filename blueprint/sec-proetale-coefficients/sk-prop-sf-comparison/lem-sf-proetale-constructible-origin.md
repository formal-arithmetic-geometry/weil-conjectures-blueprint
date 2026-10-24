+++
id = "lem-sf-proetale-constructible-origin"
kind = "lemma"
title = "Constructible pro-étale coefficients are of étale origin"
lean = ["AlgebraicGeometry.ProEtale.isConstructible_iff_exists_isConstructibleSheaf_iso_comparisonUpperStar_obj", "AlgebraicGeometry.ProEtale.full_comparisonUpperStar", "AlgebraicGeometry.ProEtale.faithful_comparisonUpperStar", "AlgebraicGeometry.ProEtale.bijective_comparisonUpperStar_mapDerivedCategory_map", "AlgebraicGeometry.ProEtale.DerivedCategory.boundedConstructible_iff", "AlgebraicGeometry.ProEtale.DerivedCategory.boundedConstructibleIntrinsic", "AlgebraicGeometry.ProEtale.DerivedCategory.boundedConstructible_le_boundedConstructibleIntrinsic"]
order = 1036
uses = ["def-weil-finite-torsion-constructibility", "def-weil-pbc-constructible-complexes", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "lem-cbc-proetale-stalk-conservative", "thm-weil-pbc-site-comparison"]
+++
Let $A$ be a finite commutative ring (for instance $A=A_{E,n}$ for the global
finite-field datum, a prime $\ell\ne p$ and an integer $n\geq1$), and let $T$
be a scheme. Write
$\nu_T:T_{\Proet}\to T_{\Et}$ for the
comparison morphism of
sites. Call a sheaf of $A$-modules on $T_{\Et}$ constructible when it
satisfies the condition of [def-weil-pbc-constructible-complexes], and
call a sheaf of $A$-modules on $T_{\Proet}$ constructible when it
satisfies the intrinsic condition of
[def-weil-finite-torsion-constructibility]: there is a finite disjoint
partition of $T$ into locally closed constructible subschemes on each of
which the restriction is locally constant with finite $A$-module stalks.

1. **(i)** The pullback $\nu_T^*$ induces an equivalence of categories
between the constructible sheaves of $A$-modules on $T_{\Et}$ and the
constructible sheaves of $A$-modules on $T_{\Proet}$.
1. **(ii)** Consequently $\nu_T^*$ induces an equivalence between the
bounded complexes with constructible cohomology sheaves on the two sites.
In particular the two readings of the bounded constructible pro-étale
category — the intrinsic one of
[def-weil-finite-torsion-constructibility] and the one by étale
origin of [def-weil-pbc-proetale-modules], recorded in clause (3) of
[lem-cbc-proetale-stalk-conservative] — agree.
