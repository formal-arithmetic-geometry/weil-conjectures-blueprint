+++
id = "dag-lem-sfb-integral-closure-rank"
kind = "dag-lemma"
title = "Rank of an integral closure over a principal ideal domain"
name_showing = false
order = 187501
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves"
dag_id = "lem-sfb-integral-closure-rank"
dag_kind = "statement"
dag_status = "mathlib"
serial = false
+++
Let $A$ be a principal ideal domain with fraction field $K$, and let $L/K$ be a finite separable field extension `def-pc-field-extension`, `def-weil-pbc-separable-algebraic-extension`. Let $C$ be a commutative $A$-algebra embedded in $L$, with both structural maps $A\to L$ equal to the composite through $K$ and through $C$, and suppose $C$ is the integral closure of $A$ in $L$ `def-weil-pbc-integral-closure`. Then $\operatorname{finrank}_A C=\dim_K L$ `def-weil-vector-space-dimension`. Here the rank of the finite free $A$-module $C$ `def-weil-pbc-free-module` is the cardinality of any basis.

(SHEAF DAG node `lem-sfb-integral-closure-rank`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves]. DAG kind: statement. Placed through `sk-prop-sfb-cartesian-coefficients` (ancestor-1). DAG status: mathlib. Lean names not on master: `IsIntegralClosure.rank`. Statement dependencies not drawn: `def-pc-field-extension`, `def-weil-pbc-free-module`, `def-weil-pbc-integral-closure`, `def-weil-pbc-separable-algebraic-extension`, `def-weil-vector-space-dimension`.
