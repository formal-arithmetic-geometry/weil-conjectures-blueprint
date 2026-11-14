+++
id = "dag-sk-def-pe-replete"
kind = "dag-definition"
title = "Repleteness"
name_showing = false
order = 84502
tags = ["sheaf-dag"]
split_from = "definition-repleteness--1"
dag_id = "sk-def-pe-replete"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.GrothendieckTopology.IsReplete"]
uses = ["dag-det-pe-replete-definition"]
+++
A topos $\mathcal T$ is *replete* if, for every inverse sequence
$\cdots\to F_2\to F_1\to F_0$ of sheaves of sets with epimorphic transition maps, the
projection $\varprojlim_nF_n\to F_m$ is an epimorphism for every $m$.

The inverse sequences, their limits and projections, and epimorphisms of sheaves
are those of [dag-det-pe-replete-definition].

(SHEAF DAG node `sk-def-pe-replete`; machine-alignment layer.) Split from [definition-repleteness--1]. DAG kind: definition. DAG status: split.
