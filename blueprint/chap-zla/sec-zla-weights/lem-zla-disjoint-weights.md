+++
id = "lem-zla-disjoint-weights"
kind = "lemma"
title = "Different weights have disjoint reciprocal roots"
order = 1024
uses = ["def-zla-pure-polynomial", "lem-zla-scalar-weight-unique"]
+++
Assume $P_i$ is pure of weight $i$ for every $i$. If $i\neq j$, then $P_i$
and $P_j$ have no common reciprocal root in $\Omega$.

## Proof

A common reciprocal root would be universally pure of weight $i$ and of weight
$j$, so $i=j$ by [lem-zla-scalar-weight-unique].
