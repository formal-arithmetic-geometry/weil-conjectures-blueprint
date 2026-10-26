+++
id = "def-weil-presheaf-modules-sheafification"
kind = "definition"
title = "Sheafification of a presheaf of modules over a sheaf of rings"
order = 1255
uses = ["def-weil-pbc-sheafification", "def-weil-sheaf-of-modules-category"]
lean = ["PresheafOfModules.sheafification", "PresheafOfModules.sheafificationAdjunction"]
tags = ["mathlib", "stacks-03CX"]
+++
Let $\mathcal C$ be a site and $\mathcal O$ a sheaf of rings on $\mathcal C$. A *presheaf of $\mathcal O$-modules* is a presheaf of abelian groups $\mathcal P$ on $\mathcal C$ with an $\mathcal O(V)$-module structure on each $\mathcal P(V)$ such that every restriction map $\mathcal P(V)\to\mathcal P(V')$ along $V'\to V$ is semilinear over $\mathcal O(V)\to\mathcal O(V')$; morphisms are the morphisms of presheaves of abelian groups that are $\mathcal O(V)$-linear on every $V$. Let $\mathcal P^\#$ be the sheafification of $\mathcal P$ as a presheaf of abelian groups [def-weil-pbc-sheafification]. There is a unique map of sheaves of sets $\mathcal O\times\mathcal P^\#\to\mathcal P^\#$ extending the module structure $\mathcal O\times\mathcal P\to\mathcal P$ along $\mathcal P\to\mathcal P^\#$, and it makes $\mathcal P^\#$ a sheaf of $\mathcal O$-modules [def-weil-sheaf-of-modules-category], the *sheafification* of $\mathcal P$. The map $\mathcal P\to\mathcal P^\#$ is $\mathcal O$-linear, and every $\mathcal O$-linear map from $\mathcal P$ to a sheaf of $\mathcal O$-modules factors uniquely through it; so $\mathcal P\mapsto\mathcal P^\#$ is a functor from presheaves of $\mathcal O$-modules to sheaves of $\mathcal O$-modules, left adjoint to the inclusion.
