+++
id = "lem-zla-normalized-fraction-unique"
kind = "lemma"
title = "Uniqueness of normalized reduced fractions"
order = 1014
+++
Let $K$ be a field. Suppose $A,B,O,E\in K[T]$ have constant coefficient $1$,
both pairs $(A,B)$ and $(O,E)$ are coprime, and $OB=EA$. Then

$$
O=A,\qquad E=B.
$$

## Proof

From $OB=EA$ and coprimality of $(A,B)$, Euclid's lemma gives $A\mid O$ and
$B\mid E$; symmetrically coprimality of $(O,E)$ gives $O\mid A$ and
$E\mid B$. So $O$ and $A$ agree up to a unit of $K[T]$, that is a nonzero
scalar, and likewise for $E$ and $B$; the normalization by constant
coefficient $1$ makes both scalars equal to $1$.
