+++
id = "lem-weil-pbc-tower-compatibility"
kind = "lemma"
title = "Compatibility with the coefficient tower"
order = 1345
uses = ["def-weil-pbc-four-arrows", "def-weil-pbc-four-corners", "lem-weil-pbc-finite-level-rectangle"]
+++
The transition morphisms $P_{n+1}\to P_n$ make each of the four corner
families an object
$$
 A_\bullet,B_\bullet,C_\bullet,D_\bullet
 \in D(\operatorname{Tow}_{A}(Y'))
$$
after restriction of scalars, and make $h,h',v,v'$ morphisms in this derived
tower category. Evaluation at $n$ recovers the four displayed corners and
arrows. The rectangle equation commutes with every transition and with every
compatible endomorphism of $K$.

## Proof

The normalization isomorphisms of [def-weil-pbc-four-arrows] make the four
families strict towers, and the reduction compatibilities of the projection
formula and of the finite-level exchange map make the four arrows tower
morphisms; the rectangle equation of [lem-weil-pbc-finite-level-rectangle]
is then compatible with the transitions by construction.
