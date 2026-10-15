+++
id = "def-weil-pbc-finite-local-model-compatible-transport"
kind = "definition"
title = "Natural section-compatible transport"
uses = ["def-pc-scheme", "def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.FiniteLocalModelCompatibleTransport"]
+++
For a scheme T [def-pc-scheme], a sheaf E `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)), an etale U over T [def-weil-pbc-etale-site], finite etale Q over U `CategoryTheory.MorphismProperty.Over, CategoryTheory.MorphismProperty.Over.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/MorphismProperty/Comma.lean)) and representation e of E restricted to U, a compatible natural transport consists of maps sending Q-points above a to Q-points above b for scheme maps a,b with equal composite to T. These maps commute with precomposition and send the point corresponding to a section s under e at a to the point corresponding to s at b on every etale source.
