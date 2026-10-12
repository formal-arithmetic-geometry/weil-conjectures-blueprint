+++
id = "lem-weil-pbc-coefficient-residue-section"
kind = "lemma"
title = "A section of the characteristic-zero residue map"
lean = ["IsLocalRing.exists_residue_section"]
source = "literature/stacks-project/algebra.tex, Algebra, Theorem Tag 032A(1), first proof paragraph, using Proposition Tag 0322"
+++
Let R be a commutative local ring, complete for its maximal ideal m `IsAdicComplete` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean)). If its residue field has characteristic zero, then there is a ring homomorphism f: R/m -> R with residue_R composed with f equal to the identity of R/m.
