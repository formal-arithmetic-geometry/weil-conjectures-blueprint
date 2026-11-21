+++
id = "dag-det-pe-hypercover-single-cover"
kind = "dag-lemma"
title = "Every quasi-compact pro-etale object has a single covering arrow whose source is the spectrum of a w-contractible ring."
name_showing = false
order = 103507
tags = ["sheaf-dag"]
split_from = "proposition-weakly-contractible-hypercovers--1"
dag_id = "det-pe-hypercover-single-cover"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["exists_single_wContractible_affine_cover"]
uses = ["dag-det-pe-wlocal-strict-contractible", "dag-sk-def-pe-wlocal"]
+++
For every scheme X and every quasi-compact object V of its small pro-etale site, there are a commutative ring D, a weakly etale map Spec D to X, and an arrow g from this site object to V such that D is w-contractible and the singleton presieve of g is a pro-etale covering. No quasi-separatedness hypothesis on V or X is required.

(SHEAF DAG node `det-pe-hypercover-single-cover`; machine-alignment layer.) Split from [proposition-weakly-contractible-hypercovers--1]. DAG kind: statement. Placed through `det-pe-hypercover-existence` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-affine-spectrum`, `def-weil-pbc-scheme-conventions`, `sk-def-pe-site`.
