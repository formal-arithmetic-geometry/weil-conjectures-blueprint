+++
id = "lem-weil-pbc-presheaf-modules-colimits-sectionwise"
kind = "lemma"
title = "Colimits of presheaves of modules are computed sectionwise"
order = 1060
uses = ["def-weil-presheaf-modules-sheafification"]
lean = ["PresheafOfModules.toPresheaf_preservesColimitsOfSize"]
tags = ["mathlib", "stacks-03DB"]
+++
Let $\mathcal C$ be a category, $\mathcal O$ a presheaf of rings on $\mathcal C$, $\mathrm{PMod}(\mathcal O)$ the category of presheaves of $\mathcal O$-modules [def-weil-presheaf-modules-sheafification] and $\mathrm{PAb}(\mathcal C)$ the category of presheaves of abelian groups. Let $\mathcal I$ be a small category and $i\mapsto\mathcal P_i$ a diagram $\mathcal I\to\mathrm{PMod}(\mathcal O)$. For each object $V$ let $\mathcal P(V)=\colim_i\mathcal P_i(V)$ be the colimit of the $\mathcal O(V)$-modules $\mathcal P_i(V)$, whose underlying abelian group is the colimit of the abelian groups $\mathcal P_i(V)$; for $V'\to V$ the restriction maps of the $\mathcal P_i$ induce a map $\mathcal P(V)\to\mathcal P(V')$, semilinear over $\mathcal O(V)\to\mathcal O(V')$. Then $\mathcal P$ is a presheaf of $\mathcal O$-modules, and $\mathcal P$ with the maps $\mathcal P_i\to\mathcal P$ induced by the coprojections is a colimit of the diagram in $\mathrm{PMod}(\mathcal O)$; in particular $\mathrm{PMod}(\mathcal O)$ has all small colimits and evaluation at each $V$ preserves them. Moreover the functor $\mathrm{PMod}(\mathcal O)\to\mathrm{PAb}(\mathcal C)$ forgetting the module structures preserves small colimits: the underlying presheaf of abelian groups of $\mathcal P$, with the same maps, is the colimit of the underlying presheaves of abelian groups of the $\mathcal P_i$ in $\mathrm{PAb}(\mathcal C)$, which is computed sectionwise.
