+++
id = "lemma-internal-adjunction-two-exchange-formulas"
kind = "lemma"
title = "Internal adjunction and two exchange formulas"
order = 830
lean = ["AlgebraicGeometry.Etale.nonempty_iso_verdierDual_leftDerivedUpperStar"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "lemma-integral-models", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "lemma-inverse-image-tensor-product", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "corollary-open-direct-image-over-field", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "definition-verdier-dual-evaluation", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Let $f:X\to Y$ be a morphism, $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ and
$L\in D^b_{\mathrm{ctf}}(Y,\Lambda)$. The map
(10.1) and the two maps derived from it
and defined above are isomorphisms

$$
\begin{align}
\cHom_Y(Rf_!K,L)&\simeq
Rf_*\cHom_X(K,f^!L),\tag{10.2}\\
e_K:\mathbb D_YRf_!K&\xrightarrow{\ \sim\ } Rf_*\mathbb D_XK,
\tag{10.3}\\
f^!\mathbb D_YL&\simeq\mathbb D_Xf^*L.
\tag{10.4}\end{align}
$$

If $f$ is proper, then the composite

$$
Rf_*K\xrightarrow{Rf_*\delta_K}Rf_*\mathbb D_X\mathbb D_XK
\simeq\mathbb D_YRf_*\mathbb D_XK
$$

of $Rf_*\delta_K$ and $e_{\mathbb D_XK}$
equals the composite

$$
Rf_*K\xrightarrow{\delta_{Rf_*K}}\mathbb D_Y\mathbb D_YRf_*K
\simeq\mathbb D_YRf_*\mathbb D_XK
$$

of $\delta_{Rf_*K}$ and $\mathbb D_Y$ applied to
$e_K$.
