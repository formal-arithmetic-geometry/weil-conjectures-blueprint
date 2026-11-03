+++
id = "def-sfb-left-derived-exact"
kind = "definition"
title = "Left derived functor of an exact functor"
order = 1121
uses = ["def-sfb-left-derived-functor"]
lean = ["CategoryTheory.Functor.leftDerivedFunctorIsoMapDerivedCategory"]
+++
Let $\mathcal C$ be as in [def-sfb-left-derived-functor], and let
$F\colon\mathcal C\to\mathcal D$ be an exact functor (exact functors preserve K-flat
quasi-isomorphisms). Then there is a canonical isomorphism $LF\cong D(F)$ with the
termwise functor $D(F)$.
