+++
id = "dag-sk-thm-pe-indetale-refinement"
kind = "dag-lemma"
title = "Weakly étale maps admit pro-étale refinements"
name_showing = false
order = 62502
tags = ["sheaf-dag"]
split_from = "theorem-pro-etale-refinements-weakly-etale--1"
dag_id = "sk-thm-pe-indetale-refinement"
dag_kind = "statement"
dag_status = "imported"
serial = false
dag_lean = ["RingHom.WeaklyEtale.exists_indEtale_comp"]
uses = ["dag-sk-def-pe-morphisms"]
+++
If $R\to B$ is weakly étale [dag-sk-def-pe-morphisms], there is a faithfully flat ind-étale map
$B\to B'$ such that $R\to B'$ is ind-étale.

Objects of $X_{\mathrm{proét}}$ are weakly étale, while the covers of [dag-sk-thm-pe-wc-cover]
are ind-étale. This theorem bridges the two: it is the reason a site defined by weakly étale
morphisms can be computed with inverse limits of étale affines.

(SHEAF DAG node `sk-thm-pe-indetale-refinement`; machine-alignment layer.) Split from [theorem-pro-etale-refinements-weakly-etale--1]. DAG kind: statement. DAG status: imported. Statement dependencies not drawn: `sk-thm-pe-wc-cover`.
