+++
kind  = "proof"
of    = "prop-sf-closed-unit-all-stages"
+++
*Finite stage.* By [prop-weil-open-closed-recollement-adjunctions] the
counit $i^*i_*\to\operatorname{id}$ of $i^*\dashv i_*$ is an isomorphism, so
$i_*$ is fully faithful on the ambient categories and hence on the full
subcategories $D^b_c$.

*Integral stage.* Put $R=\mathcal O_E$ and $A_n=R/\varpi_E^n$. For
$P,Q\in D^b_c(Z,R)$ one has $Q\cong R\varprojlim_n\operatorname{Res}_nQ_n$
and, by [prop-weil-pbc-direct-image-limits],
$i_*Q\cong R\varprojlim_n\operatorname{Res}_ni_*Q_n$ with
$(i_*P)_n\cong i_*P_n$. Extension and restriction of scalars give
$\operatorname{Hom}(P[m],\operatorname{Res}_nQ_n)
=\operatorname{Hom}_{A_n}(P_n[m],Q_n)$ and
$\operatorname{Hom}(i_*P[m],\operatorname{Res}_ni_*Q_n)
=\operatorname{Hom}_{A_n}(i_*P_n[m],i_*Q_n)$, and $i_*$ identifies the two by
the finite stage, compatibly with the transition maps. Apply
$\operatorname{Hom}(P[m],-)$ and $\operatorname{Hom}(i_*P[m],-)$ to the two
Roos triangles of [prop-weil-pbc-roos-triangle]; the map induced by $i_*$ is
an isomorphism on the two product terms for all $m$, so by the five lemma
$\operatorname{Hom}(P,Q)\to\operatorname{Hom}(i_*P,i_*Q)$ is bijective.

*Rational stage.* Hom groups in $D^b_c(-,E)$ are the integral ones tensored
with $E$ ([def-weil-rationalization-karoubi]), and $i_*$ is the
rationalized integral functor, so bijectivity persists.

*Algebraically closed stage.* Hom groups in $D^b_c(-,\Qlb)$ are filtered
colimits over finite extensions $L$ of Hom groups at the stage $L$
([def-weil-algebraically-closed-coefficients]), and $i_*$ commutes with
finite scalar extension ([prop-weil-pbc-scalar-extension]); a colimit of
bijections is a bijection.

*The unit.* Given a right adjoint $Ri^!$ at the stage $\Lambda$, fix $Q$.
For every $P$ the composite of $\eta_Q\circ-:\operatorname{Hom}(P,Q)\to
\operatorname{Hom}(P,Ri^!i_*Q)$ with the adjunction bijection onto
$\operatorname{Hom}(i_*P,i_*Q)$ is, by a triangle identity, $g\mapsto i_*g$,
which is bijective by full faithfulness. So $\eta_Q\circ-$ is bijective,
naturally in $P$, and Yoneda makes $\eta_Q$ an isomorphism, exactly as in
[prop-sf-closed-immersion-unit].
