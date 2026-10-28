+++
id = "sk-p-trace"
kind = "proposition"
title = "Trace laws"
order = 3691
uses = ["sk-d-trace"]
lean = ["DerivedCategory.trace_eq_algebraMap_sum_negOnePow_linearMapTrace"]
tags = ["sketch"]
+++
Let $P\in\operatorname{Perf}(A)$ and $v:P\to P$, with trace
$\operatorname{tr}_A(v\mid P)$ as in [sk-d-trace].
The trace is $A$-linear in $v$, invariant under conjugacy, and compatible with
derived scalar extension: for every ring map $A\to B$,

$$
\operatorname{tr}_A(v\mid P)\longmapsto
\operatorname{tr}_B(v\dt B\mid P\dt B).
$$

For a bounded complex of finite projective modules and a chain endomorphism
$v^\bullet$ representing $v$ one has

$$
\operatorname{tr}_A(v\mid P)
=\sum_i(-1)^i\operatorname{Tr}_A(v^i\mid P^i).
$$

The trace is additive on a cofibre sequence of perfect complexes with a
*coherent* endomorphism of that sequence, equivalently here an endomorphism in
the filtered derived category. Over a field $L$ it is also

$$
\operatorname{tr}_L(v\mid P)
=\sum_i(-1)^i\operatorname{Tr}_L(H^i(v)\mid H^i(P)).
$$
