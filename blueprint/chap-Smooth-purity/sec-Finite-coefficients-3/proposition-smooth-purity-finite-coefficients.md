+++
id = "proposition-smooth-purity-finite-coefficients"
kind = "proposition"
title = "Smooth purity with finite coefficients"
order = 752
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_twistShift", "AlgebraicGeometry.Etale.smoothPurityIso"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "definition-relative-dualizing-complex", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
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
