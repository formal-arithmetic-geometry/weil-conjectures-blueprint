+++
id = "sk-p-readout"
kind = "lemma"
title = "Determinant weight from a central scalar"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.detWeight_eq_of_isPositiveCentralPair"]
order = 4066
uses = ["sk-d-real-weil", "sk-r-linear-library", "sk-p-central", "sk-d-weights"]
tags = ["sketch"]
+++
Let $V=\bigoplus_iV_i$, $N$ and $z=h\rho(s)^N$ be as in [sk-p-central],
and let $Q$ be a nonzero subquotient of a tensor construction on $V$ on
which $z$ acts by a scalar $c_Q$. Then

$$
\dw_\iota(Q)=\frac{\lambda_\iota(c_Q)}{N}.
$$

By [sk-p-central], the element $z$ acts by a scalar on every simple such
subquotient, and so the formula applies to each of them.

*Complement.* The same holds for any real weight character $\lambda$ of
[sk-d-weights] in place of $\lambda_\iota$, and for any positive central
pair $(N,z)$ of a represented datum over an algebraically closed field $k$
and any nonzero $W$-subquotient $Q$ of its defining representation $k^n$
with finite geometric determinant on which $z$ acts by a scalar; this does
not use the existence statement of [sk-p-central].
