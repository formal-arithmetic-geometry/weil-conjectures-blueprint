+++
id = "theorem-smooth-base-change-all-admissible"
kind = "theorem"
title = "Smooth base change for all admissible coefficients"
order = 701
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_app_padicIntegers_of_smooth", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_smooth"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
In (8.1), assume that all schemes are of finite type over $k$
and that $g$ is smooth. For every admissible coefficient ring

$$
\Lambda\in\{A,\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\}
$$

and every $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, the
base change map (4.5) is an isomorphism

$$
g^*Rf_*K\xrightarrow{\sim}Rf'_*g'^*K.
\tag{8.2}
$$
