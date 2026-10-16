+++
id = "def-pc-subfunctor"
kind = "definition"
title = "Subfunctors"
lean = ["AlgebraicGeometry.isRepresentable_of_isSheaf_of_zariskiCovers"]
order = 782
uses = ["def-pc-scheme"]
+++
Let $F:(\mathit{Sch})^{\mathrm{op}}\to\textit{Sets}$ be a functor. A
*subfunctor* $H\subseteq F$ is an assignment
$T\mapsto H(T)\subseteq F(T)$ such that the maps $F(f):F(T)\to F(T')$
send $H(T)$ into $H(T')$ for all morphisms $f:T'\to T$.
