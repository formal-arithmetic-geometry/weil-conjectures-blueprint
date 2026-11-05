+++
kind = "proof"
of = "lemma-constructible-sheaves--6"
order = 268015
uses = ["definition-constructible-sheaves", "proposition-topos-functoriality"]
+++
A finite presentation over the condensed coefficient ring on the point
is specified by two natural numbers and a morphism between the
corresponding finite free modules. Their cokernels form an essentially
small family, and so do their pullbacks.

Fix a pro-étale cover and choose representatives for the local models.
Adjunction gives a map from a sheaf to the product of the direct images
of its chosen local representatives. Each restriction of this map is
monic by the counit identity, and restrictions to a cover jointly detect
monomorphisms. The module category is well-powered, so subobjects of
these products form an essentially small family. Taking the small union
over covers proves smallness of finite constant local models.

Repeat this argument for each finite stratification. Restrictions to
its strata jointly detect monomorphisms; Noetherianity ensures that the
stratum immersions are quasi-compact. Taking the small union over
stratifications proves the result, using the qcqs clause of
[definition-constructible-sheaves]. This also accounts for the gluing
between different strata.
