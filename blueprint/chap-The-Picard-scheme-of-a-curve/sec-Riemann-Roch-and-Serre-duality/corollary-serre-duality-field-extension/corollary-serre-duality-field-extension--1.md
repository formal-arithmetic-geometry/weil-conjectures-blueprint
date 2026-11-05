+++
id = "corollary-serre-duality-field-extension--1"
kind = "corollary"
title = "Field extension of quasi-coherent cohomology"
order = 1527002
aliases = ["bp-r476-1"]
lean = ["AlgebraicGeometry.Scheme.Modules.nonempty_H_pullback_linearEquiv", "AlgebraicGeometry.Scheme.Modules.finrankH_pullback"]
uses = []
+++
Compatibility of the Serre duality pairing with field extension is
bypassed by the Lean route, which uses the following base change result.

Let $X$ be a quasi-compact quasi-separated $k$-scheme and let $\mathcal F$
be a quasi-coherent $\mathcal O_X$-module. For every $q\geq0$ there is a
$k'$-linear isomorphism
$$
H^q(X_{k'},\mathcal F|_{X_{k'}})
\simeq k'\otimes_kH^q(X,\mathcal F).
$$
Consequently,
$$
\operatorname{finrank}_{k'}H^q(X_{k'},\mathcal F|_{X_{k'}})
=\operatorname{finrank}_kH^q(X,\mathcal F).
$$
