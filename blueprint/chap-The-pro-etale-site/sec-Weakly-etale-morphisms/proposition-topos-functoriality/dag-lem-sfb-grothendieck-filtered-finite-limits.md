+++
id = "dag-lem-sfb-grothendieck-filtered-finite-limits"
kind = "dag-lemma"
title = "Limits, colimits, and left exact filtered colimits in Grothendieck abelian categories"
name_showing = false
order = 39506
tags = ["sheaf-dag"]
split_from = "proposition-topos-functoriality--2"
dag_id = "lem-sfb-grothendieck-filtered-finite-limits"
dag_kind = "statement"
dag_status = "mathlib"
serial = false
+++
Fix a universe $\mathcal V$ and a Grothendieck abelian category $\mathcal A$ `def-sp-grothendieck-abelian` relative to $\mathcal V$, with $\mathcal V$-small morphism sets. Then $\mathcal A$ has all $\mathcal V$-small limits and colimits. For every $\mathcal V$-small filtered category $I$ `def-weil-pbc-category-colimit`, the colimit functor
$$
\operatorname{colim}_I:\operatorname{Fun}(I,\mathcal A)\to\mathcal A
$$
preserves finite limits `def-galois-finite-limits-colimits`. In particular, for a finite category $J$ and $M:I\times J\to\mathcal A$, the canonical comparison $\operatorname{colim}_i\operatorname{lim}_j M(i,j)\to\operatorname{lim}_j\operatorname{colim}_i M(i,j)$ is an isomorphism.

(SHEAF DAG node `lem-sfb-grothendieck-filtered-finite-limits`; machine-alignment layer.) Split from [proposition-topos-functoriality--2]. DAG kind: statement. Placed through `lem-sfb-finite-upper-star-exact` (ancestor-1). DAG status: mathlib. Statement dependencies not drawn: `def-sp-grothendieck-abelian`, `def-weil-pbc-category-colimit`, `def-galois-finite-limits-colimits`.
