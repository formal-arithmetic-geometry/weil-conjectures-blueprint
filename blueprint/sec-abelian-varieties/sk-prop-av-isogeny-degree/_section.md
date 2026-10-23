+++
id = "sk-prop-av-isogeny-degree"
kind = "proposition"
title = "The degree of an isogeny is the degree of the kernel"
lean = ["AlgebraicGeometry.IsIsogeny.finrank_eq", "AlgebraicGeometry.IsIsogeny.isFinite", "AlgebraicGeometry.IsIsogeny.flat"]
order = 578
uses = ["sk-def-av", "sk-def-av-isogeny", "sk-def-av-pic", "sk-prop-av-mult-finite"]
tags = ["sketch"]
+++
Let $f:A\to B$ be an isogeny of abelian varieties ([sk-def-av-isogeny])
with kernel $K$ of order $d=\dim_k\cO_K$. Then $f$ is finite and flat
and $f_*\cO_A$ is a locally free $\cO_B$-module of rank $d$: the
degree of the finite flat morphism $f$ equals the order of its kernel.
