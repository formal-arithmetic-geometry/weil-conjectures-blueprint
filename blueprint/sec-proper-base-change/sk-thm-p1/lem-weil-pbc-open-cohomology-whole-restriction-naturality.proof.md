+++
kind = "proof"
of = "lem-weil-pbc-open-cohomology-whole-restriction-naturality"
uses = ["lem-weil-pbc-cohomology-pullback-functorial", "lem-weil-pbc-inverse-image-composition"]
+++
Apply composition functoriality to (g restricted to W) followed by W.ι, with named composite (g^{-1}W).ι ≫ g. Apply it also to (g^{-1}W).ι followed by g. The restriction identity makes the two named composites equal. ([lem-weil-pbc-cohomology-pullback-functorial], [lem-weil-pbc-inverse-image-composition]).

Sheaf.H.map_comp_apply identifies H^q of the composite coefficient morphisms with the composite H^q maps. The inverse comparison cancels its hom comparison since upperStarComp is an isomorphism. Apply the remaining H^q comparison to the cancellation equality; this gives the claimed square. The Lean calc explicitly writes these equalities, without any connecting map or cover assumption. ([lem-weil-pbc-inverse-image-composition]).
