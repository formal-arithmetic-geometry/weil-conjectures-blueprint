+++
id = "proposition-adjunction-projective-line"
kind = "proposition"
title = "The adjunction for the projective line"
order = 554
lean = ["AlgebraicGeometry.Etale.exists_projectiveLineAdjunction", "AlgebraicGeometry.Etale.projectiveLineAdjunctionBaseChange_of_isNormalized"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "proposition-construction-independence-rf-shriek", "proposition-forgetting-supports-composition", "lemma-cohomology-projective-line-trace", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
+++
Let $S$ be of finite type over $k$, and let $p:\mathbf P^1_S\to S$ be the
projection. The functors
$Rp_*:D((\mathbf P^1_S)_{\acute{e}t},A)\to
D(S_{\acute{e}t},A)$ and
$p^*(1)[2]:D(S_{\acute{e}t},A)\to
D((\mathbf P^1_S)_{\acute{e}t},A)$ form
an adjunction

$$
Rp_* \ \dashv\ p^*(1)[2],
\tag{6.9}
$$

with unit (6.7) and counit (6.8). For every morphism
$g:S'\to S$ with $S'$ of finite type over $k$, the unit and counit
are compatible with base change along $g$. They are
also compatible with change of finite coefficients.
