+++
id = "sk-p-readout"
kind = "lemma"
title = "Determinant weight from a central scalar"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.detWeight_eq_of_isPositiveCentralPair"]
order = 3754
uses = ["sk-d-weights", "sk-i-restriction", "sk-p-central", "sk-r-linear-library"]
tags = ["sketch"]
+++
Suppose $Q$ is a nonzero subquotient of a tensor construction on the
semisimple representation used in [sk-p-central]. Suppose that $Q$ has
finite geometric determinant and that $z=hF^N$ acts on $Q$ by a scalar
$c_Q$. Then

$$
\dw_\iota(Q)=\frac{\lambda_\iota(c_Q)}{N}.
$$

In particular the formula applies to every simple such subquotient with
finite geometric determinant.

*Complement.* The same holds for any real weight character $\lambda$ of
[sk-d-weights] in place of $\lambda_\iota$, and for any positive central
pair $(N,z)$ of a represented datum over an algebraically closed field $k$
and any nonzero $W$-subquotient $Q$ of its defining representation $k^n$
with finite geometric determinant on which $z$ acts by a scalar; this does
not use the existence statement of [sk-p-central].
