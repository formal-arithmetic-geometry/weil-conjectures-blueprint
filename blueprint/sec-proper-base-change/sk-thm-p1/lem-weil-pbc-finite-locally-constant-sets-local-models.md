+++
id = "lem-weil-pbc-finite-locally-constant-sets-local-models"
kind = "lemma"
title = "Finite locally constant sheaves admit finite constant local models"
uses = ["def-pc-scheme", "def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.finiteLocallyConstant_exists_local_models"]
source = "literature/stacks-project/etale-cohomology.tex, Tag 03RV, converse descent part"
+++
Let T be a scheme [def-pc-scheme] and E a sheaf of sets `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)) on its small etale site [def-weil-pbc-etale-site]. If E is constant `CategoryTheory.constantSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/ConstantSheaf.lean)) on the members of some etale cover and all its separably closed geometric stalks are finite, there is an etale cover on every member U of which the restriction of E is isomorphic to a constant sheaf of some finite set S. The sets S may have different sizes and may lie in the next universe.
