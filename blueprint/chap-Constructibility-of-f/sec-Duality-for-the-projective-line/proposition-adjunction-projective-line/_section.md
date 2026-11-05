+++
id = "proposition-adjunction-projective-line"
kind = "proposition"
title = "The adjunction for the projective line"
order = 554
lean = ["AlgebraicGeometry.Etale.exists_projectiveLineAdjunction", "AlgebraicGeometry.Etale.projectiveLineAdjunctionBaseChange_of_isNormalized"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "lemma-kunneth-field-coefficients", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
