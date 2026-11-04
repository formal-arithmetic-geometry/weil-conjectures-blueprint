+++
id = "lemma-local-term-restriction-map"
kind = "lemma"
title = "The local term as a restriction map"
order = 959
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_point_traceClass_eq_supportedRestriction", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_eq_integral_supportedRestriction", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.supportedRestriction"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "corollary-continuity-cohomology", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-proper-direct-image-unbounded-complexes", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "lemma-perfect-complexes-geometric-point", "definition-trace-class-local-terms", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
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
