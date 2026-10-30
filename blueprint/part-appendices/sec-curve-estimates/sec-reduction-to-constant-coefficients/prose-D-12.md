+++
id = "prose-D-12"
kind = "hidden"
title = "Reduction to constant coefficients (2)"
order = 935
+++
To apply this to $j_!G$ on a reduced curve $C$, we take for $U$ a dense
smooth open on which $G$ is locally constant. Normalizing $C$ in the
finite extensions of function fields defined by $V$, we get a finite
morphism $\bar v:Y\to C$ with $V$ the inverse image of $U$, and an
open immersion $j':V\hookrightarrow Y$. From the cartesian square
formed by these maps and the formula for stalks of direct images along
finite morphisms, we find that

$$
j_!v_*v^*G=\bar v_*j'_!v^*G,
$$

which is also the exchange formula of [Stacks, Tag 0GJ1](https://stacks.math.columbia.edu/tag/0GJ1). If
$C$ is proper, then $Y$ is proper, and if $C$ is affine, then $Y$ is affine.

Using the filtration of $v^*G$, the exactness of $j'_!$, and the
calculation for constant sheaves extended by zero, we therefore get
the assertions of Theorem [sk-thm-curve-package] for $j'_!v^*G$. Since
$\bar v_*$ is exact, they hold for $j_!v_*v^*G$, and by the splitting
given by the trace they hold for its direct summand $j_!G$. For
invariance under field extension, note that the unit and the trace
commute with extension of the ground field. Hence the pullback map for
$j_!G$ is a retract of the pullback map for $j_!v_*v^*G$, and a retract
of an isomorphism is an isomorphism [Stacks, Tag 03SD](https://stacks.math.columbia.edu/tag/03SD).

If $C$ is not equidimensional, we first choose a dense open that is
smooth and is the disjoint union of the regular loci of the
one-dimensional components and the isolated points. On the isolated
points, taking sections is exact. We treat each connected
one-dimensional piece as above, and we use that finite direct sums
preserve all the assertions.
