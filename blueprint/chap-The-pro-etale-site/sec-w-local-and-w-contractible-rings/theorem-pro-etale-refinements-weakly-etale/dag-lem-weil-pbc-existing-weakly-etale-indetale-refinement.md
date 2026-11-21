+++
id = "dag-lem-weil-pbc-existing-weakly-etale-indetale-refinement"
kind = "dag-lemma"
title = "Existing existential ind-etale refinement of a weakly etale map"
name_showing = false
order = 62501
tags = ["sheaf-dag"]
split_from = "theorem-pro-etale-refinements-weakly-etale--1"
dag_id = "lem-weil-pbc-existing-weakly-etale-indetale-refinement"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["RingHom.WeaklyEtale.exists_indEtale_comp"]
uses = ["dag-sk-def-pe-morphisms"]
+++
Let $R,S$ be commutative rings in a common universe and let $f:R\to S$ be weakly etale [dag-def-weil-pbc-ind-etale-algebra]. There exist a commutative ring $T$ in the same universe and a ring homomorphism $g:S\to T$ such that $g$ is ind-etale and faithfully flat `def-weil-pbc-faithfully-flat-ring-map` and $g\circ f$ is ind-etale.

(SHEAF DAG node `lem-weil-pbc-existing-weakly-etale-indetale-refinement`; machine-alignment layer.) Split from [theorem-pro-etale-refinements-weakly-etale--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-weil-pbc-faithfully-flat-ring-map`.
