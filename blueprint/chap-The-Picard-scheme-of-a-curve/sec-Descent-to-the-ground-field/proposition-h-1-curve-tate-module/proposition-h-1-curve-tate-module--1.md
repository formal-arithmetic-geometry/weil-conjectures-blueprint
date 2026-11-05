+++
id = "proposition-h-1-curve-tate-module--1"
kind = "proposition"
title = "The finite-level Kummer comparison"
name_showing = false
order = 1565001
aliases = ["bp-r489-1"]
lean = ["AlgebraicGeometry.Scheme.kummerTorsionEquiv", "AlgebraicGeometry.Scheme.coe_kummerTorsionEquiv_restrictMuH", "AlgebraicGeometry.Scheme.coe_kummerTorsionEquiv_map_rootsOfUnityInclusion"]
uses = []
+++
The pro-étale Jacobian formulation is bypassed by the Lean route, which
uses the following étale comparison at finite level.

Let $X$ be a proper scheme over an algebraically closed field $\Omega$,
and let $m\geq1$ be invertible in $\Omega$. The inclusion
$\mu_m\to\mathbf G_m$ induces a canonical isomorphism of abelian groups

$$
\kappa_m:H^1(X_{\acute{e}t},\mu_m)
\xrightarrow{\ \sim\ }\operatorname{Pic}(X)[m].
$$

For every automorphism $f:X\to X$, not necessarily over $\Omega$, this
identification commutes with pullback:

$$
\kappa_m(f^*x)=f^*\kappa_m(x).
$$

If $m\mid m'$ and $m'$ is also invertible in $\Omega$, write
$i:\mu_m\hookrightarrow\mu_{m'}$ for the inclusion. Then

$$
\kappa_{m'}(H^1(i)(x))=\kappa_m(x)
\quad\text{in }\operatorname{Pic}(X).
$$
