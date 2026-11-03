+++
id = "sk-p-trace"
kind = "proposition"
title = "Properties of the trace"
order = 543
lean = ["DerivedCategory.trace_eq_algebraMap_sum_negOnePow_linearMapTrace"]
uses = ["sk-d-trace"]
tags = ["sketch"]
+++
The trace is $A$-linear in $v$, invariant under conjugacy, and compatible
with derived scalar extension: for every ring map $A\to B$,

$$
\operatorname{tr}_A(v\mid P)\longmapsto
\operatorname{tr}_B(v\otimes^{\mathbf L} B\mid P\otimes^{\mathbf L} B).
$$

For a bounded complex of finite projective modules and a chain
endomorphism $v^\bullet$ representing $v$ one has

$$
\operatorname{tr}_A(v\mid P)
=\sum_i(-1)^i\operatorname{Tr}_A(v^i\mid P^i).
$$

The trace is additive on a cofibre sequence of perfect complexes with a
*coherent* endomorphism of that sequence, equivalently here an
endomorphism in the filtered derived category. Over a field $L$ it is
also

$$
\operatorname{tr}_L(v\mid P)
=\sum_i(-1)^i\operatorname{Tr}_L(H^i(v)\mid H^i(P)).
$$
