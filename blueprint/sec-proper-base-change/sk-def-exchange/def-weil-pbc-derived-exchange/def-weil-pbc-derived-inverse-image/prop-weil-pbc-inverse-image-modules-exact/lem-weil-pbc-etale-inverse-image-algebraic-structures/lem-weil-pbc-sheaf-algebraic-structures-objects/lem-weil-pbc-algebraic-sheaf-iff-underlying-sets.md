+++
id = "lem-weil-pbc-algebraic-sheaf-iff-underlying-sets"
kind = "lemma"
title = "A presheaf of abelian groups or commutative rings is a sheaf iff its underlying presheaf of sets is"
refines = "proof/lem-weil-pbc-sheaf-algebraic-structures-objects"
lean = ["CategoryTheory.Presheaf.isSheaf_iff_isSheaf_forget"]
tags = ["sheaf-dag", "mathlib", "stacks-00YR"]
+++
Let $\mathcal C$ be a site (Stacks Sites, Definition 00VH) and let $\mathcal A$ be the category of abelian groups or the category of commutative rings, with forgetful functor $s:\mathcal A\to\textit{Sets}$. Let $\mathcal F$ be a presheaf on $\mathcal C$ with values in $\mathcal A$, i.e. a functor $\mathcal C^{op}\to\mathcal A$, and $s\circ\mathcal F$ its underlying presheaf of sets. Then $\mathcal F$ is a sheaf with values in $\mathcal A$ (for every covering $\{U_i\to U\}_{i\in I}$ the diagram $\mathcal F(U)\to\prod_i\mathcal F(U_i)\rightrightarrows\prod_{i,j}\mathcal F(U_i\times_UU_j)$ is an equalizer diagram in $\mathcal A$, Sites Definition 00VR and the discussion before it) if and only if $s\circ\mathcal F$ is a sheaf of sets (the same diagram of underlying sets is an equalizer diagram of sets).
