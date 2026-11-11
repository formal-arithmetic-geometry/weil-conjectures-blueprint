+++
id = "proposition-purity-trace-commute-frobenius"
kind = "proposition"
title = "Purity and trace commute with Frobenius"
order = 882
lean = ["AlgebraicGeometry.Etale.isWeilMorphism_smoothPurityIso_hom", "AlgebraicGeometry.Etale.isWeilMorphism_smoothCoefficientTrace", "AlgebraicGeometry.Etale.PurityFrobeniusDatum.isWeilMorphism_schemeFrobenius_smoothPurityIso_hom", "AlgebraicGeometry.Etale.PurityFrobeniusDatum.isWeilMorphism_schemeFrobenius_smoothCoefficientTrace", "AlgebraicGeometry.WeilComplex.nonempty_derivedLowerShriek_adjunction_of_smooth_of_isSeparated", "AlgebraicGeometry.WeilComplex.nonempty_derivedLowerShriek_adjunction_of_smooth"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-composition-open-restriction-compactifications-f", "definition-relative-dualizing-complex", "proposition-smooth-purity-finite-coefficients", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
