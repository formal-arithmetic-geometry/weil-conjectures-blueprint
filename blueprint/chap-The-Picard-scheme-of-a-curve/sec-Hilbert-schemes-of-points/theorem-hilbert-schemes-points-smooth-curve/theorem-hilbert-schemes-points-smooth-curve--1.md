+++
id = "theorem-hilbert-schemes-points-smooth-curve--1"
kind = "theorem"
title = "Hilbert schemes of points over an arbitrary field"
order = 1537001
aliases = ["bp-r478-1"]
lean = ["AlgebraicGeometry.IsHilbertSubscheme.isInvertible", "AlgebraicGeometry.hilbertPresheaf_curve_representable", "AlgebraicGeometry.isIso_of_representableBy_hilbertPresheaf_zero", "AlgebraicGeometry.isRelativeEffectiveCartier_universal_hilbertPresheaf"]
uses = ["definition-relative-picard-functor--2"]
+++
Let $k$ be a field, let $C$ be a smooth proper geometrically integral
curve over $k$, and let $d\geq0$. The functor
$\operatorname{Hilb}^{d}_{C/k}$ is represented by a smooth proper
geometrically integral $k$-scheme $H_d$ of dimension $d$, and
$H_0\simeq\operatorname{Spec}k$.

For every $k$-scheme $T$, its $T$-points are the relative effective
Cartier divisors $D\subset C_T$ that are finite locally free of degree
$d$ over $T$. The identity of $H_d$ corresponds to a universal relative
effective Cartier divisor $D_d\subset C\times_k H_d$. If
$h:T\to H_d$ classifies $D_h$, then

$$
D_h=(1_C\times h)^*D_d,\qquad
\mathcal O(D_h)\simeq(1_C\times h)^*\mathcal O(D_d).
$$

Here $\mathcal O(D_d)$ is the dual of the invertible ideal of $D_d$.
