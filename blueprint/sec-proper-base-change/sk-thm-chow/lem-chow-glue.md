+++
id = "lem-chow-glue"
kind = "lemma"
title = "Gluing the projections"
order = 1058
lean = ["AlgebraicGeometry.ChowGraph.modificationMap", "AlgebraicGeometry.ChowGraph.projPreimage", "AlgebraicGeometry.ChowGraph.projRestrict"]
uses = ["def-nagata-affine-proj", "def-nagata-dense-compactification", "def-nagata-projective-space-base-change", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-weil-pbc-scheme-conventions", "lem-chow-agree-on-dense-open", "lem-chow-closed-model", "lem-chow-graph", "lem-chow-tuple-immersion", "lemma-nagata-dense-flat-pullback", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-scheme-image-ideal-qc"]
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
