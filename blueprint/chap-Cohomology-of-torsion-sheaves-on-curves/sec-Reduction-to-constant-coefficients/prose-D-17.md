+++
id = "prose-D-17"
kind = "hidden"
title = "Reduction to constant coefficients (2)"
order = 1615
+++
To apply this to $j_!G$ on a reduced curve $C$, we take for $U$ a dense
smooth open on which $G$ is locally constant.  Normalizing $C$ in the
finite extensions of function fields defined by $V$, we get a finite
morphism $\bar v:Y\to C$ with $V$ the inverse image of $U$, and an
open immersion $j':V\hookrightarrow Y$.  From the cartesian square
formed by these maps and the formula for stalks of direct images along
finite morphisms, we find that

$$
j_!v_*v^*G=\bar v_*j'_!v^*G,
$$

which is also the exchange formula of [Stacks, [0GJ1](https://stacks.math.columbia.edu/tag/0GJ1)].  If
$C$ is proper, then $Y$ is proper, and if $C$ is affine, then $Y$ is affine.

The assertions travel from constant sheaves to $j'_!v^*G$ on $Y$, then
to $j_!v_*v^*G$ on $C$, and from there to the direct summand $j_!G$.
Since $j'_!$ is exact, the filtration of $v^*G$
gives a filtration of $j'_!v^*G$ with graded pieces $j'_!\mathbf F_\ell$.
The assertions of Theorem [theorem-cohomology-curves] hold for these
pieces by the calculation for constant sheaves extended by zero. As we
show at the start of the next section, they pass along
extensions, so they hold for $j'_!v^*G$. Since
$\bar v_*$ is exact, they hold for $j_!v_*v^*G$. By the splitting
given by the trace, they hold for its direct summand $j_!G$. For
invariance under field extension we use that the unit and the trace
commute with extension of the ground field. Then the pullback map for
$j_!G$ is a retract of the pullback map for $j_!v_*v^*G$, and a retract
of an isomorphism is an isomorphism [Stacks, [03SD](https://stacks.math.columbia.edu/tag/03SD)].

If $C$ is not equidimensional, we choose a dense open that is
smooth and is the disjoint union of the regular loci of the
one-dimensional components and the isolated points.  On the isolated
points taking sections is exact, each connected
one-dimensional piece is treated as above, and finite direct sums
preserve all the assertions.
