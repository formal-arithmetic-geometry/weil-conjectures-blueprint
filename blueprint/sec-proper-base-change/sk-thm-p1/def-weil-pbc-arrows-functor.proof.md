+++
kind = "proof"
of = "def-weil-pbc-arrows-functor"
+++
For arrows_map_id, apply function extensionality to an arrow a and simplify the identity functor map and Arrow.mk.

For arrows_map_comp, apply function extensionality to an arrow a; both sides reduce definitionally to Arrow.mk of the composite functor map.

Define arrows with Arrow as the object assignment and the image-arrow function as the map; the functor laws follow by congrArg from the two preceding equalities.
