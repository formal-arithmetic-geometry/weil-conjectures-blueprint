+++
id = "lem-weil-pbc-strict-w-cover"
kind = "lemma"
title = "Properties of the strict w-local cover"
order = 945
lean = ["WStrictLocalization.indEtale", "WStrictLocalization.faithfullyFlat", "WStrictLocalization.isWLocalRing", "WStrictLocalization.isWStrictlyLocalRing", "WStrictLocalization.zeroLocus_map_eq_closedPoints", "WStrictLocalization.exists_mem_zeroLocus_comap_eq", "exists_isWStrictlyLocalRing"]
uses = ["def-weil-pbc-henselian-terminology", "def-weil-pbc-ind-etale-algebra", "def-weil-pbc-strict-w-cover", "def-weil-pbc-w-local", "lem-weil-pbc-etale-contraction", "lem-weil-pbc-ind-etale-stability", "lem-weil-pbc-retained-localization", "lem-weil-pbc-w-localization-points", "lem-weil-pbc-weak-etale-field"]
+++
The algebra $C_A$ is faithfully flat and ind-etale
[def-weil-pbc-ind-etale-algebra] over $A$. Its spectrum is w-local
[def-weil-pbc-w-local], its closed points are exactly the points of
$V(IC_A)$ (notation of [def-weil-pbc-strict-w-cover]), its maximal local
rings are strictly henselian [def-weil-pbc-henselian-terminology], and its
closed points surject onto $\operatorname{Spec}A$.
