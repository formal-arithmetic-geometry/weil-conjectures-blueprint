+++
kind = "proof"
of = "lemma-identity-pasting--2"
order = 319006
uses = ["definition-underived-base-change-map", "definition-derived-base-change-map"]
+++
On sheaves, the composition isomorphisms for pullback identify the
square isomorphism of the pasted square with the composite of the two
square isomorphisms. Taking adjoint mates as in
[definition-underived-base-change-map] gives the underived horizontal
pasting formula.

For the derived formula, first compose both candidate maps with the
isomorphism $Rf''_*(g'h')^*\simeq Rf''_*h'^*g'^*$. By the universal
property of the right derived functor in
[definition-derived-base-change-map], equality can be checked after
precomposing with the unit on every bounded below complex. The defining
factorization of each derived base change map replaces it by its
underived map followed by the derived-functor unit. Move the comparison
isomorphisms and units through these maps by naturality. Compatibility
of the derived pullback composition isomorphisms with their underived
counterparts reduces the equality to the underived pasting formula.
Cancel the final composition isomorphism to conclude.
