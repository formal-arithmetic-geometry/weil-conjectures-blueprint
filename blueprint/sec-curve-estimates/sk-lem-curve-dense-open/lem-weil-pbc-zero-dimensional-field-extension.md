+++
id = "lem-weil-pbc-zero-dimensional-field-extension"
kind = "lemma"
title = "Field extension in dimension zero"
lean = ["AlgebraicGeometry.IsCurve.bijective_cohomologyMap_of_topologicalKrullDim_le_zero"]
order = 1493
uses = ["def-weil-pbc-curve-setting", "def-weil-pbc-eight-curve-assertions", "lem-weil-pbc-zero-dimensional-cohomology", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $k\subset k'$ be algebraically closed fields, let $C$ be a separated
finite-type $k$-scheme of dimension at most zero, and let $F$ be a torsion
etale sheaf. The pullback map $\rho^q_{k'/k}(C,F)$ of the curve coefficient
pair [def-weil-pbc-curve-setting] is an isomorphism for every $q\geq0$.
