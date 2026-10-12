+++
id = "thm-pc-hilb-curves"
kind = "theorem"
title = "Hilbert schemes of smooth projective curves"
order = 796
uses = ["def-pc-base-change", "def-pc-curve", "def-pc-degree-line-bundle", "def-pc-hilb-functor", "def-pc-morphism-conventions", "def-sc-effective-cartier-divisor", "lem-pc-ample-positive-degree", "lem-pc-cartier-criterion", "lem-pc-degree-base-change", "lem-pc-flat-source-descent", "lem-pc-hilb-addition", "lem-pc-hilb-smooth", "lem-sc-ample-complement-affine", "thm-pqf-finite-iff-proper-finite-fibres"]
lean = ["AlgebraicGeometry.hilbertPresheaf_curve_representable", "AlgebraicGeometry.hilbertPresheaf_curve_points", "AlgebraicGeometry.hilbertPresheaf_curve_add"]
+++
Let $X$ be a
geometrically integral smooth proper curve over a field $k$ and let
$d\geq0$. Then:

1. $\operatorname{Hilb}^d_{X/k}$ is representable by a smooth proper geometrically
integral variety $\underline{\operatorname{Hilb}}^d_{X/k}$ of dimension $d$ over $k$,
and $\underline{\operatorname{Hilb}}^d_{X/k}\times_kX$ carries a universal effective
Cartier divisor $D_{\mathrm{univ}}$: for every $k$-scheme $T$ and every
$h:T\to\underline{\operatorname{Hilb}}^d_{X/k}$, the point of
$\operatorname{Hilb}^d_{X/k}(T)$ classified by $h$ is the pullback of
$D_{\mathrm{univ}}$ along $h\times\mathrm{id}_X:X_T\to\underline{\operatorname{Hilb}}^d_{X/k}\times_kX$;
1. for a field extension $k'/k$ the $k'$-rational points of
$\underline{\operatorname{Hilb}}^d_{X/k}$ are in bijection with the effective Cartier
divisors of degree $d$ on $X_{k'}$;
1. for $d_1,d_2\geq0$ there is a morphism
$$
\underline{\operatorname{Hilb}}^{d_1}_{X/k}\times_k\underline{\operatorname{Hilb}}^{d_2}_{X/k}
\longrightarrow\underline{\operatorname{Hilb}}^{d_1+d_2}_{X/k}
$$
which on points is the addition of divisors $(D_1,D_2)\mapsto D_1+D_2$
(the product of the ideal sheaves) and which is finite locally free of
degree $\binom{d_1+d_2}{d_1}$.
