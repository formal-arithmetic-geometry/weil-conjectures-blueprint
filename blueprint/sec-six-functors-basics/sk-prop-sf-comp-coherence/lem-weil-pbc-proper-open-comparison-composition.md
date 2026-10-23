+++
id = "lem-weil-pbc-proper-open-comparison-composition"
kind = "lemma"
title = "Composition of proper-open comparison maps"
order = 2281
lean = ["AlgebraicGeometry.ProperOpenDatum.comparison_comp", "AlgebraicGeometry.ProperOpenDatum.comparison_id"]
uses = ["def-weil-pbc-extension-by-zero", "def-weil-pbc-proper-open-comparison", "lem-weil-pbc-derived-open-restriction", "lem-weil-pbc-proper-open-identification", "lem-weil-pbc-proper-open-section"]
+++
Let $u:T_1\to T_2$ and $v:T_2\to T_3$ be proper maps with
open immersions $j_i:X\hookrightarrow T_i$ satisfying
$u j_1=j_2$ and $v j_2=j_3$. For $K\in D^+(X_{\Et},\Lambda)$
with $\Lambda$ a commutative ring, the maps of
the comparison-map
construction satisfy

$$
\alpha_{vu,K}
= (Rv_*\alpha_{u,K})\circ\alpha_{v,K},
$$

under the canonical identification $R(vu)_*=Rv_*Ru_*$.
For the identity map the comparison is the identity.
