+++
id = "lem-weil-pbc-colimit-constant-connected-diagram"
kind = "lemma"
title = "The colimit of a constant diagram over a connected (e.g. nonempty filtered) category"
uses = ["def-weil-pbc-category-colimit"]
lean = ["CategoryTheory.Limits.isColimitConstCocone"]
tags = ["sheaf-dag", "mathlib", "stacks-040R"]
+++
Let $I$ be a small category that is connected: nonempty, and any two objects are joined by a finite zigzag of morphisms. Every nonempty filtered category is connected (two objects map to a common object), in particular the opposite $\mathcal N^{\mathrm{op}}$ of a cofiltered category $\mathcal N$. Let $E$ be an object of a category $\mathcal C$ (e.g. an abelian group) and $D:I\to\mathcal C$ the constant diagram with value $E$, all of whose transition maps are $\mathrm{id}_E$. Then the cocone $(E,(\mathrm{id}_E)_{i\in I})$ is a colimit of $D$ [def-weil-pbc-category-colimit]: for every cocone $(M,(\mu_i)_i)$ all $\mu_i$ are equal to one morphism $\mu:E\to M$, and $\mu$ is the unique morphism $u$ with $u\circ\mathrm{id}_E=\mu_i$ for all $i$. Consequently, for any chosen colimit $(\varinjlim_ID,(c_i)_i)$, every coprojection $c_i:E\to\varinjlim_ID$ is an isomorphism, and $c_i=c_j$ for all $i,j$.
