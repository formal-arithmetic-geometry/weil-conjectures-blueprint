+++
id = "corollary-plancherel--2"
kind = "corollary"
title = "Plancherel (2)"
name_showing = false
order = 1241003
aliases = ["bp-r382-2"]
lean = ["AlgebraicGeometry.WeilComplex.l2Weight_fourierTransform"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "definition-change-of-coefficients-maps--6", "proposition-six-operations-change-coefficients--23", "proposition-sp-unique-adjoint--1", "definition-weil-structure--1", "definition-weil-structure--3", "definition-growth-squared-traces--3", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "definition-admissible-blow-up--1", "theorem-extension-partial-section--1", "theorem-elimination-indeterminacy--1", "lemma-extending-graph-from-compactification--1", "lemma-separation-closures--1", "lemma-extending-isomorphism-over-closure-closed--1", "lemma-gluing-after-admissible-blow-ups--1", "lemma-affine-covers-dense-intersection--1"]
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
