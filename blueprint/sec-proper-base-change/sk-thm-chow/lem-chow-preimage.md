+++
id = "lem-chow-preimage"
kind = "lemma"
title = "The preimages of the members of the cover"
order = 1059
lean = ["AlgebraicGeometry.ChowGraph.isProper_morphismRestrict_modificationMap", "AlgebraicGeometry.ChowGraph.preimage_modificationMap"]
uses = ["def-nagata-affine-proj", "def-nagata-dense-compactification", "def-nagata-projective-space-base-change", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-weil-pbc-scheme-conventions", "lem-chow-agree-on-dense-open", "lem-chow-closed-model", "lem-chow-glue", "lem-chow-graph", "lem-chow-tuple-immersion", "lemma-nagata-dense-flat-pullback", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-projective-space-base-change-proper", "lemma-nagata-proper-to-separated-target", "lemma-nagata-scheme-image-ideal-qc"]
+++
In the situation of [lem-chow-glue] (so the underlying space of $X$ is
noetherian, $m\geq1$ and $f$ is separated) one has $\pi^{-1}(U_i)=V_i$ for
every $i$. Consequently $\pi^{-1}(U_i)\to U_i$ is the proper morphism
$p_i|_{V_i}$; in particular the restriction $\pi^{-1}(U_i)\to U_i$ of $\pi$ is
proper.

## Proof

The inclusion $V_i\subseteq\pi^{-1}(U_i)$ holds because $\pi|_{V_i}=p_i|_{V_i}$
takes values in $U_i$. The morphism $p_i|_{V_i}\colon V_i\to U_i$ is proper,
being the base change of the proper morphism $p_i$ along the open immersion
$U_i\to Z_i$. The open subscheme $\pi^{-1}(U_i)\subseteq Z$ is separated over
$S$, hence $\pi^{-1}(U_i)\to U_i$ is separated. Applying 01W6
to the commutative triangle formed by $V_i\to\pi^{-1}(U_i)$ and the two
morphisms to $U_i$, we conclude that $V_i\to\pi^{-1}(U_i)$ is universally
closed; in particular $V_i$ is closed in $\pi^{-1}(U_i)$. On the other hand
$U\subseteq V_i$ and $U$ is dense in the open subscheme
$\pi^{-1}(U_i)\subseteq Z$, so $V_i$ is dense in $\pi^{-1}(U_i)$. Being closed
and dense, $V_i=\pi^{-1}(U_i)$.
