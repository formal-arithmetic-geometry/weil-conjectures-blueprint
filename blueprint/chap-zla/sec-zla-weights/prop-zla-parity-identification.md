+++
id = "prop-zla-parity-identification"
kind = "theorem"
title = "Identification of the two parity factors"
order = 1025
tags = ["latex:proposition"]
uses = ["def-zla-pure-polynomial", "lem-zla-disjoint-weights", "lem-zla-normalized-fraction-unique"]
+++
Assume every $P_i$ is pure of weight $i$. Let $A,B\in\mathbf Q[T]$ be
coprime with $A(0)=B(0)=1$, and suppose that

$$
\frac{O(T)}{E(T)}=\frac{A(T)}{B(T)}
\qquad\text{in }\Omega(T).
$$

Then, after coefficient extension to $\Omega$,

$$
O(T)=A(T),\qquad E(T)=B(T).
$$

Thus no reciprocal root cancels between odd and even cohomological degrees.

## Proof

By [lem-zla-disjoint-weights] the polynomials $O$ and $E$ have no common
root in the algebraically closed field $\Omega$, hence are coprime in
$\Omega[T]$; the pair $(A,B)$ stays coprime after extension of scalars since a
Bézout identity extends. Both denominators are nonzero because their constant
coefficients are $1$, so the equality of fractions may be cross-multiplied to
$OB=EA$ in $\Omega[T]$, and all four polynomials have constant coefficient
$1$. [lem-zla-normalized-fraction-unique] over $\Omega$ concludes.
