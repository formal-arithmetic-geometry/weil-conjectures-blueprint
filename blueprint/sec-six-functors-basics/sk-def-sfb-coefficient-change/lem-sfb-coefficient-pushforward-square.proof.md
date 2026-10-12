+++
kind  = "proof"
of    = "lem-sfb-coefficient-pushforward-square"
uses = ["lem-sfb-coefficient-pullback-square"]
+++
By [sk-def-sfb-coefficient-morphisms], $\eta_f$ is the unit $u_{\Lambda_Y}\colon\Lambda_Y\to
f_*f^*\Lambda_Y$ of the adjunction $f^*\dashv f_*$ of
[sk-def-sfb-finite-pushforward-pullback] followed by $f_*\alpha_f$, and likewise for $\eta'_f$.
Hence, using [lem-sfb-coefficient-pullback-square] in the second step and the naturality of the
unit in the third,

$$
f_*a_X\circ\eta_f=f_*(a_X\circ\alpha_f)\circ u_{\Lambda_Y}
=f_*\alpha'_f\circ f_*f^*a_Y\circ u_{\Lambda_Y}
=f_*\alpha'_f\circ u_{\Lambda'_Y}\circ a_Y=\eta'_f\circ a_Y .
$$
