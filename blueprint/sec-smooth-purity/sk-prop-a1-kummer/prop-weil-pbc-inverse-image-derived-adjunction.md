+++
id = "prop-weil-pbc-inverse-image-derived-adjunction"
kind = "theorem"
title = "Derived adjunction of inverse image"
order = 1952
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-weil-pbc-kinjective-resolutions", "def-weil-pbc-scheme-conventions", "prop-weil-pbc-inverse-image-exact", "prop-weil-pbc-kinjective-resolutions-exist"]
tags = ["latex:proposition"]
+++
For a morphism [def-weil-pbc-scheme-conventions] $u:U\to V$, inverse image
acts termwise on complexes and induces an adjunction

$$
 u^{-1}:\Dplus(V_{\Et})\rightleftarrows\Dplus(U_{\Et}):Ru_*
$$

on the derived categories [def-weil-pbc-derived-categories], whose unit and
counit extend the unit $\eta_u$ and the counit $\varepsilon_u$ of
[def-weil-pbc-inverse-image].

## Proof

By [prop-weil-pbc-inverse-image-exact] the functor $u^{-1}$ of
[def-weil-pbc-inverse-image] is exact, so applying it term by term to
complexes is an exact functor on the complex categories of
[def-weil-pbc-derived-categories] which preserves quasi-isomorphisms and
therefore descends to a triangulated functor on the derived categories. For
the adjunction, let $K\in\Dplus(V_{\Et})$, let $L\in\Dplus(U_{\Et})$, and
choose a K-injective resolution $L\to J$, which exists by
[prop-weil-pbc-kinjective-resolutions-exist] and is K-injective in the sense
of [def-weil-pbc-kinjective-resolutions]. Since the direct image $u_*$ of
[def-weil-pbc-direct-image] is right adjoint to the exact functor $u^{-1}$,
it carries K-injective complexes to K-injective complexes (Stacks Project,
Lemma 13.31.9, Tag [08BJ](https://stacks.math.columbia.edu/tag/08BJ)), and
the right derived functor of $u_*$ is computed by K-injective resolutions
(Stacks Project, Lemma 13.31.7, Tag
[070K](https://stacks.math.columbia.edu/tag/070K)), so that $Ru_*L=u_*J$ for
such a resolution. For K-injective $J$ the group of maps in the derived
category is the group of homotopy classes of maps (Stacks Project, Lemma
13.31.2, Tag [070I](https://stacks.math.columbia.edu/tag/070I)), so

$$
 \Hom_{\Dplus(U_{\Et})}(u^{-1}K,L)
 =\Hom_{K(U_{\Et})}(u^{-1}K,J)
 =\Hom_{K(V_{\Et})}(K,u_*J)
 =\Hom_{\Dplus(V_{\Et})}(K,Ru_*L),
$$

the middle equality being the termwise adjunction of
[def-weil-pbc-inverse-image]. These bijections are natural in $K$ and $L$,
and the unit and counit of the induced adjunction are the images of the unit
and counit of the underived adjunction of
[def-weil-pbc-inverse-image]; hence $u^{-1}\dashv Ru_*$ on the bounded-below
derived categories.
