+++
id = "lemma-internal-adjunction-two-exchange-formulas"
kind = "lemma"
title = "Internal adjunction and two exchange formulas"
order = 829
lean = ["AlgebraicGeometry.Etale.derivedHomRightDerivedLowerShriekIsoOfFinite", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_verdierExchange", "AlgebraicGeometry.Etale.nonempty_verdierDual_rightDerivedLowerShriek_natIso", "AlgebraicGeometry.Etale.nonempty_iso_verdierDual_leftDerivedUpperStar", "AlgebraicGeometry.Etale.nonempty_arrowIso_rightDerivedLowerStar_map_verdierDualDoubleDual", "AlgebraicGeometry.Etale.nonempty_iso_verdierDual_rightDerivedLowerShriek"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-inverse-image-tensor-product", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "proposition-adjunction-projective-line", "proposition-exceptional-inverse-image-smooth-morphism", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "definition-verdier-dual-evaluation", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
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
