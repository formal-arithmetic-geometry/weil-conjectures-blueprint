+++
id = "lem-weil-pbc-affine-etale-closed-immersion-lift"
kind = "lemma"
title = "Affine étale schemes lift across closed immersions into affine schemes"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.Etale.exists_affine_lift_of_closedImmersion"]
source = "literature/stacks-project/etale-cohomology.tex, Stacks Tag 09ZA, proof, first paragraph; https://stacks.math.columbia.edu/tag/09ZA"
+++
Let X, Z, V be schemes [def-pc-scheme], X and V affine, i : Z → X a closed immersion `AlgebraicGeometry.IsClosedImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/ClosedImmersion.lean)), and p : V → Z étale `AlgebraicGeometry.Etale` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Etale.lean)). There exists an affine scheme U with an étale q : U → X and a : V → U making the square (a,p,q,i) a fiber product `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)).
