+++
id = "dag-def-pur-sheaf-modules-hom-module"
kind = "dag-definition"
title = "Hom of sheaves of modules as a module over global sections"
name_showing = false
order = 184510
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "def-pur-sheaf-modules-hom-module"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.homModule", "SheafOfModules.homLinear"]
+++
Let $\mathcal C$ be a site, $\mathcal O$ a sheaf of commutative rings on $\mathcal C$ and $\Gamma(\mathcal C,\mathcal O)$ its ring of global sections (the families $(s_V)_{V\in\mathcal C}$, $s_V\in\mathcal O(V)$, compatible with all restriction maps; when $\mathcal C$ has a final object $T$ it is $\mathcal O(T)$). For sheaves of $\mathcal O$-modules $\mathcal F,\mathcal G$ the abelian group $\operatorname{Hom}_{\mathcal O}(\mathcal F,\mathcal G)$ of morphisms of sheaves of $\mathcal O$-modules is a $\Gamma(\mathcal C,\mathcal O)$-module by $(s\varphi)_V(x)=s_V\,\varphi_V(x)$ for $x\in\mathcal F(V)$; equivalently $s\varphi=\varphi\circ(s\cdot)=(s\cdot)\circ\varphi$, where $s\cdot$ is multiplication by $s$ on $\mathcal F$, resp. $\mathcal G$ (these agree, and $s\varphi$ is again $\mathcal O$-linear, because $\mathcal O$ is commutative). Composition of morphisms is $\Gamma(\mathcal C,\mathcal O)$-bilinear.

(SHEAF DAG node `def-pur-sheaf-modules-hom-module`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: definition. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`.
