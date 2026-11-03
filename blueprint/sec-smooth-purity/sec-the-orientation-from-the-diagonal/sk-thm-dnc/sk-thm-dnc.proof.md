+++
kind = "proof"
of = "sk-thm-dnc"
uses = ["sk-prop-cohsm"]
+++
By Proposition [sk-prop-cohsm](3), applied to the inclusions
of the fibres $t=1$ and $t=0$, the restrictions of
$\widetilde s^{*}\omega_{\widetilde g}$ to $t=1$ and $t=0$ are
$s^{*}\omega_{g}$ and $z^{*}\omega_{\pi}$. By Proposition [sk-prop-cohsm](1), both
$\widetilde s^{*}\omega_{\widetilde g}[-2d]$ and
$s^{*}\omega_{g}[-2d]$ are locally constant sheaves, free of rank one
over $\mathbf Z/\ell^n\mathbf Z$. Hence morphisms between two such
complexes are morphisms of sheaves, and they glue.

*Local construction.* After passing to an étale cover
$\{S_\alpha\to S\}_\alpha$ we may choose, for the base change of the section
$s_\alpha:S_\alpha\to V\times_SS_\alpha$, a neighbourhood $U_\alpha$ of $s_\alpha(S_\alpha)$ and an
étale map $e_\alpha:U_\alpha\to\mathbf A^d_{S_\alpha}$ sending $s_\alpha$ to the zero
section. The inverse image of the zero section under $e_\alpha$ is
separated and étale over $S_\alpha$, and hence $s_\alpha(S_\alpha)$ is open and
closed in it. Removing the complement, which is closed in $U_\alpha$, we
may assume that the inverse image of the zero section is exactly
$s_\alpha(S_\alpha)$. Then $e_\alpha$ is an étale map of pairs whose square
of centers is cartesian. Since blowing up and removing the strict transform
commute with étale base change, $e_\alpha$ induces an étale map from a
neighbourhood of the deformed section in $\mathcal D_{s(S)}V$ to the
deformation space of the zero section of $\mathbf A^d_{S_\alpha}$. The latter
is $\mathbf A^d_{\mathbf A^1_{S_\alpha}}$, with coordinates $u_1,\ldots,u_d$
and $t$; its map to $\mathbf A^d_{S_\alpha}\times\mathbf A^1$ sends
$(u,t)$ to $(tu,t)$, that is, $x_i=tu_i$, and the deformed zero section is
$u=0$.

The relative dualizing complex of the projection
$\mathbf A^d_{\mathbf A^1_{S_\alpha}}\to\mathbf A^1_{S_\alpha}$ is identified by
the adjunction for affine space with the constant sheaf
$(\mathbf Z/\ell^n\mathbf Z)(d)[2d]$. Pulling back along the étale map
just constructed, and composing adjunctions for it, we obtain the same
identification for $\omega_{\widetilde g}$ near the deformed section. The
chart $e_\alpha$ gives the analogous identification of $s^{*}\omega_{g}$ over
$S_\alpha$. Composing these two identifications
we obtain an isomorphism over $\mathbf A^1_{S_\alpha}$

$$
\widetilde s^{*}\omega_{\widetilde g}\xrightarrow{\sim}
a^{*}s^{*}\omega_{g}.
$$

At $t=1$ it restricts to an automorphism of $s^{*}\omega_{g}$ over
$S_\alpha$. Composing with the pullback along $a$ of the inverse of this
automorphism, we may assume that the local isomorphism is the identity
at $t=1$.

*Gluing.* Over $S_\alpha\times_SS_\beta$ the two local
isomorphisms that are the identity at $t=1$ differ by an automorphism of the locally constant sheaf
$a^{*}s^{*}\omega_g[-2d]$ of rank one, that is, by a section of a locally
constant sheaf of units of $\mathbf Z/\ell^n\mathbf Z$. The locus where
this section equals $1$ is open and closed. On each geometric fibre
$\mathbf A^1_{\bar b}$, which is connected, it contains the point $t=1$,
and so it is the whole fibre. Thus the section is $1$ at every geometric
point, and the local isomorphisms agree on overlaps. They glue to a
unique isomorphism over $\mathbf A^1_S$ that is the identity at $t=1$.

Restricting it to $t=0$, we obtain an isomorphism
$z^{*}\omega_{\pi}\simeq s^{*}\omega_g$, whose inverse is
(10.12).
