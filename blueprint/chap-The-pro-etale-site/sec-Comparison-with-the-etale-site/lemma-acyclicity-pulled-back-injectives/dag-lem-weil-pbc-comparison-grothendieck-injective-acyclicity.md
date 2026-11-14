+++
id = "dag-lem-weil-pbc-comparison-grothendieck-injective-acyclicity"
kind = "dag-lemma"
title = "Comparison pullbacks of injective module sheaves are direct-image acyclic"
name_showing = false
order = 120503
tags = ["sheaf-dag"]
split_from = "lemma-acyclicity-pulled-back-injectives--1"
dag_id = "lem-weil-pbc-comparison-grothendieck-injective-acyclicity"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.rightAcyclic_comparisonUpperStar_obj_of_injective"]
uses = ["dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $X$ be any scheme and let $\Lambda$ be a finite ring in the common larger universe of its small sites. Form the canonical comparison adjunction $\nu_X^*\dashv\nu_{X,*}$ on sheaves of left $\Lambda$-modules by `def-weil-pbc-site-comparison-morphism`. For every injective etale module sheaf $I$ and every $n\geq0$, one has $R^{n+1}\nu_{X,*}(\nu_X^*I)=0$. There are no affineness or quasi-compactness hypotheses on $X$.

(SHEAF DAG node `lem-weil-pbc-comparison-grothendieck-injective-acyclicity`; machine-alignment layer.) Split from [lemma-acyclicity-pulled-back-injectives--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-sp-acyclic`, `lem-coef-grothendieck-locally-presentable`, `lem-sfb-proetale-sheaves-grothendieck`, `sk-def-groth-ss`.
