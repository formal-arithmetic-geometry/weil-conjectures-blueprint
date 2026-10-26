+++
id = "def-pur-abelian-sheaf-kernel"
kind = "definition"
title = "Kernel of a morphism of sheaves of abelian groups on a site"
order = 1249
lean = ["CategoryTheory.sheafIsAbelian", "CategoryTheory.Limits.kernel", "CategoryTheory.Sheaf.createsLimits"]
tags = ["mathlib", "stacks-03CO"]
+++
Let $\mathcal C$ be a site and $\varphi:\mathcal F\to\mathcal G$ a morphism of sheaves
of abelian groups on $\mathcal C$. Its *kernel* $\ker\varphi$ is the kernel of $\varphi$
in the abelian category $\mathrm{Ab}(\mathcal C)$ of sheaves of abelian groups. It
exists and is computed sectionwise: it is the subsheaf

$$
 (\ker\varphi)(U)=\ker\bigl(\varphi_U:\mathcal F(U)\to\mathcal G(U)\bigr)
 =\{x\in\mathcal F(U):\varphi_U(x)=0\}
$$

of $\mathcal F$, with the restriction maps of $\mathcal F$, and the inclusion
$\ker\varphi\to\mathcal F$ is the canonical morphism. (The presheaf so defined is a
sheaf because a kernel is a limit and limits of sheaves are the limits of the
underlying presheaves.)
