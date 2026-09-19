+++
id = "lem-zla-normalized-gauss"
kind = "lemma"
title = "Normalized Gauss factor lemma"
order = 1012
+++
Let $A\in\mathbf Z[T]$ satisfy $A(0)=1$. If

$$
A(T)=P(T)Q(T),\qquad P,Q\in\mathbf Q[T],\qquad P(0)=Q(0)=1,
$$

then $P,Q\in\mathbf Z[T]$.

## Proof

Reversal turns a polynomial with constant coefficient $1$ and degree $b$ into
the monic polynomial $U^bA(U^{-1})$, and it is multiplicative for the
degrees involved here, so the factorization becomes a factorization of the
monic integral polynomial $U^{\deg A}A(U^{-1})$ into the monic rational
polynomials $U^{\deg P}P(U^{-1})$ and $U^{\deg Q}Q(U^{-1})$. Gauss's lemma –
primitive integral normalization together with multiplicativity of the content
– forces both monic rational factors to be integral, and reversing back gives
$P,Q\in\mathbf Z[T]$.
