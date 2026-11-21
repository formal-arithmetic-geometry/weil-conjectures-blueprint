+++
id = "dag-lem-pur-sheaf-hom-cover-gluing"
kind = "dag-lemma"
title = "Gluing O-linear maps on one covering family"
name_showing = false
order = 184519
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-pur-sheaf-hom-cover-gluing"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.existsUnique_hom_of_cover"]
uses = ["dag-def-pur-localized-ringed-site"]
+++
Let C be a site with the fiber products U_i\times_U U_j and V\times_U U_i used below `def-weil-sheaf-of-modules-category`, O a sheaf of commutative rings, and F,G sheaves of O-modules `def-weil-sheaf-of-modules-category`. Given an object U and a covering family {U_i\to U}, every family of O|_{U_i}-linear morphisms φ_i:F|_{U_i}\to G|_{U_i} that agrees after restriction to U_i\times_U U_j glues to a unique O|_U-linear morphism φ:F|_U\to G|_U.

(SHEAF DAG node `lem-pur-sheaf-hom-cover-gluing`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`.
