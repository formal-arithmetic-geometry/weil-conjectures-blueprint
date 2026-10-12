+++
kind = "proof"
of = "def-weil-pbc-tensor-bicomplex"
+++
Apply HomologicalComplex₂.ofGradedObject to the displayed terms and differentials. Tensor functoriality and the chain-complex identities prove the square-zero, shape and commuting-square conditions. Use homMk for the termwise map, and mapHomologicalComplex followed by NatTrans.mapHomologicalComplex for chainTensorMap. (`CategoryTheory.Functor.mapHomologicalComplex` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Homology/Additive.lean)), `TensorProduct` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/TensorProduct/Defs.lean))).
