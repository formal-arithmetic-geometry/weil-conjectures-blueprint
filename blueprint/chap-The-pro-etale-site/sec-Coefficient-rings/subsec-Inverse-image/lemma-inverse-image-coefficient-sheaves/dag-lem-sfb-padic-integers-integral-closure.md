+++
id = "dag-lem-sfb-padic-integers-integral-closure"
kind = "dag-lemma"
title = "The integers of a finite local-field extension are the integral closure"
name_showing = false
order = 187554
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--3"
dag_id = "lem-sfb-padic-integers-integral-closure"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["Padic.padic_integers_integralClosure"]
+++
Let $\ell$ be a prime and let $E\subseteq F$ be finite extensions of $\mathbf Q_\ell$. Give them their compatible extending $\ell$-adic absolute values, and put $\mathcal O_E=\{a\in E:|a|_E\leq1\}$ and $\mathcal O_F=\{x\in F:|x|_F\leq1\}$, as in `def-weil-l-adic-coefficient-extension`. Then, for every $x\in F$, $x\in\mathcal O_F$ if and only if $x$ satisfies a monic polynomial with coefficients in $\mathcal O_E$. Equivalently, $\mathcal O_F$ is the integral closure of $\mathcal O_E$ in $F$ `def-weil-pbc-integral-closure`.

(SHEAF DAG node `lem-sfb-padic-integers-integral-closure`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--3]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-finite-free` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-pbc-integral-closure`, `lem-weil-l-adic-extension-integers-dvr`.
