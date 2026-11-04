+++
kind = "proof"
of = "lemma-section-normal-bundle"
order = 743
uses = ["proposition-exceptional-inverse-image-smooth-morphism"]
+++
The fibres of $\widetilde s^{*}\omega_{\widetilde g}$ at $t=1$ and $t=0$
are the two sides of (9.13), so it suffices to show that this
shifted sheaf of rank one is pulled back from $S$, étale locally on $S$.
In positive characteristic a locally constant sheaf on $\mathbf A^1_S$ need
not be pulled back from $S$, so we use coordinates. Étale locally on
$S$, near the section the deformation is étale over
$\mathbf A^d_{\mathbf A^1_S}=\mathbf A^d_S\times\mathbf A^1$. This family
is pulled back from $S$, and hence so is
$\widetilde s^{*}\omega_{\widetilde g}[-2d]$. We normalize the local
comparisons at $t=1$. Since the geometric fibres of $\mathbf A^1_S\to S$
are connected, this makes them agree on overlaps. They glue because all
objects involved are shifted locally constant sheaves.

*Step 1: the objects.* The restrictions of
$\widetilde s^{*}\omega_{\widetilde g}$ to $t=1$ and $t=0$ are
$s^{*}\omega_{g}$ and $z^{*}\omega_{\pi}$, by
Proposition [proposition-exceptional-inverse-image-smooth-morphism](3) applied to the inclusions
of these fibres. Proposition [proposition-exceptional-inverse-image-smooth-morphism](1) shows that both
$\widetilde s^{*}\omega_{\widetilde g}[-2d]$ and
$s^{*}\omega_{g}[-2d]$ are locally constant sheaves, free of rank one
over $\mathbf Z/\ell^n\mathbf Z$. Hence morphisms between two such
complexes are morphisms of sheaves, and they glue.

*Step 2: local construction.* Étale
locally on $S$ we reduce to the zero section of affine space, whose deformation is
pulled back from $S$. After passing to an étale cover
$\{S_\alpha\to S\}_\alpha$ we may choose, for the base change of the section
$s_\alpha:S_\alpha\to V\times_SS_\alpha$, a neighbourhood $U_\alpha$ of $s_\alpha(S_\alpha)$ and an
étale map $e_\alpha:U_\alpha\to\mathbf A^d_{S_\alpha}$ sending $s_\alpha$ to the zero
section. We may assume that the inverse image of the zero section under
$e_\alpha$ is exactly $s_\alpha(S_\alpha)$. Indeed, this inverse image is
separated and étale over $S_\alpha$, so $s_\alpha(S_\alpha)$ is open and
closed in it. We remove the complement, which is closed in $U_\alpha$.
Then $e_\alpha$ is an étale map of pairs whose square of centers is
cartesian. Blowing up and removing the strict transform commute with
étale base change. Hence $e_\alpha$ induces an étale map from a
neighbourhood of the deformed section in $\mathcal D_{s(S)}V$ to the
deformation space of the zero section of $\mathbf A^d_{S_\alpha}$. The latter
is $\mathbf A^d_{\mathbf A^1_{S_\alpha}}$, with coordinates $u_1,\ldots,u_d$
and $t$. Its map to $\mathbf A^d_{S_\alpha}\times\mathbf A^1$ sends
$(u,t)$ to $(tu,t)$, that is, $x_i=tu_i$, and the deformed zero section is
$u=0$.

The adjunction for affine space identifies the relative dualizing complex
of the projection
$\mathbf A^d_{\mathbf A^1_{S_\alpha}}\to\mathbf A^1_{S_\alpha}$ with the
constant sheaf $(\mathbf Z/\ell^n\mathbf Z)(d)[2d]$. Pulling back along the
étale map just constructed, and composing adjunctions for it, gives the
same identification for $\omega_{\widetilde g}$ near the deformed section.
The chart $e_\alpha$ gives the analogous identification of
$s^{*}\omega_{g}$ over $S_\alpha$. Composing the two identifications we
obtain an isomorphism over $\mathbf A^1_{S_\alpha}$

$$
\widetilde s^{*}\omega_{\widetilde g}\xrightarrow{\sim}
a^{*}s^{*}\omega_{g}.
$$

At $t=1$ it restricts to an automorphism of $s^{*}\omega_{g}$ over
$S_\alpha$. Composing with the pullback along $a$ of the inverse of this
automorphism, we may assume that the local isomorphism is the identity
at $t=1$.

*Step 3: gluing.* The local isomorphisms from different charts agree on
overlaps, because of the normalization at $t=1$. Over $S_\alpha\times_SS_\beta$ the two local
isomorphisms that are the identity at $t=1$ differ by an automorphism of the locally constant sheaf
$a^{*}s^{*}\omega_g[-2d]$ of rank one, that is, by a section of a locally
constant sheaf of units of $\mathbf Z/\ell^n\mathbf Z$. The locus where
this section equals $1$ is open and closed. It contains the point $t=1$
of each geometric fibre $\mathbf A^1_{\bar b}$. As these fibres are
connected, the section is $1$ at every geometric point. So the local
isomorphisms glue to a unique isomorphism over $\mathbf A^1_S$ that is the
identity at $t=1$. Restricting it to $t=0$ gives an isomorphism
$z^{*}\omega_{\pi}\simeq s^{*}\omega_g$, whose inverse is
(9.13).
