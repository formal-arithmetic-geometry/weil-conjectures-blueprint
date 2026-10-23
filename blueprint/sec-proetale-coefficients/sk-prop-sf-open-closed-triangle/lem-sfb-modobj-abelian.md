+++
id = "lem-sfb-modobj-abelian"
kind = "lemma"
title = "Module objects form an abelian category"
order = 1133
uses = ["det-def-sfb-module-objects-definition", "lem-sfb-modobj-cokernels", "lem-sfb-modobj-kernels"]
lean = ["CategoryTheory.Mod.instAbelian"]
+++
Let $\mathcal C$ be an abelian monoidal category whose tensor product is additive in each
variable. Let $\mathcal R$ be a monoid object of $\mathcal C$ such that $\mathcal R\otimes-$
preserves finite colimits. Then $\Mod_{\mathcal R}(\mathcal C)$
([det-def-sfb-module-objects-definition]) is an abelian category.
