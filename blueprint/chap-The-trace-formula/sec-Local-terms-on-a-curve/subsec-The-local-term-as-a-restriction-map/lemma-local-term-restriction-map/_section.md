+++
id = "lemma-local-term-restriction-map"
kind = "lemma"
title = "The local term as a restriction map"
order = 966
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.supportedRestriction", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_point_traceClass_eq_supportedRestriction", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_eq_integral_supportedRestriction"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "definition-verdier-dual-evaluation", "definition-correspondence", "lemma-external-duality-trace-morphism", "definition-trace-class-local-terms", "definition-frobenius-correspondences-their-operators", "lemma-frobenius-fixed-scheme", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
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
