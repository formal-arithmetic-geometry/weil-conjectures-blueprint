+++
id = "def-sbc-smooth-morphisms"
kind = "definition"
title = "Smooth morphisms"
order = 1143
uses = ["def-weil-pbc-scheme-conventions"]
+++
A morphism of schemes $f:X\to Y$ is *smooth* if it is locally of
finite presentation and formally smooth, the latter meaning that every
morphism $T\to X$ over $Y$ from a closed subscheme $T\subset T'$
defined by a nilpotent ideal sheaf extends, Zariski locally on $T'$,
to a morphism $T'\to X$ over $Y$. A smooth morphism $f$ has
*relative dimension $n$ at a point $x\in X$* if the fibre
$X_{f(x)}$ through that point has dimension $n$ at $x$; it has relative dimension
$n$ if this holds at every point. An
*etale* morphism is a smooth
morphism of relative dimension zero.

This notion of smoothness agrees with the one defined by local standard
smooth presentations (Stacks Project, Tag `02H6`). Smooth morphisms are
exactly the flat morphisms locally of finite presentation with smooth
fibres, and the relative dimension of a smooth morphism at $x$ is a
locally constant function of $x$.
