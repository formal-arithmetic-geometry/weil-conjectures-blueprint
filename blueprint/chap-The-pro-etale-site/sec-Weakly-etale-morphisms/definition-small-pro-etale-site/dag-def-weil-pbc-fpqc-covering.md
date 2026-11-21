+++
id = "dag-def-weil-pbc-fpqc-covering"
kind = "dag-definition"
title = "fpqc covering of a scheme"
name_showing = false
order = 34502
tags = ["sheaf-dag"]
split_from = "definition-small-pro-etale-site--1"
dag_id = "def-weil-pbc-fpqc-covering"
dag_kind = "definition"
dag_status = "mathlib"
serial = false
+++
Let $T$ be a scheme `def-pc-scheme`. A family of morphisms of schemes $\{f_i:T_i\to T\}_{i\in I}$ is an *fpqc covering* of $T$ if every $f_i$ is flat `def-weil-flat-morphism` and for every affine open $V\subset T$ there are $n\ge0$, indices $i_1,\dots,i_n\in I$ and affine opens $V_j\subset T_{i_j}$ with $\bigcup_{j=1}^n f_{i_j}(V_j)=V$. (Then $T=\bigcup_i f_i(T_i)$, since $T$ is covered by affine opens.)

(SHEAF DAG node `def-weil-pbc-fpqc-covering`; machine-alignment layer.) Split from [definition-small-pro-etale-site--1]. DAG kind: definition. Placed through `def-weil-pbc-proetale-site` (ancestor-1). DAG status: mathlib. Lean names not on master: `AlgebraicGeometry.Scheme.fpqcPrecoverage`. Statement dependencies not drawn: `def-pc-scheme`, `def-weil-flat-morphism`.
