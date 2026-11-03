+++
kind  = "proof"
of    = "def-sfb-derived-comap-lower-star-iso"
uses = ["def-sfb-comap-lower-star-iso", "lem-sfb-comap-preserves-k-injectives"]
+++
Restriction of scalars is exact, so its right derived functor is the levelwise
$D(\operatorname{Res})$, and post-composing a right derived functor with an exact functor gives
the right derived functor of the composite:
$D(\operatorname{Res}_{a_Y})\circ R(f_*)\cong R(\operatorname{Res}_{a_Y}\circ f_*)$. By
[def-sfb-comap-lower-star-iso] the latter is $R(f_*\circ\operatorname{Res}_{a_X})$. Since
$\operatorname{Res}_{a_X}$ is exact and preserves K-injective complexes
([lem-sfb-comap-preserves-k-injectives]), computing on K-injective resolutions gives
$R(f_*\circ\operatorname{Res}_{a_X})\cong R(f_*)\circ R(\operatorname{Res}_{a_X})\cong
R(f_*)\circ D(\operatorname{Res}_{a_X})$.
