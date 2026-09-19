+++
id = "lem-zla-det-scalar-extension"
kind = "lemma"
title = "Finite determinants reflect scalar extension"
order = 1004
+++
Let $K\hookrightarrow L$ be an injective field homomorphism. For every finite
square matrix $M$ over $K$,

$$
\det(M)=0
\quad\Longleftrightarrow\quad
\det(M\otimes_KL)=0.
$$

Consequently a finite family of sequences in $K^{\mathbf N}$ that is linearly
independent over $K$ remains linearly independent over $L$, and every finite
bound on the dimension of the shift span over $L$ descends to a bound over
$K$.

## Proof

The determinant is a finite polynomial expression in the matrix entries and is
compatible with the ring homomorphism $K\to L$, which is injective, so it
reflects the vanishing of that expression. The consequence follows from
[lem-zla-finite-coordinates]: a $K$-independent family has a nonvanishing
finite coordinate determinant, which stays nonzero over $L$.
