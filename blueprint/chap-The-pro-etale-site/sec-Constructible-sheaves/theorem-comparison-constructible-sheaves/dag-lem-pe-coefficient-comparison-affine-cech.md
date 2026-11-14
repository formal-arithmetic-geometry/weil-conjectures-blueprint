+++
id = "dag-lem-pe-coefficient-comparison-affine-cech"
kind = "dag-lemma"
title = "Finite affine Cech vanishing for coefficient-sized intrinsic comparison"
name_showing = false
order = 149507
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-pe-coefficient-comparison-affine-cech"
dag_kind = "lemma"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.coefficientComparison_affineCech_vanishing"]
uses = ["dag-lem-pe-coefficient-comparison-data", "dag-sk-def-pe-morphisms"]
+++
Let X be a scheme in universe u and A any commutative ring in max(v,u+1), with additive sheafification on the coefficient-sized etale and pro-etale site models of [dag-lem-pe-coefficient-comparison-data]. Let I be injective in constant-A module sheaves on the etale model. Let V_a -> U be a finite covering in the precoverage associated to the pro-etale model topology, such that AsSmall.down(U) and every AsSmall.down(V_a) have proAffineEtale structure morphism to X [dag-sk-def-pe-morphisms]. For every choice S of the iterated fibre products and index maps of `def-weil-pbc-site-cech-complex` and every q >= 0, the (q+1)-st Cech cohomology of the underlying abelian presheaf of the intrinsic comparison pullback of I is zero. There is no enough-injectives assumption and no derived functor in this statement. The finite family may be empty; X need not be affine, qcqs, or nonempty; A need not be finite.

(SHEAF DAG node `lem-pe-coefficient-comparison-affine-cech`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: lemma. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-pbc-site-cech-complex`, `def-sp-injective-resolutions`.
