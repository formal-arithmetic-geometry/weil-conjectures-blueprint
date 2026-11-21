+++
id = "dag-lem-weil-pbc-derived-sections-pushforward"
kind = "dag-lemma"
title = "Derived global sections via comparison pushforward"
name_showing = false
order = 123504
tags = ["sheaf-dag"]
split_from = "theorem-bounded-below-cohomology-comparison--3"
dag_id = "lem-weil-pbc-derived-sections-pushforward"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.comparisonLowerStarCompRightDerivedGlobalSectionsIso"]
uses = ["dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
For a scheme $T$ and a finite ring $\Lambda$, let $\nu_T:T_{\Proet}\to T_{\Et}$ be the comparison morphism `def-weil-pbc-site-comparison-morphism`. For every bounded-below complex $J$ of $\Lambda$-module sheaves on $T_{\Proet}$ `def-weil-pbc-proetale-modules`, the canonical comparison induced by evaluation on the final object is a natural isomorphism
$$R\Gamma(T_{\Et},R\nu_{T,*}J)\cong R\Gamma(T_{\Proet},J),$$
where $R\Gamma(T_{\Et},-)$ and $R\Gamma(T_{\Proet},-)$ are the ordinary right-derived functors of sections at the terminal objects (the etale construction is `def-weil-pbc-etale-cohomology`).

(SHEAF DAG node `lem-weil-pbc-derived-sections-pushforward`; machine-alignment layer.) Split from [theorem-bounded-below-cohomology-comparison--3]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-kun-rgamma-unbounded`, `def-sfb-finite-derived-global-sections`, `def-weil-derived-direct-image`, `def-weil-pbc-etale-cohomology`, `lem-coef-grothendieck-locally-presentable`, `lem-pc-derived-category-locally-small`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-proetale-sheaves-grothendieck`, `lem-weil-pbc-sheaf-tensor-closed`, `pur7710-def-derived-sections`, `sk-def-sfb-finite-derived-functors`, `sk-def-sfb-module-derived-pushpull`.
