+++
id = "dag-def-pur-abelian-sheaf-kernel"
kind = "dag-definition"
title = "Kernel of a morphism of sheaves of abelian groups on a site"
name_showing = false
order = 184502
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "def-pur-abelian-sheaf-kernel"
dag_kind = "definition"
dag_status = "mathlib"
serial = false
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

(SHEAF DAG node `def-pur-abelian-sheaf-kernel`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: definition. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: mathlib.
