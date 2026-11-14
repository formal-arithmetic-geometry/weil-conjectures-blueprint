+++
id = "dag-det-pe-milnor-epimorphic"
kind = "dag-lemma"
title = "Towers with epimorphic transitions have no derived limit terms"
name_showing = false
order = 91501
tags = ["sheaf-dag"]
split_from = "proposition-milnor-sequence--3"
dag_id = "det-pe-milnor-epimorphic"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.milnorLimitProjection", "AlgebraicGeometry.ProEtale.milnorLimitComparison_condition", "AlgebraicGeometry.ProEtale.milnorLimitComparison", "AlgebraicGeometry.ProEtale.milnor_epimorphic"]
uses = ["dag-def-weil-pbc-proetale-site"]
+++
Let $X$ be a scheme `def-pc-scheme`, with small pro-étale site $X_{\mathrm{proét}}$
[dag-def-weil-pbc-proetale-site], and let $\mathcal R$ be a sheaf of rings on this site.
Let $(M_n,t_n)_{n\geq0}$ be a tower of sheaves of $\mathcal R$-modules
`def-weil-sheaf-of-modules-category`, with epimorphic transition maps
$t_n\colon M_{n+1}\to M_n$. Put $P=\prod_{n\geq0}M_n$ and let $T\colon P\to P$
be the morphism whose $n$th coordinate is $t_n$ composed with the $(n+1)$st projection.
Use the convention $R\varprojlim_nM_n=\operatorname{Cone}(1-T)[-1]$ of
`det-pe-milnor-sequence`, and $R^p\varprojlim_nM_n=H^p(R\varprojlim_nM_n)$.
Write $D(X_{\mathrm{proét}},\mathcal R)$ for the derived category of these module
sheaves `def-weil-abstract-derived-category`. Then $1-T\colon P\to P$ is an epimorphism,
$R^1\varprojlim_nM_n=0$, and the canonical map from the ordinary inverse limit [dag-def-pur-sheaf-inverse-limit]
$\varprojlim_nM_n[0]\to R\varprojlim_nM_n$ is an isomorphism in
$D(X_{\mathrm{proét}},\mathcal R)$.

(SHEAF DAG node `det-pe-milnor-epimorphic`; machine-alignment layer.) Split from [proposition-milnor-sequence--3]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-pc-scheme`, `def-pe-milnor-towers`, `def-pur-sheaf-inverse-limit`, `def-weil-abstract-derived-category`, `def-weil-sheaf-of-modules-category`, `def-weil-tower-transition-endomorphism`, `det-pe-milnor-sequence`.
