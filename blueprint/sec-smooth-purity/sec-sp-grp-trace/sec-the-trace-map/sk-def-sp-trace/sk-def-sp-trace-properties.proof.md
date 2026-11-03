+++
kind = "proof"
of = "det-sp-trace-basic"
+++
(1) $\gamma_f$ and $\varepsilon_f$ are natural transformations, so their composite
is natural. Transporting an adjunction $F\dashv G$ along a natural isomorphism
$\gamma:G'\xrightarrow{\sim}G$ gives an adjunction $F\dashv G'$ with counit
$\varepsilon\circ F\gamma$, which is exactly $\operatorname{Tr}_f$.

(2) The purity map of $p_d$ is the inverse orientation followed by the tensor
map; by [det-sp-orientation-charts] (the case $U=\mathbf A^d_Y$, $e=\mathrm{id}$) the
orientation of $p_d$ is the affine-space orientation given by its coordinate
adjunction, whose counit is iterated affine-line integration. Hence
$\operatorname{Tr}_{p_d}(\Lambda_Y)=\varepsilon_{p_d}\circ Rp_{d!}\gamma_{p_d}$ is the
counit of the coordinate adjunction at $\Lambda_Y$, i.e. affine-space
integration, normalized on geometric fibres by sending the class of the
origin (the $d$-fold product of the Cartier classes of the coordinate
hyperplanes) to $1$. Since each Kummer boundary $\partial\kappa(t_j)$ is minus
the Cartier class of $V(t_j)$ ([lem-pur-divisor-class]), the product of the
Kummer boundaries goes to $(-1)^d$. For finite
coefficients this is the finite trace of [def-pur-smooth-trace]; for the other
coefficients it is its transport.

(3) For étale $f$ the adjunction $f_!\dashv f^*$ has as counit the sum over the
fibres; with $d=0$ the orientation is the identity ($\omega_f=f^*\Lambda_Y=\Lambda_X$
by the étale chart description), so $\gamma_f=\mathrm{id}$ and $\operatorname{Tr}_f$ is
this counit; for finite $f$, $f_!=f_*$.
