+++
id = "dag-def-pur-sheaf-hom"
kind = "dag-definition"
title = "Sheaf Hom of sheaves of modules on a site"
name_showing = false
order = 184508
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "def-pur-sheaf-hom"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.homObj"]
uses = ["dag-def-pur-localized-ringed-site"]
+++
Let $\mathcal C$ be a site, $\mathcal O$ a sheaf of commutative rings on $\mathcal C$, and
$\mathcal F,\mathcal G$ sheaves of $\mathcal O$-modules. For an object $U$ of
$\mathcal C$ write $\mathcal F|_U$ for the restriction of $\mathcal F$ to the
localized site $\mathcal C/U$. The *sheaf Hom*
$\mathcal{H}om_{\mathcal O}(\mathcal F,\mathcal G)$ is the presheaf

$$
 U\longmapsto\operatorname{Hom}_{\mathcal O|_U}
 (\mathcal F|_U,\mathcal G|_U),
$$

the set of $\mathcal O|_U$-linear maps of sheaves on $\mathcal C/U$, with the
restriction map along $V\to U$ given by restricting a map on $\mathcal C/U$ to
$\mathcal C/V$, and with $f\in\mathcal O(U)$ acting on $\varphi$ by composing
$\varphi$ with multiplication by $f$. This presheaf is a sheaf of
$\mathcal O$-modules, and its global sections are
$\operatorname{Hom}_{\mathcal O}(\mathcal F,\mathcal G)$ (the statement
that it is a sheaf of $\mathcal O$-modules is a theorem of its own, from which
this definition takes its sheaf structure). In the twist
notation of the blueprint, $\operatorname{Hom}_{\Lambda_S}(\Lambda(-m),\Lambda_S)$
for a sheaf $\Lambda(-m)$ of $\Lambda_S$-modules on a site denotes this sheaf
Hom.

(SHEAF DAG node `def-pur-sheaf-hom`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: definition. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Lean names not on master: `CategoryTheory.ihom`, `CategoryTheory.ihom.ev`. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`.
