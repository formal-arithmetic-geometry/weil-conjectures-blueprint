+++
id = "lemma-identity-pasting--1"
kind = "lemma"
title = "Identity square"
order = 319002
aliases = ["bp-r095-1"]
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_id"]
+++
Let $A$ be a Grothendieck abelian category, for instance the category of
$\Lambda$-modules, let $f:X\to Y$ be a morphism of schemes, and let
$K\in D^+(X_{\acute{e}t},A)$. For the commutative square with vertical
maps $f,f$ and horizontal maps $\mathrm{id}_X,\mathrm{id}_Y$, the base
change map of [definition-derived-base-change-map] is the composite

$$
(\mathrm{id}_Y)^*Rf_*K
\xrightarrow{\sim}Rf_*K
\xrightarrow{\sim}Rf_*(\mathrm{id}_X)^*K,
$$

where the arrows come from the canonical identity isomorphisms of
pullback. This is an equality of natural transformations in $K$; under
these identifications the base change map is the identity.
