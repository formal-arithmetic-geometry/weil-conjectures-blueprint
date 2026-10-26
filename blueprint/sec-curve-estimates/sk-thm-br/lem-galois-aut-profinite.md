+++
id = "lem-galois-aut-profinite"
kind = "lemma"
title = "$\\operatorname{Aut}(F)$ is profinite"
lean = ["CategoryTheory.PreGaloisCategory.autEmbedding", "CategoryTheory.PreGaloisCategory.autEmbedding_range", "CategoryTheory.PreGaloisCategory.autEmbedding_range_isClosed", "CategoryTheory.PreGaloisCategory.autEmbedding_isClosedEmbedding"]
order = 1378
uses = ["def-galois-category", "def-galois-fibre-functor"]
+++
Let $\mathcal C$ be a category and $F:\mathcal C\to(\text{finite sets})$
a functor. Then the evaluation embedding identifies
$\operatorname{Aut}(F)$ with the closed subgroup of
$\prod_X\operatorname{Aut}(F(X))$ formed by the families compatible with
all $F(f)$, and this embedding is a closed embedding for the topology of
[def-galois-category]. Consequently $\operatorname{Aut}(F)$ is a
compact, Hausdorff, totally disconnected topological group, i.e.
profinite.
