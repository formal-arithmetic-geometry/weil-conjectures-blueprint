+++
id = "def-weil-pbc-etale-mayer-vietoris-section-complex"
kind = "definition"
title = "The explicit two-open section short complex"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.Etale.etaleSectionShortComplex", "AlgebraicGeometry.Etale.etaleSectionFunctor", "AlgebraicGeometry.Etale.etaleSectionMap"]
order = 1748
+++
Let $X$ be a scheme [def-pc-scheme], $U,V\subseteq X$ opens, and $I$ a cochain complex of abelian etale sheaves on $X$ concentrated in degrees $\ge0$. For an etale object $W$ of $X$ let $\mathrm{Sec}(I,W)$ be the complex of abelian groups obtained by evaluating $I$ at $W$ degreewise; a morphism $W'\to W$ of etale objects induces the restriction map $\mathrm{Sec}(I,W)\to\mathrm{Sec}(I,W')$, a map of complexes since restriction commutes with the differentials. The *two-open section short complex* is
$$
\mathrm{Sec}(I,X)\xrightarrow{\ (\mathrm{res}^X_U,\ \mathrm{res}^X_V)\ }\mathrm{Sec}(I,U)\oplus\mathrm{Sec}(I,V)\xrightarrow{\ (a,b)\mapsto\mathrm{res}^U_{U\cap V}a-\mathrm{res}^V_{U\cap V}b\ }\mathrm{Sec}(I,U\cap V),
$$
a short complex of complexes of abelian groups: the composite is zero because both $\mathrm{res}^U_{U\cap V}\circ\mathrm{res}^X_U$ and $\mathrm{res}^V_{U\cap V}\circ\mathrm{res}^X_V$ are the restriction from $X$ to $U\cap V$.
