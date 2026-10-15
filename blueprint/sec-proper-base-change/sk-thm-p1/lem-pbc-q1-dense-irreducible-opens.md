+++
id = "lem-pbc-q1-dense-irreducible-opens"
kind = "lemma"
title = "Dense disjoint irreducible opens inside a prescribed dense open"
uses = ["def-weil-pbc-curve-setting"]
lean = ["AlgebraicGeometry.IsCurve.exists_dense_irreducible_opens"]
+++
Let k be a field, f:X → Spec k a separated finite-type curve of dimension at most one [def-weil-pbc-curve-setting], and V a dense open. There are n and pairwise disjoint nonempty irreducible opens U_a inside V, indexed by Fin n, with dense union W, topological Krull dimension of X minus W at most zero `topologicalKrullDim` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Topology/KrullDimension.lean)), and every connected component in W of a point of W is irreducible. This includes X empty and n = 0.
