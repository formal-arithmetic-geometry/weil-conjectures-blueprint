+++
id = "lemma-nearby-duality-proper-direct-image"
kind = "lemma"
title = "Duality for nearby cycles and proper direct image"
order = 1676
lean = ["CategoryTheory.Verdier.nearbyDualityMap_proper", "CategoryTheory.Verdier.nearbyDualityMap_restrict", "AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_lowerStar_nearbyDualityMap_of_isProper"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-w-local-components", "example-locally-constant-functions-w-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "theorem-enough-affine-weakly-contractible-objects", "definition-weak-contractibility", "corollary-evaluation-weakly-contractible-objects", "proposition-milnor-sequence", "corollary-continuity-cohomology", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-pro-etale-base-change-map", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-change-coefficients", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "definition-verdier-dual-evaluation", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology", "lemma-sheaves-finite-support-finite-morphisms"]
+++
Let $f:X\to Y$ be a proper morphism of separated $S$-schemes of finite
type, and let $M\in D^b_{\mathrm{ctf}}(X_\eta,A)$. Under the
isomorphism $\chi_f$ and the Verdier duality isomorphisms
$Rf_*\mathbb D\simeq\mathbb DRf_*$ of Section [chap-Verdier-and-Poincare-duality] on
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
