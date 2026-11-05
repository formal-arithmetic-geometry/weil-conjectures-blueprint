+++
id = "proposition-purity-vector-bundles"
kind = "proposition"
title = "Purity for vector bundles"
order = 741
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_affineSpace", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_affineSpaceZero"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $\pi:V\to S$ be a vector bundle of rank $d$.
For $K\in D^b_{\mathrm{ctf}}(S_{\mathrm{pro}\acute{e}t},\mathbf Z/\ell^n\mathbf Z)$, the trace map induces an
isomorphism

$$
\pi^{*}K(d)[2d]\xrightarrow{\sim}\pi^{!}K.
$$
