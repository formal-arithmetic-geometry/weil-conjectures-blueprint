+++
id = "dag-lem-weil-pbc-source-wcontractible-extension"
kind = "dag-lemma"
title = "Closed source construction of a w-contractible ind-etale extension"
name_showing = false
order = 59501
tags = ["sheaf-dag"]
split_from = "theorem-existence-contractible-covers--1"
dag_id = "lem-weil-pbc-source-wcontractible-extension"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["exists_isWContractibleRing"]
uses = ["dag-def-weil-pbc-ind-etale-algebra", "dag-det-pe-wlocal-strict-contractible", "dag-sk-def-pe-morphisms", "dag-sk-def-pe-wlocal"]
+++
For every commutative ring R in Type u, there are a commutative ring D in Type u and an R-algebra structure such that D is ind-etale over R [dag-def-weil-pbc-ind-etale-algebra], faithfully flat as an R-module `def-weil-pbc-faithfully-flat-ring-map`, and w-contractible in the geometric sense: Spec D is w-local, the localizations at all maximal ideals are strictly henselian, and the connected-component space of Spec D is extremally disconnected. These last conditions are precisely the source-library class IsWContractibleRing D. Universes follow `def-weil-size-convention`; no nontriviality hypothesis is imposed.

(SHEAF DAG node `lem-weil-pbc-source-wcontractible-extension`; machine-alignment layer.) Split from [theorem-existence-contractible-covers--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-weil-pbc-faithfully-flat-ring-map`, `def-weil-size-convention`.
