+++
id = "def-weil-pbc-tensor-bicomplex"
kind = "definition"
title = "The unsigned tensor bicomplex and its maps"
lean = ["HomologicalComplex₂.tensorBicomplex"]
+++
Let R be a commutative ring and P,Q be N-indexed chain complexes of R-modules `CategoryTheory.Functor.mapHomologicalComplex` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Homology/Additive.lean)). Define A(P,Q) `TensorProduct` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/LinearAlgebra/TensorProduct/Defs.lean)) by A(p,q)=P_p tensor_R Q_q, horizontal differential d_P tensor 1 and vertical differential 1 tensor d_Q. The differentials square to zero and commute. For chain maps a:P→P' and b:Q→Q', define A(a,b) termwise by a_p tensor b_q. Also define chainTensorMap(a,g) for a module map g:N→N' as the chain map P tensor N→P' tensor N' with components a_p tensor g.
