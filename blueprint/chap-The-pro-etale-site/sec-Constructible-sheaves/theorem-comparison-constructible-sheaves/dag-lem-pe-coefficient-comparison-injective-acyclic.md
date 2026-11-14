+++
id = "dag-lem-pe-coefficient-comparison-injective-acyclic"
kind = "dag-lemma"
title = "Injective unit and acyclicity for coefficient-sized intrinsic comparison"
name_showing = false
order = 149517
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-pe-coefficient-comparison-injective-acyclic"
dag_kind = "lemma"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.coefficientComparison_injectiveAcyclic"]
uses = ["dag-lem-pe-coefficient-comparison-data"]
+++
Let X be a scheme in universe u and A a commutative ring in max(v,u+1). Use the canonical constant-ring intrinsic module adjunction from [dag-lem-pe-coefficient-comparison-data] on the coefficient-sized small site models. Specify the ordinary additive sheafification instances on both small sites, the enough-injectives instance on the target module category, and the additive structure of direct image R. These instances exist canonically and only determine the ordinary derived-functor constructions. For any adjunction between these fixed functors and every injective etale module I, the unit I -> R(L(I)) is invertible and L(I) is R-acyclic: each positive right-derived direct image vanishes. No finiteness, torsion, constructibility or qcqs assumption is made.

(SHEAF DAG node `lem-pe-coefficient-comparison-injective-acyclic`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: lemma. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split.
