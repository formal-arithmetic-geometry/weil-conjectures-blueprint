+++
kind = "proof"
of = "sk-l-dl-general-normalization"
+++
We spread out Noether normalization from the generic points of the
target and then argue by induction on the dimension of the complement.
Recall Noether normalization over a field $k'$ [Stacks, Tag 00OY](https://stacks.math.columbia.edu/tag/00OY): a
nonzero finitely generated $k'$-algebra is finite over a polynomial
subalgebra.

Now let $R$ be an integral domain with fraction field $k'$, let
$\operatorname{Spec}R$ be an affine open of the target, and let $B$ be
a finitely generated $R$-algebra. If $B\otimes_Rk'=0$, then $B_s=0$ for
some nonzero $s\in R$. Otherwise, Noether normalization over $k'$
provides elements $t_1,\ldots,t_d$ and monic equations for each of a
fixed set of algebra generators of $B$ over $k'[t_1,\ldots,t_d]$.
Choose a nonzero $s\in R$ divisible by all denominators of the $t_i$
and of the coefficients of these equations. Each equation, read in
$B_s$, has a left-hand side that vanishes in $B\otimes_Rk'$ and is
therefore killed by a nonzero element of $R$. Multiplying $s$ by these
finitely many elements, we may assume that the equations hold in
$B_s$. Hence bounded powers of the generators span
$B_s$ over $R_s[t_1,\ldots,t_d]$, and the resulting map to
$\mathbf A^d_{R_s}$ is finite.

To obtain the partitions, choose disjoint integral affine opens
containing the generic points of the reduced target. Partition their
inverse images into finitely many reduced affine locally closed pieces
and apply the preceding construction to each piece. On each target
open, a single product of the finitely many denominators works, and
the complement of the resulting open has smaller dimension. By
induction on this complement we obtain finite partitions of the whole
source and target, and all choices are made over $k_0$.
