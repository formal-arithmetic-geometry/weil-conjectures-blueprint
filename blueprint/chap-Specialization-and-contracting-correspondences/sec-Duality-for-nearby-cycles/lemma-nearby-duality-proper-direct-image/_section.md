+++
id = "lemma-nearby-duality-proper-direct-image"
kind = "lemma"
title = "Duality for nearby cycles and proper direct image"
order = 1678
lean = ["CategoryTheory.Verdier.nearbyDualityMap_proper", "CategoryTheory.Verdier.nearbyDualityMap_restrict", "AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_lowerStar_nearbyDualityMap_of_isProper", "AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.pushforwardExchange_comp_lowerStar_map_nearbyDualityMap"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "corollary-evaluation-weakly-contractible-objects", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "definition-relative-dualizing-complex", "definition-verdier-dual-evaluation", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian", "lemma-sheaves-finite-support-finite-morphisms"]
+++
Let $f:X\to Y$ be a proper morphism of separated $S$-schemes of finite
type, and let $M\in D^b_{\mathrm{ctf}}(X_\eta,A)$. Under the
isomorphism $\chi_f$ and the Verdier duality isomorphisms
$Rf_*\mathbb D\simeq\mathbb DRf_*$ of Chapter [chap-Verdier-and-Poincare-duality] on
both fibres,

$$
Rf_{s*}\delta_{X,M}\quad\text{is identified with}\quad
\delta_{Y,Rf_{\eta*}M}.
\tag{E.13}
$$

For an open immersion $j:U\to X$, the restriction $j_s^*\delta_{X,M}$ is
$\delta_{U,j_\eta^*M}$ under the base change isomorphism $\alpha_j$. If
$X$ is proper over $S$, then under global Verdier duality on both fibres

$$
R\Gamma(X_s,\delta_{X,M})
\quad\text{is identified with the identity of}\quad
R\operatorname{Hom}_A(R\Gamma(X_{\bar\eta},M),A).
\tag{E.14}
$$
