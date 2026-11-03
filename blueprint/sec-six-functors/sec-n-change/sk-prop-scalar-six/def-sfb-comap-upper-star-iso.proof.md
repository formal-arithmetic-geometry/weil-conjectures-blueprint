+++
kind  = "proof"
of    = "def-sfb-comap-upper-star-iso"
uses = ["det-def-sfb-transport", "sk-prop-sfb-cartesian-coefficients", "def-sfb-extend-comap-iso-of-iso", "lem-sfb-coefficient-pullback-square"]
+++
On module objects $f^*=\operatorname{Ext}_{\alpha_f}\circ\mathrm{mapMod}(f^*)$
([det-def-sfb-module-pushforward-pullback]). Transport commutes with restriction of scalars
([det-def-sfb-transport]):
$\mathrm{mapMod}(f^*)\circ\operatorname{Res}_{a_Y}\cong\operatorname{Res}_{f^*a_Y}\circ
\mathrm{mapMod}(f^*)$. The square $\alpha'_f\circ f^*a_Y=a_X\circ\alpha_f$ of
[lem-sfb-coefficient-pullback-square] has invertible horizontal sides $\alpha_f$, $\alpha'_f$
([sk-prop-sfb-cartesian-coefficients]), so [def-sfb-extend-comap-iso-of-iso] gives
$\operatorname{Res}_{a_X}\circ\operatorname{Ext}_{\alpha'_f}\cong\operatorname{Ext}_{\alpha_f}
\circ\operatorname{Res}_{f^*a_Y}$. Combining,

$$
\operatorname{Res}_{a_X}\operatorname{Ext}_{\alpha'_f}\mathrm{mapMod}(f^*)
\cong\operatorname{Ext}_{\alpha_f}\operatorname{Res}_{f^*a_Y}\mathrm{mapMod}(f^*)
\cong\operatorname{Ext}_{\alpha_f}\mathrm{mapMod}(f^*)\operatorname{Res}_{a_Y}.
$$
