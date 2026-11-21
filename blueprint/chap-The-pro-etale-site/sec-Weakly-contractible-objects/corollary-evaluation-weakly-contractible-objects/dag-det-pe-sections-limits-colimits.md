+++
id = "dag-det-pe-sections-limits-colimits"
kind = "dag-lemma"
title = "Evaluation on a weakly contractible affine preserves limits and colimits of modules"
name_showing = false
order = 79501
tags = ["sheaf-dag"]
split_from = "corollary-evaluation-weakly-contractible-objects--4"
dag_id = "det-pe-sections-limits-colimits"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.peSectionsLimitsColimits"]
uses = ["dag-def-weil-pbc-small-proetale-site", "dag-sk-def-pe-weak-contractible"]
+++
Let $\mathcal R$ be a sheaf of rings on $X_{\mathrm{proét}}$ and let $W$ be an affine
weakly contractible object. Then $\Gamma(W,-)$ from $\mathcal R$-modules to
$\mathcal R(W)$-modules preserves all limits and all colimits. In particular, for every
family $(M_i)_{i\in I}$ the map $\bigoplus_iM_i(W)\to(\bigoplus_iM_i)(W)$ is an
isomorphism, and $\Gamma(W,-)$ commutes with filtered colimits.

(SHEAF DAG node `det-pe-sections-limits-colimits`; machine-alignment layer.) Split from [corollary-evaluation-weakly-contractible-objects--4]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-pc-scheme`, `def-weil-pbc-category-colimit`, `def-weil-sheaf-of-modules-category`, `def-weil-size-convention`.
