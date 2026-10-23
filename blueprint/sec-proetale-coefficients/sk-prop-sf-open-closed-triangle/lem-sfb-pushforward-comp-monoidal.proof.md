+++
kind  = "proof"
of    = "lem-sfb-pushforward-comp-monoidal"
+++
The tensor product of sheaves is the sheafification of the objectwise tensor product
of presheaves ([lem-weil-pbc-sheaf-tensor-closed]). Both lax monoidal structures, on
$g_*\circ f_*$ and on $(g\circ f)_*$, are the sheafification of the objectwise one,
transported along the base change functors of the sites
([def-sfb-finite-lower-star-lax-monoidal]): on sections over $V$ they are the maps
$G(W)\otimes H(W)\to(G\otimes H)(W)$ for $W=(V\times_ZY)\times_YX$ resp.
$W=V\times_ZX$. The composition isomorphism is induced by the pasting isomorphism
$(V\times_ZY)\times_YX\cong V\times_ZX$, which is natural in the sheaves and hence
compatible with these objectwise tensor maps, and with the unit maps. Passing to
sheafifications gives the claim.
