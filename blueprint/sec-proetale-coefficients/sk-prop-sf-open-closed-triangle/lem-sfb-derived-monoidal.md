+++
id = "lem-sfb-derived-monoidal"
kind = "lemma"
title = "The derived category of a monoidal Grothendieck abelian category is monoidal"
order = 1187
uses = ["det-def-sfb-derived-categories"]
lean = ["DerivedCategory.hasDerivedMonoidalCategory"]
+++
Let $\mathcal C$ be a Grothendieck abelian category with a closed braided monoidal
structure whose tensor product is additive, and assume that $\mathcal C$ has functorial
flat resolutions. Then the derived category $D(\mathcal C)$ carries a monoidal structure
whose tensor product $-\otimes^{\mathrm L}-$ is the left derived functor, in two
variables, of the tensor product of complexes on $K(\mathcal C)$ with respect to the
quasi-isomorphisms. It is computed by replacing either argument by a K-flat resolution.
The associativity and unit constraints are induced from those of complexes, and the
localization functor $K(\mathcal C)\to D(\mathcal C)$ is lax monoidal.
