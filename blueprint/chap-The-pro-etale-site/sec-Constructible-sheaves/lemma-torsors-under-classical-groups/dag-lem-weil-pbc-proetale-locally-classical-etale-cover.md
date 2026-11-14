+++
id = "dag-lem-weil-pbc-proetale-locally-classical-etale-cover"
kind = "dag-lemma"
title = "Locally constant pro-etale sheaves admit etale sections"
name_showing = false
order = 143505
tags = ["sheaf-dag"]
split_from = "lemma-torsors-under-classical-groups--1"
dag_id = "lem-weil-pbc-proetale-locally-classical-etale-cover"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.proEtale_locallyClassical_etaleCover", "AlgebraicGeometry.Scheme.proEtaleSetRestriction", "AlgebraicGeometry.Scheme.IsProEtaleClassical", "AlgebraicGeometry.Scheme.IsProEtaleLocallyClassical", "AlgebraicGeometry.Scheme.IsProEtaleLocallyConstant"]
uses = ["dag-def-weil-pbc-constant-sheaf", "dag-def-weil-pbc-proetale-site"]
+++
Let $X$ be a scheme `def-pc-scheme` and let $\nu_X:X_{\mathrm{proet}}\to X_{\mathrm{et}}$ be the comparison morphism [def-weil-pbc-proetale-site, def-weil-pbc-etale-site, def-weil-pbc-site-comparison-morphism]. A sheaf of sets $F$ on $X_{\mathrm{proet}}$ is called classical if $F\cong\nu_X^*G$ for a sheaf of sets $G$ on $X_{\mathrm{et}}$, and locally classical if there is a pro-etale covering family $\{U_j\to X\}_j$ such that $F|_{U_j}\cong\nu_{U_j}^*G_j$ for etale sheaves of sets $G_j$. Every locally classical $F$ is classical. In particular this holds for every locally constant sheaf of sets, meaning one that becomes a constant sheaf $\underline{S_j}$ on each member of a pro-etale covering, where constant sheaf means sheafification of the constant presheaf [dag-def-weil-pbc-constant-sheaf]. If a locally classical $F$ has sections on every member of some pro-etale covering family of $X$, then there is an etale covering family $\{Y_i\to X\}_i$ with $F(Y_i)\ne\varnothing$ for every $i$.

(SHEAF DAG node `lem-weil-pbc-proetale-locally-classical-etale-cover`; machine-alignment layer.) Split from [lemma-torsors-under-classical-groups--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-pc-scheme`, `def-weil-pbc-etale-site`.
