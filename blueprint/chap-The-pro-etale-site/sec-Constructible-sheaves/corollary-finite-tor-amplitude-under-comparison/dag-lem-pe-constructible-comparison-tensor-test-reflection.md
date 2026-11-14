+++
id = "dag-lem-pe-constructible-comparison-tensor-test-reflection"
kind = "dag-lemma"
title = "Reflection of a single comparison tensor test"
name_showing = false
order = 152505
tags = ["sheaf-dag"]
split_from = "corollary-finite-tor-amplitude-under-comparison--1"
dag_id = "lem-pe-constructible-comparison-tensor-test-reflection"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.constructibleComparisonTensorTest_reflects_zero"]
uses = ["dag-sk-thm-pe-constructible-comparison", "dag-lem-pe-coefficient-tor-flat-model"]
+++
Let X be a scheme and A a discrete commutative ring in max(v,u+1). Let P be any cochain complex of modules over the constant ring on the coefficient-sized etale site, M any module sheaf on that site, and q any integer. If degree-q homology of the ordinary total tensor of the termwise canonical comparison inverse image of P with the degree-zero canonical inverse image of M vanishes, then degree-q homology of the ordinary total tensor of P with M in degree zero vanishes. No K-flatness, constructibility, boundedness or Noetherian hypothesis is needed.

(SHEAF DAG node `lem-pe-constructible-comparison-tensor-test-reflection`; machine-alignment layer.) Split from [corollary-finite-tor-amplitude-under-comparison--1]. DAG kind: statement. Placed through `det-pe-finite-tor-comparison-noetherian` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-pc-tensor-complex-sheaves`.
