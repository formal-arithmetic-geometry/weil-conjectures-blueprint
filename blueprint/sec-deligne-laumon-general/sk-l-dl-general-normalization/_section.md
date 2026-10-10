+++
id = "sk-l-dl-general-normalization"
kind = "section"
title = "Generic relative Noether normalization"
order = 2822
lean = ["AlgebraicGeometry.exists_dense_isFinite_toIteratedAffineLine"]
uses = ["sk-i-real-normalization"]
+++
*Lemma (sketch).*

Let $f_0:X_0\to Y_0$ be a dominant affine morphism of finite type
between integral schemes, whose generic fibre has dimension $r$. Then
there are a dense open $V_0\subseteq Y_0$ and a finite surjective
morphism $\nu_0$ factoring the restriction of $f_0$ over $V_0$ as

$$
f_0^{-1}(V_0)\xrightarrow{\nu_0}\mathbf A^r_{V_0}
\xrightarrow{\pi_0}V_0,
$$

where $\pi_0$ is the projection of the $r$-fold relative affine line,
a composition of $r$ affine-line projections.

## Proof

Over the function field of $Y_0$, apply Noether normalization to the
coordinate algebra of the generic fiber. The algebraic argument in
[sk-i-real-normalization], before its final dimension-one
specialization, gives a finite algebra over a polynomial ring in $r$
variables. The generic fibre has dimension $r$, so the $r$ chosen elements are
algebraically independent and the polynomial ring injects into the
coordinate algebra. Clear the finitely many denominators in these
variables and the monic integral relations by passing to a nonempty
affine open $V_0$ of $Y_0$, which is dense since $Y_0$ is irreducible.
This spreads out the finite map $\nu_0$ over $V_0$. The map of
coordinate rings from the polynomial ring over $V_0$ is injective,
since its composite with the passage to the generic fibre is. An injective
integral extension of rings satisfies lying over, so $\nu_0$ is
surjective. Dropping one coordinate at a time factors $\pi_0$.
