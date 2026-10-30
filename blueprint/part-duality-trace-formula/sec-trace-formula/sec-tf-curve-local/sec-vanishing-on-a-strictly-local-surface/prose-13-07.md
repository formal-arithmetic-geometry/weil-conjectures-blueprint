+++
id = "prose-13-07"
kind = "hidden"
title = "Vanishing on a strictly local surface"
order = 584
+++
The vanishing comes from the position of the curves at $(y,y)$. Since
$d\Phi_X=0$, the transposed graph $\Gamma$ is tangent to the vertical
axis $V=\{y\}\times X$, while the diagonal $\Delta$ and the horizontal
axis $H$ have other tangent directions, and this persists on the cover
of degree prime to $\ell$ chosen above. Blowing up the closed point
separates them: the strict transforms of $\Gamma\cup V$, of $\Delta$
and of $H$ meet the exceptional divisor $E\simeq\mathbf P^1$ in
different points. On $E$ minus the points of $\Gamma\cup V$, the
direct image $M$ of the coefficients from the complement of $E$ is
locally constant away from the point $z$ where $H$ meets $E$, and its
stalk at $z$ is zero; both facts use that the monodromy is an
$\ell$-group (Lemma [sk-lem-tf-transverse-boundary]). The restriction to a
branch of $\Delta$, which meets $E$ in one point $w$, factors through
the stalk $M_w$. Composed with the specialization isomorphism from
$M_w$ to the generic stalk of $E$, the restriction from $E$ to $M_w$
becomes the restriction to the zero stalk $M_z$ followed by
specialization, so it is zero.

It remains to prove Lemma [sk-lem-tf-blowup-restriction], the vanishing of
restriction maps on a strictly local surface used in the proof of
Lemma [sk-lem-tf-curve-restriction-zero]. Blowing up the closed point turns it
into a statement about a smooth surface with two transverse divisors,
Lemma [sk-lem-tf-transverse-boundary], which we prove first. We compute
on classical étale models of strictly local
schemes, which are filtered limits of schemes of finite type, and the
proof of Lemma [sk-lem-tf-curve-restriction-zero] transports the result
to the pro-étale site.
