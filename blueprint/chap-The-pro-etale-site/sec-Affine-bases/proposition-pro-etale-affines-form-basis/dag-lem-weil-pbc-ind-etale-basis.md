+++
id = "dag-lem-weil-pbc-ind-etale-basis"
kind = "dag-lemma"
title = "The ind-etale subsite is a basis"
name_showing = false
order = 66501
tags = ["sheaf-dag"]
split_from = "proposition-pro-etale-affines-form-basis--1"
dag_id = "lem-weil-pbc-ind-etale-basis"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.AffineProEt.isCoverDense_toProEt", "AlgebraicGeometry.Scheme.AffineProEt.exists_finite_jointly_surjective_of_mem_topology", "AlgebraicGeometry.Scheme.AffineProEt.isPullback_left", "AlgebraicGeometry.Scheme.AffineProEt.sheafPushforward", "AlgebraicGeometry.Scheme.AffineProEt.isEquivalence_sheafPushforwardContinuous_toProEt"]
uses = ["dag-def-weil-pbc-ind-etale-algebra", "dag-def-weil-pbc-proetale-site", "dag-sk-def-pe-morphisms"]
+++
Every pro-etale object over an affine $X$ has a cover by objects of $\mathcal
B_X$. Every covering of a basis object has a refinement by a finite covering
of basis objects. Fibre products of basis objects over a basis object remain
in the basis. Restriction to this basis determines a sheaf and its morphisms
uniquely and detects isomorphisms of sheaves.

(SHEAF DAG node `lem-weil-pbc-ind-etale-basis`; machine-alignment layer.) Split from [proposition-pro-etale-affines-form-basis--1]. DAG kind: statement. DAG status: split. Lean names not on master: `AlgebraicGeometry.Scheme.AffineProEt.instHasPullbacks`. Statement dependencies not drawn: `def-weil-pbc-ind-etale-basis`, `lem-weil-pbc-flat-colimit-presentation-same-universe`.
