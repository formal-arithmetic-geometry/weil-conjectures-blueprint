+++
id = "corollary-plancherel--1"
kind = "corollary"
title = "Plancherel (1)"
name_showing = false
order = 1238001
aliases = ["bp-r382-1"]
lean = ["AlgebraicGeometry.WeilComplex.traceEnergy_affineSpaceFourierTransform"]
uses = ["definition-weil-structure", "definition-trace-function", "lemma-artin-schreier-character-sheaf", "prose-16-06"]
+++
Let $k_0=\Fq$, let $\ell\ne\operatorname{char}k_0$ be prime, and fix an
embedding $\iota:\Qbarl\hookrightarrow\C$ and a nontrivial additive
character $\psi:k_0\to\Qbarl^\times$. Let $K$ be a constructible Weil
complex on $\mathbf A^r_{k_0}$ with coefficients in $\Qbarl$.
For every $n\ge1$,

$$
\sum_{y\in\mathbf F_{q^n}^r}|\iota t_{\operatorname{FT}_\psi K,n}(y)|^2
=q^{nr}\sum_{x\in\mathbf F_{q^n}^r}|\iota t_{K,n}(x)|^2.
$$
