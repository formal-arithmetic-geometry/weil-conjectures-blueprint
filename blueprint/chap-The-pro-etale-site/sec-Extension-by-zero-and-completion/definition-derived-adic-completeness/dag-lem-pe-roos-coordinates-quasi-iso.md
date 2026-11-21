+++
id = "dag-lem-pe-roos-coordinates-quasi-iso"
kind = "dag-lemma"
title = "Diagonal quasi-isomorphisms of Roos coordinate complexes"
name_showing = false
order = 208506
tags = ["sheaf-dag"]
split_from = "definition-derived-adic-completeness--1"
dag_id = "lem-pe-roos-coordinates-quasi-iso"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["CochainComplex.quasiIso_of_roos_coordinates"]
+++
Let $\mathcal A$ be an abelian category `def-sp-abelian`. Let $V,V^{\prime},L,L^{\prime}$ be cochain complexes `def-weil-abstract-derived-category`, and $s:V\to V$, $s^{\prime}:V^{\prime}\to V^{\prime}$ chain endomorphisms. Suppose specified isomorphisms identify $L^i=V^i\oplus V^{i-1}$ and $L^{\prime i}=V^{\prime i}\oplus V^{\prime i-1}$ with differential $(x,y)\mapsto(dx,sx-dy)$ in both cases. If $a:V\to V^{\prime}$ is a quasi-isomorphism and a chain map $f:L\to L^{\prime}$ acts in these coordinates by $(a^i,a^{i-1})$, then $f$ is a quasi-isomorphism.

(SHEAF DAG node `lem-pe-roos-coordinates-quasi-iso`; machine-alignment layer.) Split from [definition-derived-adic-completeness--1]. DAG kind: statement. Placed through `sk-def-pe-derived-completion` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-sp-abelian`, `def-weil-abstract-derived-category`.
