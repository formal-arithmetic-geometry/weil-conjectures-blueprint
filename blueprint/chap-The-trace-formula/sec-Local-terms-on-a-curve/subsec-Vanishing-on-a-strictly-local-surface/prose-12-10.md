+++
id = "prose-12-10"
kind = "hidden"
title = "Vanishing on a strictly local surface (1)"
order = 963
+++
The vanishing of the local term is explained by the position of the curves at $(y,y)$. Since
$d\Phi_X=0$, the transposed graph $\Gamma$ is tangent to the vertical
axis $V=\{y\}\times X$. The diagonal $\Delta$ and the horizontal
axis $H$ have other tangent directions. This persists on suitable covers
of degree prime to $\ell$ (Lemma [lemma-tangent-cones-on-cover] below). Blowing up the closed point
separates the curves: the strict transforms of $\Gamma\cup V$, of $\Delta$
and of $H$ meet the exceptional divisor $E\simeq\mathbf P^1$ in
different points.

Let $M$ be the direct image of the coefficients from the complement of $E$.
Consider $M$ on $E$ minus the points of $\Gamma\cup V$, and let $z$ be the
point where $H$ meets $E$. There $M$ is locally constant away from $z$, and its
stalk at $z$ is zero. Both facts use that the monodromy is an
$\ell$-group (Lemma [lemma-cohomology-near-two-transverse-divisors]). A
branch of $\Delta$ meets $E$ in one point $w$, and the restriction to this
branch factors through the stalk $M_w$. Compose the restriction from
$E$ to $M_w$ with the specialization isomorphism from
$M_w$ to the generic stalk of $E$. The result equals the restriction to the
zero stalk $M_z$ followed by specialization, so the restriction is zero.

The transverse case is
Lemma [lemma-cohomology-near-two-transverse-divisors], and
Lemma [lemma-vanishing-restrictions-after-blowing-up] reduces to it by
blowing up the closed point. We compute
on classical étale models of strictly local
schemes, which are filtered limits of schemes of finite type, and in the
proof of Lemma [lemma-vanishing-local-term-zero-stalk] we transport the result
to the pro-étale site.
