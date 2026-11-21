+++
id = "dag-def-sf-strict-roos-functor"
kind = "dag-definition"
title = "Strict-complex Roos functor"
name_showing = false
order = 210506
tags = ["sheaf-dag"]
split_from = "lemma-reduction-derived-nakayama--2"
dag_id = "def-sf-strict-roos-functor"
dag_kind = "definition"
dag_status = "split"
serial = false
uses = ["dag-def-weil-signed-mapping-cocone-functor"]
+++
Let $\mathcal A$ be an abelian category `def-sp-abelian` with countable products `def-weil-category-product`. For a strict tower $C:\mathbf N^{op}\to\operatorname{CochainComplex}(\mathcal A,\mathbf Z)$ `def-weil-inverse-system`, set $s_C$ to be its product shift and $b_C=1-s_C$ `def-weil-tower-transition-endomorphism`. Define $\operatorname{Roos}(C)=\operatorname{Cone}(b_C)[-1]$, using the signed cochain mapping cocone [dag-def-weil-signed-mapping-cocone-functor]. Define the functor on strict towers by sending a natural transformation $a:C\to C'$ to the mapping-cocone map whose two coordinates are $\prod_n a_n$. This is the strict-complex Roos construction associated with `def-weil-derived-limit`, with actual chosen product projections and cone coordinates. The comparison identifying its image in the derived category with a derived limit is a separate assertion: as in the cited blueprint, it applies when termwise countable products represent products in the derived category (in particular under exact countable products).

(SHEAF DAG node `def-sf-strict-roos-functor`; machine-alignment layer.) Split from [lemma-reduction-derived-nakayama--2]. DAG kind: definition. Placed through `det-pe-derived-nakayama-first-reduction` (ancestor-1). DAG status: split. Lean names not on master: `CategoryTheory.StrictTowerRoos.productFunctor`, `CategoryTheory.StrictTowerRoos.boundary`, `CategoryTheory.StrictTowerRoos.functor`. Statement dependencies not drawn: `def-sp-abelian`, `def-weil-category-product`, `def-weil-inverse-system`, `def-weil-tower-transition-endomorphism`, `def-weil-derived-limit`.
