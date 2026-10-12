+++
id = "lem-weil-pbc-derived-plus-iso-on-cohomology"
kind = "lemma"
title = "A morphism of the bounded below derived category is an isomorphism iff it is so on cohomology"
uses = ["def-weil-pbc-derived-categories"]
lean = ["DerivedCategory.Plus.isIso_iff"]
tags = ["sheaf-dag", "mathlib"]
+++
Let $\mathcal A$ be an abelian category and $\Dplus(\mathcal A)$ its bounded below derived category [def-weil-pbc-derived-categories]. A morphism $\varphi:K\to L$ of $\Dplus(\mathcal A)$ is an isomorphism if and only if the induced morphism $\mathcal H^n(\varphi):\mathcal H^n(K)\to\mathcal H^n(L)$ of cohomology objects is an isomorphism for every integer $n$.
