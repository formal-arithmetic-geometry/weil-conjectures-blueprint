+++
id = "lem-weil-pbc-constant-module-pushforward-functoriality"
kind = "lemma"
title = "ConstantModulePushforwardFunctoriality"
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lemma-constructible-pullback-constant"]
lean = ["AlgebraicGeometry.Etale.constantModulePushforwardMap_id_comp"]
source = "literature/stacks-project/etale-cohomology.tex, Tag 09Z1, degree-zero transition maps and continuity; Tag 09Z6, finite approximation paragraph, lines 12999-13008"
+++
For every commutative ring Lambda in universe u+1 and every Lambda-module M, the map from f1_* M_Y1 to f2_* M_Y2 associated to g:Y2 -> Y1 over X is defined by the inverse-image unit, the canonical constant-sheaf comparison [lemma-constructible-pullback-constant], and direct-image composition [def-weil-pbc-direct-image]. This map preserves identity and composition contravariantly in g. No finiteness assumptions are imposed.
