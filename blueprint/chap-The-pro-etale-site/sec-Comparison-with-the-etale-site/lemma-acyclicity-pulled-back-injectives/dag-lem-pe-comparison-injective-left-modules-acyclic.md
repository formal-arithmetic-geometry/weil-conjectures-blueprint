+++
id = "dag-lem-pe-comparison-injective-left-modules-acyclic"
kind = "dag-lemma"
title = "Comparison pullbacks of injective left-module sheaves are acyclic for arbitrary rings"
name_showing = false
order = 120502
tags = ["sheaf-dag"]
split_from = "lemma-acyclicity-pulled-back-injectives--1"
dag_id = "lem-pe-comparison-injective-left-modules-acyclic"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.rightAcyclic_comparisonUpperStar_obj_of_injective"]
uses = ["dag-def-weil-pbc-constant-sheaf", "dag-def-weil-pbc-proetale-site", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $X$ be a scheme `def-pc-scheme` and $\Lambda$ a discrete associative unital ring, not assumed commutative, in the coefficient universe. Use the small étale and pro-étale sites [def-weil-pbc-etale-site, def-weil-pbc-proetale-site] in a common larger universe in which their underlying categories are small. A $\Lambda$-module sheaf means a sheaf of left $\Lambda$-modules; equivalently it is a sheaf of modules `def-weil-sheaf-of-modules-category` over the constant sheaf of rings, the sheafification of the constant ring presheaf [dag-def-weil-pbc-constant-sheaf]. Let $\nu_X:X_{\mathrm{proét}}\to X_{\mathrm{ét}}$ be the comparison geometric morphism `def-weil-pbc-site-comparison-morphism`. On module sheaves, $\nu_X^*$ applies its set inverse image to addition, zero, negation and each scalar endomorphism of the underlying abelian sheaf; $\nu_{X,*}$ is restriction to the étale subsite, with its induced scalar actions. Compute $R^q\nu_{X,*}$ by injective resolutions in these module categories [def-sp-left-exact-additive, def-sp-injective-resolutions]. Then for every injective left $\Lambda$-module sheaf $I$ on $X_{\mathrm{ét}}$ and every integer $q>0$,
$$
R^q\nu_{X,*}(\nu_X^*I)=0.
$$
No affineness, quasi-compactness, torsion or finite-ring hypothesis is imposed.

(SHEAF DAG node `lem-pe-comparison-injective-left-modules-acyclic`; machine-alignment layer.) Split from [lemma-acyclicity-pulled-back-injectives--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-pc-scheme`, `def-sp-acyclic`, `def-sp-injective-resolutions`, `def-sp-left-exact-additive`, `def-weil-pbc-etale-site`, `def-weil-sheaf-of-modules-category`, `lem-coef-grothendieck-locally-presentable`, `lem-sfb-proetale-sheaves-grothendieck`, `sk-def-groth-ss`.
