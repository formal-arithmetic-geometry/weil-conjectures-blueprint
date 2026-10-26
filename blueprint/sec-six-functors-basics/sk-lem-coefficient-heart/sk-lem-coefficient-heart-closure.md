+++
id = "det-lem-coefficient-heart-closure"
kind = "lemma"
title = "Lisse sheaves on a stratum are closed under kernels, cokernels, extensions"
order = 2125
uses = ["det-lem-coefficient-heart-common-stratification", "sk-prop-sfb-qlbar-colimit-x", "det-def-sfb-constructible-local-model"]
+++
Let $S$ be a topologically Noetherian scheme and $\Lambda=E$ or $\Qlb$.

1. If $0\to F'\to F\to F''\to0$ is an exact sequence of $\Lambda_S$-modules with $F'$, $F''$
   lisse, then $F$ is lisse.
2. If $\phi\colon F\to G$ is a morphism of lisse $\Lambda_S$-modules, then $\ker\phi$ and
   $\coker\phi$ are lisse.

Consequently, for a Noetherian scheme $X$, $\Cons(X,\Lambda)$ is closed under kernels,
cokernels and extensions in $\Mod(X_{\mathrm{proét}},\Lambda)$, is an abelian category, and
the inclusion is exact. A $\Lambda_X$-module is constructible iff it is lisse on each stratum
of a finite stratification (the scalar ring $\Lambda(*)$ is a field, so a finite constant
local model is a finite free module, [det-def-sfb-constructible-local-model]).
