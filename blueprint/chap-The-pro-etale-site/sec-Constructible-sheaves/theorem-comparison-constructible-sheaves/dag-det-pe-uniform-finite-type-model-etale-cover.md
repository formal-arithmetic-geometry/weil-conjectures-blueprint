+++
id = "dag-det-pe-uniform-finite-type-model-etale-cover"
kind = "dag-lemma"
title = "Etale trivializations for a fixed finitely generated module model"
name_showing = false
order = 149503
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "det-pe-uniform-finite-type-model-etale-cover"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.etale_cover_of_proetale_uniform_finiteType_model"]
uses = ["dag-def-sfb-finite-upper-star", "dag-def-weil-pbc-constant-sheaf", "dag-def-weil-pbc-proetale-site", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $X$ be a scheme, $\Lambda$ a discrete commutative ring, $M$ a finitely generated $\Lambda$-module, and $F$ a sheaf of $\Lambda$-modules on the small pro-etale site. Suppose a pro-etale covering $\{W_i\to X\}$ identifies every scheme inverse image of $F$ with the constant module sheaf of the same $M$. Then an etale covering of $X$, indexed in the universe of $X$, has the same constant model $M$ on every member. No finiteness assumption on the underlying set of $\Lambda$ or $M$ is imposed. The sites are [dag-def-weil-pbc-proetale-site] and `def-weil-pbc-etale-site`, inverse images are `def-weil-proetale-inverse-image`, constants are [dag-def-weil-pbc-constant-sheaf], and module sheaves use `def-weil-sheaf-of-modules-category`.

(SHEAF DAG node `det-pe-uniform-finite-type-model-etale-cover`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: statement. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-pbc-etale-site`, `def-weil-sheaf-of-modules-category`, `lem-coef-grothendieck-locally-presentable`.
