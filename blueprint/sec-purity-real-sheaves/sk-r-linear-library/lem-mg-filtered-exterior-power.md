+++
id = "lem-mg-filtered-exterior-power"
kind = "lemma"
title = "Exterior power of a filtered representation"
lean = ["Subrepresentation.exteriorPowerGradedEquiv", "Representation.ConstituentsLE.exteriorPower_of_tprod", "Representation.ConstituentsLE.exteriorPower_of_chain", "Representation.CompositionSeries.constituentsLE_exteriorPower_semisimplification", "Representation.CompositionSeries.constituentsLE_exteriorPower_semisimplification'", "Representation.hasGradedPieces_exteriorPower_of_monotone", "Representation.CompositionSeries.hasGradedPieces_exteriorPower"]
order = 4047
uses = ["def-mg-weil-composition-series"]
+++
Let $0=V_0\subsetneq\cdots\subsetneq V_t=V$ be a
composition series,
put $A_i=V_i/V_{i-1}$ and $d_i=\dim A_i$, and fix
$0\le r\le\dim V$. The Weil representation $\bigwedge^rV$ has a
finite filtration whose nonzero successive quotients are

$$
\bigotimes_{i=1}^{t}\bigwedge\nolimits^{n_i}A_i,
\qquad
0\le n_i\le d_i,
\qquad
\sum_i n_i=r.
$$

Every admissible tuple $(n_1,\ldots,n_t)$ occurs once.
