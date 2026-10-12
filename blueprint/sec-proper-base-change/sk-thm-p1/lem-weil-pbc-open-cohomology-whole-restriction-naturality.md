+++
id = "lem-weil-pbc-open-cohomology-whole-restriction-naturality"
kind = "lemma"
title = "Restriction from the whole scheme commutes with cohomology pullback"
uses = ["def-pc-scheme", "def-weil-pbc-cohomology-pullback", "lem-weil-pbc-inverse-image-composition"]
lean = ["AlgebraicGeometry.Etale.openCohomologyPullback_restrict"]
source = "literature/stacks-project/cohomology.tex, Tag 01F7, functoriality of cohomology; agent-written composition and restriction consequence."
+++
Let g:Y→X be a scheme morphism [def-pc-scheme], W an open of X, G an abelian etale sheaf `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)), and q≥0. Let P_W be pullback along g restricted to W, followed by the coefficient identification (upperStarComp(g_W,j_W))^{-1} followed by upperStarComp(j_W_prime,g) [def-weil-pbc-cohomology-pullback], [lem-weil-pbc-inverse-image-composition]. Then for every x in H^q(X,G), restriction to g^{-1}W of g^*(x) equals P_W of restriction to W of x. This includes W empty, W=X, and the identity morphism. The module also abbreviates the explicitly prescribed restriction and restricted-pullback maps; it introduces no new cohomology notion.
