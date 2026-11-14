+++
id = "dag-prop-weil-pbc-comparison-direct-image"
kind = "dag-lemma"
title = "Comparison direct image"
name_showing = false
order = 136502
tags = ["sheaf-dag"]
split_from = "lemma-comparison-direct-images-compatibilities--3"
dag_id = "prop-weil-pbc-comparison-direct-image"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.etaleComparisonDirectImageCompIso", "AlgebraicGeometry.ProEtale.proEtaleComparisonDirectImageCompIso", "AlgebraicGeometry.ProEtale.isIso_comparisonDirectImagePlus", "AlgebraicGeometry.ProEtale.comparisonDirectImagePlus_id", "AlgebraicGeometry.ProEtale.comparisonDirectImagePlus_comp"]
uses = ["dag-def-sfb-finite-lower-star", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $u:U\to V$ be quasi-compact and quasi-separated and let
$L\in\Dplus(U_{\Et},\Lambda)$. There is a natural isomorphism

$$
 \nu_V^*Ru_{\Et,*}L
 \xrightarrow{\sim}
 Ru_{\Proet,*}\nu_U^*L.
$$

It is compatible with identities, composites, and morphisms of $L$.

(SHEAF DAG node `prop-weil-pbc-comparison-direct-image`; machine-alignment layer.) Split from [lemma-comparison-direct-images-compatibilities--3]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-weil-pbc-derived-inverse-image`, `def-weil-pbc-direct-image`, `def-weil-pbc-scheme-conventions`, `lem-coef-grothendieck-locally-presentable`, `lem-pc-derived-category-locally-small`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-proetale-sheaves-grothendieck`, `lem-weil-pbc-direct-image-left-exact`, `lem-weil-pbc-etale-base-change-continuous`, `lem-weil-pbc-inverse-image-composition`, `lem-weil-pbc-sheaf-tensor-closed`.
