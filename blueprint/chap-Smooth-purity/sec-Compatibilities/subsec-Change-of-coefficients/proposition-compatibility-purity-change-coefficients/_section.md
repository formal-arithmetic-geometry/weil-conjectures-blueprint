+++
id = "proposition-compatibility-purity-change-coefficients"
kind = "proposition"
title = "Compatibility of purity with change of coefficients"
order = 812
lean = ["AlgebraicGeometry.Etale.map_smoothPurityIso_hom_comp", "AlgebraicGeometry.Etale.map_smoothPurityTrace"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "definition-relative-dualizing-complex", "proposition-smooth-purity-finite-coefficients", "proposition-sp-unique-adjoint", "definition-trace-map", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
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
