+++
kind = "proof"
of = "sk-def-sfb-finite-pushforward-pullback"
+++
Identity covers, composites of covers, and base changes of covers satisfy the axioms by
[sk-lem-pe-weakly-etale-stability] and the fpqc covering axioms. Representable presheaves
satisfy descent for these covers by fpqc descent for morphisms of schemes, so they are
sheaves; this is [det-pe-topos-functoriality-site]. Finally, $V\mapsto V\times_YX$
preserves finite limits and covering families. It therefore defines the displayed
geometric morphism, with inverse image left exact by the site construction; exactness on
abelian sheaves and compatibility with composition follow
([det-pe-topos-functoriality-inverse-image]). These are the small-site versions of the
constructions in Stacks, Tag 0988.

The same base change functor gives, for sheaves with values in any Grothendieck abelian
category $\mathcal A$, the pushforward $f_*$ of [def-sfb-finite-lower-star] and the
pullback $f^*$ of [def-sfb-finite-upper-star] (left Kan extension followed by
sheafification). They satisfy $f^*\dashv f_*$
([def-sfb-finite-upper-lower-star-adjunction]), $f^*$ is exact
([lem-sfb-finite-upper-star-exact]), and the composition isomorphisms are
[def-sfb-finite-lower-star-comp] and [def-sfb-finite-upper-star-comp]. For $\mathcal A$
closed symmetric monoidal, with the tensor product of [sk-def-sfb-sheaf-tensor], $f_*$ is
lax symmetric monoidal ([def-sfb-finite-lower-star-lax-monoidal]), $f^*$ is strong
symmetric monoidal ([def-sfb-finite-upper-star-monoidal],
[lem-sfb-finite-upper-star-unit], [lem-sfb-finite-upper-star-tensor],
[lem-sfb-finite-upper-star-braided]), and $f^*\dashv f_*$ is a monoidal adjunction
([lem-sfb-finite-monoidal-adjunction]).
