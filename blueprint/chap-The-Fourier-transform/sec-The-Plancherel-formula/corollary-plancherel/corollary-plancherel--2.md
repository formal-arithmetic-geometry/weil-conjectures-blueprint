+++
id = "corollary-plancherel--2"
kind = "corollary"
title = "Plancherel (2)"
name_showing = false
order = 1238002
aliases = ["bp-r382-2"]
lean = ["AlgebraicGeometry.WeilComplex.l2Weight_fourierTransform"]
uses = ["definition-weil-structure", "definition-growth-squared-traces", "lemma-artin-schreier-character-sheaf", "prose-16-06"]
+++
Let $k_0=\Fq$, let $\ell\ne\operatorname{char}k_0$ be prime, and fix an
embedding $\iota:\Qbarl\hookrightarrow\C$ and a nontrivial additive
character $\psi:k_0\to\Qbarl^\times$. For a constructible Weil complex
$K$ on $\mathbf A^1_{k_0}$ with coefficients in $\Qbarl$, write

$$
S_n(K)=\sum_{x\in\mathbf F_{q^n}}|\iota t_{K,n}(x)|^2,
\qquad
\nu(K)=\sup\left\{\beta\in\mathbf R:
\limsup_{n\to\infty}\frac{S_n(K)}{q^{n(\beta+1)}}>0\right\}.
$$

Here the limsup is taken in $[0,+\infty]$ and the supremum in
$[-\infty,+\infty]$, with $\sup\varnothing=-\infty$. This is the
supremum formulation of the growth parameter in
Definition [definition-growth-squared-traces]. Then

$$
\nu(\operatorname{FT}_\psi K)=\nu(K)+1
$$

in the extended real numbers; no finiteness assumption is needed.
