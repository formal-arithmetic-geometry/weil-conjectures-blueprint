+++
id = "dag-lem-weil-pbc-existing-wcontractible-indetale-retraction"
kind = "dag-lemma"
title = "Existing ind-etale splitting theorem for a geometrically w-contractible ring"
name_showing = false
order = 56501
tags = ["sheaf-dag"]
split_from = "proposition-splitting-ind-etale-covers--1"
dag_id = "lem-weil-pbc-existing-wcontractible-indetale-retraction"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["IsWContractibleRing.exists_retraction"]
uses = ["dag-def-weil-pbc-ind-etale-algebra", "dag-det-pe-wlocal-strict-contractible", "dag-sk-def-pe-morphisms", "dag-sk-def-pe-wlocal"]
+++
Let $R,S$ be commutative rings in a common universe, and give $S$ an $R$-algebra structure. Assume $R$ is w-local [dag-def-weil-pbc-w-local], its connected-component space is extremally disconnected, and $R_m$ is strictly henselian for every maximal ideal $m$ `def-weil-pbc-henselian-terminology`. If $S$ is ind-etale over $R$ [dag-def-weil-pbc-ind-etale-algebra] and faithfully flat over $R$ `def-weil-pbc-faithfully-flat-ring-map`, there exists a ring homomorphism $s:S\to R$ such that $s\circ\operatorname{algebraMap}=\mathrm{id}_R$. These three geometric assumptions are exactly the fields of the source class IsWContractibleRing.

(SHEAF DAG node `lem-weil-pbc-existing-wcontractible-indetale-retraction`; machine-alignment layer.) Split from [proposition-splitting-ind-etale-covers--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-weil-pbc-faithfully-flat-ring-map`.
