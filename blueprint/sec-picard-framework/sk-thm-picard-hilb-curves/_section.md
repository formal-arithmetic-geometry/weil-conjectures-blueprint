+++
id = "sk-thm-picard-hilb-curves"
kind = "theorem"
title = "Hilbert schemes of points on a smooth curve"
order = 782
uses = ["sk-prop-picard-pic-split", "sk-def-picard-pic", "sec-abelian-varieties", "sec-nagata-compactification"]
lean = ["AlgebraicGeometry.hilbertPresheaf_curve_representable", "AlgebraicGeometry.isIso_of_representableBy_hilbertPresheaf_zero"]
tags = ["sketch"]
+++
Let $C/k$ be a smooth projective geometrically connected curve. For
$d\geq0$, let $H_d=\Hilb^d_{C/k}$ be the functor of closed subschemes
$D\subset C_T$ which are finite locally free of rank $d$ over $T$.

The functor $H_d$ is represented by a smooth proper geometrically
integral $k$-scheme of dimension $d$, with $H_0=\Spec k$. Its $T$-points are
precisely the relative effective Cartier divisors which are finite
locally free of degree $d$. It has a universal divisor
$D_d\subset C\times_kH_d$ and an associated invertible sheaf
$\cO(D_d)$.
