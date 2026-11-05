+++
id = "proposition-unbounded-comparison-finite-coefficients--1"
kind = "proposition"
title = "Unbounded comparison for finite coefficients (1)"
name_showing = false
order = 166001
aliases = ["bp-r049-1"]
lean = []
uses = ["definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image"]
+++
The mainline Lean proof bypasses the unbounded full-faithfulness assertion
below and uses the bounded-below comparison of
[theorem-bounded-below-cohomology-comparison]. Preservation of arbitrary
direct sums follows from the unbounded derived adjunction
$\nu_X^*\dashv R\nu_{X,*}$.

Let $X$ and $Y$ be of finite type over the base field $k$, let
$A$ be a finite commutative $\ell$-primary ring, and let
$g:X\to Y$ be of finite type. Then
$\nu_X^*:D(X_{\acute{e}t},A)\to D(X_{\mathrm{pro}\acute{e}t},A)$ is fully faithful and
preserves arbitrary direct sums.
