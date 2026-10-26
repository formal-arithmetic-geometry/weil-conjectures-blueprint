+++
id = "lem-weil-pbc-etale-constant-ring-module-equivalence"
kind = "lemma"
title = "Constant-coefficient etale sheaves and modules over the constant ring sheaf are equivalent"
uses = ["def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.etaleConstantModuleFunctor_isEquivalence", "AlgebraicGeometry.Scheme.etaleConstantModuleFunctor", "AlgebraicGeometry.Scheme.etaleConstantModuleUnderlyingIso", "AlgebraicGeometry.Scheme.etaleConstantModuleRestrictionFunctor"]
order = 1704
+++
Let $Y$ be a scheme with its small étale site $Y_{\Et}$ [def-weil-pbc-etale-site], and let $\Lambda$ be a commutative ring. Let $\underline\Lambda$ be the constant sheaf of rings on $Y_{\Et}$ associated to $\Lambda$ (the sheafification of the constant presheaf of rings). Extending the scalar action of a sheaf of $\Lambda$-modules to $\underline\Lambda$ (by sheafifying the module structure) gives an equivalence from the category of sheaves of $\Lambda$-modules on $Y_{\Et}$ to the category of sheaves of $\underline\Lambda$-modules. This extension leaves the underlying abelian sheaf unchanged, and an inverse equivalence restricts scalars along the map from the constant presheaf of rings to its sheafification. No nonzero-ring or nonempty-scheme hypothesis is imposed.
