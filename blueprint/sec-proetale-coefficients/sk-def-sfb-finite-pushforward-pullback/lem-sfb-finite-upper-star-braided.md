+++
id = "lem-sfb-finite-upper-star-braided"
kind = "lemma"
title = "$g^*$ is braided monoidal"
order = 888
uses = ["def-sfb-finite-lower-star-lax-monoidal", "def-sfb-finite-upper-star-monoidal"]
lean = ["AlgebraicGeometry.ProEtale.laxBraided_upperStar"]
+++
Let $\mathcal A$ be a closed braided monoidal Grothendieck abelian category. The strong
monoidal functor $g^*$ of [def-sfb-finite-upper-star-monoidal] is compatible with the
braidings: it is a braided monoidal functor, hence symmetric monoidal when $\mathcal A$ is
symmetric. In particular $g^*$ sends commutative ring objects to commutative ring objects.
