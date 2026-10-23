+++
kind  = "proof"
of    = "lem-sfb-pullback-from-point-comp-monoidal"
uses = ["lem-sfb-finite-monoidal-adjunction"]
+++
By construction, the isomorphism is $p^*$ whiskered with the inverse of the
composition isomorphism $(\pi_Y\circ f)^*\cong f^*\circ\pi_Y^*$, followed by
an equality. It therefore suffices that this composition isomorphism is
monoidal.

That isomorphism is the mate, under the adjunctions $g^*\dashv g_*$, of the
composition isomorphism $\pi_{Y*}\circ f_*\cong(\pi_Y\circ f)_*$ of
pushforwards. The latter is monoidal for the lax monoidal structures of the
pushforwards, because on sections both sides are restriction along canonical
isomorphisms of iterated fibre products, and these commute with the
objectwise tensor product. The adjunctions are monoidal
([lem-sfb-finite-monoidal-adjunction]). The mate of a monoidal natural
transformation between lax monoidal right adjoints is monoidal for the
induced oplax structures on the left adjoints, and these are the strong
monoidal structures.
