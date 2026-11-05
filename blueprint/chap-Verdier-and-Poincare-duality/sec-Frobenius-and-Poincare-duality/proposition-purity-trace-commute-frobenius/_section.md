+++
id = "proposition-purity-trace-commute-frobenius"
kind = "proposition"
title = "Purity and trace commute with Frobenius"
order = 881
lean = ["AlgebraicGeometry.Etale.isWeilMorphism_smoothPurityIso_hom", "AlgebraicGeometry.Etale.isWeilMorphism_smoothCoefficientTrace", "AlgebraicGeometry.Etale.PurityFrobeniusDatum.isWeilMorphism_schemeFrobenius_smoothPurityIso_hom", "AlgebraicGeometry.Etale.PurityFrobeniusDatum.isWeilMorphism_schemeFrobenius_smoothCoefficientTrace"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "definition-relative-dualizing-complex", "proposition-smooth-purity-finite-coefficients", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
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
