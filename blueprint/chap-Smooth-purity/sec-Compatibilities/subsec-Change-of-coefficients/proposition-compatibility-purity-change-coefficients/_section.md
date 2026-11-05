+++
id = "proposition-compatibility-purity-change-coefficients"
kind = "proposition"
title = "Compatibility of purity with change of coefficients"
order = 811
lean = ["AlgebraicGeometry.Etale.map_smoothPurityIso_hom_comp", "AlgebraicGeometry.Etale.map_smoothPurityTrace"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "definition-relative-dualizing-complex", "proposition-smooth-purity-finite-coefficients", "definition-trace-map", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$, let
$\Lambda\to\Lambda'$ be a coefficient map of
Proposition [proposition-six-operations-change-coefficients] and let
$K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$. Then the change-of-coefficients isomorphism
$(f^!K)_{\Lambda'}\to f^!(K_{\Lambda'})$ carries
$(\gamma_{f,\Lambda}(K))_{\Lambda'}$ to $\gamma_{f,\Lambda'}(K_{\Lambda'})$, the
sources being identified by the change-of-coefficients isomorphism for $f^*$.
The same holds for the trace maps: the change-of-coefficients isomorphism for
$Rf_!$ carries $(\operatorname{Tr}_{f,\Lambda}(K))_{\Lambda'}$ to
$\operatorname{Tr}_{f,\Lambda'}(K_{\Lambda'})$.
