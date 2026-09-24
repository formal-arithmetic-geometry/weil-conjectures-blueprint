+++
id = "lem-weil-pbc-chow-projection-gluing"
kind = "lemma"
title = "Gluing the projections along the cover"
order = 1591
uses = ["def-weil-pbc-scheme-conventions", "lem-weil-pbc-chow-product-image-model", "lem-weil-pbc-chow-separated-density-equality"]
+++
In the situation of [lem-weil-pbc-chow-product-image-model], put

$$
 V_i:=p_i^{-1}(U_i)\subseteq\widetilde X
$$

and $X':=V_1\cup\dots\cup V_m$. Then for all $i,j$, $U\subseteq V_i\cap V_j$
is scheme-theoretically dense, and the morphisms $p_i|_{V_i}:V_i\to U_i$ glue
to a morphism

$$
 \pi:X'\longrightarrow X
$$

over $Y$. (Here $X$ is identified with the separated scheme in which the
affine opens $U_i\subseteq X$ sit; $X$ is separated over $Y$ since $X\to Y$ is
proper.) One has $\pi|_U=\operatorname{id}_U$.

## Proof

Since $U\subseteq\widetilde X$ is scheme-theoretically dense by
[lem-weil-pbc-chow-product-image-model] (i), and $V_i\cap V_j$ is an open
subscheme of $\widetilde X$, the open $U\subseteq V_i\cap V_j$ is
scheme-theoretically dense in $V_i\cap V_j$ (restriction of density to opens).
The two morphisms $p_i|_{V_i\cap V_j}$ and $p_j|_{V_i\cap V_j}$ take values in
$U_i\cap U_j\subseteq X$ and agree on $U$; by
[lem-weil-pbc-chow-separated-density-equality] (whose hypotheses hold: $X$ is
separated over $Y$ because it is proper over $Y$), they agree. Hence the
morphisms $p_i|_{V_i}$ are compatible on overlaps and glue to a morphism
$\pi:X'\to X$ (gluing of schemes coincides with gluing of morphisms), and to
see $\pi|_U=\operatorname{id}_U$: each $p_i|_{V_i}$ restricts on $U\subseteq
V_i$ to the identity on $U$ (the open immersion $U\hookrightarrow U_i$ and the
composite $U\hookrightarrow\widetilde X\hookrightarrow Z_i$ are the same
morphism by construction of the diagonal morphism $j$ in
[lem-weil-pbc-chow-product-image-model]).
