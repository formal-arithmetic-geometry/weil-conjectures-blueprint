+++
id = "dag-sk-def-pe-classical-definition"
kind = "dag-definition"
title = "Classical pro-étale sheaves"
name_showing = false
order = 111504
tags = ["sheaf-dag"]
split_from = "definition-classical-pro-etale-sheaves--1"
dag_id = "sk-def-pe-classical-definition"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.IsClassicalModuleSheaf", "AlgebraicGeometry.ProEtale.IsClassicalModuleComplex"]
uses = ["dag-def-weil-pbc-constant-sheaf"]
+++
Let $X$ be a scheme and let $X_{\Proet}$ be its small pro-étale site
`sk-def-pe-site`. Let $\Lambda$ be a discrete commutative ring and let
$\Lambda_X$ be its constant sheaf of rings [dag-def-weil-pbc-constant-sheaf].

For a sheaf of sets $F$ on $X_{\Proet}$ and each pro-étale affine presentation
$U\cong\varprojlim_{i\in I}U_i$ as defined in
[dag-det-pe-classical-definition-continuity-map], write
$$
c_{F,U}\colon\varinjlim_{i\in I^{\mathrm{op}}}F(U_i)\longrightarrow F(U)
$$
for the canonical map induced by restriction along the projections $U\to U_i$.
Here $I$ is a small cofiltered category, the $U_i$ are affine and étale over
$X$, and the limit and transition morphisms are over $X$; the colimit is over
the corresponding filtered diagram of sections.

The sheaf $F$ is *classical* if $c_{F,U}$ is bijective for every such
presentation. For a sheaf of $\Lambda_X$-modules
`def-weil-sheaf-of-modules-category`, the colimit and canonical map are taken
in $\Lambda$-modules, and *classical* means that each $c_{F,U}$ is an
isomorphism of $\Lambda$-modules. A cochain complex $K$ of $\Lambda_X$-module
sheaves is *classical* if every cohomology sheaf $H^q(K)$, $q\in\mathbf Z$, is
classical, with cohomology taken in the abelian category of module sheaves
`def-weil-abstract-derived-category`.

(SHEAF DAG node `sk-def-pe-classical-definition`; machine-alignment layer.) Split from [definition-classical-pro-etale-sheaves--1]. DAG kind: definition. DAG status: split. Lean names not on master: `AlgebraicGeometry.ProEtale.IsClassicalModuleCochainComplex`. Statement dependencies not drawn: `def-weil-abstract-derived-category`, `def-weil-sheaf-of-modules-category`, `sk-def-pe-site`.
