+++
id = "def-v2-prime-field-filtration"
kind = "definition"
title = "Finite extension trees with prime-field factors"
uses = ["def-constructible-constructible", "def-weil-pbc-etale-sheaves"]
lean = ["AlgebraicGeometry.Scheme.HasPrimeFieldFiltration"]
source = "Stacks Project, Theorem 03SC, second proof paragraph"
+++
Let $X$ be a scheme and $\Lambda$ a commutative ring. In the category of $\Lambda$-module sheaves on $X_{\mathrm{\acute et}}$ [def-weil-pbc-etale-sheaves], define $\mathrm{HasPrimeFieldFiltration}_{\Lambda,X}$ inductively by two constructors. (1) A constructible sheaf $F$ [def-constructible-constructible] belongs if there exist a prime $r$, a constructible $\mathbf F_r$-module sheaf $G$, and an isomorphism between their underlying abelian sheaves. (2) If $0\to F_1\to F\to F_3\to0$ is short exact, the outer terms are constructible, and both belong, then $F$ belongs. Thus a witness is a finite extension tree with constructible prime-field factors; there is no cohomological condition.
