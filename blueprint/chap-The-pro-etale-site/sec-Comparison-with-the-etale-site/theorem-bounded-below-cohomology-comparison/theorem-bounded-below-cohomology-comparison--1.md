+++
id = "theorem-bounded-below-cohomology-comparison--1"
kind = "theorem"
title = "Bounded-below cohomology comparison (1)"
name_showing = false
order = 123001
aliases = ["bp-r035-1"]
lean = ["AlgebraicGeometry.ProEtale.isIso_derivedComparisonAdjunction_unit_app"]
uses = ["definition-small-pro-etale-site--1", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2"]
+++
Let $X$ be a scheme and $\mathcal A$ a Grothendieck abelian category.
For a bounded below object $K\in D(X_{\acute{e}t},\mathcal A)$, the unit of the
derived adjunction $\nu_X^*\dashv R\nu_{X,*}$ is an isomorphism

$$
K\xrightarrow{\ \sim\ }R\nu_{X,*}\nu_X^*K.
\tag{2.7}
$$

Here $\nu_X^*$ on derived categories is induced by the exact inverse image
on sheaves. In particular, taking $\mathcal A=\operatorname{Mod}(\Lambda)$ for a
discrete commutative ring $\Lambda$ gives the comparison on
$D^+(X_{\acute{e}t},\Lambda)$.
