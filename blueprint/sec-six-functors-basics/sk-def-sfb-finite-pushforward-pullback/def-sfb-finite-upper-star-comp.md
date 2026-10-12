+++
id = "def-sfb-finite-upper-star-comp"
kind = "definition"
title = "Composition isomorphism for pullbacks"
order = 1510
uses = ["def-sfb-finite-lower-star-comp", "def-sfb-finite-upper-lower-star-adjunction"]
lean = ["AlgebraicGeometry.ProEtale.upperStarComp"]
+++
For morphisms $h_1\colon T\to S$ and $h_2\colon S\to R$, the *composition isomorphism*
of pullbacks

$$
(h_2\circ h_1)^*\xrightarrow{\ \sim\ }h_1^*\circ h_2^*
$$

is the conjugate, under the adjunctions of
[def-sfb-finite-upper-lower-star-adjunction], of the inverse of the composition
isomorphism $(h_2)_*\circ(h_1)_*\cong(h_2\circ h_1)_*$ of [def-sfb-finite-lower-star-comp].
