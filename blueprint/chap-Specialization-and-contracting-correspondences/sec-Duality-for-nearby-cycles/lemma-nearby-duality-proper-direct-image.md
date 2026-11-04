+++
id = "lemma-nearby-duality-proper-direct-image"
kind = "lemma"
title = "Duality for nearby cycles and proper direct image"
order = 1667
lean = ["CategoryTheory.Verdier.nearbyDualityMap_proper", "CategoryTheory.Verdier.nearbyDualityMap_restrict", "AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_lowerStar_nearbyDualityMap_of_isProper"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-proper-direct-image-unbounded-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-dctf-x-qbar-2-colimit", "lemma-perfect-complexes-geometric-point", "definition-verdier-dual-evaluation", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $f:X\to Y$ be a proper morphism of separated $S$-schemes of finite
type, and let $M\in D^b_{\mathrm{ctf}}(X_\eta,A)$. Under the
isomorphism $\chi_f$ and the Verdier duality isomorphisms
$Rf_*\mathbb D\simeq\mathbb DRf_*$ of Section [chap-Verdier-and-Poincare-duality] on
both fibres,

$$
Rf_{s*}\delta_{X,M}\quad\text{is identified with}\quad
\delta_{Y,Rf_{\eta*}M}.
\tag{E.14}
$$

For an open immersion $j:U\to X$, the restriction $j_s^*\delta_{X,M}$ is
$\delta_{U,j_\eta^*M}$ under the base change isomorphism $\alpha_j$. If
$X$ is proper over $S$, then under global Verdier duality on both fibres

$$
R\Gamma(X_s,\delta_{X,M})
\quad\text{is identified with the identity of}\quad
R\operatorname{Hom}_A(R\Gamma(X_{\bar\eta},M),A).
\tag{E.15}
$$
