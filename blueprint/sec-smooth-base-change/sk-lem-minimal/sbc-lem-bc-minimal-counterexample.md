+++
id = "sbc-lem-bc-minimal-counterexample"
kind = "lemma"
title = "Minimal counterexamples occur over a point"
order = 2079
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $T$ be a
quasi-compact and
quasi-separated scheme and let $P$ be a property for quasi-compact
quasi-separated schemes over $T$. Assume:

1. if $T''\to T'$ is a thickening of quasi-compact quasi-separated
schemes over $T$, then $P(T'')$ if and only if $P(T')$;
1. if $T'=\varprojlim T_i$ is a limit of an inverse system of
quasi-compact quasi-separated schemes over $T$ with affine
transition morphisms and $P(T_i)$ holds for all $i$, then
$P(T')$ holds;
1. if $Z\subset T'$ is a closed subscheme with quasi-compact
complement $V\subset T'$ and $P(T')$ holds, then either $P(V)$
or $P(Z)$ holds;
1. $P(\emptyset)$ does not hold.

Then $P(T)$ implies $P(\operatorname{Spec}K)$ for some morphism
$\operatorname{Spec}K\to T$ where $K$ is a field.
