+++
kind  = "proof"
of    = "def-sfb-comap-lower-star-iso"
uses = ["def-sfb-comap-mapmod-square", "lem-sfb-coefficient-pushforward-square"]
+++
On module objects $f_*=\operatorname{Res}_{\eta_f}\circ\mathrm{mapMod}(f_*)$
([sk-def-sfb-module-pushforward-pullback]), with $f_*$ on abelian sheaves lax monoidal. Apply
[def-sfb-comap-mapmod-square] to $F=f_*$, $\varphi_X=a_X$, $\varphi_Y=a_Y$, $\eta_R=\eta_f$,
$\eta_S=\eta'_f$; the required square commutes by [lem-sfb-coefficient-pushforward-square].
