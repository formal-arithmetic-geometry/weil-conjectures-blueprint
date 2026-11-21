+++
id = "dag-def-pur-twist-sheaves"
kind = "dag-definition"
title = "Concrete root-limit and scalar-tensor Tate sheaves"
name_showing = false
order = 184513
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "def-pur-twist-sheaves"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.purTwistZlOne", "AlgebraicGeometry.Scheme.purTwistForgetPreservesSheafification", "AlgebraicGeometry.Scheme.purTwistFiniteRingIso", "AlgebraicGeometry.Scheme.purTwistRootsModule", "AlgebraicGeometry.Scheme.purTwistZlAction_existsUnique", "AlgebraicGeometry.Scheme.purTwistZlAction", "AlgebraicGeometry.Scheme.purTwistZlAction_restriction", "AlgebraicGeometry.Scheme.purTwistZlModule", "AlgebraicGeometry.Scheme.purTwistIntegralOne", "AlgebraicGeometry.Scheme.purTwistIntegralTensor", "AlgebraicGeometry.Scheme.purTwistIntegralAction_existsUnique", "AlgebraicGeometry.Scheme.purTwistIntegralAction", "AlgebraicGeometry.Scheme.purTwistIntegralAction_restriction", "AlgebraicGeometry.Scheme.purTwistIntegralModule", "AlgebraicGeometry.Scheme.purTwistFiniteOne"]
uses = ["dag-def-pur-roots-of-unity-sheaf", "dag-def-pur-twist-coefficient-rings"]
+++
For a scheme S and prime l, construct the inverse limit of the root sheaves, its uniquely specified completed Z_l action, the discrete integral coefficient tensor with its uniquely specified completed action, and its ordinary positive-level finite coefficient reductions. All fifteen declarations are the unchanged constructions formerly owned by lem-pur-twist-sheaf-locally-free. Coefficient sheaves and their scalar maps are those of [dag-def-pur-twist-coefficient-rings]; the underlying root sheaves are [dag-def-pur-roots-of-unity-sheaf].

def purTwistZlOne

(SHEAF DAG node `def-pur-twist-sheaves`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: definition. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `lem-weil-l-adic-extension-integers-dvr`.
