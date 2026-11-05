+++
kind = "proof"
of = "lemma-identity-pasting--1"
order = 319005
uses = ["definition-underived-base-change-map", "definition-derived-base-change-map"]
+++
First work with the underived map of [definition-underived-base-change-map].
The square isomorphism for the identity square is expressed by the
identity isomorphisms of pullback. Expanding its adjoint mate, naturality
moves these isomorphisms past the unit and counit, and the triangle
identity gives the claimed identity on sheaves.

For the derived map, use the universal property of the right derived
functor in [definition-derived-base-change-map]. It suffices to check
the proposed natural transformation after precomposing, on each bounded
below complex, with the unit from the underived direct image to its
right derived functor. Substitute the underived identity just proved.
Naturality of the derived pullback identity isomorphisms and of the
derived-functor unit gives the required equality. Uniqueness then gives
the identity on $D^+$.
