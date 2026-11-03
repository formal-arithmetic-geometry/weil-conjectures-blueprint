+++
kind  = "proof"
of    = "def-sfb-finite-extension-by-zero-adjunction"
uses = ["def-sfb-finite-lower-star", "def-sfb-finite-upper-lower-star-adjunction"]
+++
The localization functor $\ell$ is continuous and cocontinuous, so restriction along it,
$G\mapsto G\circ\ell^{\mathrm{op}}$, is a functor $j^{-1}$ on sheaves. As for
[def-sfb-finite-upper-lower-star-adjunction], $j_!=\operatorname{sheafify}\circ
\operatorname{Lan}_{\ell^{\mathrm{op}}}$ is left adjoint to $j^{-1}$. Since $j$ is weakly
étale, $\ell$ is left adjoint to base change along $j$, and this induces an adjunction
$j^{-1}\dashv j_*$, with $j_*$ as in [def-sfb-finite-lower-star]. Both $j^{-1}$ and $j^*$
are then left adjoint to $j_*$ ([def-sfb-finite-upper-lower-star-adjunction]), so
$j^*\cong j^{-1}$, and $j_!\dashv j^{-1}\cong j^*$.
