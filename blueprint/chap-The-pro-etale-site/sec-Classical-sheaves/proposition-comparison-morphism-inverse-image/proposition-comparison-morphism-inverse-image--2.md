+++
id = "proposition-comparison-morphism-inverse-image--2"
kind = "proposition"
title = "The comparison morphism and its inverse image (2)"
name_showing = false
order = 112002
aliases = ["bp-r031-2"]
lean = ["AlgebraicGeometry.ProEtale.comparisonUpperStar", "AlgebraicGeometry.ProEtale.comparisonAdjunction", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_comparisonUpperStar", "AlgebraicGeometry.ProEtale.preservesFiniteColimits_comparisonUpperStar"]
uses = ["proposition-comparison-morphism-inverse-image--1"]
+++
For $X$ and $A$ as in [proposition-comparison-morphism-inverse-image--1],
restriction has a left adjoint

$$
\nu_X^*:\Sh(X_{\acute{e}t},A)
\longrightarrow\Sh(X_{\mathrm{pro}\acute{e}t},A),
\qquad \nu_X^*\dashv\nu_{X,*}.
$$

It is constructed by taking the left Kan extension of the underlying
presheaf along $i_X^{\mathrm{op}}$ and then sheafifying on
$X_{\mathrm{pro}\acute{e}t}$. It preserves finite limits and finite colimits,
and hence is exact. In particular, taking $A$ to be the category of
$\Lambda$-modules gives the adjoint functors between
$\operatorname{Mod}(X_{\acute{e}t},\Lambda)$ and
$\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$.
