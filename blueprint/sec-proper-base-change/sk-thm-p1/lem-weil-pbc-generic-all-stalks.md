+++
id = "lem-weil-pbc-generic-all-stalks"
kind = "lemma"
title = "Propagation of generic vanishing to all geometric stalks"
uses = ["def-constructible-locally-constant", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks"]
lean = ["AlgebraicGeometry.Scheme.all_sheafFiber_map_eq_zero_of_generic"]
+++
Let X be an irreducible scheme with generic point eta `IsGenericPoint` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Topology/Sober.lean)), and Lambda a commutative ring. For module sheaves F and G on the small etale site [def-weil-pbc-etale-site], with G locally constant [def-constructible-locally-constant], let phi:F to G have zero geometric stalk map at every separably closed geometric point over eta [def-weil-pbc-geometric-stalks]. Then its map at every geometric stalk is zero, without any finiteness assumptions.
