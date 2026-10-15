+++
id = "sk-thm-picard-hilb-curves"
kind = "theorem"
title = "Hilbert schemes of points on a smooth curve"
order = 607
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sk-the-hilbert-functor--definition-1", "sk-thm-picard-hilb-general"]
lean = ["AlgebraicGeometry.hilbertPresheaf_curve_representable", "AlgebraicGeometry.hilbertPresheaf_curve_points", "AlgebraicGeometry.hilbertPresheaf_curve_add"]
tags = ["sketch"]
+++
Let $C/k$ be a smooth projective geometrically connected curve. For
$d\geq0$, let $H_d=\Hilb^d_{C/k}$ be the functor of closed subschemes
$D\subset C_T$ which are finite locally free of rank $d$ over $T$.

The functor $H_d$ is represented by a smooth projective geometrically
integral $k$-scheme of dimension $d$, with $H_0=\Spec k$. Its objects are
precisely the relative effective Cartier divisors which are finite
locally free of degree $d$. It has a universal divisor
$D_d\subset C\times_kH_d$ and an associated invertible sheaf
$\cO(D_d)$.

*Complements* (proved in this sketch). For a field extension $k'/k$ the
$k'$-points of $H_d$ are the effective Cartier divisors of degree $d$ on
$C_{k'}$, and $\cO(D_d)|_{C\times\{[D]\}}\cong\cO_C(D)$; there is an
addition morphism $H_{d_1}\times_kH_{d_2}\to H_{d_1+d_2}$, given on
points by $(D_1,D_2)\mapsto D_1+D_2$ (product of the ideal sheaves),
finite locally free of degree $\binom{d_1+d_2}{d_1}$; in particular the
iterated addition $C^d\to H_d$ is finite locally free and surjective.
