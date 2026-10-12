+++
id = "sk-thm-picard-hilb-curves"
kind = "theorem"
title = "Hilbert schemes of smooth projective curves"
order = 789
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
lean = ["AlgebraicGeometry.hilbertPresheaf_curve_representable", "AlgebraicGeometry.hilbertPresheaf_curve_points", "AlgebraicGeometry.hilbertPresheaf_curve_add"]
tags = ["sketch"]
+++
Let $X$ be a geometrically integral smooth proper curve over $k$
and $d\ge0$. Then:

1. **(1)** $\Hilb^d_{X/k}$ is representable by a smooth proper
geometrically integral *variety* of dimension $d$;
1. **(2)** for $k'/k$, the $k'$-points of $\underline{\Hilb}^d_{X/k}$
are naturally the effective Cartier divisors of degree $d$ on
$X_{k'}$;
1. **(3)** there is an addition morphism
$\underline{\Hilb}^{d_1}_{X/k}\times_k\underline{\Hilb}^{d_2}_{X/k} \to\underline{\Hilb}^{d_1+d_2}_{X/k}$, given on points by
$(D_1,D_2)\mapsto D_1+D_2$ (product of the ideal sheaves), finite locally free of degree
$\binom{d_1+d_2}{d_1}$; and a universal effective Cartier divisor
$D_{\mathrm{univ}}\subseteq\underline{\Hilb}^d_{X/k}\times_kX$ (the point of
$\Hilb^d_{X/k}(T)$ classified by $h:T\to\underline{\Hilb}^d_{X/k}$ is the pullback of
$D_{\mathrm{univ}}$ along $X_T\to\underline{\Hilb}^d_{X/k}\times_kX$), with
$\cO(D_{\mathrm{univ}})|_{\{[D]\}\times X}\cong\cO_X(D)$.
