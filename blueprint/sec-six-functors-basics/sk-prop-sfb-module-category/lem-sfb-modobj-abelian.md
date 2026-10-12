+++
id = "lem-sfb-modobj-abelian"
kind = "lemma"
title = "Module objects form an abelian category"
order = 1556
uses = ["lem-sfb-modobj-cokernels", "lem-sfb-modobj-kernels", "sk-def-sfb-module-objects"]
lean = ["CategoryTheory.Mod.instAbelian_weilConjectures"]
+++
Let $\mathcal C$ be an abelian monoidal category whose tensor product is additive in each
variable. Let $\mathcal R$ be a monoid object of $\mathcal C$ such that $\mathcal R\otimes-$
preserves finite colimits. Then $\Mod_{\mathcal R}(\mathcal C)$
([sk-def-sfb-module-objects]) is an abelian category.
