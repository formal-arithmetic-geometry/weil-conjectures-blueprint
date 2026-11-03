+++
kind  = "proof"
of    = "def-sfb-comap-open-immersion-shriek-iso"
uses = ["def-sfb-projection-formula-comap", "lem-sfb-coefficient-pullback-square"]
+++
On module objects $j_!=(j_!)_{\Lambda_X}\circ\operatorname{Res}_{\alpha_j}$, the linearization of
the abelian $j_!$ through its projection formula with respect to $j^*$, after restriction of
scalars along $\alpha_j\colon j^*\Lambda_X\to\Lambda_U$ ([det-def-sfb-module-lower-shriek]). By
[def-sfb-projection-formula-comap] (with $S=j^*$, $\varphi=a_X$),
$\operatorname{Res}_{a_X}\circ(j_!)_{\Lambda'_X}\cong(j_!)_{\Lambda_X}\circ
\operatorname{Res}_{j^*a_X}$, so

$$
\operatorname{Res}_{a_X}\circ j_!\cong(j_!)_{\Lambda_X}\circ\operatorname{Res}_{j^*a_X}\circ
\operatorname{Res}_{\alpha'_j}\cong(j_!)_{\Lambda_X}\circ\operatorname{Res}_{\alpha'_j\circ j^*a_X}.
$$

By [lem-sfb-coefficient-pullback-square], $\alpha'_j\circ j^*a_X=a_U\circ\alpha_j$, and
$\operatorname{Res}_{a_U\circ\alpha_j}\cong\operatorname{Res}_{\alpha_j}\circ
\operatorname{Res}_{a_U}$, which gives $j_!\circ\operatorname{Res}_{a_U}$.
