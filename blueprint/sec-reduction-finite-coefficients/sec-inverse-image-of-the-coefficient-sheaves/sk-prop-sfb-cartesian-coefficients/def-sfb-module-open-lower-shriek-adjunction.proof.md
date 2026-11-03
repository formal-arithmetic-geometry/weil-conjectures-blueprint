+++
kind  = "proof"
of    = "def-sfb-module-open-lower-shriek-adjunction"
uses = ["sk-prop-sfb-cartesian-coefficients"]
+++
The composite of $\operatorname{Res}_{\alpha_j}\dashv\operatorname{Coext}_{\alpha_j}$
and $j^{\mathrm{lin}}_!\dashv\operatorname{mapMod}(j^*_{\Ab})$ is an adjunction
$j^{\mathrm{lin}}_!\circ\operatorname{Res}_{\alpha_j}\dashv
\operatorname{Coext}_{\alpha_j}\circ\operatorname{mapMod}(j^*_{\Ab})$. The coefficient
morphism $\alpha_j$ is an isomorphism ([sk-prop-sfb-cartesian-coefficients]), and for
an invertible morphism of ring objects extension, restriction and coextension of
scalars agree ([det-def-sfb-change-of-scalars]); in particular
$\operatorname{Coext}_{\alpha_j}\cong\operatorname{Ext}_{\alpha_j}$, so the right
adjoint is isomorphic to $j^*$.
