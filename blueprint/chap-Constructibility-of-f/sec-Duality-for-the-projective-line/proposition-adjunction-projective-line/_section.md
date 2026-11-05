+++
id = "proposition-adjunction-projective-line"
kind = "proposition"
title = "The adjunction for the projective line"
order = 553
lean = ["AlgebraicGeometry.Etale.exists_projectiveLineAdjunction", "AlgebraicGeometry.Etale.projectiveLineAdjunctionBaseChange_of_isNormalized"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-exceptional-inverse-image-smooth-morphism", "lemma-kunneth-one-identity-factor", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
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
\tag{6.7}
$$

with unit (6.5) and counit (6.6). For every morphism
$g:S'\to S$ with $S'$ of finite type over $k$, the unit and counit
are compatible with base change along $g$. They are
also compatible with change of finite coefficients.
