+++
id = "dag-det-pe-left-complete-iso"
kind = "dag-lemma"
title = "Postnikov convergence in the pro-étale derived category"
name_showing = false
order = 97501
tags = ["sheaf-dag"]
split_from = "proposition-left-completeness--1"
dag_id = "det-pe-left-complete-iso"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["DerivedCategory.isHomotopyLimit_truncGECone"]
+++
Let $\mathcal C$ be an abelian category with K-injective resolutions in which countable
products exist and are exact; for instance the sheaves of $\Lambda$-modules on
$X_{\mathrm{proét}}$ ($\Lambda$ a ring). For every object $K$ of $D(\mathcal C)$, the
truncation maps $K\to\tau_{\geq-n}K$ exhibit $K$ as a homotopy limit of the tower
$\cdots\to\tau_{\geq-1}K\to\tau_{\geq0}K$: with $T$ the transition endomorphism of
$\prod_n\tau_{\geq-n}K$, there is a distinguished triangle

$$
K\longrightarrow\prod_n\tau_{\geq-n}K\xrightarrow{\,1-T\,}\prod_n\tau_{\geq-n}K
\longrightarrow K[1]
$$

whose first map has the truncation maps as components. In other words,
$K\to R\varprojlim_n\tau_{\geq-n}K$ is an isomorphism.

(SHEAF DAG node `det-pe-left-complete-iso`; machine-alignment layer.) Split from [proposition-left-completeness--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-sp-abelian`, `def-sp-kinjective-bridge`, `def-weil-abstract-derived-category`, `def-sbc-standard-tstructure-derived-category`, `def-weil-category-product`, `def-weil-inverse-system`, `def-weil-tower-transition-endomorphism`, `def-weil-derived-limit`, `def-weil-sheaf-of-modules-category`, `sk-def-pe-site`.
