+++
id = "lem-sfb-derived-monoidal-closed"
kind = "lemma"
title = "The derived category of a closed monoidal Grothendieck abelian category is closed"
order = 1178
uses = ["lem-sfb-derived-monoidal"]
lean = ["DerivedCategory.monoidalClosed"]
+++
In the situation of [lem-sfb-derived-monoidal], the monoidal category
$(D(\mathcal C),\otimes^{\mathrm L})$ is closed: for every $K\in D(\mathcal C)$ the
functor $K\otimes^{\mathrm L}-$ has a right adjoint.
