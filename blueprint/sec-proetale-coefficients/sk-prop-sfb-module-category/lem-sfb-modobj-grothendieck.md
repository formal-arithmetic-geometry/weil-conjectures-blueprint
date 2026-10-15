+++
id = "lem-sfb-modobj-grothendieck"
kind = "lemma"
title = "Module objects form a Grothendieck abelian category"
order = 1582
uses = ["lem-sfb-modobj-abelian", "lem-sfb-modobj-forget-faithful", "lem-sfb-modobj-forget-left-exact", "lem-sfb-modobj-forget-right-exact"]
lean = ["CategoryTheory.Mod.isGrothendieckAbelian"]
+++
Let $\mathcal C$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive in each variable, and let $\mathcal R$ be a commutative monoid object.
Then $\Mod_{\mathcal R}(\mathcal C)$ is a Grothendieck abelian category.
