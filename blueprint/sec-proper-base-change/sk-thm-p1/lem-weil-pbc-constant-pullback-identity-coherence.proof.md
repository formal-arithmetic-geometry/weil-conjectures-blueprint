+++
kind = "proof"
of = "lem-weil-pbc-constant-pullback-identity-coherence"
uses = ["def-constructible-constant", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "lem-weil-pbc-inverse-image-composition"]
+++
Compose constant sheaf adjoint to sections [def-constructible-constant] with identity inverse image adjoint to identity direct image [def-weil-pbc-inverse-image]. Transport along the canonical identity comparison for direct image. The section comparison over the terminal object is identity, as follows by evaluating [def-weil-pbc-direct-image] and the identity pullback isomorphism.

The unit equation for a in [lem-weil-pbc-inverse-image-composition] identifies this transported adjunction with the original constant-sheaf adjunction. The inverse constant comparison c is the comparison of the same two adjunctions in the other direction. Hence a after c and the identity have the same adjoint, the unit at M. Uniqueness of conjugate natural transformations compatible with the units makes their components equal. This uses no cohomology functor.
