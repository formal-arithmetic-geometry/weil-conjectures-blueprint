+++
kind = "proof"
of = "lem-weil-pbc-constant-pullback-composition-coherence"
uses = ["def-constructible-constant", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "lem-weil-pbc-inverse-image-composition"]
+++
The constant-sheaf functor is left adjoint to global sections by [def-constructible-constant]. Compose that adjunction on Z with the inverse-image adjunctions for v and u [def-weil-pbc-inverse-image]. Global sections of direct image are sections on the source [def-weil-pbc-direct-image]; the right-adjoint comparisons use the pullback-pasting isomorphism, which identifies the terminal base-change objects with the terminal object of X.

The isomorphism a_{u,v} has the unit compatibility of [lem-weil-pbc-inverse-image-composition]. Under the composed adjunctions, the map a_{u,v,M_Z} after c_{uv} has adjoint the unit of constant sheaf at M: the unit equation converts the composite inverse-image unit into the two successive units. The map u^{-1}(c_v) after c_u has the same adjoint by the defining unit equations of c_u and c_v and the formula for the unit of a composite adjunction. The terminal pullback-pasting identifications on sections are the same: both are induced by the unique maps between the terminal base-change objects. Injectivity of the adjunction bijection, equivalently uniqueness of conjugate natural transformations, equates the two sheaf morphisms.
