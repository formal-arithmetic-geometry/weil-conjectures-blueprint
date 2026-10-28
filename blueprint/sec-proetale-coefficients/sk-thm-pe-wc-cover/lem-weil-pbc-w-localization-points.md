+++
id = "lem-weil-pbc-w-localization-points"
kind = "lemma"
title = "Points of the affine w-localization"
order = 944
lean = ["WLocalization.indZariski", "WLocalization.faithfullyFlat", "RingHom.IndZariski.bijectiveOnStalks", "WLocalization.isWLocalRing", "WLocalization.zeroLocus_ideal_eq", "WLocalization.eq_of_specializes_of_mem_zeroLocus_ideal", "WLocalization.bijOn_algebraMap_specComap_zeroLocus_ideal", "WLocalization.bijOn_specComap_zeroLocus_map", "WLocalization.quotientMap_algebraMap_bijective_of_ideal"]
uses = ["def-weil-pbc-ind-etale-algebra", "def-weil-pbc-w-local", "def-weil-pbc-w-localization", "lem-weil-pbc-ind-etale-stability"]
+++
The map $A\to A^w$ of [def-weil-pbc-w-localization] is ind-Zariski
[def-weil-pbc-ind-etale-algebra] and faithfully flat, and it identifies local
rings: $A_{\mathfrak q\cap A}\to A^w_{\mathfrak q}$ is an isomorphism for
every prime $\mathfrak q$ of $A^w$. The spectrum of $A^w$ is w-local
[def-weil-pbc-w-local], its closed points are exactly the points of
$V(I_A)$, every point specializes to a unique point of $V(I_A)$, and
$\operatorname{Spec}A^w\to\operatorname{Spec}A$ restricts to a bijection
$V(I_A)\to\operatorname{Spec}A$. If $J\subset A$ is an ideal such that
$V(J)$ consists of closed points, then $V(JA^w)\to V(J)$ is bijective and
$A/J\to A^w/JA^w$ is an isomorphism.
