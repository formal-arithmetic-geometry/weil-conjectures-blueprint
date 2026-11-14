+++
id = "dag-lem-sfb-local-field-integral-basis"
kind = "dag-lemma"
title = "Existence of an integral basis for a finite extension of local coefficient fields"
name_showing = false
order = 187502
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves"
dag_id = "lem-sfb-local-field-integral-basis"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["Padic.exists_integral_basis"]
+++
Let $\ell$ be a prime and let $E\subseteq F$ be finite extensions of $\mathbf Q_\ell$ `def-weil-l-adic-coefficient-extension`, with the compatible absolute values extending the $\ell$-adic absolute value. Put $\mathcal O_E=\{x\in E:|x|\leq1\}$ and $\mathcal O_F=\{x\in F:|x|\leq1\}$, the rings of integers, with the inclusion induced by $E\subseteq F$. Let $d=[F:E]=\dim_E F$. There exist elements $b_1,\ldots,b_d\in\mathcal O_F$ such that every $x\in\mathcal O_F$ has a unique expression $x=\sum_{i=1}^d a_i b_i$ with $a_i\in\mathcal O_E$.

(SHEAF DAG node `lem-sfb-local-field-integral-basis`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves]. DAG kind: statement. Placed through `sk-prop-sfb-cartesian-coefficients` (ancestor-1). DAG status: split. Statement dependencies not drawn: `lem-weil-l-adic-extension-integers-dvr`.
