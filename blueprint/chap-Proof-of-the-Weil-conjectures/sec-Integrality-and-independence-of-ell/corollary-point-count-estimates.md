+++
id = "corollary-point-count-estimates"
kind = "corollary"
title = "Point-count estimates"
order = 1388
lean = ["AlgebraicGeometry.Scheme.abs_pointCount_sub_le_sum_finrank", "AlgebraicGeometry.Scheme.Hom.abs_pointCount_sub_le_two_mul_genus"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-compactification-refinement"]
+++
Let $X_0/\mathbf F_q$ be smooth, proper and geometrically connected
of dimension $d\geq1$, and let $b_i$ be as in
Theorem [theorem-weil-conjectures-smooth-proper-schemes]. Then for every $m\geq1$,

$$
\left|\#X_0(\mathbf F_{q^m})-(1+q^{dm})\right|
\leq\sum_{i=1}^{2d-1}b_iq^{mi/2}.
$$

For a smooth proper geometrically connected curve of genus $g$, this is

$$
\left|\#X_0(\mathbf F_{q^m})-(1+q^m)\right|
\leq 2gq^{m/2}.
$$
