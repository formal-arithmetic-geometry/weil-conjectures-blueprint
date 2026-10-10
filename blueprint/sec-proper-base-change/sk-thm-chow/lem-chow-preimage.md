+++
id = "lem-chow-preimage"
kind = "lemma"
title = "The preimages of the members of the cover"
order = 1059
lean = ["AlgebraicGeometry.ChowGraph.isProper_morphismRestrict_modificationMap", "AlgebraicGeometry.ChowGraph.preimage_modificationMap"]
uses = ["def-weil-pbc-scheme-conventions", "lem-chow-closed-model", "lem-chow-glue", "lem-chow-graph"]
+++
In the situation of [lem-chow-glue] (so the underlying space of $X$ is
noetherian, $m\geq1$ and $f$ is separated) one has $\pi^{-1}(U_i)=V_i$ for
every $i$. Consequently $\pi^{-1}(U_i)\to U_i$ is the proper morphism
$p_i|_{V_i}$; in particular the restriction $\pi^{-1}(U_i)\to U_i$ of $\pi$ is
proper.
