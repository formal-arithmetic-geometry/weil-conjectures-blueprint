+++
id = "proposition-smooth-purity-finite-coefficients"
kind = "proposition"
title = "Smooth purity with finite coefficients"
order = 759
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_twistShift", "AlgebraicGeometry.Etale.smoothPurityIso"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "definition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $A$ be any finite admissible coefficient ring, and let
$f:X\to Y$ be smooth of pure relative dimension $d$.
For $K\in D^b_{\mathrm{ctf}}(Y_{\mathrm{pro}\acute{e}t},A)$ there is a canonical
isomorphism, natural in $K$,

$$
f_A^{*}K(d)[2d]
\xrightarrow{\ \gamma_{f,A}(K)\ }f_A^{!}K.
\tag{9.15}
$$
