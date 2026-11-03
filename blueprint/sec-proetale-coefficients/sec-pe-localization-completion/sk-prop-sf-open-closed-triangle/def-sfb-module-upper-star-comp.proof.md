+++
kind  = "proof"
of    = "def-sfb-module-upper-star-comp"
+++
A composite of adjunctions is an adjunction, so $f^*\circ g^*\dashv g_*\circ f_*$ by
[def-sfb-module-upper-lower-adjunction] applied to $f$ and $g$; also
$(g\circ f)^*\dashv(g\circ f)_*$. Natural transformations between right adjoints
correspond bijectively (by conjugation, i.e. taking mates) to natural transformations
in the opposite direction between the left adjoints, compatibly with composition and
identities. Hence the isomorphism $g_*\circ f_*\to(g\circ f)_*$ of
[def-sfb-module-lower-star-comp] corresponds to a transformation
$(g\circ f)^*\to f^*\circ g^*$, its inverse corresponds to a transformation
$f^*\circ g^*\to(g\circ f)^*$, and these two are mutually inverse, giving the
isomorphism $(g\circ f)^*\cong f^*\circ g^*$. This is the uniqueness of left adjoints.
