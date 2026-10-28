+++
id = "det-pe-wc-rings-w-local-refinement"
kind = "lemma"
title = "A w-local refinement over the closed points"
lean = ["Ideal.WLocalization", "Ideal.WLocalization.indZariski", "Ideal.WLocalization.isWLocalRing", "Ideal.WLocalization.faithfullyFlat_map_algebraMap", "Ideal.WLocalization.algebraMap_specComap_preimage_closedPoints_eq", "Algebra.IndEtale.trans", "Algebra.IndEtale.isSeparable_residueField", "RingHom.IndZariski.bijectiveOnStalks"]
order = 938
uses = ["def-weil-pbc-retained-localization", "lem-weil-pbc-retained-localization", "lem-weil-pbc-ind-etale-stability", "lem-weil-pbc-weak-etale-field", "det-pe-wlocal-strict-contractible"]
+++
Let $R$ be w-local [det-pe-wlocal-strict-contractible], let $I\subset R$ be an ideal with
$V(I)=(\operatorname{Spec}R)^c$, and let $R\to B$ be faithfully flat and ind-étale. Put
$B'=B_{[IB]}$ [def-weil-pbc-retained-localization]. Then:

1. $B\to B'$ is ind-Zariski, and $R\to B'$ is ind-étale and faithfully flat;
2. $\operatorname{Spec}B'$ is w-local;
3. the closed points of $\operatorname{Spec}B'$ are exactly the points of $V(IB')$; in
   particular every closed point of $\operatorname{Spec}B'$ lies over a closed point of
   $\operatorname{Spec}R$, and the induced map
   $(\operatorname{Spec}B')^c\to(\operatorname{Spec}R)^c$ is surjective;
4. $B\to B'$ identifies local rings.
