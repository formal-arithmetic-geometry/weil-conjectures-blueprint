+++
id = "lem-weil-pbc-locally-constant-germ-evaluation"
kind = "lemma"
title = "Evaluation identifies germs of locally constant maps with the fibre"
lean = ["TopCat.existsUnique_locallyConstant_germ_evaluation"]
source = "literature/stacks-project/sheaves.tex, Sheaves, Example Tag 007B, line 995, together with Definition Tag 006W"
+++
Let U be a topological space, x a point of U, and R a set. A map from an open subset V of U to R is locally constant if every point of V has an open neighbourhood in V on which the map is constant. For each open neighbourhood V of x let L_R(V) be the set of such maps. Let L_R,x be their colimit `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)) over the open neighbourhoods of x ordered by reverse inclusion, with coprojections sending g to its germ g_x. There is a unique evaluation map from L_R,x to R sending g_x to g(x), and it is bijective.
