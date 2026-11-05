+++
id = "proposition-unbounded-comparison-finite-coefficients--2"
kind = "proposition"
title = "Unbounded comparison for finite coefficients (2)"
name_showing = false
order = 166002
aliases = ["bp-r049-2"]
lean = []
uses = ["definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "theorem-comparison-direct-images"]
+++
The mainline Lean proof bypasses the assertion below for arbitrary
unbounded complexes and uses [theorem-comparison-direct-images] for
bounded-below complexes. Its comparison map is defined on the unbounded
derived categories, but the isomorphism theorem assumes
$K\in D^+(X_{\acute{e}t},A)$.

The map
(2.9), now a natural transformation of
functors $D(X_{\acute{e}t},A)\to D(Y_{\mathrm{pro}\acute{e}t},A)$, is an isomorphism for every
$K\in D(X_{\acute{e}t},A)$.
