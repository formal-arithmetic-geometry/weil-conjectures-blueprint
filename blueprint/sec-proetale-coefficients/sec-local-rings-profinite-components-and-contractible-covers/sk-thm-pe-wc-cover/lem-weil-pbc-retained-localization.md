+++
id = "lem-weil-pbc-retained-localization"
kind = "lemma"
title = "Properties of the retained localization"
order = 946
lean = ["Ideal.WLocalization.indZariski", "Ideal.WLocalization.isWLocalRing", "Ideal.WLocalization.zeroLocus_map_algebraMap_eq_closedPoints", "Ideal.WLocalization.bijOn_zeroLocus_map", "Ideal.WLocalization.quotientMap_algebraMap_bijective", "Ideal.WLocalization.algebraMap_specComap_preimage_closedPoints_eq", "Ideal.WLocalization.faithfullyFlat_map_algebraMap"]
uses = ["def-weil-pbc-ind-etale-algebra", "def-weil-pbc-retained-localization", "def-weil-pbc-w-local", "lem-weil-pbc-ind-etale-stability", "lem-weil-pbc-w-localization-points"]
+++
Let $R$ be a ring and $J\subset R$ an ideal, and let $R_{[J]}$ be as in
[def-weil-pbc-retained-localization].

1. The map $R\to R_{[J]}$ is ind-Zariski [def-weil-pbc-ind-etale-algebra], and
   $\operatorname{Spec}R_{[J]}$ is w-local [def-weil-pbc-w-local].
2. If $V(J)$ consists of closed points of $\operatorname{Spec}R$, then the
   closed points of $\operatorname{Spec}R_{[J]}$ are exactly the points of
   $V(JR_{[J]})$, the map $V(JR_{[J]})\to V(J)$ is bijective, and
   $R/J\to R_{[J]}/JR_{[J]}$ is an isomorphism.
3. Let $A$ be a w-local ring, $I\subset A$ an ideal with $V(I)$ the set of closed
   points of $\operatorname{Spec}A$, and $B$ an $A$-algebra such that for every
   prime $\mathfrak q$ of $B$ over a maximal ideal $\mathfrak m$ of $A$ the residue
   field extension $\kappa(\mathfrak q)/\kappa(\mathfrak m)$ is algebraic. Then the
   closed points of $\operatorname{Spec}B_{[IB]}$ are exactly the points of
   $V(IB_{[IB]})$. If moreover $A\to B$ is faithfully flat, so is
   $A\to B_{[IB]}$.
