+++
kind = "proof"
of = "lem-weil-pbc-charpoly-locally-free-direct-sum-identity"
+++
Apply the characterizing property after scalar extension to every product localization, use the free direct-sum characteristic-polynomial identity, and descend coefficientwise by localization injectivity. (`LinearMap.charpoly_prodMap` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/Charpoly/ToMatrix.lean)), `Module.eq_zero_of_isLocalized_span` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/LocalProperties/Submodule.lean))).
