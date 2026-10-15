+++
kind  = "proof"
of    = "det-prop-sfb-cartesian-coefficients-finite-free"
+++
$\cO_F$ is a finite torsion-free, hence free, module over the discrete valuation ring
$\cO_E$, of rank $d$. The map $\cO_E^d\to\cO_F$, $(a_i)\mapsto\sum a_ib_i$, is a continuous
$\cO_E$-linear bijection between compact Hausdorff spaces, hence a homeomorphism. So for
every profinite $S$ it induces a bijection $C(S,\cO_E)^d=C(S,\cO_E^d)\to C(S,\cO_F)$, natural in
$S$ and $C(S,\cO_E)$-linear: an isomorphism of condensed $\underline{\cO_E}$-modules
$\underline{\cO_E}^{\,d}\cong\underline{\cO_F}$ ([sk-def-sfb-condensed-ring]). Apply the
additive, monoidal functor $p_X^*$ ([sk-def-sfb-pullback-from-point]): it gives
$\cO_{E,X}^{\,d}\cong\cO_{F,X}$ as $\cO_{E,X}$-modules. Inverting $\ell$
([det-prop-sfb-qlbar-colimit-x-invert-ell]) gives $E_X^{\,d}\cong F_X$, and the two
isomorphisms are compatible with $\cO\to E$ by construction. Compatibility with inverse
image follows from naturality of $f^{-1}p_Y^*\cong p_X^*$.
