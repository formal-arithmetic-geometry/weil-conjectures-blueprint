+++
id = "dag-lem-pe-coefficient-tor-flat-model"
kind = "dag-lemma"
title = "Bounded flat criterion for coefficient-model Tor tests"
name_showing = false
order = 152502
tags = ["sheaf-dag"]
split_from = "corollary-finite-tor-amplitude-under-comparison--1"
dag_id = "lem-pe-coefficient-tor-flat-model"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.coefficientModelTensorTest", "CategoryTheory.exists_coefficientModelFlatKFlatRepresentative", "CategoryTheory.coefficientModelTensorTest_iso", "CategoryTheory.coefficientModelTorAmplitude_iff_flatModel"]
+++
For a small site (C,J) in universe w, a commutative ring sheaf R with modules in the same universe, K in its standard derived localization, and integers a <= b, the coefficient-model Tor test in [a,b] holds if and only if there is a complex P with flat terms, zero below a and above b, and Q(P) isomorphic to K. The predicate is HasCoefficientModelTorAmplitude and the flatness predicate is SheafOfModules.IsFlat.

(SHEAF DAG node `lem-pe-coefficient-tor-flat-model`; machine-alignment layer.) Split from [corollary-finite-tor-amplitude-under-comparison--1]. DAG kind: statement. Placed through `det-pe-finite-tor-comparison-noetherian` (ancestor-1). DAG status: split. Lean names not on master: `CategoryTheory.exists_coefficientModelKFlatRepresentative`. Statement dependencies not drawn: `def-weil-abstract-derived-category`, `def-pc-flat-sheaf-modules`, `def-weil-proetale-tor-amplitude`.
