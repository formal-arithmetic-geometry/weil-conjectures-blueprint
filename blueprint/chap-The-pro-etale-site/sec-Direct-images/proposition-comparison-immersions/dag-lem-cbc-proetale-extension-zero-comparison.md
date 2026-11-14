+++
id = "dag-lem-cbc-proetale-extension-zero-comparison"
kind = "dag-lemma"
title = "Comparison of extension by zero with the site morphism"
name_showing = false
order = 139501
tags = ["sheaf-dag"]
split_from = "proposition-comparison-immersions--1"
dag_id = "lem-cbc-proetale-extension-zero-comparison"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.openImmersionLowerShriekComparisonUpperStarIso", "AlgebraicGeometry.ProEtale.proEtaleOpenExtensionComp", "AlgebraicGeometry.ProEtale.openImmersionLowerShriekComparison_coherence"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $\nu_X:X_{\Proet}\to X_{\Et}$ be the comparison morphism of
`def-weil-pbc-site-comparison-morphism`. For an open immersion
$j:U\hookrightarrow X$ and a finite commutative ring $\Lambda$ the
canonical comparison

$$
\nu_X^*j^{\mathrm{et}}_!F\xrightarrow{\ \sim\ }j^{\mathrm{proet}}_!\nu_U^*F
$$

is an isomorphism for every sheaf $F$ of $\Lambda$-modules on
$U_{\Et}$, naturally in $F$ and compatible with composition of
open immersions; here the two $j_!$ are those of
`def-weil-pbc-extension-by-zero` and
`def-weil-extension-by-zero`.

(SHEAF DAG node `lem-cbc-proetale-extension-zero-comparison`; machine-alignment layer.) Split from [proposition-comparison-immersions--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-sfb-finite-extension-by-zero`, `def-weil-open-immersion`, `def-weil-pbc-extension-by-zero`, `def-weil-sheaf-of-modules-category`, `lem-coef-grothendieck-locally-presentable`, `sk-def-sfb-finite-lower-shriek`.
