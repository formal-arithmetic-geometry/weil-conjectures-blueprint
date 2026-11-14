+++
id = "dag-def-pur-signed-line-scalar-normalization-data"
kind = "dag-definition"
title = "Signed line powers and normalized scalar comparisons"
name_showing = false
order = 187513
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "def-pur-signed-line-scalar-normalization-data"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.signedLinePower", "SheafOfModules.SignedLineComparisonNormalized"]
+++
Let $(\mathcal C,J)$ be a site small relative to the coefficient universe, $R$ a commutative ring sheaf and $P$ an $R$-module sheaf `def-weil-sheaf-of-modules-category`. Using the powers of `def-sp-scalar-tensor-comparison-data`, define $P^{[n]}=P^{\otimes n}$ for $n\geq0$ and $P^{[-n]}=\mathcal Hom_R(P^{\otimes n},R)$ for $n>0$, using [dag-def-pur-sheaf-hom]. For $\alpha:R\to S$, an $S$-module $Q$, an isomorphism $b:S\otimes_RP\cong Q$ and a family $B_d:S\otimes_RP^{[d]}\cong Q^{[d]}$, SignedLineComparisonNormalized means: $B_0$ is the coefficient-unit map, $B_1=b$, positive powers obey the tensor recursion on every local pure tensor, and $B_{-n}$ is the canonical scalar-extension dual map of `def-sp-canonical-scalar-extension-maps` followed by precomposition with $B_n^{-1}$. This defines a predicate, without asserting existence of B.

(SHEAF DAG node `def-pur-signed-line-scalar-normalization-data`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: definition. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`, `sk-def-pbc-conventions`.
