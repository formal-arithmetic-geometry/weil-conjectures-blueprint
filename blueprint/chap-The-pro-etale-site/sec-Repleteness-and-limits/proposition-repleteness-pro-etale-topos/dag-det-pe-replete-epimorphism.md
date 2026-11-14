+++
id = "dag-det-pe-replete-epimorphism"
kind = "dag-lemma"
title = "The pro-étale topos is replete"
name_showing = false
order = 85501
tags = ["sheaf-dag"]
split_from = "proposition-repleteness-pro-etale-topos--1"
dag_id = "det-pe-replete-epimorphism"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.isReplete_proEtale"]
uses = ["dag-det-pe-replete-definition"]
+++
For every scheme $X$ and every inverse sequence $(F_n,t_n)$ of sheaves of sets on
$X_{\mathrm{proét}}$ with epimorphic transition maps, each projection
$p_m\colon\varprojlim_nF_n\to F_m$ is an epimorphism. Thus $\Sh(X_{\mathrm{proét}})$ is
replete in the sense of [dag-det-pe-replete-definition].

(SHEAF DAG node `det-pe-replete-epimorphism`; machine-alignment layer.) Split from [proposition-repleteness-pro-etale-topos--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `sk-def-pe-site`.
