+++
id = "thm-fin-proper-case"
kind = "theorem"
title = "The proper case: direct images of proper morphisms"
order = 5210
lean = ["AlgebraicGeometry.Etale.isConstructible_higherDirectImage_of_isProper"]
uses = ["sbc-def-coefficient-conventions", "thm-fin-proper-constructibility-complete", "fin4-lem-fibrewise-cohomological-dimension"]
+++
Let $f:X\to S$ be a proper morphism with $S$ of finite type over $k$, all
geometric fibres of $f$ of dimension at most $d\in\mathbf Z_{\geq0}$, and
let $F$ be a constructible $\Lambda$-sheaf on $X_{\Et}$. Then $R^qf_*F$ is
constructible on $S_{\Et}$ for every $q\geq0$, and $R^qf_*F=0$ for $q>2d$.

## Proof

Constructibility follows from [thm-fin-proper-constructibility-complete],
applied to the given proper morphism and constructible coefficient sheaf.

For every geometric point $\bar s$, proper base change identifies
$$
(R^qf_*F)_{\bar s}=H^q(X_{\bar s},F|_{X_{\bar s}}).
$$
The right side is zero above twice the specified fibre-dimension bound by
[fin4-lem-fibrewise-cohomological-dimension]. Geometric stalk conservativity
proves the sheaf vanishing. Each fibre group is finite because constructible
sheaves have finite stalks.

The constructibility proof uses finite resolutions and proper
modifications; the sharp bound is obtained separately from this
geometric-fibre calculation.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-direct-image, cor:weil-pbc-geometric-fiber-finite, lem:weil-pbc-geometric-stalk-conservative
