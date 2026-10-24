+++
id = "def-pc-zariski-sheaf-property"
kind = "definition"
title = "Zariski sheaf property of a functor"
order = 853
lean = ["CategoryTheory.Presheaf.IsSheaf", "AlgebraicGeometry.Scheme.zariskiTopology", "CategoryTheory.GrothendieckTopology.over"]
uses = ["def-pc-scheme"]
+++
Let $S$ be a scheme and let
$F:(\mathit{Sch}/S)^{\mathrm{op}}\to\textit{Sets}$ be a functor. $F$
*satisfies the sheaf property for the Zariski topology* if for every
$S$-scheme $T$, every open covering $T=\bigcup_{i\in I}U_i$ and every
collection $\xi_i\in F(U_i)$ with
$\xi_i|_{U_i\cap U_j}=\xi_j|_{U_i\cap U_j}$ there is a unique
$\xi\in F(T)$ with $\xi|_{U_i}=\xi_i$.
