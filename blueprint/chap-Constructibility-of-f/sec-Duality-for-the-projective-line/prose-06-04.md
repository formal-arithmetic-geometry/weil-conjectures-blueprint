+++
id = "prose-06-04"
kind = "hidden"
title = "Duality for the projective line (1)"
order = 541
+++
Let $p:\mathbf P^1_S\to S$ be the projection. We construct the adjunction $Rp_*\dashv p^*(1)[2]$ from two maps: the counit is a trace
$Rp_*A(1)[2]\to A$, obtained from the cohomology of $\mathbf P^1$, and the unit is the cycle class of the diagonal in
$\mathbf P^1_S\times_S\mathbf P^1_S$, a special case of the cycle class of
an effective Cartier divisor. Both triangle identities say that pushing the
class of the diagonal forward along either projection
$\mathbf P^1\times\mathbf P^1\to\mathbf P^1$ and applying the trace gives
$1$. This holds because the diagonal meets each fibre of either projection
in a single point.

In topology the same two maps appear. For instance, for a bundle $E\to B$ with fibre
$S^2$, integration over the fibre $H^2(S^2)\to\mathbf Z$ is the counit of
Poincaré duality on the fibres, and the unit is the Thom class of the
diagonal of $E\times_BE$, which is Poincaré dual to the identity
correspondence. In étale cohomology, by contrast, the fundamental class of a point on
$\mathbf P^1$ comes from a line bundle through the Kummer sequence. So both maps are
built from line bundles: the trace comes from $c_1(\mathcal O(1))$, and the
class of the diagonal comes from the divisor $x_0y_1-x_1y_0=0$.

For every other morphism, we shall compute $f^!$ from this adjunction, from
$j_!\dashv j^*$ for open immersions and from localization.
