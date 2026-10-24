+++
id = "lem-sp-right-adjoint-preserves-injectives"
kind = "lemma"
title = "Right adjoints of exact functors preserve injectives"
lean = ["CategoryTheory.Adjunction.preservesInjectiveObjects_of_preservesFiniteLimits"]
order = 752
uses = ["def-sp-abelian", "def-sp-injective-resolutions"]
+++
Let $u:\mathcal A\to\mathcal B$ be a functor which preserves finite
limits (for instance an exact functor between abelian categories
[def-sp-abelian]) and admits a right adjoint $u_*:\mathcal
B\to\mathcal A$. Then $u_*$ sends injective
[def-sp-injective-resolutions] objects to injective objects.
