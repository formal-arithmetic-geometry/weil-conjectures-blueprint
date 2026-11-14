+++
id = "proposition-purity-trace-commute-frobenius"
kind = "proposition"
title = "Purity and trace commute with Frobenius"
order = 882
lean = ["AlgebraicGeometry.Etale.isWeilMorphism_smoothPurityIso_hom", "AlgebraicGeometry.Etale.isWeilMorphism_smoothCoefficientTrace", "AlgebraicGeometry.Etale.PurityFrobeniusDatum.isWeilMorphism_schemeFrobenius_smoothPurityIso_hom", "AlgebraicGeometry.Etale.PurityFrobeniusDatum.isWeilMorphism_schemeFrobenius_smoothCoefficientTrace", "AlgebraicGeometry.WeilComplex.nonempty_derivedLowerShriek_adjunction_of_smooth_of_isSeparated", "AlgebraicGeometry.WeilComplex.nonempty_derivedLowerShriek_adjunction_of_smooth"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "lemma-structure-integral-constructible-complexes", "proposition-construction-independence-rf-shriek", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-exceptional-inverse-image-smooth-morphism", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-smooth-purity-finite-coefficients", "proposition-sp-unique-adjoint", "proposition-weights-under-usual-operations", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
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
