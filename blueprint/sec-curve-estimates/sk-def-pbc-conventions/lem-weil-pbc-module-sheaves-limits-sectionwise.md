+++
id = "lem-weil-pbc-module-sheaves-limits-sectionwise"
kind = "lemma"
title = "Limits of sheaves of modules exist and are computed sectionwise"
order = 1374
uses = ["def-weil-sheaf-of-modules-category"]
lean = ["SheafOfModules.hasLimitsOfSize", "SheafOfModules.evaluationPreservesLimitsOfSize"]
tags = ["mathlib", "stacks-03DB"]
+++
Let $\mathcal C$ be a site, $\mathcal O$ a sheaf of rings on $\mathcal C$, $\Mod(\mathcal O)$ the category of sheaves of $\mathcal O$-modules [def-weil-sheaf-of-modules-category], $\mathcal I$ a small category and $i\mapsto\mathcal F_i$ a diagram $\mathcal I\to\Mod(\mathcal O)$. Let $\mathcal L$ be the presheaf $V\mapsto\lim_i\mathcal F_i(V)$, the limit of the $\mathcal O(V)$-modules $\mathcal F_i(V)$, i.e. the set of families $(x_i)_i\in\prod_i\mathcal F_i(V)$ with $\mathcal F(a)(x_i)=x_j$ for every arrow $a:i\to j$, with componentwise addition, $\mathcal O(V)$-action and restriction maps; its underlying abelian group is the limit of the abelian groups $\mathcal F_i(V)$. Then $\mathcal L$ is a sheaf of $\mathcal O$-modules, and $\mathcal L$ with the coordinate projections $\mathcal L\to\mathcal F_i$ is a limit of the diagram in $\Mod(\mathcal O)$, and also in the category of presheaves of $\mathcal O$-modules; in particular every small diagram in $\Mod(\mathcal O)$ has a limit, and evaluation at each object $V$ carries it to the limit of the $\mathcal O(V)$-modules $\mathcal F_i(V)$.
