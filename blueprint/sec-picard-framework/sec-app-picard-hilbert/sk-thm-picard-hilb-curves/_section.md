+++
id = "sk-thm-picard-hilb-curves"
kind = "theorem"
title = "Hilbert schemes of points on a smooth curve"
order = 890
lean = ["AlgebraicGeometry.hilbertPresheaf_curve_representable", "AlgebraicGeometry.isIso_of_representableBy_hilbertPresheaf_zero"]
uses = ["sk-prop-picard-pic-split", "sk-def-picard-pic", "sec-abelian-varieties", "sec-nagata-compactification"]
tags = ["sketch"]
+++
The functor $H_d$ is represented by a smooth proper geometrically
integral $k$-scheme of dimension $d$, with $H_0=\operatorname{Spec}k$.
Its $T$-points are precisely the relative effective Cartier divisors
that are finite locally free of degree $d$. It has a universal
divisor $D_d\subset C\times_kH_d$ and an associated invertible sheaf
$\mathcal O(D_d)$.
