+++
id = "lem-sp-finite-filtration-induction"
kind = "lemma"
title = "Finite filtration induction"
order = 1973
lean = ["CategoryTheory.PBCFilteredObject.finite_filtration_induction", "CategoryTheory.FilteredObject.finite_filtration_induction"]
uses = ["def-sp-filtration"]
+++
Let $(A,F)$ and $(A',F')$ be filtered objects [def-sp-filtration] with finite
filtrations, and let $\varphi:A\to A'$ be a morphism of filtered objects. If
$\operatorname{gr}^p\varphi$ is an isomorphism for all $p$, then $\varphi$ is
an isomorphism, and for every $p$ the restriction
$F^pA\to F^pA'$ of $\varphi$ is an isomorphism.
