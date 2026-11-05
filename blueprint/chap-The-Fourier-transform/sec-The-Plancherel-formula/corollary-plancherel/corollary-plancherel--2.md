+++
id = "corollary-plancherel--2"
kind = "corollary"
title = "Plancherel (2)"
name_showing = false
order = 1241002
aliases = ["bp-r382-2"]
lean = ["AlgebraicGeometry.WeilComplex.l2Weight_fourierTransform"]
+++
Let $k_0=\Fq$, let $\ell\ne\operatorname{char}k_0$ be prime, and fix an
embedding $\iota:\Qbarl\hookrightarrow\C$ and a nontrivial additive
character $\psi:k_0\to\Qbarl^\times$. For a constructible Weil complex
$K$ on $\mathbf A^1_{k_0}$ with coefficients in $\Qbarl$, let $S_n(K)$
and $\nu(K)$ be as in Definition [definition-growth-squared-traces].
Equivalently,

$$
\nu(K)=\sup\left\{\beta\in\mathbf R:
\limsup_{n\to\infty}\frac{S_n(K)}{q^{n(\beta+1)}}>0\right\},
$$

with the limsup taken in $[0,+\infty]$, the supremum in
$[-\infty,+\infty]$ and $\sup\varnothing=-\infty$: this upper limit is
$+\infty$ for $\beta<\nu(K)$ and $0$ for $\beta>\nu(K)$. Then

$$
\nu(\operatorname{FT}_\psi K)=\nu(K)+1
$$

in the extended real numbers; no finiteness assumption is needed.
