+++
kind  = "proof"
of    = "def-sfb-modobj-linearization-transport-adjunction"
+++
Take $G=S$ in [def-sfb-modobj-linearization-right-adjoint]. Then $\theta_{L,N}$ is the lax
structure map $\mu^S_{L,N}$. Indeed, $\theta_{L,N}$ is the adjoint of
$(L\otimes c_N)\circ\pi_{L,SN}$, and by the definition of $\pi$
([def-sfb-adjunction-projection-formula]) and naturality of $\mu^S$ this is
$\mu^S_{L,N}\circ(SL\otimes Sc_N\,u_{SN})=\mu^S_{L,N}$, by a triangle identity. So
$S_{\mathcal B}$ is $\operatorname{mapMod}(S)$ ([def-sfb-modobj-transport]), and the
adjunction is the one of [def-sfb-modobj-linearized-adjunction].
