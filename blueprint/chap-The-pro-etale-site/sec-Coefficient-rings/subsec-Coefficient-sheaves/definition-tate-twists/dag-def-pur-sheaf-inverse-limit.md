+++
id = "dag-def-pur-sheaf-inverse-limit"
kind = "dag-definition"
title = "Inverse limit of a sequence of sheaves of modules on a site"
name_showing = false
order = 184509
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "def-pur-sheaf-inverse-limit"
dag_kind = "definition"
dag_status = "mathlib"
serial = false
+++
Let $\mathcal C$ be a site, $\mathcal O$ a sheaf of rings on $\mathcal C$, and
$(\mathcal F_r,t_r)_{r\geq1}$ an inverse system of sheaves of $\mathcal O$-modules,
with transition maps $t_r:\mathcal F_{r+1}\to\mathcal F_r$. Its *inverse limit*
$\varprojlim_r\mathcal F_r$ is the limit of this diagram in the category of
sheaves of $\mathcal O$-modules. It exists, and it is computed sectionwise: for
every object $U$ of $\mathcal C$,

$$
 \Bigl(\varprojlim_r\mathcal F_r\Bigr)(U)
 =\varprojlim_r\mathcal F_r(U)
 =\Bigl\{(x_r)_{r\geq1}\in\prod_{r\geq1}\mathcal F_r(U):
   t_r(x_{r+1})=x_r\text{ for all }r\Bigr\},
$$

with the restriction maps and the $\mathcal O(U)$-module structure taken
componentwise; the presheaf so defined is a sheaf, and the projections
$\varprojlim_r\mathcal F_r\to\mathcal F_r$ are the coordinate maps. The same
applies to sheaves of abelian groups ($\mathcal O=\mathbf Z$) and of rings.

(SHEAF DAG node `def-pur-sheaf-inverse-limit`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: definition. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: mathlib. Lean names not on master: `CategoryTheory.Limits.limit`, `CategoryTheory.Limits.limit.π`.
