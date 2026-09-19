+++
id = "lem-zla-taylor-faithful"
kind = "lemma"
title = "Faithfulness of the Taylor map"
order = 997
uses = ["def-zla-rational-germ"]
+++
If two normalized rational germs have the same Taylor series, then they are
equal. Equivalently, Taylor expansion gives an injective map

$$
K(T)_0\hookrightarrow K[[T]].
$$

## Proof

A denominator with constant coefficient $1$ is invertible in $K[[T]]$, so the
equality $AB^{-1}=A'B'^{-1}$ of power series may be cross-multiplied to
$AB'=A'B$ in $K[[T]]$; both sides are polynomials, and $K[T]\to K[[T]]$ is
injective, so the equality holds in $K[T]$, which is the defining relation of
the equivalence.
