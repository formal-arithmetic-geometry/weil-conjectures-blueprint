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

For the last assertion no ambient datum is used. Write $Ri^!_c$ for the
functor of [def-weil-exceptional-inverse-image]; its adjunction
$\Hom_T(Ri_*P,M)\cong\Hom_Z(P,Ri^!_cM)$ holds for every bounded-below $P$ of
etale origin and every bounded-below $M$ ([thm-sf-ambient-adjoint-class]),
and $Ri^!_cM=\nu_Z^*i^{\times}R\nu_{T,*}M$ is then again bounded below of
etale origin. Let $Q\in D^b_c(Z,A)$, so that $Q$ and $Ri^!_cRi_*Q$ both
lie in the full subcategory of bounded-below objects of etale origin. For
$P$ in that subcategory the composite of composition with the unit
$Q\to Ri^!_cRi_*Q$ and the adjunction bijection is, by the triangle
identity as above, the map $g\mapsto Ri_*g$, which is bijective by the full
faithfulness just shown. The Yoneda lemma in that full subcategory shows that
the unit $Q\to Ri^!_cRi_*Q$ is an isomorphism.
