+++
id = "def-weil-pbc-finite-global-dimension"
kind = "definition"
title = "Projective dimension of a module and finite global dimension of a ring"
lean = ["Ring.HasFiniteGlobalDimension", "Ring.HasGlobalDimensionLE", "Ring.globalDimension", "ModuleCat.HasFiniteProjectiveDimension", "ModuleCat.HasProjectiveResolutionLE", "ModuleCat.hasProjectiveResolutionLE_iff_hasProjectiveDimensionLE", "CategoryTheory.projectiveDimension"]
order = 1624
+++
Let $R$ be a commutative ring and $M$ an $R$-module. A *projective resolution of $M$ of length $\le n$* ($n\ge0$ an integer) is an exact sequence of $R$-modules $0\to P_n\to P_{n-1}\to\dots\to P_0\to M\to0$ with every $P_i$ a projective $R$-module (a direct summand of a free $R$-module). $M$ has *projective dimension $\le n$* if it has a projective resolution of length $\le n$, and *finite projective dimension* if this holds for some $n$; the minimal such $n$ is the *projective dimension* $\operatorname{pd}_R M$. The ring $R$ *has global dimension $\le n$* if every $R$-module (not only every finite one) has projective dimension $\le n$, and *finite global dimension* if this holds for some integer $n\ge0$; the minimal such $n$ is the *global dimension* $\operatorname{gl.dim}R$.
