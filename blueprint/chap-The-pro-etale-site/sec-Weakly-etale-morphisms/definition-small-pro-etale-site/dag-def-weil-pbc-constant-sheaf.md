+++
id = "dag-def-weil-pbc-constant-sheaf"
kind = "dag-definition"
title = "Constant sheaf on a site"
name_showing = false
order = 34501
tags = ["sheaf-dag"]
split_from = "definition-small-pro-etale-site--1"
dag_id = "def-weil-pbc-constant-sheaf"
dag_kind = "definition"
dag_status = "mathlib"
serial = false
uses = ["dag-def-weil-pbc-sheafification"]
+++
Let $\mathcal C$ be a site and $\mathcal A$ a category of values in which sheafification exists (sets, abelian groups, rings). For an object $E$ of $\mathcal A$ the *constant sheaf* $\underline E$ on $\mathcal C$ is the sheafification [dag-def-weil-pbc-sheafification] of the constant presheaf $U\mapsto E$, all of whose restriction maps are the identity of $E$. For a commutative ring $A$ the constant sheaf of rings $\underline A$ is a sheaf of commutative rings; on $Y_{\mathrm{proet}}$ it is written $A_Y$.

(SHEAF DAG node `def-weil-pbc-constant-sheaf`; machine-alignment layer.) Split from [definition-small-pro-etale-site--1]. DAG kind: definition. Placed through `def-weil-pbc-proetale-site` (ancestor-1). DAG status: mathlib. Lean names not on master: `CategoryTheory.constantSheaf`.
