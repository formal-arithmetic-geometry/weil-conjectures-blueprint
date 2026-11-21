+++
id = "dag-lem-pe-coefficient-comparison-affine-sections"
kind = "dag-lemma"
title = "Affine derived sections of coefficient-sized intrinsic comparison on injectives"
name_showing = false
order = 149508
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-pe-coefficient-comparison-affine-sections"
dag_kind = "lemma"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.coefficientComparison_affineSections_vanishing"]
uses = ["dag-lem-pe-coefficient-comparison-data"]
+++
Let X be a scheme in universe u, and A a commutative ring in max(v,u+1). Use the canonical constant-ring module pullback on the coefficient-sized etale and pro-etale site models of [dag-lem-pe-coefficient-comparison-data]. Assume the ordinary additive sheafification instances on the two model sites and enough injectives on the pro-etale module category, so that the displayed derived evaluation is defined. For an injective etale constant-ring module I, an affine etale object W over X, and each natural number q, the (q+1)-st right derived functor of evaluation of the underlying abelian sheaf at the pro-etale image of W is zero on the comparison pullback of I. W is transported to the models by AsSmall.up and the recorded inclusion. This is local derived sections on a single affine etale object, not a higher-direct-image sheaf. No finiteness, torsion, qcqs or nonempty-scheme assumption is made.

(SHEAF DAG node `lem-pe-coefficient-comparison-affine-sections`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: lemma. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-sp-injective-resolutions`.
