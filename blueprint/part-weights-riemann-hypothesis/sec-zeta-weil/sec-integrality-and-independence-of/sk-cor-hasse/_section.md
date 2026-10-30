+++
id = "sk-cor-hasse"
kind = "corollary"
title = "Point-count estimates"
order = 803
lean = ["AlgebraicGeometry.Scheme.abs_pointCount_sub_le_sum_finrank", "AlgebraicGeometry.Scheme.Hom.abs_pointCount_sub_le_two_mul_genus", "AlgebraicGeometry.Scheme.Hom.abs_pointCount_one_sub_le"]
uses = ["sk-cor-tf-point-counting", "sk-input-weights", "sk-thm-weil-final", "sk-thm-curveestimate", "sk-prop-av-tate-rank"]
tags = ["sketch"]
+++
Let $X_0/\mathbf F_q$ be smooth, proper and geometrically connected
of dimension $d\geq1$, and let $b_i$ be as in
Theorem [sk-thm-weil-final]. Then for every $m\geq1$,

$$
\left|\#X_0(\mathbf F_{q^m})-(1+q^{dm})\right|
\leq\sum_{i=1}^{2d-1}b_iq^{mi/2}.
$$

For a smooth proper geometrically connected curve of genus $g$, this is

$$
\left|\#X_0(\mathbf F_{q^m})-(1+q^m)\right|
\leq 2gq^{m/2}.
$$

*Complement (abstract form).* Let $X_0$ be any scheme over $\mathbf F_q$,
$d\ge1$, and $P_0,\dots,P_{2d}\in\Z[T]$ with $P_i(0)=1$, $P_0=1-T$,
$P_{2d}=1-q^{d}T$, $Z(X_0,T)\prod_{i\ \text{even}}P_i(T)=\prod_{i\ \text{odd}}P_i(T)$
in $\Q[[T]]$, and every complex root $z$ of $P_i$ of absolute value
$q^{-i/2}$. Then
$\bigl|\#X_0(\mathbf F_{q^m})-(q^{dm}+1)\bigr|\le\sum_{i=1}^{2d-1}b_iq^{mi/2}$
with $b_i=\deg P_i$, for every $m\ge1$.
