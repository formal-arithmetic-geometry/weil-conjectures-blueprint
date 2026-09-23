+++
id = "lem-weil-pbc-chow-fibres-proper-over-cover"
kind = "lemma"
title = "The fibres of the glued morphism"
order = 1485
uses = ["def-weil-pbc-scheme-conventions", "lem-weil-pbc-chow-product-image-model", "lem-weil-pbc-chow-projection-gluing"]
+++
In the situation of [lem-weil-pbc-chow-projection-gluing],

$$
 \pi^{-1}(U_i)=V_i
$$

for every $i$; consequently the restriction $\pi^{-1}(U_i)\to U_i$ is the
morphism $p_i|_{V_i}$, which is proper by
[lem-weil-pbc-chow-product-image-model] (ii) and the stability of properness
under base change.

## Proof

The inclusion $V_i\subseteq\pi^{-1}(U_i)$ holds because $\pi|_{V_i}=p_i|_{V_i}$
maps $V_i$ into $U_i$ ([lem-weil-pbc-chow-projection-gluing]).

*Step 1: $\pi$ is separated.* Each $p_i|_{V_i}:V_i\to U_i$ is proper by
[lem-weil-pbc-chow-product-image-model] (ii) (its properness is stable under
the base change along the open immersion $U_i\to Z_i$, Stacks Project,
Morphisms, Lemma 29.42.5, Tag
[01W4](https://stacks.math.columbia.edu/tag/01W4)), hence separated; since
separatedness is local on the source and the $V_i$ cover $X'$, the morphism
$\pi$ is separated. Hence its base change
$\pi^{-1}(U_i)=X'\times_XU_i\to U_i$ along the open immersion $U_i\to X$ is
separated.

*Step 2: $V_i$ is closed in $\pi^{-1}(U_i)$.* Apply Stacks Project,
Morphisms, Lemma 29.42.7 (Tag
[01W6](https://stacks.math.columbia.edu/tag/01W6)) to the diagram whose
composite $V_i\to\pi^{-1}(U_i)\to U_i$ is the proper morphism $p_i|_{V_i}$ and
whose second member $\pi^{-1}(U_i)\to U_i$ is separated: the lemma says that
the morphism $V_i\to\pi^{-1}(U_i)$ is proper, hence closed, so its image
(which is $V_i$ itself) is closed in $\pi^{-1}(U_i)$.

*Step 3: $V_i$ is dense in $\pi^{-1}(U_i)$.* By
[lem-weil-pbc-chow-product-image-model] (i), $U$ is scheme-theoretically dense
in $\widetilde X$; since $U\subseteq V_i$ and
$\pi^{-1}(U_i)\subseteq\widetilde X$ is open, the closure of $V_i$ in
$\pi^{-1}(U_i)$ is all of $\pi^{-1}(U_i)$. Steps 2 and 3 give
$V_i=\pi^{-1}(U_i)$.
