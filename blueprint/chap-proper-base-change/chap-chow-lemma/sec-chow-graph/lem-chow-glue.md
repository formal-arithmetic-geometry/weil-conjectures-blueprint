+++
id = "lem-chow-glue"
kind = "lemma"
title = "Gluing the projections"
order = 626
lean = ["AlgebraicGeometry.ChowGraph.modificationMap", "AlgebraicGeometry.ChowGraph.projPreimage", "AlgebraicGeometry.ChowGraph.projRestrict"]
uses = ["lem-chow-agree-on-dense-open", "lem-chow-graph"]
+++
In the situation of [lem-chow-graph] put $V_i:=p_i^{-1}(U_i)$ and
$X':=V_1\cup\dots\cup V_m$, an open subscheme of $Z$. Then the morphisms
$p_i|_{V_i}\colon V_i\to U_i\subseteq X$ glue to a morphism of $S$-schemes

$$
\pi\colon X'\longrightarrow X
$$

with $\pi|_{V_i}=p_i|_{V_i}$, and $\pi|_U=\mathrm{id}_U$.

In the formalisation $V_i$ is the preimage under $p_i$ of the image of $U_i$ in
$Z_i$, and $V_i$, $U$ and $X'$ are all opens of $Z$; the last assertion reads
that the composition of the open immersion $U\to X'$ with $\pi$ is the inclusion
$U\to X$.

## Proof

By [lem-chow-graph](3) we have $U\subseteq V_i$ for every $i$, and
$p_i|_U\colon U\to U_i\subseteq X$ is the inclusion. Since $U$ is
scheme-theoretically dense in $Z$ and $V_i\cap V_j\subseteq Z$ is open, $U$ is
scheme-theoretically dense in $V_i\cap V_j$. The two morphisms
$p_i|_{V_i\cap V_j}$ and $p_j|_{V_i\cap V_j}$ into $X$ agree on $U$, and
$X\to S$ is separated, so they are equal by
[lem-chow-agree-on-dense-open]. Hence the $p_i|_{V_i}$ glue to
$\pi\colon X'\to X$, and $\pi|_U=\mathrm{id}_U$.
