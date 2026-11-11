+++
id = "lemma-local-term-restriction-map--1"
kind = "lemma"
title = "The local term as a restriction map (1)"
name_showing = false
order = 966001
aliases = ["bp-r294-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_point_traceClass_eq_supportedRestriction", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_frobeniusGraph_eq_supportedRestriction"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "theorem-f-shriek-ell-adic-coefficients--5", "theorem-f-shriek-ell-adic-coefficients--6", "proposition-six-operations-dctf--14", "proposition-six-operations-dctf--15", "definition-verdier-dual-evaluation--2", "definition-correspondence--1", "definition-correspondence--2", "definition-correspondence--3", "lemma-external-duality-trace-morphism--2", "definition-trace-class-local-terms--1", "definition-trace-class-local-terms--3", "definition-frobenius-correspondences-their-operators--1", "definition-frobenius-correspondences-their-operators--5", "lemma-frobenius-fixed-scheme--3", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
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
