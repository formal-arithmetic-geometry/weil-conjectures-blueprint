+++
id = "lem-weil-pbc-constant-module-sheaves-forget-colimits"
kind = "lemma"
title = "Constant-module sheaves forget coefficients preserving colimits"
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Etale.constantModuleSheaves_forget_preservesColimits"]
+++
Let $X$ be a scheme in universe $u$ [def-weil-pbc-scheme-conventions], and let $\Lambda$ be a commutative ring with underlying type in universe $u+1$. Let $V:\mathrm{Sheaf}(X_{\mathrm{et}},\mathrm{Mod}_\Lambda)\to\mathrm{Sheaf}(X_{\mathrm{et}},\mathrm{Ab})$ [def-weil-pbc-etale-sheaves], `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)) send a module-valued sheaf to its underlying abelian-group-valued sheaf. For every category with objects and arrows in universe $u+1$, $V$ maps every colimit cocone `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)) to a colimit cocone. No quasi-compactness or finiteness assumption is required.
