+++
id = "lemma-weil-pbc-direct-image-filtered-colimit"
kind = "lemma"
title = "Filtered colimits and higher direct image"
order = 1545
lean = ["AlgebraicGeometry.Etale.preservesColimitsOfShape_higherDirectImage"]
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-cohomology-filtered-colimit", "lem-weil-pbc-qcqs-higher-direct-image"]
+++
Let $\Lambda$ be a commutative ring. If $u:U\to V$ is quasi-compact and
quasi-separated [def-weil-pbc-scheme-conventions] and $(F_i)$ is a filtered
system of etale sheaves of $\Lambda$-modules on $U$ [def-weil-pbc-etale-sheaves]
(for instance torsion sheaves), then for every $q\geq0$ the canonical map

$$
 \varinjlim_iR^qu_*F_i\xrightarrow{\sim}R^qu_*(\varinjlim_iF_i)
$$

involving the higher direct image [def-weil-pbc-direct-image] is an
isomorphism; that is, $R^qu_*$ commutes with filtered colimits. The same
assertion holds after arbitrary base change of $u$.
