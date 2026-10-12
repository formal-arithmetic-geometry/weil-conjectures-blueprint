+++
id = "def-weil-sheaf-of-modules-category"
kind = "definition"
title = "Category of sheaves of modules over a sheaf of rings"
lean = ["SheafOfModules"]
tags = ["mathlib", "stacks-03CV"]
+++
Let $\mathcal C$ be a site and $\mathcal O$ a sheaf of rings on $\mathcal C$. A *sheaf of $\mathcal O$-modules* is a sheaf of abelian groups $\mathcal F$ on $\mathcal C$ together with, for every object $U$, an $\mathcal O(U)$-module structure on $\mathcal F(U)$ (extending its abelian group structure) such that every restriction map $\mathcal F(U)\to\mathcal F(V)$ along $V\to U$ is semilinear over the restriction $\mathcal O(U)\to\mathcal O(V)$: $(a x)|_V=a|_V\,x|_V$. A morphism of sheaves of $\mathcal O$-modules $\mathcal F\to\mathcal G$ is a morphism of sheaves of abelian groups whose component at every $U$ is $\mathcal O(U)$-linear. These form a category $\Mod(\mathcal O)$, which is abelian when the site is small relative to the universe of the modules (or essentially so): kernels are computed sectionwise, and cokernels are the sheafifications of the sectionwise cokernels.
