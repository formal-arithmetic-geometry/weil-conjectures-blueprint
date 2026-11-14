+++
id = "dag-lem-weil-pbc-fixed-module-derived-hom-bijection"
kind = "dag-lemma"
title = "Derived comparison Hom bijection with bounded below target"
name_showing = false
order = 123503
tags = ["sheaf-dag"]
split_from = "theorem-bounded-below-cohomology-comparison--2"
dag_id = "lem-weil-pbc-fixed-module-derived-hom-bijection"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.bijective_comparisonUpperStar_mapDerivedCategory_map"]
uses = ["dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let X be a scheme and A a Grothendieck abelian symmetric monoidal closed coefficient category, with monoidal preadditivity and functorial flat resolutions, as in the existing derived comparison construction `def-weil-pbc-proetale-modules`. For etale derived objects K and M with M bounded below, the exact inverse image induces a bijection Hom(K,M) to Hom(nu* K,nu* M). In particular this applies to modules over any commutative coefficient ring.

(SHEAF DAG node `lem-weil-pbc-fixed-module-derived-hom-bijection`; machine-alignment layer.) Split from [theorem-bounded-below-cohomology-comparison--2]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-pc-flat-sheaf-modules`, `lem-coef-grothendieck-locally-presentable`, `lem-pc-derived-category-locally-small`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-proetale-sheaves-grothendieck`, `lem-weil-pbc-sheaf-tensor-closed`.
