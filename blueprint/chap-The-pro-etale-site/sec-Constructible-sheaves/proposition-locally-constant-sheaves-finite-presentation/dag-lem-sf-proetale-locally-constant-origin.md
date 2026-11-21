+++
id = "dag-lem-sf-proetale-locally-constant-origin"
kind = "dag-lemma"
title = "Locally constant pro-etale sheaves with finite values are of etale origin"
name_showing = false
order = 146503
tags = ["sheaf-dag"]
split_from = "proposition-locally-constant-sheaves-finite-presentation--3"
dag_id = "lem-sf-proetale-locally-constant-origin"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.IsLisseProEtaleFixedModuleSheaf", "AlgebraicGeometry.Scheme.proEtale_lisse_origin"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $X$ be a scheme, let $\Lambda$ be a finite commutative ring, and let $\nu_X:X_{\mathrm{proet}}\to X_{\mathrm{et}}$ be the comparison morphism of sites `def-weil-pbc-site-comparison-morphism`, with inverse image $\nu_X^*$ on sheaves of $\Lambda$-modules. Call a sheaf of $\Lambda$-modules on the small etale site $X_{\mathrm{et}}$ `def-weil-pbc-etale-site` *lisse* if it is locally constant with finite stalks `def-weil-pbc-etale-sheaves`, and call a sheaf of $\Lambda_X$-modules on the small pro-etale site $X_{\mathrm{proet}}$ [dag-def-weil-pbc-proetale-site] *lisse* if it is locally constant `def-weil-proetale-locally-constant-sheaf` (there are a covering $\{U_j\to X\}$ in $X_{\mathrm{proet}}$ and $\Lambda$-modules $M_j$ with $\mathcal F|_{U_j}\cong\underline{M_j}_{U_j}$) and its stalk at every geometric point of $X$ `def-weil-proetale-geometric-stalk` is a finite $\Lambda$-module.

1. **(a)** If $G$ is a lisse sheaf of $\Lambda$-modules on $X_{\mathrm{et}}$, then $\nu_X^*G$ is a lisse sheaf of $\Lambda$-modules on $X_{\mathrm{proet}}$.
1. **(b)** If $\mathcal F$ is a lisse sheaf of $\Lambda$-modules on $X_{\mathrm{proet}}$, then there are a lisse sheaf $G$ of $\Lambda$-modules on $X_{\mathrm{et}}$ and an isomorphism $\nu_X^*G\cong\mathcal F$ of sheaves of $\Lambda$-modules.

(SHEAF DAG node `lem-sf-proetale-locally-constant-origin`; machine-alignment layer.) Split from [proposition-locally-constant-sheaves-finite-presentation--3]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-constructible-finite-locally-constant`, `def-weil-pbc-etale-site`, `def-weil-pbc-locally-constant-finite-type-modules`, `lem-coef-grothendieck-locally-presentable`.
