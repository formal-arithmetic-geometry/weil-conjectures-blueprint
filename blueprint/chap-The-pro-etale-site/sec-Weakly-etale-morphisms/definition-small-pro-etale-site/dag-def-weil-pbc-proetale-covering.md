+++
id = "dag-def-weil-pbc-proetale-covering"
kind = "dag-definition"
title = "Pro-etale covering of a scheme"
name_showing = false
order = 34503
tags = ["sheaf-dag"]
split_from = "definition-small-pro-etale-site--1"
dag_id = "def-weil-pbc-proetale-covering"
dag_kind = "definition"
dag_status = "mathlib"
serial = false
uses = ["dag-def-weil-pbc-fpqc-covering"]
+++
Let $U$ be a scheme `def-pc-scheme`. A family of morphisms of schemes $\{f_i:U_i\to U\}_{i\in I}$ is a *pro-etale covering* if every $f_i$ is weakly etale `def-weil-weakly-etale-morphism` and the family is an fpqc covering [dag-def-weil-pbc-fpqc-covering]: for every affine open $V\subset U$ there are finitely many indices $i_1,\dots,i_n$ and affine opens $V_j\subset U_{i_j}$ with $\bigcup_j f_{i_j}(V_j)=V$.

(SHEAF DAG node `def-weil-pbc-proetale-covering`; machine-alignment layer.) Split from [definition-small-pro-etale-site--1]. DAG kind: definition. Placed through `def-weil-pbc-proetale-site` (ancestor-1). DAG status: mathlib. Statement dependencies not drawn: `def-pc-scheme`, `def-weil-weakly-etale-morphism`.
