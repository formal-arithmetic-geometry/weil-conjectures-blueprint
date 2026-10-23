+++
id = "def-weil-pbc-arrows-functor"
kind = "definition"
title = "The functor taking a category to its set of arrows"
lean = ["CategoryTheory.Cat.arrows"]
order = 1626
+++
For a category $C$ whose objects and morphisms are sets, let $\mathrm{Arrows}(C)$ be the set of triples $(X,Y,f)$ with $f:X\to Y$. For a functor $v:C\to D$, put $\mathrm{Arrows}(v)(X,Y,f)=(vX,vY,vf)$. These maps define the functor $\mathrm{Arrows}:\mathit{Cat}\to\mathit{Sets}$ used to form the arrow-set diagram of a strict system of categories.
