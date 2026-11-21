+++
id = "dag-lem-pe-higher-direct-image-filtered-colimits"
kind = "dag-lemma"
title = "Pro-étale higher direct images of abelian sheaves commute with filtered colimits"
name_showing = false
order = 106501
tags = ["sheaf-dag"]
split_from = "corollary-continuity-cohomology--2"
dag_id = "lem-pe-higher-direct-image-filtered-colimits"
dag_kind = "statement"
dag_status = "unsplit"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.preservesColimitsOfShape_rightDerived_lowerStar"]
uses = ["dag-def-sfb-finite-lower-star", "dag-def-weil-pbc-proetale-site", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $f\colon X\to Y$ be a quasi-compact `def-weil-finite-type-morphism` and quasi-separated `def-weil-quasi-separated-morphism` morphism of schemes and $f_*$ the direct image of abelian sheaves on the small pro-étale sites [dag-def-weil-pbc-proetale-site]. Then for every $q\ge0$ the right derived functor $R^qf_*$ `def-sfb-right-derived-functor` preserves filtered colimits `def-weil-pbc-category-colimit`: for a filtered diagram $(K_i)$ of abelian sheaves on $X_{\mathrm{pro\acute et}}$ the canonical map $\varinjlim_iR^qf_*K_i\to R^qf_*(\varinjlim_iK_i)$ is an isomorphism.

(SHEAF DAG node `lem-pe-higher-direct-image-filtered-colimits`; machine-alignment layer.) Split from [corollary-continuity-cohomology--2]. DAG kind: statement. DAG status: unsplit. Statement dependencies not drawn: `def-weil-finite-type-morphism`, `def-weil-pbc-category-colimit`, `def-weil-quasi-separated-morphism`, `lem-coef-grothendieck-locally-presentable`, `lem-sfb-proetale-sheaves-grothendieck`.
