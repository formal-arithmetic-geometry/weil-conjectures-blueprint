+++
id = "lem-pc-schemes-criterion"
kind = "lemma"
title = "A representability criterion via covers"
order = 807
uses = ["def-pc-representable-functor", "def-pc-subfunctor"]
lean = ["AlgebraicGeometry.isRepresentable_of_isSheaf_of_zariskiCovers"]
+++
Let $S$ be a scheme and let
$F:(\mathit{Sch}/S)^{\mathrm{op}}\to\textit{Sets}$ be a functor on the category of
$S$-schemes whose values $F(T)$ are small, i.e. lie in the same universe as
the $S$-schemes $T$, and suppose:

1. **(1)** $F$ satisfies the sheaf property for the Zariski topology;
1. **(2)(a)** there exists a family $(F_i)_{i\in I}$, indexed by a set $I$, of subfunctors of
$F$ each of which is representable;
1. **(2)(b)** each inclusion $F_i\subseteq F$ is
representable by open immersions;
1. **(2)(c)** the family $(F_i)_{i\in I}$ covers $F$.

Then $F$ is representable by a scheme over $S$.
