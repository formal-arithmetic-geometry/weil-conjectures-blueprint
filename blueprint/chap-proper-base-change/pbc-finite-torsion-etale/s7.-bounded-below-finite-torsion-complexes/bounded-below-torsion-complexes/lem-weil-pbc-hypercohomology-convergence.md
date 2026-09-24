+++
id = "lem-weil-pbc-hypercohomology-convergence"
kind = "lemma"
title = "Half-plane convergence"
order = 1843
uses = ["def-weil-pbc-hypercohomology-filtrations-detailed"]
+++
Both spectral sequences of
[def-weil-pbc-hypercohomology-filtrations-detailed] lie in $p\geq0$, $q\geq
a$. In total degree $n$, only $a\leq q\leq n$ occurs. The induced filtrations
are finite, exhaustive, and separated, so the spectral sequences converge
without a derived inverse-limit condition.

## Proof

Right-derived direct image has no negative cohomological degree, giving
$p\geq0$, and the lower bound gives $q\geq a$. On $p+q=n$ these inequalities
give the finite interval; the truncation triangles show exhaustivity, and
finiteness shows separatedness, so convergence is immediate for the
filtrations of [def-weil-pbc-hypercohomology-filtrations-detailed].
