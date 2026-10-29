+++
id = "lem-sfb-modobj-grothendieck"
kind = "lemma"
title = "Module objects form a Grothendieck abelian category"
order = 1152
uses = ["lem-sfb-modobj-abelian", "lem-sfb-modobj-forget-faithful", "lem-sfb-modobj-forget-left-exact", "lem-sfb-modobj-forget-right-exact"]
lean = ["CategoryTheory.Mod.isGrothendieckAbelian"]
+++
Let $\mathcal C$ be a monoidal Grothendieck abelian category whose tensor product is
additive in each variable, such that $X\otimes-$ preserves colimits for every object $X$.
Let $\mathcal R$ be a monoid object of $\mathcal C$. Then $\Mod_{\mathcal R}(\mathcal C)$ is
a Grothendieck abelian category.
