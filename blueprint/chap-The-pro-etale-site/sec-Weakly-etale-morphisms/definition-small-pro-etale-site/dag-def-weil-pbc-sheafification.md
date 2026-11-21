+++
id = "dag-def-weil-pbc-sheafification"
kind = "dag-definition"
title = "Sheafification on a site"
name_showing = false
order = 34505
tags = ["sheaf-dag"]
split_from = "definition-small-pro-etale-site--1"
dag_id = "def-weil-pbc-sheafification"
dag_kind = "definition"
dag_status = "mathlib"
serial = false
+++
Let $\mathcal C$ be a site and let $\mathcal A$ be one of the categories of sets, abelian groups, rings or modules over a fixed ring (more generally a category of values in which sheafification exists). For a presheaf $\mathcal F:\mathcal C^{\mathrm{op}}\to\mathcal A$, its *sheafification* is a sheaf $\mathcal F^\#$ on $\mathcal C$ with values in $\mathcal A$ together with a morphism of presheaves $\mathcal F\to\mathcal F^\#$ through which every morphism from $\mathcal F$ to a sheaf factors uniquely; equivalently, $\mathcal F\mapsto\mathcal F^\#$ is a left adjoint to the inclusion of sheaves into presheaves.

(SHEAF DAG node `def-weil-pbc-sheafification`; machine-alignment layer.) Split from [definition-small-pro-etale-site--1]. DAG kind: definition. Placed through `def-weil-pbc-proetale-site` (ancestor-1). DAG status: mathlib. Lean names not on master: `CategoryTheory.presheafToSheaf`, `CategoryTheory.toSheafify`, `CategoryTheory.sheafificationAdjunction`.
