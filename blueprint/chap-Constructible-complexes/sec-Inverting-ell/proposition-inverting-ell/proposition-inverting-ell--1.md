+++
id = "proposition-inverting-ell--1"
kind = "proposition"
title = "Inverting $\\ell$ (1)"
name_showing = false
order = 303001
aliases = ["bp-r089-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.integral_scalar_map_eq"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves"]
+++
Let $\ell$ be prime, let $E$ be a finite normed extension of $\mathbf Q_\ell$,
and assume that the underlying topological space of $X$ is Noetherian.
In this detail, $\Dbc$ denotes bounded complexes whose cohomology sheaves
are pro-étale locally finitely presented on the strata of a finite
constructible locally closed stratification. The finite presentations
are presentations over the coefficient sheaf on each chart.

Put $F(K)=E_X\otimes^{\mathbf L}_{\mathcal O_{E,X}}K$. If
$f,g:K\to L$ are morphisms in $\Dbc(X,\mathcal O_E)$ and $F(f)=F(g)$,
then there is an integer $n\geq0$ such that

$$
\ell^n f=\ell^n g.
$$

In particular, if $F(K)=0$, then some power of $\ell$ kills $K$:
$\ell^n\operatorname{id}_K=0$.
