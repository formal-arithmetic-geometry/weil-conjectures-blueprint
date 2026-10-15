+++
id = "lem-weil-pbc-flat-fiber-prime-height"
kind = "lemma"
title = "Height formula expressed at a prime of the fibre ring"
lean = ["RingHom.height_eq_add_of_flat_fiber"]
+++
Let R and S be commutative Noetherian rings `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)), with a flat R-algebra structure `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)). Let p be a prime of R, C = p.Fiber S = kappa(p) tensor_R S, Q a prime of C, and q its inverse image under S -> C. Localizations and fibre rings are as in `Localization.AtPrime, Ideal.ResidueField, Ideal.Fiber` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Localization/AtPrime/Basic.lean)). Then height(q) = height(p) + height(Q). Height is the dimension of the prime localization `ringKrullDim` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/KrullDimension/Basic.lean)).
