+++
id = "lem-rp-determinant-log"
kind = "lemma"
title = "The formal determinant–logarithm identity"
order = 4181
+++
For a finite-dimensional complex vector space and an endomorphism $M$,
the following identities hold in the formal power-series ring
$\mathbf C[[t]]$:

$$
t\frac{d}{dt}\log\det(1-tM)^{-1}
=\sum_{m\ge1}\operatorname{Tr}(M^m)t^m,
$$

and, for every integer $d\ge1$,

$$
t\frac{d}{dt}\log\det(1-t^dM)^{-1}
=\sum_{m\ge1}d\operatorname{Tr}(M^m)t^{dm}.
$$

## Proof

Over an algebraic closure, write the eigenvalues of $M$ as
$\lambda_1,\ldots,\lambda_s$, counted with algebraic multiplicity.
The determinant is $\prod_i(1-\lambda_i t)$, and the geometric-series
identity $(1-u)^{-1}=\sum_{m\ge0}u^m$ gives

$$
-t\frac{d}{dt}\log(1-\lambda_i t)
=\sum_{m\ge1}\lambda_i^m t^m.
$$

Summing over $i$ proves the first formula; replacing $t$ by $t^d$
and applying the chain rule proves the second. Since both sides are
polynomial expressions in the matrix entries, the calculation is unchanged
by the chosen algebraic closure.
