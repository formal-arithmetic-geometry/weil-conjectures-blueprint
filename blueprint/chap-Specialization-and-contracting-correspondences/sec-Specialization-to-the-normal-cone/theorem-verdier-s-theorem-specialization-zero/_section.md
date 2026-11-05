+++
id = "theorem-verdier-s-theorem-specialization-zero"
kind = "theorem"
title = "Verdier's theorem on specialization to the zero section"
order = 1644
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_zeroSectionMap", "AlgebraicGeometry.ProEtale.CondensedRing.isZero_specializationDefect", "AlgebraicGeometry.ProEtale.CondensedRing.isZero_upperStar_zeroSection_specialization"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "corollary-evaluation-weakly-contractible-objects", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-reduction-derived-nakayama", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-inverting-ell", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "definition-change-of-coefficients-maps", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "definition-deformation-normal-bundle", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian", "lemma-sheaves-finite-support-finite-morphisms", "lemma-functoriality-deformation"]
+++
For every separated $k$-scheme $X$ of finite type, every closed subscheme
$Z\subset X$, and $K\in D^b_{\mathrm{ctf}}(X,A)$, the
map (E.1)

$$
\tau_{X,Z}(K):z^*\operatorname{Sp}_{X,Z}(K)\longrightarrow i^*K
$$

is an isomorphism.  In particular, $i^*K=0$ implies
$z^*\operatorname{Sp}_{X,Z}(K)=0$.
