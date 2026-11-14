+++
id = "dag-lem-cbc-abelian-comparison-injective-acyclicity"
kind = "dag-lemma"
title = "Comparison inverse images of injective abelian sheaves are direct-image acyclic"
name_showing = false
order = 120501
tags = ["sheaf-dag"]
split_from = "lemma-acyclicity-pulled-back-injectives--1"
dag_id = "lem-cbc-abelian-comparison-injective-acyclicity"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.rightAcyclic_comparisonUpperStar_obj_of_injective"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $X$ be any scheme `def-pc-scheme`, with small sites [def-weil-pbc-etale-site, def-weil-pbc-proetale-site] and comparison geometric morphism $\nu_X:X_{\mathrm{proet}}\to X_{\mathrm{et}}$ `def-weil-pbc-site-comparison-morphism`. Use its inverse image and direct image on abelian sheaves `def-weil-pbc-sites-and-cohomology`. For every injective abelian sheaf $I$ on $X_{\mathrm{et}}$ `def-sp-injective-resolutions`, the abelian sheaf $\nu_X^{-1}I$ is acyclic for $\nu_{X,*}$, meaning $$R^q\nu_{X,*}(\nu_X^{-1}I)=0\qquad(q>0).$$ Here $R^q\nu_{X,*}$ is computed by an injective resolution in abelian pro-etale sheaves and degree-$q$ cohomology of its direct-image complex `def-sp-left-exact-additive`. No affineness, torsion, constructibility or finite coefficient ring hypothesis is imposed.

(SHEAF DAG node `lem-cbc-abelian-comparison-injective-acyclicity`; machine-alignment layer.) Split from [lemma-acyclicity-pulled-back-injectives--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-pc-scheme`, `def-sp-acyclic`, `def-sp-injective-resolutions`, `def-sp-left-exact-additive`, `def-weil-pbc-etale-site`, `lem-coef-grothendieck-locally-presentable`, `lem-sfb-proetale-sheaves-grothendieck`, `sk-def-groth-ss`.
