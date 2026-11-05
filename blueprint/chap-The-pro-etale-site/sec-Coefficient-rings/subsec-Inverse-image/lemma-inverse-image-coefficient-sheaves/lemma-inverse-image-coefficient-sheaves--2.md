+++
id = "lemma-inverse-image-coefficient-sheaves--2"
kind = "lemma"
title = "Inverse image of torsion Tate twists"
order = 187003
aliases = ["bp-r054-2"]
lean = ["AlgebraicGeometry.Etale.leftDerivedUpperStarTateTwistObjectIso"]
uses = ["definition-tate-twists"]
+++
The assertion for all admissible pro-étale Tate twists is bypassed by the
Lean route; the comparison used here is formulated for torsion coefficients
on the étale site.

Let $A$ be a commutative ring of positive characteristic $N$, and suppose
that $N$ is invertible on $X$ and $Y$. Write $A_T(d)$ for the étale Tate
twist on $T$, placed in degree zero: its degree-one sheaf is
$\mu_{N,T}\otimes_{\mathbf Z/N\mathbf Z}A_T$, and its signed tensor powers
are formed using duals for negative integers, as in the finite-coefficient
part of [definition-tate-twists]. For every $d\in\mathbf Z$ there is a
canonical isomorphism

$$
\mathbf Lf_{\acute{e}t}^*A_Y(d)\simeq A_X(d)
\qquad\text{in }D(X_{\acute{e}t},A).
$$

The ring $A$ need not be finite.
