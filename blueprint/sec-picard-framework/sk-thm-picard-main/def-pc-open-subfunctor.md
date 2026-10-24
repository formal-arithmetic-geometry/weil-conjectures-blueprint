+++
id = "def-pc-open-subfunctor"
kind = "definition"
title = "Subfunctors representable by open immersions"
lean = ["AlgebraicGeometry.exists_opens_of_relative_isOpenImmersion", "AlgebraicGeometry.relative_isOpenImmersion_of_exists_opens"]
order = 854
uses = ["def-pc-scheme", "def-pc-subfunctor"]
+++
Let $S$ be a scheme, let
$F:(\mathit{Sch}/S)^{\mathrm{op}}\to\textit{Sets}$ be a functor and
$H\subseteq F$ a subfunctor. $H\subseteq F$ is *representable by open immersions* if for all pairs
$(T,\xi)$ with $T$ an $S$-scheme and $\xi\in F(T)$ there is an open
subscheme $U_\xi\subseteq T$ such that a morphism $f:T'\to T$ of
$S$-schemes factors through $U_\xi$ if and only if $f^*\xi\in H(T')$.
