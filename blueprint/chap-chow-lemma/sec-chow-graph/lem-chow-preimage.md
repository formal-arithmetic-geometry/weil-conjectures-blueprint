+++
id = "lem-chow-preimage"
kind = "lemma"
title = "The preimages of the members of the cover"
order = 626
lean = ["AlgebraicGeometry.ChowGraph.isProper_morphismRestrict_modificationMap", "AlgebraicGeometry.ChowGraph.preimage_modificationMap"]
uses = ["lem-chow-glue"]
+++
In the situation of [lem-chow-glue] one has $\pi^{-1}(U_i)=V_i$ for every
$i$. Consequently $\pi^{-1}(U_i)\to U_i$ is the proper morphism
$p_i|_{V_i}$.

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
