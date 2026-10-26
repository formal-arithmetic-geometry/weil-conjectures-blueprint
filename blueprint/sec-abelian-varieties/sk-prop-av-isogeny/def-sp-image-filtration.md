+++
id = "def-sp-image-filtration"
kind = "definition"
title = "Image filtrations"
lean = ["CategoryTheory.DecreasingFiltration.image"]
order = 493
uses = ["def-sp-abelian", "def-sp-filtration"]
+++
Let $(A,F)$ be a filtered object [def-sp-filtration] and let $A\to B$ be a
morphism in the abelian category [def-sp-abelian] $\mathcal A$. The *image
filtration* on $B$ is the filtration

$$
 F^nB:=\operatorname{im}\bigl(F^nA\to B\bigr).
$$
