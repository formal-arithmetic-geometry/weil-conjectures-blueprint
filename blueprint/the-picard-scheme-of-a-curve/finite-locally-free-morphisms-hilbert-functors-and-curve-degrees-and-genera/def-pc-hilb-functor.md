+++
id = "def-pc-hilb-functor"
kind = "definition"
title = "The Hilbert functor Hilb^d_{X/S}"
order = 4252
lean = ["AlgebraicGeometry.hilbFunctor"]
uses = ["def-pc-base-change", "def-pc-representable-functor", "def-pc-finite-locally-free", "lem-pc-hilb-functorial"]
+++
Let $X\to S$ be a morphism of schemes and $d\geq0$. For a scheme $T$ over
$S$ put
$$
\operatorname{Hilb}^d_{X/S}(T):=\bigl\{Z\subset X_T\ \text{a closed subscheme}:\
Z\to T\text{ is finite locally free of degree }d\bigr\},
$$
where "finite locally free of degree $d$" is
[def-pc-finite-locally-free]; the assignment is contravariant by base
change of closed subschemes, and the resulting functor's sheaf properties
are [lem-pc-hilb-functorial]. If it is representable
[def-pc-representable-functor], the representing scheme is
$\underline{\operatorname{Hilb}}^d_{X/S}$ (Stacks Project, Picard Schemes
of Curves, Chapter 44, Section 44.2, [Tag
0B94](https://stacks.math.columbia.edu/tag/0B94)).

*Import note.* The source's definition states only the representability
sentence, the functor itself never being defined; the display above is the
definition the source states in its own pointer remark
[rem-ptr-pc-hilb-functor-12], copied back here. Nothing is added beyond
what that remark says.
