+++
id = "dag-sk-thm-pe-classical-sheaves"
kind = "dag-lemma"
title = "Recognizing the classical part"
name_showing = false
order = 115508
tags = ["sheaf-dag"]
split_from = "theorem-classical-sheaves-essential-image--1"
dag_id = "sk-thm-pe-classical-sheaves"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.proEtaleClassicalSheaves"]
uses = ["dag-def-weil-pbc-constant-sheaf", "dag-det-pe-classical-definition-continuity-map", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $X$ be a scheme and let $\nu_X^*\dashv\nu_{X,*}$ be the comparison adjunction from the small étale site to the small pro-étale site `def-weil-pbc-site-comparison-morphism`. The functor
$\nu_X^*\colon\Sh(X_{\Et})\to\Sh(X_{\Proet})$ on sheaves of sets is fully faithful. Its essential image is exactly the classical sheaves of [dag-sk-def-pe-classical-definition].

Let $\Lambda$ be a discrete commutative ring, let $\Lambda_{X,\Et}$ be its constant sheaf of rings [dag-def-weil-pbc-constant-sheaf], and write $\Lambda_X=\nu_X^*\Lambda_{X,\Et}$. For module sheaves `def-weil-sheaf-of-modules-category`, the same inverse image is an exact equivalence between $\Mod(X_{\Et},\Lambda)$ and the full subcategory of classical $\Lambda_X$-module sheaves on $X_{\Proet}$, where classicality is as in [dag-sk-def-pe-classical-definition].

(SHEAF DAG node `sk-thm-pe-classical-sheaves`; machine-alignment layer.) Split from [theorem-classical-sheaves-essential-image--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`, `lem-coef-grothendieck-locally-presentable`.
