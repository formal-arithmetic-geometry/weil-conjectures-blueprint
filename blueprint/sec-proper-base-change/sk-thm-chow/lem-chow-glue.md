+++
id = "lem-chow-glue"
kind = "lemma"
title = "Gluing the projections"
order = 1058
lean = ["AlgebraicGeometry.ChowGraph.modificationMap", "AlgebraicGeometry.ChowGraph.projPreimage", "AlgebraicGeometry.ChowGraph.projRestrict"]
uses = ["def-weil-pbc-scheme-conventions", "lem-chow-closed-model", "lem-chow-graph"]
+++
In the situation of [lem-chow-graph], assume that the underlying space of $X$
is noetherian, that $m\geq1$, and that $f\colon X\to S$ is separated. Put
$V_i:=p_i^{-1}(U_i)$, the preimage under $p_i$ of the image of $U_i$ in $Z_i$,
and $X':=V_1\cup\dots\cup V_m$, an open subscheme of $Z$. Then the morphisms
$p_i|_{V_i}\colon V_i\to U_i\subseteq X$ glue to a morphism of $S$-schemes

$$
\pi\colon X'\longrightarrow X
$$

with $\pi|_{V_i}=p_i|_{V_i}$, and $\pi|_U$ is the inclusion $U\subseteq X$.
