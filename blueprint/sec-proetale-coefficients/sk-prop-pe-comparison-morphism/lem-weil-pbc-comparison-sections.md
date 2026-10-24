+++
id = "lem-weil-pbc-comparison-sections"
kind = "lemma"
title = "Sections of the comparison inverse image"
order = 993
lean = ["AlgebraicGeometry.ProEtale.isColimit_comparisonUpperStar_mapCocone"]
uses = ["def-weil-pbc-ind-etale-basis", "def-weil-pbc-site-comparison-morphism", "lem-weil-pbc-etale-finite-data-descent", "lem-weil-pbc-ind-etale-basis", "lem-weil-pbc-ind-etale-stability"]
+++
Let $S$ be a scheme, $\Lambda$ a ring, and $F$ a sheaf of $\Lambda$-modules on
$S_{\Et}$. Let $(U_i)_{i\in I}$ be a cofiltered diagram of quasi-compact
quasi-separated etale $S$-schemes with affine transition maps, and let $U$ be
an object of $S_{\Proet}$ with compatible maps $U\to U_i$ exhibiting
$U=\varprojlim_iU_i$ as a limit of schemes. Then the restriction maps of
$\nu_S^*F$ along $U\to U_i$ induce an isomorphism

$$
 \varinjlim_i F(U_i)\xrightarrow{\ \sim\ }(\nu_S^*F)(U).
$$
