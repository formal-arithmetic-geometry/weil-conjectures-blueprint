+++
id = "lem-weil-pbc-isolated-fibre-point-residue-finite"
kind = "lemma"
title = "An isolated point of a fibre of a locally finite type morphism has finite residue field extension"
uses = ["def-pc-scheme", "def-weil-finite-type-morphism"]
lean = ["AlgebraicGeometry.Scheme.Hom.finiteDimensional_residueField_of_isOpen_singleton_asFiber"]
+++
Let $f:X\to S$ be a morphism of schemes [def-pc-scheme] which is locally of finite type [def-weil-finite-type-morphism], let $x\in X$, put $s=f(x)$, and let $X_s=X\times_S\operatorname{Spec}\kappa(s)$ be the fibre of $f$ at $s$ `AlgebraicGeometry.Scheme.Hom.fiber` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Fiber.lean)). If the point of $X_s$ corresponding to $x$ is isolated in $X_s$ (the singleton is open in $X_s$), then the field extension $\kappa(s)\to\kappa(x)$ induced by $f$ on residue fields `AlgebraicGeometry.Scheme.residueField` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/ResidueField.lean)) is finite, i.e. $\kappa(x)$ is a finite-dimensional $\kappa(s)$-vector space `Algebra` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Algebra/Defs.lean)).
