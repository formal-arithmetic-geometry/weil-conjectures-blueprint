+++
kind  = "proof"
of    = "sk-prop-sfb-qlbar-colimit-point"
+++
The transition maps are [def-sfb-qlbar-subextension-map], and the cocone maps, with their
compatibility, are [def-sfb-qlbar-subextension-to-qlbar].

Colimits in $\Sh(*_{\mathrm{proét}},\Ab)$ are computed as follows: take the colimit of
presheaves, which is formed sectionwise, and then sheafify. Let
$P=\colim_E\underline E$ be the presheaf colimit and fix a profinite set $S$. Each map
$C(S,E)\to C(S,\Qlb)$ is injective, because $E\to\Qlb$ is. The poset $\mathcal E$ is
directed. Hence the filtered colimit $P(S)=\colim_EC(S,E)$ maps isomorphically onto the
union $\bigcup_EC(S,E)$ inside $C(S,\Qlb)$.

This union is $\underline{\Qlb}(S)$. A continuous map $S\to E$ composed with
$E\subseteq\Qlb$ is a section of $\underline{\Qlb}$ over $S$. Conversely, let
$a\in\underline{\Qlb}(S)$ take values in $E$. Its corestriction $S\to E$ is continuous for
the subspace topology on $E$, so $a$ comes from $C(S,E)$. Therefore the map
$P\to\underline{\Qlb}$ induced by the cocone is an isomorphism of presheaves. Now
$\underline{\Qlb}$ is a sheaf ([sk-def-sfb-qlbar-condensed]), so $P$ is already a sheaf and
sheafification does not change it. Hence the cocone is a colimit in
$\Sh(*_{\mathrm{proét}},\Ab)$.
