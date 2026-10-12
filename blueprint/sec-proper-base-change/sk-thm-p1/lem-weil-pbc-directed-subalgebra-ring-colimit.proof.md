+++
kind = "proof"
of = "lem-weil-pbc-directed-subalgebra-ring-colimit"
+++
Use the partial order of integer subalgebras satisfying P as the index, with inclusions as transition maps and inclusions into R as a cocone. Nonempty directedness makes the category filtered by `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)).

For any cocone, its ring maps from stages can be regarded as Z-algebra maps. Apply Mathlib Subalgebra.iSupLift to the directed family and the compatible algebra maps. The supremum-top hypothesis identifies the domain with R. The iSupLift_inclusion formula proves factorization through each stage.

For uniqueness, every x in R lies in a stage, by the directed-supremum union formula and supremum top. Two candidate ring maps agree on that stage, hence on x. This proves the colimit universal property `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)). The adopted source declaration already implements this proof.
