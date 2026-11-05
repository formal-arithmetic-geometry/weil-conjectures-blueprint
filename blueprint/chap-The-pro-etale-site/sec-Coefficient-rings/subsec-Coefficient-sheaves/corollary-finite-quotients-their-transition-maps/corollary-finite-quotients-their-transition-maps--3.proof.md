+++
kind = "proof"
of = "corollary-finite-quotients-their-transition-maps--3"
order = 181006
uses = ["prose-02-51", "proposition-topos-functoriality", "corollary-finite-quotients-their-transition-maps--1", "corollary-finite-quotients-their-transition-maps--2"]
+++
Write $s_X:X\to\operatorname{Spec}\mathbf Z$ for the structure morphism.
By [prose-02-51], $p_X^*=s_X^{-1}p^*$, where $p^*$ is the inverse image
from the condensed point to $\operatorname{Spec}\mathbf Z$. Compose the
inverse-image comparison of [proposition-topos-functoriality] with
$s_Y\circ f=s_X$. This gives the displayed natural isomorphism.
The inverse-image comparison and the identification of structure
morphisms respect the monoidal structures, so the resulting comparison
also respects rings and their module actions.

Apply its naturality to the uniformizer, reduction and quotient maps
on the point. It identifies every arrow in
[corollary-finite-quotients-their-transition-maps--1] after inverse image.
Applied degree by degree, it also identifies the two-term complexes and
the maps $(\pi_E,\mathrm{id})$ in
[corollary-finite-quotients-their-transition-maps--2].
