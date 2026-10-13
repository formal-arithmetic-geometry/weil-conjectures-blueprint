+++
kind  = "proof"
of    = "prop-sf-closed-immersion-unit"
+++
By [lem-exc-proetale-closed-exact], the closed direct image is exact (the
complement of $Z$ is quasi-compact because $T$ is Noetherian), so $Ri_*$ is
computed by $i_*$ on any complex, and [lem-exc-proetale-closed-support]
provides its right adjoint $Ri^!$ on the ambient derived categories.

By [prop-weil-open-closed-recollement-adjunctions], $i^*\dashv Ri_*$ on the
ambient derived categories and the counit $i^*Ri_*\to\operatorname{id}$ is an
isomorphism. A right adjoint whose counit is an isomorphism is fully
faithful, so for all $P,Q\in D(Z_{\mathrm{proet}},A)$ the map
$g\mapsto Ri_*g$ is a bijection

$$
\Hom(P,Q)\xrightarrow{\ \sim\ }\Hom(Ri_*P,Ri_*Q).
$$

Now fix $Q$ and consider, for every $P$, the composite

$$
\Hom(P,Q)\xrightarrow{\ \eta^!_{i,Q}\circ-\ }\Hom(P,Ri^!Ri_*Q)
\xrightarrow{\ \sim\ }\Hom(Ri_*P,Ri_*Q),
$$

the second map being the adjunction bijection of $Ri_*\dashv Ri^!$. By the
triangle identity, the adjoint of $\eta^!_{i,Q}\circ g$ is
$\epsilon^!_{Ri_*Q}\circ Ri_*(\eta^!_{i,Q})\circ Ri_*g=Ri_*g$, so the
composite is the bijection displayed above. Hence composition with
$\eta^!_{i,Q}$ is a bijection $\Hom(P,Q)\to\Hom(P,Ri^!Ri_*Q)$, naturally in
$P$, and the Yoneda lemma shows that $\eta^!_{i,Q}$ is an isomorphism.

For the last assertion, the right adjoint $Ri_n^{\times}$ of
$Ri_{!,n}=Ri_*$ given by the datum of [def-weil-ambient-exceptional-adjoint]
is, by uniqueness of right adjoints, identified with $Ri^!$ together with its
unit. The functor $Ri^!$ of [def-weil-exceptional-inverse-image] is its
restriction to $D^b_c$, with the same unit, so its unit at $Q\in D^b_c(Z,A)$
is the isomorphism just proved.
