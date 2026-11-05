+++
id = "proposition-properties-trace"
kind = "proposition"
title = "Properties of the trace"
order = 896
lean = ["DerivedCategory.exists_trace_eq_algebraMap_and_trace_extendScalars_eq_algebraMap", "DerivedCategory.trace_eq_algebraMap_sum_negOnePow_linearMapTrace", "DerivedCategory.trace_eq_algebraMap_sum_negOnePow_trace_homologyMap", "DerivedCategory.trace_eq_trace_add_trace_of_shortExact", "CategoryTheory.Functor.trace_eq_unitEndRingHom_trace"]
uses = ["definition-categorical-trace"]
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

If $P$ is the underlying complex of a two-step filtered object
$F^1P\to P\to P/F^1P$ of the filtered derived category, with $F^1P$ and
$P/F^1P$ perfect, and $v$ is the underlying map of an endomorphism $\tilde v$
of this filtered object, with graded pieces $v_1$ on $F^1P$ and $v_0$ on
$P/F^1P$, then

$$
\operatorname{tr}_A(v\mid P)=\operatorname{tr}_A(v_1\mid F^1P)
+\operatorname{tr}_A(v_0\mid P/F^1P).
$$

Over a field $L$ it is
also

$$
\operatorname{tr}_L(v\mid P)
=\sum_i(-1)^i\operatorname{Tr}_L(H^i(v)\mid H^i(P)).
$$
