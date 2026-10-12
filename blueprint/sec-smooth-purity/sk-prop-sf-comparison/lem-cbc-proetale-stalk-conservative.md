+++
id = "lem-cbc-proetale-stalk-conservative"
kind = "lemma"
title = "Detecting isomorphisms on the pro-etale site"
order = 1993
uses = ["def-weil-pbc-ind-etale-basis", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "lem-weil-pbc-ind-etale-basis", "lemma-weil-pbc-geometric-stalk-conservative", "thm-weil-pbc-site-comparison"]
+++
Let $\Lambda$ be a finite discrete ring and let $T$ be a scheme.

1. *locality for covering families.* A morphism
$F\to G$ of complexes of $\Lambda$-module sheaves on
$T_{\Proet}$ is an isomorphism if and only if its inverse image
along every member of one
pro-etale covering family
of $T$ is an isomorphism. Equivalently: a complex on
$T_{\Proet}$ is acyclic if and only if its cohomology sheaves
vanish, and a sheaf on $T_{\Proet}$ vanishes if and only if it
vanishes after inverse image along the members of a covering family.
1. *detection on the affine ind-etale basis.* For affine
$T$, a sheaf on $T_{\Proet}$ vanishes if and only if its sections
on every object of the affine ind-etale basis
[def-weil-pbc-ind-etale-basis] vanish; consequently a morphism
of complexes on $T_{\Proet}$ is an isomorphism if and only if it
induces a quasi-isomorphism of sections on every object of that
basis. For general $T$ the same holds with the bases of the
members of an affine open cover.
1. *complexes of etale origin.* Let
$\nu_T:T_{\Proet}\to T_{\Et}$ be the comparison morphism of
[def-weil-pbc-site-comparison-morphism] and let
$F'\to G'$ be a morphism of bounded-below complexes of etale
$\Lambda$-sheaves. Then $\nu_T^*F'\to\nu_T^*G'$ is an
isomorphism if and only if it is an isomorphism at every geometric
point of $T$. In particular the geometric-point stalks are
jointly conservative on the bounded constructible objects
$\Dbc(T_{\Proet},\Lambda)$, which are of etale origin by
[def-weil-pbc-proetale-modules].
1. *warning.* None of this extends to arbitrary pro-etale
sheaves: the collection of geometric-point stalks is *not*
conservative on $\Sh(T_{\Proet})$. For
$T=\operatorname{Spec}k$ with $k$ algebraically closed and a
nonzero abelian group $A$, the sheafified quotient of functions
modulo locally constant functions, $\mathcal F(U)=\{\text{functions } U\to A\}/\{\text{locally constant functions}\}$, has
$\mathcal F(T)=0$ while $\mathcal F\neq0$, the site
$T_{\Proet}$ containing affine objects with infinitely many points
(Stacks Project, Pro-étale Cohomology, Section 61.18,
[Tag 0991](https://stacks.math.columbia.edu/tag/0991)).
