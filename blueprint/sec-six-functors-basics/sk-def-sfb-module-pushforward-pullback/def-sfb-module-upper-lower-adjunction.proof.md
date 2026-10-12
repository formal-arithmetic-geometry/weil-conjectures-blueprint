+++
kind  = "proof"
of    = "def-sfb-module-upper-lower-adjunction"
+++
The adjunction $f^*_{\Ab}\dashv f^{\Ab}_*$ is monoidal
([sk-def-sfb-finite-pushforward-pullback]), so it lifts to module objects as stated
([sk-def-sfb-transport]); a composite of adjunctions is an adjunction. For the
displayed isomorphism: transport along $f^{\Ab}_*$ commutes with restriction of
scalars, $\operatorname{mapMod}(f^{\Ab}_*)\circ\operatorname{Res}_{\alpha_f}\cong
\operatorname{Res}_{f^{\Ab}_*\alpha_f}\circ\operatorname{mapMod}(f^{\Ab}_*)$, and
restrictions of scalars compose,
$\operatorname{Res}_u\circ\operatorname{Res}_{f^{\Ab}_*\alpha_f}
=\operatorname{Res}_{f^{\Ab}_*\alpha_f\circ u}$. Since $\eta_f$ is the mate of
$\alpha_f$, i.e. $\eta_f=f^{\Ab}_*\alpha_f\circ u$
([sk-def-sfb-coefficient-morphisms]), the right-hand side is
$\operatorname{Res}_{\eta_f}\circ\operatorname{mapMod}(f^{\Ab}_*)=f_*$.
