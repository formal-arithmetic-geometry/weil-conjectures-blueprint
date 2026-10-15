+++
kind = "proof"
of = "sk-thm-dnc"
uses = ["sk-prop-sp-exceptional-bc", "sk-prop-sp-tensor"]
+++
By [sk-prop-sp-exceptional-bc], applied to the inclusions of the fibres $t=1$
and $t=0$, the restrictions of $\widetilde s^*\omega_{\widetilde g}$ to $t=1$ and
$t=0$ are $s^*\omega_g$ and $z^*\omega_\pi$. By [sk-prop-sp-tensor], both
$\widetilde s^*\omega_{\widetilde g}[-2d]$ and $s^*\omega_g[-2d]$ are locally
constant sheaves, free of rank one over $\mathbf Z/\ell^n\mathbf Z$. Morphisms between
two such complexes are therefore morphisms of sheaves, and they glue.

*Local construction.* After passing to an étale cover $\{S_i\to S\}$ we may
choose, for the base-changed section $s_i:S_i\to V\times_SS_i$, a neighbourhood
$U_i$ of $s_i(S_i)$ and an étale map $e_i:U_i\to\mathbf A^d_{S_i}$ sending $s_i$ to
the zero section. The inverse image of the zero section under $e_i$ is
separated and étale over $S_i$, so $s_i(S_i)$ is open and closed in it. Its
complement is closed in $U_i$, and we remove it from $U_i$. After this, the
inverse image of the zero section is exactly $s_i(S_i)$, so $e_i$ is an étale
map of pairs whose square of centres is Cartesian. Blowing up and removing the
strict transform commute with étale base change, so $e_i$ induces an étale map
from a neighbourhood of the deformed section in $\operatorname{Def}_s(V)$ to the
deformation space of the zero section of $\mathbf A^d_{S_i}$. The latter is
$\mathbf A^d_{\mathbf A^1_{S_i}}$, mapping to $\mathbf A^d_{S_i}$ by $x_i=tu_i$.

On $\mathbf A^d_{\mathbf A^1_{S_i}}$ the affine-space adjunction identifies the
dualizing complex with the constant sheaf $(\mathbf Z/\ell^n\mathbf Z)(d)[2d]$, and so
does the chart $e_i$ for $s^*\omega_g$ over $S_i$. Composing these two
identifications gives an isomorphism over $\mathbf A^1_{S_i}$

$$
\widetilde s^*\omega_{\widetilde g}\xrightarrow{\ \sim\ }a^*s^*\omega_g.
$$

At $t=1$ it restricts to an automorphism of $s^*\omega_g$ over $S_i$. Composing
with the pullback along $a$ of the inverse of this automorphism, we may assume
that the local isomorphism is the identity at $t=1$.

*Gluing.* Over $S_i\times_SS_j$ the two normalized local isomorphisms differ by
an automorphism of the rank-one locally constant sheaf $a^*s^*\omega_g[-2d]$,
that is, by a section of a locally constant sheaf of units of
$\mathbf Z/\ell^n\mathbf Z$. The locus where this section equals $1$ is open and
closed. On each geometric fibre $\mathbf A^1_{\bar b}$, which is connected, it
contains the point $t=1$, so it is the whole fibre. Hence the section is $1$ at
every geometric point, and the local isomorphisms agree on overlaps. They glue
to a unique isomorphism over $\mathbf A^1_S$ that is the identity at $t=1$.

Restricting it to $t=0$ gives an isomorphism $z^*\omega_\pi\simeq s^*\omega_g$,
whose inverse is the asserted isomorphism.
