+++
id = "def-weil-pbc-sheafification"
kind = "definition"
title = "Sheafification on a site"
lean = ["CategoryTheory.presheafToSheaf"]
tags = ["mathlib", "stacks-00W1"]
+++
Let $\mathcal C$ be a site and let $\mathcal A$ be one of the categories of sets, abelian groups, rings or modules over a fixed ring (more generally a category of values in which sheafification exists). For a presheaf $\mathcal F:\mathcal C^{\mathrm{op}}\to\mathcal A$, its *sheafification* is a sheaf $\mathcal F^\#$ on $\mathcal C$ with values in $\mathcal A$ together with a morphism of presheaves $\mathcal F\to\mathcal F^\#$ through which every morphism from $\mathcal F$ to a sheaf factors uniquely; equivalently, $\mathcal F\mapsto\mathcal F^\#$ is a left adjoint to the inclusion of sheaves into presheaves.
