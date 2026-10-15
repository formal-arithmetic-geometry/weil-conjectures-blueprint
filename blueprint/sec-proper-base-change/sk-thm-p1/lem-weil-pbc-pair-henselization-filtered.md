+++
id = "lem-weil-pbc-pair-henselization-filtered"
kind = "lemma"
title = "Filteredness of the pair henselization category"
lean = ["RingTheory.pair_henselization_filtered"]
+++
For a commutative ring B and ideal J, let C be the full category of ring maps B to D with Spec(D) to Spec(B) etale `AlgebraicGeometry.Etale` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Etale.lean)) and the canonical map B/J to D/JD bijective, with all B-algebra maps as morphisms. Then C is filtered: it is nonempty, any two objects admit a common successor, and every pair of parallel maps is coequalized.
