+++
id = "lemma-weil-pbc-finite-pullback-identity"
kind = "lemma"
title = "Finite pullback identity"
order = 1562
lean = ["AlgebraicGeometry.Etale.globalSectionsUpperStarMap_id"]
uses = ["def-weil-pbc-finite-section-pullback"]
+++
Let $T$ be a scheme and $G$ an etale sheaf on $T$ (with values in $\mathcal A$
as in [def-weil-pbc-finite-section-pullback]). The pullback of global sections
$\mathrm{id}_T^\sharp:\Gamma(T,G)\to\Gamma(T,\mathrm{id}_T^{-1}G)$ along the
identity, followed by the map on global sections induced by the canonical
isomorphism $\mathrm{id}_T^{-1}G\cong G$, is the identity of $\Gamma(T,G)$.
