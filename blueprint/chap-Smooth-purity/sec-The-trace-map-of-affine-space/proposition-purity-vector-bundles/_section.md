+++
id = "proposition-purity-vector-bundles"
kind = "proposition"
title = "Purity for vector bundles"
order = 740
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_affineSpace", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_affineSpaceZero"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
+++
Let $\pi:V\to S$ be a vector bundle of rank $d$.
For $K\in D^b_{\mathrm{ctf}}(S_{\mathrm{pro}\acute{e}t},\mathbf Z/\ell^n\mathbf Z)$, the trace map induces an
isomorphism

$$
\pi^{*}K(d)[2d]\xrightarrow{\sim}\pi^{!}K.
$$
