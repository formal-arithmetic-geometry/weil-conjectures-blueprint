+++
id = "dag-def-pur-presheaf-tensor-product"
kind = "dag-definition"
title = "Presheaf tensor product of modules"
name_showing = false
order = 184504
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "def-pur-presheaf-tensor-product"
dag_kind = "definition"
dag_status = "mathlib"
serial = false
+++
Let $\mathcal C$ be a site, let $\mathcal O$ be a sheaf of commutative rings on $\mathcal C$, and let $\mathcal F,\mathcal G$ be presheaves of $\mathcal O$-modules `def-weil-presheaf-modules-sheafification`. Their presheaf tensor product $\mathcal F\otimes_{p,\mathcal O}\mathcal G$ is the presheaf of modules whose value on each object $U$ is $\mathcal F(U)\otimes_{\mathcal O(U)}\mathcal G(U)$ and whose restriction along a morphism $V\to U$ is the map induced by the restriction maps of $\mathcal F$, $\mathcal G$, and $\mathcal O$.

(SHEAF DAG node `def-pur-presheaf-tensor-product`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: definition. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: mathlib. Statement dependencies not drawn: `def-weil-presheaf-modules-sheafification`.
