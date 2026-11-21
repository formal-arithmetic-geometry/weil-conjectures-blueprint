+++
id = "dag-sk-thm-pe-constructible-comparison"
kind = "dag-lemma"
title = "Constructible comparison"
name_showing = false
order = 149537
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "sk-thm-pe-constructible-comparison"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.constructibleComparison"]
uses = ["dag-def-pe-etale-constructible-module", "dag-det-pe-classical-definition-continuity-map"]
+++
For Noetherian $\Lambda$, a sheaf on $X_{\Proet}$ is constructible if locally on $X$
a finite partition into constructible locally closed strata makes it locally
constant of finite type on each stratum.

Let $X$ be quasi-compact and quasi-separated. For a discrete Noetherian
$\Lambda$, every constructible pro-étale $\Lambda_X$-module sheaf is classical.
The functor $\nu_X^*$ gives an equivalence from constructible étale sheaves of
$\Lambda$-modules to $\operatorname{Cons}(X,\Lambda)$, and an equivalence
$D^b_c(X_{\Et},\Lambda)\to\Dbc(X,\Lambda)$ of bounded constructible derived
categories.

(SHEAF DAG node `sk-thm-pe-constructible-comparison`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `sk-def-sfb-constructible`, `sk-def-sfb-bounded-constructible`, `def-pc-scheme`, `def-weil-pbc-noetherian-ring`, `def-weil-pbc-quasi-compact-scheme`, `def-weil-quasi-separated-morphism`, `def-weil-pbc-site-comparison-morphism`, `def-sfb-affine-locally-constructible-proetale-modules`.
