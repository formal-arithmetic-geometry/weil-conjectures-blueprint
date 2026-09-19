+++
id = "lem-zla-integral-cayley-hamilton"
kind = "lemma"
title = "Integral Cayley–Hamilton recurrence"
order = 1010
uses = ["def-zla-integral-shift-lattice", "lem-zla-finite-coordinate-lattice"]
+++
With the notation of [def-zla-integral-shift-lattice], the shift
endomorphism $S:M(a)\to M(a)$ has a monic characteristic polynomial

$$
C(U)=U^r+c_{r-1}U^{r-1}+\cdots+c_0\in\mathbf Z[U],
$$

where $r$ is the rank of $M(a)$, and for every $n\geq0$,

$$
a_{n+r}+c_{r-1}a_{n+r-1}+\cdots+c_0a_n=0.
$$

## Proof

By [lem-zla-finite-coordinate-lattice] the group $M(a)$ is finite free, and
it is stable under the shift, so $S$ has an integral matrix in any basis; its
characteristic polynomial is monic with integer coefficients.
Cayley–Hamilton over $\mathbf Z$ gives
$S^ra+c_{r-1}S^{r-1}a+\cdots+c_0a=0$ in $M(a)$, and reading this equality of
sequences in coordinate $n$ is the displayed recurrence.
