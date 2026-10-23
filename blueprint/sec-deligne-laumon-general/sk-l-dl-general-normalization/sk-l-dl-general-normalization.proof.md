+++
kind  = "proof"
of    = "sk-l-dl-general-normalization"
+++
First recall Noether normalization over a field $K$. For a nonzero
algebra $B=K[b_1,\ldots,b_m]$, we induct on $m$. If the generators are
algebraically independent, there is nothing to prove. Otherwise choose
a nonzero polynomial relation, and choose positive integers $N_i$ such
that the finitely many monomials of the relation have distinct weights
for the weighting $(N_1,\ldots,N_{m-1},1)$. Substituting
$b_i=y_i+b_m^{N_i}$ and dividing by the leading nonzero scalar makes
the relation monic in $b_m$. Hence $B$ is finite over
$K[y_1,\ldots,y_{m-1}]$, and induction proves normalization. This
argument works over a finite field as well.

Now let $A$ be an integral domain with fraction field $K$, let
$\operatorname{Spec}A$ be an affine open of the target, and let $B$ be
a finitely generated $A$-algebra. If $B\otimes_AK=0$, then $B_s=0$ for
some nonzero $s\in A$. Otherwise the result over $K$ gives elements
$t_1,\ldots,t_d$ and monic equations for each of a fixed set of algebra
generators of $B$ over $K[t_1,\ldots,t_d]$. We invert one product
$s\in A\setminus\{0\}$ containing all denominators of the $t_i$ and of
these equations, and enlarge it so as to kill the finitely many
differences that vanish over $K$. Then the equations hold in $B_s$.
Hence bounded powers of the generators span $B_s$ over
$A_s[t_1,\ldots,t_d]$, and the resulting map to $\mathbf A^d_{A_s}$ is
finite.

To obtain the partitions, choose disjoint integral affine opens
containing the generic points of the reduced target. Partition their
inverse images into finitely many reduced affine locally closed pieces
and apply the preceding construction to each piece. On each target
open, a single product of the finitely many denominators works, and
the complement of the resulting open has smaller dimension. Induction
on this complement gives finite partitions of the whole source and
target, and all choices are made over $k_0$. A further locally closed
refinement of a source piece restricts its finite map to a separated
quasi-finite map, to which [sk-l-dl-general-quasifinite] applies.
Finally, the projection $\mathbf A^d_V\to V$ is a composition of $d$
projections of relative affine lines.

For the complement: in the generic step $d=r$, since the generic fibre
has dimension $r$, so the $t_i$ are algebraically independent and the
polynomial ring injects into the coordinate algebra; the map of
coordinate rings over $V_0$ is injective because its composite with the
passage to the generic fibre is, and an injective integral extension
satisfies lying over, so $\nu_0$ is surjective.
