+++
id = "dag-det-pe-hypercover-existence"
kind = "dag-lemma"
title = "Hypercovers by single w-contractible affines"
name_showing = false
order = 103501
tags = ["sheaf-dag"]
split_from = "proposition-weakly-contractible-hypercovers--1"
dag_id = "det-pe-hypercover-existence"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.exists_proetale_hypercover_single_affine"]
uses = ["dag-det-pe-wlocal-strict-contractible", "dag-sk-def-pe-wlocal"]
+++
Let $U$ be a quasi-compact, quasi-separated object of $X_{\mathrm{proét}}$.

1. A finite product $D=D_1\times\dots\times D_k$ of w-contractible rings is w-contractible.
2. Every quasi-compact object $V$ of $X_{\mathrm{proét}}$ admits a single covering map
   $\operatorname{Spec}D\to V$ with $D$ w-contractible.
3. There is a hypercovering $W_\bullet\to U$ in $X_{\mathrm{proét}}$ (a simplicial object
   over $U$ such that $W_0\to U$ and every map $W_{r+1}\to(\operatorname{cosk}_r
   \operatorname{sk}_rW_\bullet)_{r+1}$ to the matching object is a covering) with every
   $W_r=\operatorname{Spec}D_r$, $D_r$ w-contractible; in particular every $W_r$ is
   affine and weakly contractible.

(SHEAF DAG node `det-pe-hypercover-existence`; machine-alignment layer.) Split from [proposition-weakly-contractible-hypercovers--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-sfb-proper-face-diagram`, `def-weil-affine-spectrum`, `def-weil-pbc-scheme-conventions`, `def-weil-pbc-simplicial-coskeleton`, `def-weil-pbc-simplicial-object`, `lem-weil-pbc-matching-object-proper-faces`, `sk-def-pe-site`.
