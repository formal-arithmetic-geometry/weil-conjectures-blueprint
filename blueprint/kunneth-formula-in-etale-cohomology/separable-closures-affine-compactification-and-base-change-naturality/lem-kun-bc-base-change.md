+++
id = "lem-kun-bc-base-change"
kind = "lemma"
title = "Base change maps are compatible with further base change"
order = 6111
lean = ["AlgebraicGeometry.Etale.exchange_comp_pullback"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange"]
+++
Given a cartesian square and a morphism $u:Y''\to Y'$, form the square
obtained by pulling all four corners and maps back along $u$. Under the
canonical pseudofunctorial identifications, the pullback along $u$ of the
original exchange morphism is the exchange morphism of the pulled-back
square.

## Proof

Both morphisms are mates (under the derived adjunctions of the inverse
image) of composites of the canonical $\theta$-isomorphism of the cartesian
square with the counit $\varepsilon_f$, and the $\theta$'s are compatible with
the identifications for the pulled-back square (compatibility with pasted
squares); hence the identity.

Unresolved dependencies: def:weil-pbc-inverse-image
