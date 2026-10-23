+++
kind  = "proof"
of    = "lem-weil-pbc-comparison-sections"
+++
Let $P$ be the presheaf inverse image of $F$, the left Kan extension along the
inclusion of [def-weil-pbc-site-comparison-morphism], so that $\nu_S^*F$ is
the sheafification of $P$ and $P(V)=F(V)$ on etale objects.

*Affine stages.* Suppose first that every $U_i$ is affine. Maps from the
cofiltered limit $U$ of quasi-compact quasi-separated schemes with affine
transition maps into an etale, hence locally finitely presented, $S$-scheme
$V$ form the filtered colimit of the sets of maps $U_i\to V$, by the descent of
finite-presentation data in [lem-weil-pbc-etale-finite-data-descent]. Hence
the system $(U_i)$ is cofinal in the category computing $P(U)$, and
$P(U)=\varinjlim_iF(U_i)$. Restricted to such affine pro-etale objects, $P$ is
already a sheaf. A covering of an affine pro-etale object is refined by a finite
covering by affine pro-etale objects; writing its members as limits of affine
etale maps by [lem-weil-pbc-ind-etale-stability], its Cech diagram is the
filtered colimit of the Cech diagrams of etale coverings at the finite stages.
The sheaf condition for $F$ holds at every stage, and filtered colimits of
modules commute with the finite products and equalizers involved. The affine
pro-etale objects form a dense subsite of $S_{\Proet}$
([def-weil-pbc-ind-etale-basis], [lem-weil-pbc-ind-etale-basis], applied over
the affine opens of $S$), so sheafification does not change the sections of
a presheaf which is already a sheaf on that subsite. Thus
$(\nu_S^*F)(U)=P(U)=\varinjlim_iF(U_i)$.

*General stages.* Fix $i_0$. As $U_{i_0}$ is quasi-compact and
quasi-separated, choose a finite cover by affine opens $O_k$ together with
finite affine open covers $W_{klm}$ of the intersections $O_k\cap O_l$. Their
preimages in the $U_i$, $i\to i_0$, are affine, so their preimages in $U$ are
affine pro-etale objects presented by affine stages. They form a finite
$1$-hypercover of $U$ and compatible etale $1$-hypercovers of the $U_i$. The
sheaf conditions for $\nu_S^*F$ on $U$ and for $F$ on each $U_i$ are equalizers
of finite products; the affine case identifies the terms for $U$ with the
filtered colimits of the terms for the $U_i$, and filtered colimits commute with
finite limits. Hence $\varinjlim_iF(U_i)\to(\nu_S^*F)(U)$ is an isomorphism.
