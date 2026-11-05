+++
id = "proposition-kummer-duality-integral-tate-module--1"
kind = "proposition"
title = "Kummer theory and compatible Jacobian torsion"
name_showing = false
order = 1094001
aliases = ["bp-r335-1"]
lean = ["AlgebraicGeometry.Scheme.kummerTorsionEquiv", "AlgebraicGeometry.JacobianTorsionDatum.nonempty"]
uses = ["definition-abelian-variety", "definition-relative-picard-functor"]
+++
Let $X$ be a proper scheme over an algebraically closed field $k$, and
let $m$ be a natural number whose image in $k$ is nonzero. The Kummer
sequence gives an additive isomorphism, with cohomology on the étale site,

$$
K_m:H^1(X,\mu_m)\xrightarrow{\sim}\operatorname{Pic}(X)[m].
$$

Now let $C_0/k_0$ be a smooth proper geometrically integral curve over a
finite field, put $k=\bar k_0$ and $C=C_0\times_{k_0}k$, and let $\ell$ be
a prime. There is an abelian variety $J_0/k_0$ representing
$\operatorname{Pic}^0_{C_0/k_0}$, together with additive isomorphisms

$$
e_n:J_0(k)[\ell^n]\xrightarrow{\sim}\operatorname{Pic}(C)[\ell^n]
\qquad(n\geq0)
$$

such that

$$
e_n(\sigma x)=(1\times\operatorname{Spec}\sigma)^*e_n(x),\qquad
e_n(\ell x)=\ell e_{n+1}(x).
$$

The first identity holds for every $\sigma\in\operatorname{Gal}(k/k_0)$
and $x\in J_0(k)[\ell^n]$; the second holds for
$x\in J_0(k)[\ell^{n+1}]$. The Picard group is written additively, so
$\ell e_{n+1}(x)$ denotes the $\ell$-th tensor power. If
$\ell\ne\operatorname{char}k_0$, the composite $e_n^{-1}K_{\ell^n}$
identifies $H^1(C,\mu_{\ell^n})$ with $J_0(k)[\ell^n]$ at each level.
