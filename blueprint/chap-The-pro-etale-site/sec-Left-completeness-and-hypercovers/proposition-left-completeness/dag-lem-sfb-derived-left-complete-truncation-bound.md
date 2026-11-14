+++
id = "dag-lem-sfb-derived-left-complete-truncation-bound"
kind = "dag-lemma"
title = "Left completeness and a uniform upper bound on lower truncations"
name_showing = false
order = 97502
tags = ["sheaf-dag"]
split_from = "proposition-left-completeness--1"
dag_id = "lem-sfb-derived-left-complete-truncation-bound"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["DerivedCategory.isHomotopyLimit_truncGECone", "DerivedCategory.isLE_of_isHomotopyLimit", "DerivedCategory.isLE_obj_of_forall_isLE_obj_truncGE"]
+++
Let C and D be abelian categories with unbounded derived categories, K-injective resolutions, and exact countable products [def-sp-abelian, def-weil-abstract-derived-category, def-weil-category-product]. Every K in D(C) is the homotopy limit, with the specified canonical projections, of its standard truncation tower tau_{>=-n}K [def-sbc-standard-tstructure-derived-category, def-weil-derived-limit]. Consequently, if G:D(C)→D(D) is triangulated and preserves countable products, and G(tau_{>=-n}K) lies in D^{<=b} for every natural n, then G(K) lies in D^{<=b+1}. No bound on K itself or heart objects is assumed.

(SHEAF DAG node `lem-sfb-derived-left-complete-truncation-bound`; machine-alignment layer.) Split from [proposition-left-completeness--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-sbc-standard-tstructure-derived-category`, `def-sp-abelian`, `def-weil-abstract-derived-category`, `def-weil-category-product`.
