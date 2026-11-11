+++
id = "lemma-nearby-duality-proper-direct-image"
kind = "lemma"
title = "Duality for nearby cycles and proper direct image"
order = 1678
lean = ["CategoryTheory.Verdier.nearbyDualityMap_proper", "CategoryTheory.Verdier.nearbyDualityMap_restrict", "AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_lowerStar_nearbyDualityMap_of_isProper", "AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.pushforwardExchange_comp_lowerStar_map_nearbyDualityMap"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-w-local-components", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "theorem-enough-affine-weakly-contractible-objects", "definition-weak-contractibility", "corollary-evaluation-weakly-contractible-objects", "proposition-exact-products", "proposition-milnor-sequence", "corollary-continuity-cohomology", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "theorem-comparison-direct-images", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-inverse-image-coefficient-sheaves", "lemma-reduction-derived-nakayama", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-integral-models", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-pro-etale-base-change-map", "theorem-comparison-over-henselian-pair-degree", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-completed-ordinary-base-change", "proposition-proper-direct-image-constructible-complexes", "proposition-comparison-etale-derived-category", "lemma-inverse-image-tensor-product", "proposition-construction-independence-rf-shriek", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "proposition-sp-unique-adjoint", "definition-sp-scalar-extension", "definition-verdier-dual-evaluation", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology", "lemma-sheaves-finite-support-finite-morphisms"]
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
