+++
id = "proposition-purity-trace-commute-frobenius"
kind = "proposition"
title = "Purity and trace commute with Frobenius"
order = 881
lean = ["AlgebraicGeometry.Etale.isWeilMorphism_smoothPurityIso_hom", "AlgebraicGeometry.Etale.isWeilMorphism_smoothCoefficientTrace", "AlgebraicGeometry.Etale.PurityFrobeniusDatum.isWeilMorphism_schemeFrobenius_smoothPurityIso_hom", "AlgebraicGeometry.Etale.PurityFrobeniusDatum.isWeilMorphism_schemeFrobenius_smoothCoefficientTrace"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "definition-relative-dualizing-complex", "proposition-smooth-purity-finite-coefficients", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Fix an admissible $\Lambda$, and let $K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$ and
$M\in D^b_{\mathrm{ctf}}(X,\Lambda)$. The square with horizontal arrows
$\operatorname{Fr}_X,\operatorname{Fr}_Y$ and vertical arrows $f,f$ is
cartesian, and its base change comparisons identify

$$
\operatorname{Fr}_X^*f^!K
\simeq f^!\operatorname{Fr}_Y^*K,
\qquad
\operatorname{Fr}_Y^*Rf_!M
\simeq Rf_!\operatorname{Fr}_X^*M.
\tag{10.9}
$$

With these identifications, and the Kummer identification
$\operatorname{Fr}_T^*\Lambda_T(1)\simeq\Lambda_T(1)$ for the twists,
we have

$$
\operatorname{Fr}_X^*\gamma_f(K)
=\gamma_f(\operatorname{Fr}_Y^*K),
\qquad
\operatorname{Fr}_Y^*\operatorname{Tr}_f(K)
=\operatorname{Tr}_f(\operatorname{Fr}_Y^*K).
$$
