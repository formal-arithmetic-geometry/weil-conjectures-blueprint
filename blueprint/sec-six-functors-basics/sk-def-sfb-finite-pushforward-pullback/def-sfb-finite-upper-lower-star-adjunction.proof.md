+++
kind  = "proof"
of    = "def-sfb-finite-upper-lower-star-adjunction"
+++
On presheaves, $\operatorname{Lan}_{b^{\mathrm{op}}}$ is left adjoint to restriction along
$b^{\mathrm{op}}$, and sheafification is left adjoint to the inclusion of sheaves into
presheaves. Restriction along $b^{\mathrm{op}}$ sends sheaves to sheaves
([def-sfb-finite-lower-star]) and there agrees with $g_*$. Composing the adjunctions gives
$\Hom(\operatorname{sheafify}\operatorname{Lan}_{b^{\mathrm{op}}}F,G)
\cong\Hom(\operatorname{Lan}_{b^{\mathrm{op}}}F,G)\cong\Hom(F,G\circ b^{\mathrm{op}})
=\Hom(F,g_*G)$.
