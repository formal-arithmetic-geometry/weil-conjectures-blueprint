+++
id = "lem-weil-pbc-flat-ses-kernel-flat"
kind = "lemma"
title = "The kernel of a surjection of flat modules is flat"
lean = ["Module.Flat.of_exact_of_flat_of_flat_right"]
+++
Let $R$ be a commutative ring and $0\to M'\xrightarrow{u}M\xrightarrow{v}M''\to0$ a short exact sequence `CategoryTheory.ShortComplex.Exact` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Homology/ShortComplex/Exact.lean)) of $R$-modules. If $M$ and $M''$ are flat `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)), then $M'$ is flat.
