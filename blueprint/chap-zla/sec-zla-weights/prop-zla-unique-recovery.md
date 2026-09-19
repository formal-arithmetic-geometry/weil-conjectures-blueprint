+++
id = "prop-zla-unique-recovery"
kind = "theorem"
title = "Unique recovery over the coefficient field"
order = 1027
tags = ["latex:proposition"]
uses = ["def-zla-complete-weight-factor", "def-zla-pure-polynomial", "prop-zla-parity-identification", "prop-zla-weight-stratum-rational"]
+++
For every $i$,

$$
P_i(T)=P_i^{\mathrm{rec}}(T)
\qquad\text{in }\Omega[T].
$$

In particular $P_i$ is the scalar extension of a unique polynomial in
$\mathbf Q[T]$, determined by the reduced fraction $A/B$, by $q$, and by the
integer $i$.

## Proof

By [prop-zla-parity-identification] the product of the $P_j$ over the
$j$ of the same parity as $i$ is the scalar extension of $R_i$, so the
reciprocal-root multiset of $R_i$ is the union, with multiplicities, of those
of the $P_j$ with $j$ of that parity. Purity and [lem-zla-disjoint-weights] show that the roots coming
from $P_i$ are exactly the reciprocal roots of $R_i$ that are universally pure
of weight $i$, and by [prop-zla-weight-stratum-rational] these are
exactly the reciprocal roots of the weight-$i$ stratum of $R_i$, with the same
multiplicities; hence $P_i$ and $P_i^{\mathrm{rec}}$ have the same
reciprocal-root multiset. Two normalized polynomials with the same
reciprocal-root multiset and constant coefficient $1$ are equal.
