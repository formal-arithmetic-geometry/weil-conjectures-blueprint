+++
id = "prop-constructible-derived-subcategory"
kind = "theorem"
title = "The constructible derived category"
order = 2645
lean = ["AlgebraicGeometry.Etale.DerivedCategory.boundedConstructible_isTriangulated", "AlgebraicGeometry.Etale.DerivedCategory.constructibleHomology_isTriangulated", "DerivedCategory.homologyProperty_isTriangulated"]
tags = ["latex:proposition"]
uses = ["def-constructible-constructible", "thm-constructible-serre"]
+++
Let $\mathcal A$ be a Grothendieck abelian coefficient category (for
instance $\mathcal A=\mathrm{Mod}_\Lambda$), and assume that the
constructible sheaves in $\shv{\et X}$ are closed under kernels, cokernels
and extensions. Then the full subcategory of the derived category
$D(\shv{\et X})$ consisting of the complexes all of whose cohomology
sheaves are constructible is a triangulated subcategory, and so is its full
subcategory $D^b_c(\et X)$ of bounded such complexes.

More generally, in the derived category of any abelian category, the
complexes all of whose cohomology objects lie in a class of objects that
contains zero and is closed under isomorphisms, kernels, cokernels and
extensions form a triangulated subcategory.
