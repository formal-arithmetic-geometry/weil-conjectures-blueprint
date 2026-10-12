+++
id = "def-sfb-right-derived-exact"
kind = "definition"
title = "Right derived functor of an exact functor"
order = 1593
uses = ["def-sfb-right-derived-functor"]
lean = ["CategoryTheory.Functor.rightDerivedFunctorIsoMapDerivedCategory"]
+++
Let $F\colon\mathcal C\to\mathcal D$ be as in [def-sfb-right-derived-functor] and moreover
exact. Then there is a canonical isomorphism $RF\cong D(F)$, where $D(F)\colon
D(\mathcal C)\to D(\mathcal D)$ is the functor induced by applying $F$ termwise.
