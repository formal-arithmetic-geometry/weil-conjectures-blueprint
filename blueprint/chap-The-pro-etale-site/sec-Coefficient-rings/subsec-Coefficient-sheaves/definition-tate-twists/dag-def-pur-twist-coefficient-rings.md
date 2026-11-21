+++
id = "dag-def-pur-twist-coefficient-rings"
kind = "dag-definition"
title = "The canonical discrete and completed scalar square of the Tate twist"
name_showing = false
order = 184512
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "def-pur-twist-coefficient-rings"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.purTwistRing", "AlgebraicGeometry.Scheme.purTwistFiniteRing", "AlgebraicGeometry.Scheme.purTwistZlConstant", "AlgebraicGeometry.Scheme.purTwistFiniteTransition", "AlgebraicGeometry.Scheme.purTwistZlTower", "AlgebraicGeometry.Scheme.purTwistZlCompletion", "AlgebraicGeometry.Scheme.purTwistZlProjection", "AlgebraicGeometry.Scheme.purTwistZlReduction", "AlgebraicGeometry.Scheme.purTwistZlCompletionMap_existsUnique", "AlgebraicGeometry.Scheme.purTwistZlCompletionMap", "AlgebraicGeometry.Scheme.purTwistIntegersMap_existsUnique", "AlgebraicGeometry.Scheme.purTwistIntegersMap", "AlgebraicGeometry.Scheme.purTwistIntegralConstant", "AlgebraicGeometry.Scheme.purTwistConstantIntegersMap", "AlgebraicGeometry.Scheme.purTwistIntegralQuotient", "AlgebraicGeometry.Scheme.purTwistIntegralCompletionMap_existsUnique", "AlgebraicGeometry.Scheme.purTwistIntegralCompletionMap", "AlgebraicGeometry.Scheme.IsPurTwistCompletedScalarMap", "AlgebraicGeometry.Scheme.purTwistCompletedScalarMap_existsUnique", "AlgebraicGeometry.Scheme.purTwistCompletedScalarMap", "AlgebraicGeometry.Scheme.purTwistCoefficientSquare", "AlgebraicGeometry.Scheme.purTwistCoefficientComparison", "AlgebraicGeometry.Scheme.purTwistRingOfUniverses", "AlgebraicGeometry.Scheme.purTwistFiniteRingOfUniverses", "AlgebraicGeometry.Scheme.purTwistZlConstantOfUniverses", "AlgebraicGeometry.Scheme.purTwistFiniteTransitionOfUniverses", "AlgebraicGeometry.Scheme.purTwistZlTowerOfUniverses", "AlgebraicGeometry.Scheme.purTwistZlCompletionOfUniverses", "AlgebraicGeometry.Scheme.purTwistZlProjectionOfUniverses", "AlgebraicGeometry.Scheme.purTwistZlReductionOfUniverses", "AlgebraicGeometry.Scheme.purTwistZlCompletionMap_existsUniqueOfUniverses", "AlgebraicGeometry.Scheme.purTwistZlCompletionMapOfUniverses"]
uses = ["dag-def-weil-pbc-constant-sheaf"]
+++
For a scheme S, a prime l and a finite extension E of Q_l `def-weil-l-adic-numbers`, let A=(Z_l)_S and B=(O_E)_S be constant commutative ring sheaves [dag-def-weil-pbc-constant-sheaf]. Let R=lim_r (Z/l^(r+1))_S and T=lim_n (O_E/(pi^(n+1)))_S `def-weil-completed-integral-coefficients`. Use the literal quotient maps as tower transitions. The maps A→R and B→T are the unique limit lifts of the quotient cones. The map Z_l→O_E is the unique map agreeing with the coefficient field inclusion, and induces A→B. The map R→T is uniquely characterized after every finite projection by a finite Z/l^r factorization of Z_l→O_E/(pi^n). These maps form a commutative square. Its comparison is the canonical morphism from the pushout of A→R and A→B to T. All of these are the unchanged named constructions extracted from the parent module; no assertion of invertibility or local freeness is included.

def purTwistCoefficientComparison

(SHEAF DAG node `def-pur-twist-coefficient-rings`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: definition. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Lean names not on master: `AlgebraicGeometry.Scheme.purTwistAbLocallyBijective`. Statement dependencies not drawn: `def-weil-l-adic-numbers`, `lem-weil-l-adic-extension-integers-dvr`.
