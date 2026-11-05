+++
id = "theorem-f-shriek-finite-coefficients"
kind = "theorem"
title = "$f^!$ with finite coefficients"
order = 592
lean = ["AlgebraicGeometry.ProEtale.constructibleFiniteTor_rightDerivedUpperShriek", "AlgebraicGeometry.Etale.exists_shift_constructibleTorAmplitudeIn_rightDerivedUpperShriek", "AlgebraicGeometry.ProEtale.DerivedCategoryFiniteTor.rightDerivedLowerShriekAdjunction"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "proposition-comparison-immersions", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "corollary-open-direct-image-over-field", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
For every separated morphism $f:X\to Y$ of finite type, the right adjoint
$f^!:\Loc(D^b_{\mathrm{ctf}}(Y,A))\to\Loc(D^b_{\mathrm{ctf}}(X,A))$ of
Theorem [theorem-existence-exceptional-inverse-image] maps $D^b_{\mathrm{ctf}}(Y,A)$ into $D^b_{\mathrm{ctf}}(X,A)$.
Consequently, its adjunction restricts to

$$
Rf_!:D^b_{\mathrm{ctf}}(X,A)\ \rightleftarrows\ D^b_{\mathrm{ctf}}(Y,A):f^!.
$$
