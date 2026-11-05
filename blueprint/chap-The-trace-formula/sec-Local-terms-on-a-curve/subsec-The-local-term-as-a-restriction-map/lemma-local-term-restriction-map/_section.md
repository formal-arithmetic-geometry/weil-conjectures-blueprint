+++
id = "lemma-local-term-restriction-map"
kind = "lemma"
title = "The local term as a restriction map"
order = 966
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.supportedRestriction", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_point_traceClass_eq_supportedRestriction", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_eq_integral_supportedRestriction"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-tate-twists", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "lemma-change-coefficients-compact-support", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "proposition-isomorphisms-reduce-finite-coefficients", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients", "definition-relative-dualizing-complex", "theorem-sp-qbar", "definition-verdier-dual-evaluation", "lemma-internal-adjunction-two-exchange-formulas", "theorem-verdier-biduality", "definition-correspondence", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $X_0$ be a smooth curve over $k_0$, let $X=X_0\times_{k_0}k$,
let $K\in D^b_{\mathrm{ctf}}(X,A)$, and let $y$ be a
fixed point of $\Phi_X^m$. Let $\Gamma\subset X\times X$ be the
transposed graph of $\Phi_X^m$, the image of the closed immersion
$\gamma=(\Phi_X^m,\operatorname{id}_X)$, and let $\Delta\subset X\times X$
be the diagonal, the image of $\delta=(\operatorname{id}_X,\operatorname{id}_X)$.
On the strict localization $T$ of $X\times X$ at $(y,y)$ put

$$
P=(\mathbb D_XK\boxtimes K)|_T.
$$

A morphism $\psi:(\Phi_X^m)^*K\to K$ determines a class
$[\psi]\in H^0_\Gamma(T,P)$, and the local term
$\operatorname{LT}_y(\psi)$ of Definition [definition-trace-class-local-terms] is the
image of this class under the composite

$$
R\Gamma_\Gamma(T,P)
\xrightarrow{\rho}
R\Gamma_y(\Delta,\delta^*P)
\xrightarrow{\mathrm{ev}_K}
R\Gamma_y(X,\omega_X)
\simeq R\Gamma(y,\omega_y)
\xrightarrow{\int_y} A,
$$

where $\rho$ is restriction from $\Gamma$-supported to $y$-supported
cohomology.
