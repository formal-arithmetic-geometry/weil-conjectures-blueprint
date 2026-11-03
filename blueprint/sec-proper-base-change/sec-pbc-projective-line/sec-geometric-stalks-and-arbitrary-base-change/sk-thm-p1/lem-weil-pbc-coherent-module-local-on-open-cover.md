+++
id = "lem-weil-pbc-coherent-module-local-on-open-cover"
kind = "lemma"
title = "Coherence of a module is local on an open covering"
uses = ["def-pc-scheme", "pqf-def-coherent"]
lean = ["AlgebraicGeometry.coherent_module_local_on_open_cover"]
order = 1801
+++
Let $X$ be a scheme [def-pc-scheme], $\mathcal F$ an $\mathcal O_X$-module and $X=\bigcup_{i\in I}U_i$ a covering by open subschemes; for an open $W\subseteq X$ write $\mathcal F|_W$ for the restriction of $\mathcal F$ to the open subscheme $W$ ($(\mathcal F|_W)(V)=\mathcal F(V)$ for $V\subseteq W$ open). (1) If $\mathcal F$ is coherent [pqf-def-coherent], then $\mathcal F|_W$ is a coherent $\mathcal O_W$-module for every open $W\subseteq X$. (2) If $\mathcal F|_{U_i}$ is a coherent $\mathcal O_{U_i}$-module for every $i\in I$, then $\mathcal F$ is a coherent $\mathcal O_X$-module. (Both conditions of [pqf-def-coherent] are local: being of finite type is a condition on neighbourhoods of points, and for the kernel condition over an open $W$ one restricts to the $W\cap U_i$, kernels of $\mathcal O_X$-modules being computed sectionwise.)
