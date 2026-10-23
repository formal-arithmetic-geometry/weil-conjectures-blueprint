+++
id = "def-weil-pbc-constant-sheaf"
kind = "definition"
title = "Constant sheaf on a site"
uses = ["def-weil-pbc-sheafification"]
lean = ["CategoryTheory.constantSheaf"]
order = 795
tags = ["mathlib", "stacks-0H7J"]
+++
Let $\mathcal C$ be a site and $\mathcal A$ a category of values in which sheafification exists (sets, abelian groups, rings). For an object $E$ of $\mathcal A$ the *constant sheaf* $\underline E$ on $\mathcal C$ is the sheafification [def-weil-pbc-sheafification] of the constant presheaf $U\mapsto E$, all of whose restriction maps are the identity of $E$. For a commutative ring $A$ the constant sheaf of rings $\underline A$ is a sheaf of commutative rings; on $Y_{\mathrm{proet}}$ it is written $A_Y$.
