+++
id = "proposition-base-change-fourier-inversion"
kind = "proposition"
title = "Base change and stalks"
order = 1232
lean = ["AlgebraicGeometry.nonempty_iso_fourierTransform_comp_upperStar", "AlgebraicGeometry.nonempty_iso_tensorLisse_upperStar_comp_fourierTransform"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "lemma-structure-integral-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "lemma-artin-schreier-character-sheaf", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Let $g:S'\to S$ be a morphism of schemes with $S'$ of finite type over
$k_0$ or over $k$, let $V'=V\times_SS'$, and
let $g_V:V'\to V$ and $g_{V^\vee}:V'^\vee\to V^\vee$ be the projections.

1. The proper base change isomorphism for $p_2$ induces an
   isomorphism $g_{V^\vee}^*\operatorname{FT}_\psi(K)\simeq
  \operatorname{FT}_\psi(g_V^*K)$.
2. For $N\in\Dbc(S,E)$, the projection formula for $p_2$ induces an
   isomorphism $\operatorname{FT}_\psi(K\otimes\pi^*N)\simeq
  \operatorname{FT}_\psi(K)\otimes\pi^{\vee*}N$, where $\pi:V\to S$ and
   $\pi^\vee:V^\vee\to S$ are the projections.
3. For a geometric point $\bar y$ of $V^\vee$, the proper base change
   map gives
   $$
   (\operatorname{FT}_\psi K)_{\bar y}
   \simeq
   R\Gamma_c\bigl(V_{\bar y},
   K|_{V_{\bar y}}\otimes
   \mathcal L_{\psi\langle x,y\rangle}\bigr)[r].
   \tag{16.2}
   $$
