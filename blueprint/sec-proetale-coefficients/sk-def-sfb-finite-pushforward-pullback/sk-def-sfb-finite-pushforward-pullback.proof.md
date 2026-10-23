+++
kind = "proof"
of = "sk-def-sfb-finite-pushforward-pullback"
+++
Identity covers, composites of covers, and base changes of covers satisfy the axioms by
[sk-lem-pe-weakly-etale-stability] and the fpqc covering axioms. Representable presheaves
satisfy descent for these covers by fpqc descent for morphisms of schemes, so they are
sheaves; this is [det-pe-topos-functoriality-site]. Finally, $V\mapsto V\times_YX$
preserves finite limits and covering families, so it is continuous, and restriction along it
is the pushforward $f_*$ of [def-sfb-finite-lower-star]. Its left adjoint $f^*$ is the left
Kan extension followed by sheafification ([def-sfb-finite-upper-star],
[def-sfb-finite-upper-lower-star-adjunction]); it preserves colimits as a left adjoint. It is
left exact because base change preserves finite limits, so the Kan extension is computed by
filtered colimits, which are exact in $\mathcal A$, and sheafification is left exact
([lem-sfb-finite-upper-star-exact]). The composition isomorphisms are
[def-sfb-finite-lower-star-comp] and [def-sfb-finite-upper-star-comp]; the identity case is
the same argument with base change along the identity. These are the small-site versions of
the constructions in Stacks, Tag 0988.

For $\mathcal A$ closed symmetric monoidal, with the tensor product of
[lem-weil-pbc-sheaf-tensor-closed], $f_*$ is lax symmetric monoidal
([def-sfb-finite-lower-star-lax-monoidal]), $f^*$ is strong symmetric monoidal
([def-sfb-finite-upper-star-monoidal], [lem-sfb-finite-upper-star-unit],
[lem-sfb-finite-upper-star-tensor], [lem-sfb-finite-upper-star-braided]), and
$f^*\dashv f_*$ is a monoidal adjunction ([lem-sfb-finite-monoidal-adjunction]).
