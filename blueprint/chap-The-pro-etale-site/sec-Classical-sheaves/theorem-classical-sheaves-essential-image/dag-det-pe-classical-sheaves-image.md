+++
id = "dag-det-pe-classical-sheaves-image"
kind = "dag-lemma"
title = "The essential image of the comparison inverse image"
name_showing = false
order = 115501
tags = ["sheaf-dag"]
split_from = "theorem-classical-sheaves-essential-image--1"
dag_id = "det-pe-classical-sheaves-image"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.proEtaleClassicalSheavesImage"]
uses = ["dag-det-pe-classical-definition-continuity-map"]
+++
Let $X$ be a scheme and $G$ a sheaf of sets on $X_{\Proet}$. The following are
equivalent:

1. $G\cong\nu_X^*F$ for some sheaf $F$ on $X_{\Et}$;
2. $G$ is classical in the sense of [dag-det-pe-classical-definition-continuity-map];
3. the counit $\varepsilon_G\colon\nu_X^*\nu_{X,*}G\to G$ is an isomorphism.

(SHEAF DAG node `det-pe-classical-sheaves-image`; machine-alignment layer.) Split from [theorem-classical-sheaves-essential-image--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-weil-pbc-site-comparison-morphism`.
