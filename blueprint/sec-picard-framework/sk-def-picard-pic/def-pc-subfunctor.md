+++
id = "def-pc-subfunctor"
kind = "definition"
title = "Subfunctors"
lean = ["CategoryTheory.Subfunctor"]
order = 628
uses = ["def-pc-scheme"]
+++
Let $S$ be a scheme and let
$F:(\mathit{Sch}/S)^{\mathrm{op}}\to\textit{Sets}$ be a functor. A
*subfunctor* $H\subseteq F$ is an assignment
$T\mapsto H(T)\subseteq F(T)$ such that the maps $F(f):F(T)\to F(T')$
send $H(T)$ into $H(T')$ for all morphisms $f:T'\to T$ of $S$-schemes.
