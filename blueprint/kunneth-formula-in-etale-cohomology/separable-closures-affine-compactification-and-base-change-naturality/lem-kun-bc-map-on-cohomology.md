+++
id = "lem-kun-bc-map-on-cohomology"
kind = "lemma"
title = "Cohomology of a derived base-change map"
order = 6112
lean = ["AlgebraicGeometry.Etale.exchange_cohomologySheaf_eq"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange", "def-weil-pbc-underived-exchange", "def-kun-truncations"]
+++
For a cartesian square and a sheaf $F$, the morphism on $q$-th cohomology
sheaves induced by
$$
 g^{-1}Rf_*F\longrightarrow Rf'_*(g')^{-1}F
$$
is the usual base-change morphism
$g^{-1}R^qf_*F\to R^qf'_*(g')^{-1}F$.

## Proof

The derived exchange morphism is the mate of the underived one, and the
mate construction is natural in the object; applying it to the truncation
triangles $\tau_{\le n}$ of [def-kun-truncations] shows that its $q$-th
cohomology sheaf is the map induced by the underived exchange of the sheaf
$\mathcal H^q(F)$. That induced map is precisely
$g^{-1}R^qf_*F\to R^qf'_*(g')^{-1}F$, by the definition of the underived
exchange morphism together with the description of higher direct images.

Unresolved dependencies: def:weil-pbc-direct-image
