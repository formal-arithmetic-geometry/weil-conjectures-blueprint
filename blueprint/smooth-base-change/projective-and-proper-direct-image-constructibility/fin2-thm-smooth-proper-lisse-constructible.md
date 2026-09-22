+++
id = "fin2-thm-smooth-proper-lisse-constructible"
kind = "theorem"
title = "Smooth proper families with locally constant coefficients"
order = 5209
lean = ["AlgebraicGeometry.Etale.isConstructible_higherDirectImage_of_smoothProper_lisse"]
uses = ["def-sbc-smooth-morphisms", "def-sbc-normal-dominant-galois", "sbc-def-coefficient-conventions", "thm-fin-proper-constructibility-complete", "fin4-lem-fibrewise-cohomological-dimension"]
+++
Let $f:X\to S$ be a smooth proper [def-sbc-smooth-morphisms] morphism with
$S$ of finite type over $k$ and geometrically connected
[def-sbc-normal-dominant-galois] geometric fibres of dimension at most
$r\in\mathbf Z_{\geq0}$, and let $M$ be a lisse $\Lambda$-sheaf on
$X_{\Et}$. Then the higher direct images $R^qf_*M$ are constructible on
$S_{\Et}$ for every $q\geq0$, and $R^qf_*M=0$ for $q>2r$.

## Proof

Constructibility follows from [thm-fin-proper-constructibility-complete],
applied to the given proper morphism and constructible coefficient sheaf.

For every geometric point $\bar s$, proper base change identifies
$$
(R^qf_*M)_{\bar s}=H^q(X_{\bar s},M|_{X_{\bar s}}).
$$
The right side is zero above twice the specified fibre-dimension bound by
[fin4-lem-fibrewise-cohomological-dimension]. Geometric stalk conservativity
proves the sheaf vanishing. Each fibre group is finite because constructible
sheaves have finite stalks.

The constructibility proof uses finite resolutions and proper
modifications; the sharp bound is obtained separately from this
geometric-fibre calculation.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-direct-image, cor:weil-pbc-geometric-fiber-finite, lem:weil-pbc-geometric-stalk-conservative
