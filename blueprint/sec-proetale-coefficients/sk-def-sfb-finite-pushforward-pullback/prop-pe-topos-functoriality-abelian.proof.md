+++
kind = "proof"
of = "prop-pe-topos-functoriality-abelian"
+++
Restriction along the continuous functor $V\mapsto V\times_YX$
is the pushforward $f_*$ of [def-sfb-finite-lower-star]; the site and its subcanonicity are
[det-pe-topos-functoriality-site]. Its left adjoint $f^*$ is the left
Kan extension followed by sheafification ([def-sfb-finite-upper-star],
[def-sfb-finite-upper-lower-star-adjunction]); it preserves colimits as a left adjoint. It is
left exact because base change preserves finite limits, so the Kan extension is computed by
filtered colimits, which are exact in $\mathcal A$, and sheafification is left exact
([lem-sfb-finite-upper-star-exact]). The composition isomorphisms are
[def-sfb-finite-lower-star-comp] and [def-sfb-finite-upper-star-comp]; the identity case is
the same argument with base change along the identity.

For $\mathcal A$ closed symmetric monoidal, with the tensor product of
[lem-weil-pbc-sheaf-tensor-closed], $f_*$ is lax symmetric monoidal
([def-sfb-finite-lower-star-lax-monoidal]), $f^*$ is strong symmetric monoidal
([def-sfb-finite-upper-star-monoidal], [lem-sfb-finite-upper-star-unit],
[lem-sfb-finite-upper-star-tensor], [lem-sfb-finite-upper-star-braided]), and
$f^*\dashv f_*$ is a monoidal adjunction ([lem-sfb-finite-monoidal-adjunction]).
