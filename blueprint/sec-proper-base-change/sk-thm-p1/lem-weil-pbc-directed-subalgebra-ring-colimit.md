+++
id = "lem-weil-pbc-directed-subalgebra-ring-colimit"
kind = "lemma"
title = "A directed union of integer subalgebras is a categorical ring colimit"
lean = ["CommRingCat.isColimitSubalgebraCocone"]
source = "literature/stacks-project/algebra.tex, Tag 033C (lemma-normal-goes-up), third paragraph; details of the normalization and directed-union construction"
+++
Let R be a commutative ring and P a predicate on its Z-subalgebras. Assume the partial order I={A : Subalgebra Z R | P A} is nonempty and directed, and the supremum of its subalgebras is top. Let F:I to CommRing have object A and transition maps the inclusions, and let the inclusions into R define a cocone `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)). Then this cocone is colimiting. This is the already proved source theorem CommRingCat.isColimitSubalgebraCocone.
