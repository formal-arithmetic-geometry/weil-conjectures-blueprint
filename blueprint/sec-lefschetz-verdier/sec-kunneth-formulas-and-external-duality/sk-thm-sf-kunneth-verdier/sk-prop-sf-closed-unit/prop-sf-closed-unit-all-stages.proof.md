+++
kind  = "proof"
of    = "prop-sf-closed-unit-all-stages"
+++
*Full faithfulness.* The argument is the same for every $\Lambda$. Apply
[sk-prop-sf-open-closed-triangle] with $B=\Lambda_X$, whose inverse image on
$Z$ is $\Lambda_Z$ ([det-def-sfb-pulled-back-coefficients]). The functors
$i^*$ and $i_*$ on $\Lambda$-module sheaves are exact, so they pass to the
derived categories without deriving, and $i^*\dashv i_*$ persists there
([prop-weil-open-closed-recollement-adjunctions]). The counit
$i^*i_*N\to N$ is an isomorphism of sheaves, because $i_*$ is fully
faithful on module sheaves ([sk-prop-sf-open-closed-triangle]). Applied
termwise to a complex, it is an isomorphism $i^*i_*\cong\operatorname{id}$ on
$D(Z_{\mathrm{proét}},\Lambda)$. A right adjoint whose counit is an
isomorphism is fully faithful, so $i_*$ is fully faithful on
$D(-_{\mathrm{proét}},\Lambda)$, hence on the full subcategories $D^b_c$.

*The unit.* Let $Ri^!$ be the right adjoint of $i_*$ on $D^b_c$
([sk-thm-existence], (3) and (4), with $Ri_!=i_*$ since $i$ is proper), and fix
$Q$. For every $P$ the composite of $\eta_Q\circ-:\operatorname{Hom}(P,Q)\to
\operatorname{Hom}(P,Ri^!i_*Q)$ with the adjunction bijection onto
$\operatorname{Hom}(i_*P,i_*Q)$ is, by a triangle identity, $g\mapsto i_*g$,
which is bijective by full faithfulness. So $\eta_Q\circ-$ is bijective,
naturally in $P$, and Yoneda makes $\eta_Q$ an isomorphism, exactly as in
[prop-sf-closed-immersion-unit].
