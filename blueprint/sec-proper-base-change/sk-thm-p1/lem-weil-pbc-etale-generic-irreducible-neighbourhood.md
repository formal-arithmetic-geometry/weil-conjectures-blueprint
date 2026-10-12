+++
id = "lem-weil-pbc-etale-generic-irreducible-neighbourhood"
kind = "lemma"
title = "Irreducible open neighbourhood above an etale generic point"
uses = ["def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Scheme.exists_irreducible_open_of_etale_generic"]
source = "Stacks Project, Tag 09BH, Proposition 59.74.1 (3), irreducible etale neighbourhood reduction; component isolation Tag 0BA8"
+++
Let X and Y be schemes [def-weil-pbc-scheme-conventions], X Noetherian, and f:Y to X etale `AlgebraicGeometry.Etale` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Etale.lean)). Let eta be a component generic point of X `IsGenericPoint` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Topology/Sober.lean)) and y a point of Y with f(y)=eta. There is an open W of Y containing y whose scheme is irreducible and for which y, viewed as a point of W, is generic for all of W. No quasi-compactness of Y and no reducedness of X or Y are assumed.
