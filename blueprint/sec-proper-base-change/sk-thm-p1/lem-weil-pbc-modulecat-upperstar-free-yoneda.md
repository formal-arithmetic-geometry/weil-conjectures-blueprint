+++
id = "lem-weil-pbc-modulecat-upperstar-free-yoneda"
kind = "lemma"
title = "Base change of free Yoneda etale module sheaves (source-library model)"
uses = ["def-pc-scheme", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-inverse-image"]
lean = ["AlgebraicGeometry.Etale.upperStarFreeYonedaIso"]
+++
Let $X,Y$ be schemes [def-pc-scheme], $g:Y\to X$ a morphism, $\Lambda$ a commutative ring and $W\to X$ an etale object [def-weil-pbc-etale-site]. Write $\Lambda[W]$ for the sheafification of the presheaf $V\mapsto\bigoplus_{\phi:V\to W}\Lambda$, with restriction reindexing by composition `PresheafOfModules.freeYonedaEquiv` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Category/ModuleCat/Presheaf/Generator.lean)), `PresheafOfModules.sheafification` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Category/ModuleCat/Presheaf/Sheafification.lean)). Using module-valued etale sheaves [def-weil-pbc-etale-sheaves] and inverse image [def-weil-pbc-inverse-image], there is an isomorphism $g^{-1}\Lambda[W]\cong\Lambda[W\times_XY]$. In the source library the free sheaf is $\mathrm{Sheaf.freeYoneda}(X_{\mathrm{Et}},W,\Lambda)$, and the asserted isomorphism is $\mathrm{Etale.upperStarFreeYonedaIso}(g,W)$.
