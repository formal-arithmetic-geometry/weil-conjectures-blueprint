+++
id = "theorem-f-shriek-finite-coefficients"
kind = "theorem"
title = "$f^!$ with finite coefficients"
order = 586
lean = ["AlgebraicGeometry.ProEtale.constructibleFiniteTor_rightDerivedUpperShriek", "AlgebraicGeometry.Etale.exists_shift_constructibleTorAmplitudeIn_rightDerivedUpperShriek", "AlgebraicGeometry.ProEtale.DerivedCategoryFiniteTor.rightDerivedLowerShriekAdjunction"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
+++
For every separated morphism $f:X\to Y$ of finite type, the right adjoint
$f^!:\Loc(D^b_{\mathrm{ctf}}(Y,A))\to\Loc(D^b_{\mathrm{ctf}}(X,A))$ of
Theorem [theorem-existence-exceptional-inverse-image] maps $D^b_{\mathrm{ctf}}(Y,A)$ into $D^b_{\mathrm{ctf}}(X,A)$.
Consequently, its adjunction restricts to

$$
Rf_!:D^b_{\mathrm{ctf}}(X,A)\ \rightleftarrows\ D^b_{\mathrm{ctf}}(Y,A):f^!.
$$
